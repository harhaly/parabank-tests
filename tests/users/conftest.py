import pytest
import requests
import time

from configuration import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.generators_user.generate_user import User


@pytest.fixture
def create_account():

    global data
    if data [0] != 0:
        return data

    # clean database
    requests.post(url=POST_CLEANDB)

    # selenium setup
    browser = webdriver.Chrome()
    browser.get(URL_MAIN)
    browser.implicitly_wait(5)

    # create field registration
    #user = User().get_Username('z').get_Password_Confirm('z').build()
    user = User().build()


    # registration
    browser.find_element(By.LINK_TEXT, 'Register').click()
    browser.find_element(By.ID, 'customer.firstName').send_keys(user['First_name'])
    browser.find_element(By.ID, 'customer.lastName').send_keys(user['Last_name'])
    browser.find_element(By.ID, 'customer.address.street').send_keys(user['Address'])
    browser.find_element(By.ID, 'customer.address.city').send_keys(user['City'])
    browser.find_element(By.ID, 'customer.address.state').send_keys(user['State'])
    browser.find_element(By.ID, 'customer.address.zipCode').send_keys(user['Zip code'])
    # bag on the serves site: number > 20 it doesn't acc
    browser.find_element(By.ID, 'customer.phoneNumber').send_keys(user['Phone'][:20])
    browser.find_element(By.ID, 'customer.ssn').send_keys(user['SSN'])
    browser.find_element(By.ID, 'customer.username').send_keys(user['Username'])
    browser.find_element(By.ID, 'customer.password').send_keys(user['Password'])
    browser.find_element(By.ID, 'repeatedPassword').send_keys(user['Confirm'])
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input').click()
    print(user)

    # find account_id
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[2]/a').click()
    time.sleep(2)
    account_id = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    time.sleep(2)

    # create second account
    browser.find_element(By.LINK_TEXT, 'Open New Account').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div/input').click()
    toAccount = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    time.sleep(2)

    # create transactions
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[3]/a').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="amount"]').send_keys(amount)
    dropdown = browser.find_element(By.ID, 'toAccountId')
    se = Select(dropdown)
    se.select_by_visible_text(toAccount)
    browser.find_element(By.CLASS_NAME, 'button').click()

    # find transactionID
    browser.find_element(By.LINK_TEXT, 'Find Transactions').click()
    browser.find_element(By.XPATH, '//*[@id="criteria.onDate"]').send_keys(on_date)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div[5]/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[2]/a').click()
    transactionsID = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]').text

    # close browser
    browser.quit()

    # return {'account_id' : account_id,
    #         'Password' : user['Password'],
    #         'Username' : user['Username']
    #         }
    data = (account_id, user['Username'], user['Password'], toAccount, transactionsID)
    print(user)
    return data


# need account_id
@pytest.fixture
def get_accounts_accountID_transactions(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS.format(create_account[0]), headers={'Accept': 'application/json'})
    return response


# need account_id, add in conftest customer_id
@pytest.fixture
def get_accounts_accountID(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID.format(create_account[0]), headers={'Accept': 'application/json'})
    customer = response.json()['customerId']
    return {'response': response, 'customerId': customer}


# need account_id, amount
@pytest.fixture
def get_accounts_accountID_transactions_amount(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT.format(create_account[0], amount), headers={'Accept': 'application/json'})
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
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE.format(create_account[0], from_date, to_date), headers={'Accept': 'application/json'})
    return response

# need user_name password
@pytest.fixture
def get_login_username_password(create_account):
    response = requests.get(url=GET_MISC.format(create_account[1], create_account[2]), headers={'Accept': 'application/json'})
    return response


# need customerId
@pytest.fixture()
def get_customers_customerID_positions(get_accounts_accountID):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID_POSITIONS.format(get_accounts_accountID['customerId']), headers={'Accept': 'application/json'})
    return response


# need transactionID
@pytest.fixture()
def get_transactions_transactionID(create_account):
    response = requests.get(url=GET_TRANSACTIONS_TRANSACTIONSID.format(create_account[4]), headers={'Accept': 'application/json'})
    return response


# need account_id, on_date
@pytest.fixture()
def get_accountID_transactions_ondate(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE.format(create_account[0], on_date), headers={'Accept': 'application/json'})
    return response


# need customer_id
@pytest.fixture
def get_customer_customerid_accounts(get_accounts_accountID):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID_ACCOUNTS.format(get_accounts_accountID['customerId']), headers={'Accept': 'application/json'})
    return response


# need customer_id
@pytest.fixture
def get_customer_customerid(get_accounts_accountID):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID.format(get_accounts_accountID['customerId']), headers={'Accept': 'application/json'})
    return response


# test_POST
# customerId, need account_id, newAccountType
@pytest.fixture()
def post_createAccount(create_account, get_accounts_accountID):
    response = requests.post(url=POST_CREATE_ACCOUNT.format(get_accounts_accountID['customerId'], newAccountType, format(create_account[0])), headers={'Accept': 'application/json'})
    return response


# need account_id, amount
@pytest.fixture()
def post_deposit(create_account):
    response = requests.post(url=POST_DEPOSIT.format(create_account[0], amount), headers={'Accept': 'application/json'})
    return response


# need account_id, amount
@pytest.fixture()
def post_withdraw(create_account):
    response = requests.post(url=POST_WITHDRAW.format(create_account[0], amount), headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def post_transfer(create_account):
    response = requests.post(url=POST_TRANSFER.format(create_account[0], create_account[3], amount), headers={'Accept': 'application/json'})
    return response


# need customerid, user_field
@pytest.fixture()
def post_update_info(get_accounts_accountID):
    #user = User().get_Username('user').get_Password_Confirm('user').build()
    user = User().build()
    response = requests.post(url=POST_UPDATE.format(
        get_accounts_accountID['customerId'],
        user['First_name'],
        user['Last_name'],
        user['City'],
        user['State'],
        user['Zip code'],
        user['Phone'],
        user['SSN'],
        user['Username'],
        user['Password'],
        user['Confirm']
    ), headers={'Accept': 'application/json'})
    return response


# need customerid, user_field
@pytest.fixture()
def post_requestloan(get_accounts_accountID, create_account):
    response = requests.post(url=POST_REQUESTLOAN.format(
        get_accounts_accountID['customerId'],
        amount,
        downPayment,
        create_account[0]
    ), headers={'Accept': 'application/json'})
    return response
