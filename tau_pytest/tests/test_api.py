# to test this - python3 -m pytest tau_pytest/tests/test_api.py
# tavern is another python plugin for testing api, its using yaml

import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():

    # Arrange
        # base url -which is api.duckduckgo.com
        # query paramters - 2 is needed for url, q for the search phrase and the second is format
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
