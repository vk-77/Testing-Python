import pytest


@pytest.fixture()
def setup():
    print(" I will be executing first")
    yield  #Post tear down methods will be executed after this.
    print("I will be executed last")