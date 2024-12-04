import pytest

# test pattern used is - arrange-act-assert
# its a classic 3 steps pattern to functional tests cases:
# 1. arrange assets for the tests
# 2. act by asserting the target behaviour
# 3  assert that expected outcome happened

# independent  & atomic tests make failure analysis easier when later doing regression

from tau_pytest.stuff.accum import Accumulator

# fixtures - a fixture should always return a value
@pytest.fixture()
def accum():
    return Accumulator()

# dependency injection

def test_accumulator_init(accum, accum2):
    assert accum.count == 0
@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

# def test_accumulator_cannot_set_count_directly(accum):
#     with pytest.raises(AttributeError, match=r"property of 'Accumulator' object has no setter") as e:
#         accum.count = 10


@pytest.mark.accumulator
def test_for_Jessica(accum):
    accum.add()
    accum.add()
    accum.add()
    assert accum.count == 3

@pytest.mark.accumulator
def test_for_Jessica_more(accum):
    accum.add()
    accum.add()
    accum.add()
    accum.add()
    accum.add()
    assert accum.count == 5