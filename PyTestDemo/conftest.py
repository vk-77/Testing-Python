import pytest


@pytest.fixture(scope="class") #when before fixure method should be executed only once.
def setup():
    print(" I will be executing first")
    yield  #Post tear down methods will be executed after this.
    print("I will be executed last")


@pytest.fixture
def dataLoad():
    print("User Profile data is being created.")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Vishal","Kumar"),("Firefox","QA"),("IE","SS")])  #Parameterization in fixtures
def crossBrowser(request): #only when you have fixture with some value available.
    return request.param


