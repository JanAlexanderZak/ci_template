""" Test pytest
1. use actual, expected, messages
2. approximate
3. assert instance!
4. with statement for exeptions / xfail

"""
import pytest

from src.calculator import (
    add,
    read_json,
    Calculator, 
    CalculatorError,
    MysteryError,
)


@pytest.mark.xfail(reason="TODO")
def test_construction():
    calculator = Calculator(1, 1)
    actual = 1
    expected = 1
    message = f"{actual} does not equal to {expected}"
    
    assert calculator.x == 1, message
    assert calculator.y == 1, "Does not equal!"
    with pytest.raises(TypeError) as exception_msg:
        # raise value error here, gets silenced
        # produce a value error with a function
        #raise TypeError
        calculator.x + "s" == 2


class TestAdd:
    # Describe in string and pass list of tuples.
    @pytest.mark.parametrize(
        'a, b, expected', [
            (1, 1, 2),
            (2, 3, 5),
        ]
    )
    def test_with_param(self, a, b, expected):
        assert add(a, b) == expected

    def test_add(self):
        assert add(1, 2) == 3

    def test_add_more(self):
        assert add(1, 100) == 101

    def test_error(self):
        # Catch the error. Test expects the MysteryError.
        with pytest.raises(MysteryError):
            add(99, 1)


def test_fixture(my_fixture):
    assert my_fixture == 42


def test_something_else(tmpdir):
    #create a file "myfile" in "mydir" in temp folder
    f1 = tmpdir.mkdir("mydir").join("myfile")

    #create a file "myfile" in temp folder
    f2 = tmpdir.join("myfile")

    #write to file as normal 
    f1.write("text to myfile")

    assert f1.read() == "text to myfile"

def test_add():
    calculator = Calculator(2, 3)

    result = calculator.add(2, 3)
    assert result == pytest.approx(5, rel=1e-3, abs=1e-3)


def test_subtract():
    calculator = Calculator(9, 3)

    result = calculator.subtract()
    assert result == 6


def test_add_weird_stuff():
    calculator = Calculator(2, 2)

    with pytest.raises(CalculatorError) as context:
        result = calculator.add('two', 'three')
        print(result)

    assert str(context.value) == "two is not a number"
