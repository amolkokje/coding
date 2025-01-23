"""
Database:
- can have multiple tables
- loose schema: can add empty rows, no type checking on rows, no PK concept, no index concept, can have duplicate rows
- filter data based on WHERE clause: <,>,= operators
- return data in ASC, DESC order

NOTE: based on the description, seems like a NoSQL database.
"""

from typing import List, Dict, Any, Tuple
from collections import defaultdict


class Database:

    def __init__(self) -> None:
        self.data = defaultdict(list)

    def insert(self, table: str, row: List[dict]) -> None:
        self.data[table].extend(row)

    def row_condition_check(self, row: Dict[str, Any], where: Tuple) -> bool:
        # print(f"row_condition_check: row: {row}, where: {where}")
        column, operator, value = where

        # corner case: if column is not in the row, return True, so that the row is not filtered out
        if column not in row:
            return True

        if operator == "=":
            return row[column] == value
        elif operator == ">":
            return row[column] > value
        elif operator == "<":
            return row[column] < value
        return False

    def query(
        self,
        table: str,
        columns: List[str],
        where: List[Tuple] = [],
        sort: Tuple = ("", ""),
    ) -> List[dict]:
        """

        Args:
            table: table name
            columns: list of columns to select
            where: list of tuples (column, operator, value) to filter data. e.g. [('age', '>', 18), ('name', '=', 'John')]
            sort: tuple (column, order) to sort data. e.g. ('age', 'ASC') or ('age', 'DESC')
        """

        result = []
        for row in self.data[table]:

            # check if row matches all where conditions
            condition_check_result = True
            for where_condition in where:
                # rrr = self.row_condition_check(row, where_condition)
                # print(f"** row={row}, where_condition={where_condition}, result: {rrr}")
                if self.row_condition_check(row, where_condition) is False:
                    condition_check_result = False
                    break

            if condition_check_result is False:
                continue

            # if row matches all where conditions, add it to the result
            result.append({column: row[column] for column in columns if column in row})

        print(f"result: {result}")

        # --------------------------------------------------------
        # SORTING

        # if no sort is specified, return the result as is
        if sort == ("", ""):
            return result

        # sort the result based on the sort column and order
        # NOTE: this sorting also works for strings, not just numbers

        # sort the columns that have the sort column
        sort_column, sort_order = sort

        # get all the dicts that have the sort column
        result_with_sort_column = [row for row in result if sort_column in row]
        result_without_sort_column = [row for row in result if sort_column not in row]

        if sort_order == "ASC":
            result_with_sort_column.sort(key=lambda x: x[sort_column])
        elif sort_order == "DESC":
            result_with_sort_column.sort(key=lambda x: x[sort_column], reverse=True)

        # merge the two lists
        result = result_with_sort_column + result_without_sort_column

        # print(f"sorted: result: {result}")

        return result


# --------------------------------------------------------
# Test cases

db = Database()

# insert
assert (
    db.insert("users", [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}])
    is None
)
assert (
    db.insert("users", [{"name": "John1", "age": 25}, {"name": "Jane1", "age": 30}])
    is None
)
assert db.insert("users", [{}, {}]) is None

# query
# - print everything
assert db.query("users", ["name", "age"]) == [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "John1", "age": 25},
    {"name": "Jane1", "age": 30},
    {},
    {},
]
# - 1 where condition
assert db.query("users", ["name", "age"], [("age", ">", 18)]) == [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "John1", "age": 25},
    {"name": "Jane1", "age": 30},
    {},
    {},
]
# - 2 where conditions
assert db.query(
    "users", ["name", "age"], [("age", ">", 18), ("name", "=", "John")]
) == [{"name": "John", "age": 25}, {}, {}]

# sort
# - ASC
assert db.query("users", ["name", "age"], [("age", ">", 18)], ("age", "ASC")) == [
    {"name": "John", "age": 25},
    {"name": "John1", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Jane1", "age": 30},
    {},
    {},
]
assert db.query("users", ["name", "age"], sort=("age", "ASC")) == [
    {"name": "John", "age": 25},
    {"name": "John1", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Jane1", "age": 30},
    {},
    {},
]
# - DESC
assert db.query("users", ["name", "age"], [("age", ">", 18)], ("age", "DESC")) == [
    {"name": "Jane", "age": 30},
    {"name": "Jane1", "age": 30},
    {"name": "John", "age": 25},
    {"name": "John1", "age": 25},
    {},
    {},
]


print("All tests passed!")
