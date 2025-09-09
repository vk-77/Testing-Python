#Any Pytest file should should start with test_
"""Pytest Testing framework :
- Python file name should always start with “test_”
- In Pytest testing standards - We need to write the code in functions.
- When we are declaring a function - Pytest requires a test method name, always should start with “test” keyword.
- In Pytest, every method is treated as a separate test case.
- In Pytest, we can’t have multiple methods with the same name.
If we keep the same name, then it overrides the previous result.
- Method names should make sense.
“-k” stands for the method name execution. “-s” logs in output. “-v” stands for more info metadata you can run specific file with py.test <filename>
You can mark (tag) test @pytest.mark.smoke and then run with “-m”
"""

import pytest


@pytest.mark.smoke
def test_firstProgram():   #syntax of writing funtion.
    print("Hello ")


def test_secondProgram():
    print("Good Morning on 9 Sep 2025.")