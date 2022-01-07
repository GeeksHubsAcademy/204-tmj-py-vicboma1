import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):

    def test_apply_1(self):
        expected = "[6, 4, -5]"
        result = apply("3 -5 4 2 6 3 1")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_2(self):
        expected = "[25, 3, -78]"
        result = apply("0 0 3 5 -78 25")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_3(self):
        expected = "[9, 1, -5]"
        result = apply("1 9 3 4 -5")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_4(self):
        expected = "[100, 1, -7]"
        result = apply("100 2 1 5 8 -5 -7")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_5(self):
        expected = "[77, 4, 0]"
        result = apply("50 10 2 0 4 1 77 58")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_6(self):
        expected = "[0, 0, 0]"
        result = apply("0")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_7(self):
        expected = "[0, 0, 0]"
        result = apply("0 0 0")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_8(self):
        expected = "[584, 1, -85]"
        result = apply("584 241 0 1 -52 -85 -41 5 0")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_9(self):
        expected = "[95, 5, -9]"
        result = apply("50 20 14 05 95 -9 0 5")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_10(self):
        expected = "[410, -5, -85]"
        result = apply("410 25 95 3 -5 -85 14 10")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_11(self):
        expected = "[-1, -10, -524]"
        result = apply("-25 -1 -20 -524 -10 -5")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 


if __name__ == '__main__':
	unittest.main()