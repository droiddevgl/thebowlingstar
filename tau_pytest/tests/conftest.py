import pytest

from tau_pytest.stuff.accum import Accumulator

#pytest can handle multiple fixtures - they just required unique name
# fixtures can also handle setup and cleanup
# can be done by replacing the return statement to yield statement
# the fixture is known in python as Generator
# everything before the yield statement is the setup
# everything after the yield statement is the cleanup

@pytest.fixture
def accum():
    yield Accumulator()
    print("done with the test!")

@pytest.fixture
def accum2():
    yield Accumulator()
    print("done with the test2!")

#
# @pytest.fixture
# def accum():
#     return Accumulator()
#
# @pytest.fixture
# def accum2():
#     return Accumulator()