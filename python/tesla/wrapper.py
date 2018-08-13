# import python modules
import unittest
import numpy as np

# import modules to test
from utils import find_mirrors, is_prime, PolygonUtils


# ----------------------------------------------------------
# TEST-1
# ----------------------------------------------------------


class IsPrime(unittest.TestCase):

    @staticmethod
    def test_is_prime():
        for i in range(1, 10):
            print "number={0}, is_prime={1}".format(i, is_prime(i))


# ----------------------------------------------------------
# TEST-2
# ----------------------------------------------------------


class FindMirrors(unittest.TestCase):

    @staticmethod
    def test_find_mirrors():
        with open("linuxwords.txt",'r') as in_file:
            with open("output.txt",'w') as out_file:
                find_mirrors(in_file, out_file)


# ----------------------------------------------------------
# TEST-4
# ----------------------------------------------------------


"""
TEST-3 --> ASSUMPTIONS, TEST CONSIDERATIONS:
- All vertices/points on boundary of Polygon is considered outside.
- All vertices and points can be integers or floating point numbers.
- It is necessary to test for both integers and floating points to see the effect on arithmetic operations
- Smoke tests are quick tests to determine if the logic works.
- In real scenarios and for testing real solutions and products, it is very important to do randomized testing with
seed inputs that generate constrained test data. This in most cases helps to get a good test coverage. In my experience
most of the hard to find product issues have been found by randomized stress testing over extended periods of time.
- Besides being able to test many cases with minimal code, it also helps to check the product stability.
"""
pu = PolygonUtils()


class IntegerPointInPolygon(unittest.TestCase):
    """
    Consists of tests with integer polygon points
    """
    # SMOKE TESTS

    @staticmethod
    def test_points_inside():
        print "TEST FOR INTEGER POINTS INSIDE POLYGON"
        polygon = [[1, 1], [1, 5], [5, 1], [5, 5]]
        points = [[2, 2], [3, 3]]
        for point in points:
            assert pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not inside the Polygon {1}". \
                format(point, polygon)

    @staticmethod
    def test_points_outside():
        print "TEST FOR INTEGER POINTS OUTSIDE POLYGON"
        polygon = [[3, 3], [3, 8], [8, 3], [8, 8]]
        points = [[2, 2], [9, 9]]
        for point in points:
            assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                format(point, polygon)

    # RANDOMIZED TESTS

    @staticmethod
    def test_points_inside_random():
        print "RANDOMIZED TEST FOR INT POINTS INSIDE POLYGON"
        polygon_size = 5
        random_tests = 10
        for i in range(5, 5+polygon_size):
            polygon = [[i, i], [i, i+polygon_size], [polygon_size+i, i], [i+polygon_size, i+polygon_size]]
            for _ in range(random_tests):
                point = [np.random.randint(i+1, i+polygon_size-1), np.random.randint(i+1, i+polygon_size-1)]
                assert pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not inside the Polygon {1}". \
                    format(point, polygon)

    @staticmethod
    def test_points_outside_random():
        print "RANDOMIZED TEST FOR INT POINTS OUTSIDE POLYGON"
        polygon_size = 5
        random_tests = 10
        for i in range(5, 5+polygon_size):
            polygon = [[i,i], [i, i+polygon_size], [polygon_size+i, i], [i+polygon_size, i+polygon_size]]
            for _ in range(random_tests):
                # lower left
                point = [np.random.randint(1, i-1), np.random.randint(1, i-1)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)
                # upper right
                point = [np.random.randint(i+polygon_size+1, i+polygon_size+20), np.random.randint(i+polygon_size+1,
                                                                                                   i+polygon_size+20)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)
                # lower right
                point = [np.random.randint(i+polygon_size+1, i+polygon_size+20), np.random.randint(1, i-1)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)
                # upper left
                point = [np.random.randint(1, i-1), np.random.randint(i+polygon_size+1, i+polygon_size+20)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)

    @staticmethod
    def test_vertices():
        print "RANDOMIZED TEST FOR CHECKING VERTICES"
        lenpoly_list = [3, 5, 7, 10, 15, 20]
        for lenpoly in lenpoly_list:
            polygon = [[np.random.randint(0, 2147483648), np.random.randint(0, 2147483648)] for _ in range(lenpoly)]
            for point in polygon:
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)


class FloatPointInPolygon(unittest.TestCase):
    """
    Consists of tests with floating point polygon points
    """
    # SMOKE TESTS

    @staticmethod
    def test_points_inside():
        print "TEST FOR FLOAT POINTS INSIDE POLYGON"
        polygon = [[1, 1], [1, 5], [5, 1], [5, 5]]
        points = [[2.5, 2.5], [4.1, 3.5]]
        for point in points:
            assert pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} is not inside the Polygon {1}".format(
                point, polygon)

    @staticmethod
    def test_points_outside():
        print "TEST FOR FLOAT POINTS OUTSIDE POLYGON"
        polygon = [[3, 3], [3, 8], [8, 3], [8, 8]]
        points = [[2.5, 2.5], [9.5, 9.5]]
        for point in points:
            assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}".format(
                point, polygon)

    # RANDOMIZED TESTS

    @staticmethod
    def test_points_inside_random():
        print "RANDOMIZED TEST FOR FLOAT POINTS INSIDE POLYGON"
        polygon_size = 5
        random_tests = 10
        for i in range(5, 5+polygon_size):
            polygon = [[i, i], [i, i+polygon_size], [polygon_size+i, i], [i+polygon_size, i+polygon_size]]
            for _ in range(random_tests):
                point = [np.random.uniform(i+1, i+polygon_size-1), np.random.uniform(i+1, i+polygon_size-1)]
                assert pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not inside the Polygon {1}".format(
                    point, polygon)

    @staticmethod
    def test_points_outside_random():
        print "RANDOMIZED TEST FOR FLOAT POINTS OUTSIDE POLYGON"
        polygon_size = 5
        random_tests = 10
        for i in range(5, 5+polygon_size):
            polygon = [[i, i], [i, i+polygon_size], [polygon_size+i, i], [i+polygon_size, i+polygon_size]]
            for _ in range(random_tests):
                # lower left
                point = [np.random.randint(1, i-1), np.random.randint(1, i-1)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}".\
                    format(point, polygon)
                # upper right
                point = [np.random.randint(i+polygon_size+1, i+polygon_size+20), np.random.randint(i+polygon_size+1,
                                                                                                   i+polygon_size+20)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}".\
                    format(point, polygon)
                # lower right
                point = [np.random.randint(i+polygon_size+1, i+polygon_size+20), np.random.randint(1, i-1)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)
                # upper left
                point = [np.random.randint(1, i-1), np.random.randint(i+polygon_size+1, i+polygon_size+20)]
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)

    def test_vertices(self):
        print "RANDOMIZED TEST FOR CHECKING VERTICES"
        lenpoly_list = [3, 5, 7, 10, 15, 20]
        for lenpoly in lenpoly_list:
            polygon = [[np.random.uniform(0.0, 1000000.0), np.random.uniform(0.0, 1000000.0)] for _ in range(lenpoly)]
            for point in polygon:
                assert not pu.is_point_in_poly(point[0], point[1], polygon), "Point {0} not outside the Polygon {1}". \
                    format(point, polygon)






