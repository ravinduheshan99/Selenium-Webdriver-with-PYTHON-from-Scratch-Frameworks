import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("User profile data is beign created")
    return ["Ravindu", "Haputhanthri", "rahulshettyacademy.com"]


@pytest.fixture(params=[("Chrome","Ravindu", "Haputhanthri"),"Firefox", "Edge"])
def crossBrowser(request):
    return request.param