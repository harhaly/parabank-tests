import pytest
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from configuration import users, URL_MAIN, SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE, SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE, SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_MONTH_TYPE, SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_AMOUNT, SERVICE_URL_GET_TRANSACTIONS_TRANSACTIONSID, SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS, SERVICE_URL_GET_CUSTOMER_CUSTOMERID_POSITIONS, SERVICE_URL_GET_MISC,SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS, SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE, SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE, SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE ,SERVICE_URL_GET_CUSTOMERS_CUSTOMERID_ACCOUNTS ,SERVICE_URL_GET_ACCOUNTS_ACCOUNTID, SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT


@pytest.fixture
def create_account():
    browser = webdriver.Chrome()
    browser.get(URL_MAIN)

    #registration
    browser.find_element(By.LINK_TEXT, 'Register').click()
    browser.find_element(By.ID, 'customer.firstName').send_keys(users[0][0])
    browser.find_element(By.ID, 'customer.lastName').send_keys(users[0][1])
    browser.find_element(By.ID, 'customer.address.street').send_keys(users[0][2])
    browser.find_element(By.ID, 'customer.address.city').send_keys(users[0][3])
    browser.find_element(By.ID, 'customer.address.state').send_keys(users[0][4])
    browser.find_element(By.ID, 'customer.address.zipCode').send_keys(users[0][5])
    browser.find_element(By.ID, 'customer.phoneNumber').send_keys(users[0][6])
    browser.find_element(By.ID, 'customer.ssn').send_keys(users[0][7])
    browser.find_element(By.ID, 'customer.username').send_keys(users[0][8])
    browser.find_element(By.ID, 'customer.password').send_keys(users[0][9])
    browser.find_element(By.ID, 'repeatedPassword').send_keys(users[0][10])
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input').click()
    time.sleep(1)

    #find account_id
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[2]/a').click()
    time.sleep(1)
    account_id = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    browser.quit()
    return account_id


@pytest.fixture
def get_accounts_accountID_transactions():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_accounts_accountID():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_accounts_accountID_transactions_amount():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_customers_customerID_accounts():
    response = requests.get(url=SERVICE_URL_GET_CUSTOMERS_CUSTOMERID_ACCOUNTS, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_accountID_transactions_month_type():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_accountID_transactions_fromdate_todate():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE, headers={'Accept': 'application/json'})
    return response


@pytest.fixture
def get_login_username_password():
    response = requests.get(url=SERVICE_URL_GET_MISC, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_customers_customerID_positions():
    response = requests.get(url=SERVICE_URL_GET_CUSTOMER_CUSTOMERID_POSITIONS, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_accountID_transactions():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_transactions_transactionID():
    response = requests.get(url=SERVICE_URL_GET_TRANSACTIONS_TRANSACTIONSID, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_accountID_transactions_amount():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_AMOUNT, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_accountID_transactions_month_type():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_MONTH_TYPE, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_accountID_transactions_fromdate_todae():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_accountID_transactions_ondate():
    response = requests.get(url=SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE, headers={'Accept': 'application/json'})
    return response
