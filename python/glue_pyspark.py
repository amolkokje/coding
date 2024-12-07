from os import stat
from typing import final

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql.functions import lit

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

"""
- data paritioned in s3 bucket
- indexed to glue database catalog

input table:
data parsed by ETL job in ECS and loaded here
- ds
- serial_number
- start_time
- station_type
- test_result

Daily First Pass Yield table:
- ds
- station_type
- first_pass_count
- total_count
- first_pass_yield

Daily Final Pass Yield table:
- ds
- station_type
- final_pass_count
- total_count
- final_pass_yield
- 
"""


def daily_failure_pareto(ds):
    """
    failure breakdown by station type
    """
    # read data for the given date partition
    dyf = glueContext.create_dynamic_frame.from_catalog(
        database="database",
        table_name="testrun",
        pushdown_predicate=f"ds = '{ds}'",  # WHERE clause
    )
    # convert
    df = dyf.toDF()

    # perform calculations
    df_fail = df.filter(df.test_result == "fail")
    df_fail_grouped = df_fail.groupby("station_type").count()
    df_fail_grouped_withdate = df_fail_grouped.withColumn("ds", ds)  # add date column

    # convert spark dataframe to dynamic frame
    output_dyf = DynamicFrame.fromDF(
        df_fail_grouped_withdate, glueContext, "daily_failure_pareto"
    )
    # write results to glue catalog
    glueContext.write_dynamic_frame.from_catalog(
        frame=output_dyf,
        database="database",
        table_name="daily_failure_pareto",
    )


def daily_final_pass_yield(ds, station_type):
    # read data for the given date partition
    dyf = glueContext.create_dynamic_frame.from_catalog(
        database="database",
        table_name="testrun",
        pushdown_predicate=f"ds = '{ds}' and station_type='{station_type}'",  # WHERE clause
    )
    # convert
    df = dyf.toDF()

    # perform calculations
    total_count = df.select("serial_number").distinct().count()
    # SN which have at least one pass
    df_at_least_one_pass_sn = (
        df.filter(df.test_result == "pass")["serial_number"].distinct().count()
    )
    final_pass_yield = df_at_least_one_pass_sn * 100 / total_count
    output_df = spark.createDataFrame(
        [
            (ds, station_type, df_at_least_one_pass_sn, total_count, final_pass_yield),
        ],
        ["ds", "station_type", "final_pass_count", "total_count", "final_pass_yield"],
    )

    # convert spark dataframe to dynamic frame
    output_dyf = DynamicFrame.fromDF(output_df, glueContext, "daily_final_pass_yield")
    # write results to glue catalog
    glueContext.write_dynamic_frame.from_catalog(
        frame=output_dyf,
        database="database",
        table_name="daily_final_pass_yield",
    )


def daily_first_pass_yield(ds, station_type):
    """
    - get data using glue dynamic frame
    - perform calculations in spark dataframe
    - load results using glue dynamic frame
    """
    # read data for the given date partition
    dyf = glueContext.create_dynamic_frame.from_catalog(
        database="database",
        table_name="testrun",
        pushdown_predicate=f"ds = '{ds}' and station_type='{station_type}'",  # WHERE clause
    )
    # convert dynamic frame to spark dataframe
    df = dyf.toDF()

    # perform calculations
    total_count = df.select("serial_number").distinct().count()
    # find count of such that for given station/sn, only have pass/fail logs
    df_pass_sn = df.filter(df.test_result == "pass")[
        "serial_number"
    ]  # OR: df.where(df.test_result == “pass”)[‘sn’]
    df_fail_sn = df.filter(df.test_result == "fail")[
        "serial_number"
    ]  # OR: df.where(df.test_result == “fail”)[‘sn’]
    only_pass_count = len(
        df_pass_sn.subtract(df_fail_sn)
    )  # count of devices with only pass records
    first_pass_yield = only_pass_count * 100 / total_count
    output_df = spark.createDataFrame(
        [
            (ds, station_type, only_pass_count, total_count, first_pass_yield),
        ],
        ["ds", "station_type", "first_pass_count", "total_count", "first_pass_yield"],
    )

    # convert spark dataframe to dynamic frame
    output_dyf = DynamicFrame.fromDF(output_df, glueContext, "daily_first_pass_yield")
    # write results to glue catalog
    glueContext.write_dynamic_frame.from_catalog(
        frame=output_dyf,
        database="database",
        table_name="daily_first_pass_yield",
    )
