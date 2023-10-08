import pytest
import requests
import time

from configuration import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.generators_user.generate_user import User
from src.baseclasses.response import Response, Response_json

@pytest.fixture
def create_account():

    global account_id
    if account_id != 0:
        return account_id

    browser = webdriver.Chrome()
    browser.get(URL_MAIN)

    # create field registration
    user = User().get_Password_Confirm('ss').get_Username('ss').build()
    #user = User().build()

    #registration
    browser.find_element(By.LINK_TEXT, 'Register').click()
    browser.find_element(By.ID, 'customer.firstName').send_keys(user['First_name'])
    browser.find_element(By.ID, 'customer.lastName').send_keys(user['Last_name'])
    browser.find_element(By.ID, 'customer.address.street').send_keys(user['Address'])
    browser.find_element(By.ID, 'customer.address.city').send_keys(user['City'])
    browser.find_element(By.ID, 'customer.address.state').send_keys(user['State'])
    browser.find_element(By.ID, 'customer.address.zipCode').send_keys(user['Zip code'])
    browser.find_element(By.ID, 'customer.phoneNumber').send_keys(user['Phone'])
    browser.find_element(By.ID, 'customer.ssn').send_keys(user['SSN'])
    browser.find_element(By.ID, 'customer.username').send_keys(user['Password'])
    browser.find_element(By.ID, 'customer.password').send_keys(user['Password'])
    browser.find_element(By.ID, 'repeatedPassword').send_keys(user['Confirm'])
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input').click()
    time.sleep(1)

    #find account_id
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[2]/a').click()
    time.sleep(1)
    account_id = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    browser.quit()

    # return {'account_id' : account_id,
    #         'Password' : user['Password'],
    #         'Username' : user['Username']
    #         }
    return account_id


# need account_id
@pytest.fixture
def get_accounts_accountID_transactions(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS.format(create_account), headers={'Accept': 'application/json'})
    return response


# need account_id, add in conftest customer_id
@pytest.fixture
def get_accounts_accountID(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID.format(create_account), headers={'Accept': 'application/json'})
    customer = response.json()['customerId']
    return {'response': response, 'customerId': customer}




# need account_id, amount
@pytest.fixture
def get_accounts_accountID_transactions_amount(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT.format(create_account, amount), headers={'Accept': 'application/json'})
    return response


# need customerId
@pytest.fixture
def get_customers_customerID_accounts(get_accounts_accountID):
    response = requests.get(url=GET_CUSTOMERS_CUSTOMERID_ACCOUNTS.format(get_accounts_accountID['customerId']), headers={'Accept': 'application/json'})
    return response

#
# @pytest.fixture
# def get_accountID_transactions_month_type():
#     response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE, headers={'Accept': 'application/json'})
#     return response


# need account_id, from_date, to_date
@pytest.fixture
def get_accountID_transactions_fromdate_todate(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE.format(create_account, from_date, to_date), headers={'Accept': 'application/json'})
    return response

#
# @pytest.fixture
# def get_login_username_password(create_account):
#     response = requests.get(url=GET_MISC, headers={'Accept': 'application/json'})
#     return response


# need customerId
@pytest.fixture()
def get_customers_customerID_positions(get_accounts_accountID):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID_POSITIONS.format(get_accounts_accountID['customerId']), headers={'Accept': 'application/json'})
    return response


# @pytest.fixture()
# def get_transactions_transactionID():
#     response = requests.get(url=GET_TRANSACTIONS_TRANSACTIONSID, headers={'Accept': 'application/json'})
#     return response
#
#
# @pytest.fixture()
# def get_accountID_transactions_amount():
#     response = requests.get(url=GET_ACCOUNTID_TRANSACTIONS_AMOUNT, headers={'Accept': 'application/json'})
#     return response


# need account_id, on_date
@pytest.fixture()
def get_accountID_transactions_ondate(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE.format(create_account, on_date), headers={'Accept': 'application/json'})
    return response


# #test_POST
# @pytest.fixture()
# def post_createAccount():
#     response = requests.post(url=POST_CREATE_ACCOUNT, headers={'Accept': 'application/json'})
#     return response
#
#
# @pytest.fixture()
# def post_deposit():
#     response = requests.post(url=POST_DEPOSIT, headers={'Accept': 'application/json'})
#     return response
#
#
# @pytest.fixture()
# def post_withdraw():
#     response = requests.post(url=POST_WITHDRAW, headers={'Accept': 'application/json'})
#     return response
#
#
# @pytest.fixture()
# def post_transfer():
#     response = requests.post(url=POST_TRANSFER, headers={'Accept': 'application/json'})
#     return response
#
#
# @pytest.fixture()
# def post_update_info():
#     response = requests.post(url=POST_UPDATE, headers={'Accept': 'application/json'})
#     return response
