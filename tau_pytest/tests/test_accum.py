# import pytest
#
# # test pattern used is - arrange-act-assert
# # its a classic 3 steps pattern to functional tests cases:
# # 1. arrange assets for the tests
# # 2. act by asserting the target behaviour
# # 3  assert that expected outcome happened
#
# # independent  & atomic tests make failure analysis easier when later doing regression
#
# from tau_pytest.stuff.accum import Accumulator
#
#
# def test_accumulator_init():
#     accum = Accumulator()
#     assert accum.count == 0
#
# def test_accumulator_add_one():
#     accum = Accumulator()
#     accum.add()
#     assert accum.count == 1
#
# def test_accumulator_add_three():
#     accum = Accumulator()
#     accum.add(3)
#     assert accum.count == 3
#
# def test_accumulator_add_twice():
#     accum = Accumulator()
#     accum.add()
#     accum.add()
#     assert accum.count == 2
#
# def test_accumulator_cannot_set_count_directly():
#     accum = Accumulator()
#     with pytest.raises(AttributeError, match=r"property of 'Accumulator' object has no setter"):
#         accum.count = 10
#
#
#



