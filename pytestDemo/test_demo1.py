import pytest

#Any pytest file should start with test or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only

#To run in cmd ----------> py.test -v / py.test -v -s / py.test test_demo2 -v -s
#                          py.test -k CreditCard -v -s / py.test -m smoke -v -s

#To run in powershell ---> python -m pytest -v / python -m pytest -v -s / python -m pytest test_demo2.py -v -s
#                          python -m pytest -k CreditCard -v -s / python -m pytest -m smoke -v -s

#-k stands for method ames execution, -s stands for logs in out put, -v stands for more metadata info
#You can mark (tag) tests @pytes.mark.smoke and then run with -m
#You can skip tests with @pytest.mark.skip
#@pytest.mark.xfail

#fixtures are used as setup and teardown methods for test cases - conftest file to generalize fixtures
#fixtures and make it available to all test cases (fixture name into parameter of method)
#data driven and parameterization can be done with return statements in tuple format
#When you define fixtures to class only, it will run once before class is initiated at the end

#pip install pytest-html
#py.test --html=report.html -v -s


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_secondProgramCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)