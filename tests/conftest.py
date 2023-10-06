import pytest
import requests

from configuration import SERVICE_URL, SERVICE_URL_GET_CUSTOMER_CUSTOMERID, SERVICE_URL_GET_CUSTOMER_CUSTOMERID_ACCOUNTS, SERVICE_URL_GET_CUSTOMER_CUSTOMERID_POSITIONS


@pytest.fixture
def get_customer_customerid_accounts():
    response = requests.get(url=SERVICE_URL_GET_CUSTOMER_CUSTOMERID_ACCOUNTS, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_customer_customerid():
    response = requests.get(url=SERVICE_URL_GET_CUSTOMER_CUSTOMERID, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_customer_customerid_position():
    response = requests.get(url=SERVICE_URL_GET_CUSTOMER_CUSTOMERID_POSITIONS, headers={'Accept': 'application/json'})
    return response
