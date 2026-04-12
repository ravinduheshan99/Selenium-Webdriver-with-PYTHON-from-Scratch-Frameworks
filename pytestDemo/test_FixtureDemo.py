import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemoOne(self):
        print("I will be executing steps in fixtureDemo method 01")

    def test_fixtureDemoTwo(self):
        print("I will be executing steps in fixtureDemo method 02")

    def test_fixtureDemoThree(self):
        print("I will be executing steps in fixtureDemo method 03")

    def test_fixtureDemoFour(self):
        print("I will be executing steps in fixtureDemo method 04")