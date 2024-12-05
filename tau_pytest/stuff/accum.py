# to run the pytest - python3 -m pytest
# some commands available
# --exitfirst - exit if there is a fail
# --maxfail=1 - maximum fail tests to stop test
# python3 -m pytest --junit-xml report.xml - to generate a report
# configuration
# adding configuration file to the project

# to test directly only one specific test -
# python3 -m pytest tau_pytest/tests/test_accum_withfixtures.py::test_accumulator_add_three

# to filter tests - for example, test with name one
# python3 -m pytest -k one
# to filter tests - for example, test with name three
# python3 -m pytest -k three
# to filter tests - for example, test add
# python3 -m pytest -k add
# to filter tests - for example, test add but not three
# python3 -m pytest -k "add and not three"
# there is one more way to create a filter - with markers
# to add a marker - for example, @pytest.mark.math
# or @pytest.mark.parametrize('a, b, product', products)
# in addition it is required to add them to the pyttest.ini to prevent warning messages
# for example, added math, and accumulator to pytest.ini
# to run the test - use, python3 -m pytest -m accumulator
# or python3 -m pytest -m math
# it will run each test with related markers
# adding boolean expressions is available too - and or not (as with the -k filter)
# there are some more builtin markers, such as xfail- to produce an outcome if condition is not met
# skip - to always skip a test function, or skipif
#testpaths can added in ini for changing, modifying path
# install plugins to pytest - like pytest html
# pip3 install pytest-html
# generating html report
# python3 -m pytest --html=report.html
# another plugin is pytest-cov
# pip3 install pytest-cov
# to run it - python3 -m pytest --cov=stuff --cov=tests
# for this example, cov(coverage) should not be run on tests but only for product code
# to run it - python3 -m pytest --cov=stuff
# python3 -m pytest --cov=tau_pytest
# or python3 -m pytest --cov=tau_pytest/stuff --cov-report html (will generate an html report page)
# to add branch coverage -
# or python3 -m pytest --cov=tau_pytest/stuff --cov-branch
# to run tests in parallel
# pip3 install pytest-xdist
# or python3 -m pytest -n 3 (number of threads)
# BDD - Behaviour Driven Development - GHERKIN or given-when-then

# api tests with pytest
# pip3 install requests

class Accumulator:

    def __init__(self) -> None:
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1) -> None:
        self._count += more

    def multi(self, more=1) -> None:
        self._count *= more






