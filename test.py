import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_correctly(self):
        self.calc.division(self, 25, 5) == 5

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self,3, 1) == 2

    def test_adding_success(self):
        assert self.calc.adding(self,3, 1) == 4



    def teardown(self):
        print('Выполнение метода Teardown')