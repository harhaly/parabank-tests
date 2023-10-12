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

    global data_create_acc
    if data_create_acc[0] != 0:
        return data_create_acc

    # clean database
    requests.post(url=POST_CLEANDB)

    # selenium setup
    browser = webdriver.Chrome()
    browser.get(URL_MAIN)
    browser.implicitly_wait(5)

    # create field registration
    # user = User().get_Username('z').get_Password_Confirm('z').build()
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
    browser.find_element(By.ID, 'customer.phoneNumber').send_keys(user['Phone'])
    browser.find_element(By.ID, 'customer.ssn').send_keys(user['SSN'])
    browser.find_element(By.ID, 'customer.username').send_keys(user['Username'])
    browser.find_element(By.ID, 'customer.password').send_keys(user['Password'])
    browser.find_element(By.ID, 'repeatedPassword').send_keys(user['Confirm'])
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input').click()

    # find account_id
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[2]/a').click()
    time.sleep(2)
    account_id = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    time.sleep(2)

    # create second account
    browser.find_element(By.LINK_TEXT, 'Open New Account').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div/input').click()
    to_account = browser.find_element(By.CLASS_NAME, 'ng-binding').text
    time.sleep(2)

    # create transactions
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[3]/a').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="amount"]').send_keys(amount)
    dropdown = browser.find_element(By.ID, 'toAccountId')
    se = Select(dropdown)
    se.select_by_visible_text(to_account)
    browser.find_element(By.CLASS_NAME, 'button').click()

    # find transactionID
    browser.find_element(By.LINK_TEXT, 'Find Transactions').click()
    browser.find_element(By.XPATH, '//*[@id="criteria.onDate"]').send_keys(on_date)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div[5]/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[2]/a').click()
    time.sleep(2)
    transactions_id = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]').text

    # close browser
    browser.quit()

    # return {'account_id' : account_id,
    #         'Password' : user['Password'],
    #         'Username' : user['Username']
    #         }
    data_create_acc = (account_id, user['Username'], user['Password'], to_account, transactions_id)
    print(data_create_acc)
    return data_create_acc


# need account_id
@pytest.fixture
def get_accounts_account_id_transactions(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS.format(create_account[0]), headers={'Accept': 'application/json'})
    return response


# need account_id, add in contest customer_id
@pytest.fixture
def get_accounts_account_id(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID.format(create_account[0]), headers={'Accept': 'application/json'})
    customer = response.json()['customerId']
    return {'response': response, 'customerId': customer}


# need account_id, amount
@pytest.fixture
def get_accounts_account_id_transactions_amount(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT.format(create_account[0], amount), headers={'Accept': 'application/json'})
    return response


# need customerId
@pytest.fixture
def get_customers_customer_id_accounts(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMERS_CUSTOMERID_ACCOUNTS.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


# need account_id, moth, transaction_type
@pytest.fixture()
def get_account_id_transactions_month_type(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE.format(create_account[0], month, transaction_type), headers={'Accept': 'application/json'})
    return response


# need account_id, from_date, to_date
@pytest.fixture
def get_account_id_transactions_from_date_to_date(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE.format(create_account[0], from_date, to_date), headers={'Accept': 'application/json'})
    return response


# need user_name password
@pytest.fixture
def get_login_username_password(create_account):
    response = requests.get(url=GET_MISC.format(create_account[1], create_account[2]), headers={'Accept': 'application/json'})
    return response


# need transactionID
@pytest.fixture()
def get_transactions_transaction_id(create_account):
    response = requests.get(url=GET_TRANSACTIONS_TRANSACTIONSID.format(create_account[4]), headers={'Accept': 'application/json'})
    return response


# need account_id, on_date
@pytest.fixture()
def get_account_id_transactions_on_date(create_account):
    response = requests.get(url=GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE.format(create_account[0], on_date), headers={'Accept': 'application/json'})
    return response


# need customer_id
@pytest.fixture
def get_customer_customer_accounts(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID_ACCOUNTS.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


# need customer_id
@pytest.fixture
def get_customer_customer(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMER_CUSTOMERID.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


# test_POST
# customerId, need account_id, newAccountType
@pytest.fixture()
def post_create_account(create_account, get_accounts_account_id):
    response = requests.post(url=POST_CREATE_ACCOUNT.format(get_accounts_account_id['customerId'], newAccountType, format(create_account[0])), headers={'Accept': 'application/json'})
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


# need customer, user_field
@pytest.fixture()
def post_update_info(get_accounts_account_id):
    # user = User().get_Username('user').get_Password_Confirm('user').build()
    user = User().build()
    response = requests.post(url=POST_UPDATE.format(
        get_accounts_account_id['customerId'],
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
    return {'response': response, 'user': user}


# need customer, user_field
@pytest.fixture()
def post_request_loan(get_accounts_account_id, create_account):
    response = requests.post(url=POST_REQUESTLOAN.format(
        get_accounts_account_id['customerId'],
        amount,
        downPayment,
        create_account[0]
    ), headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def post_buy_positions(get_accounts_account_id, create_account):
    response = requests.post(url=POST_CUSTOMERID_BUYPOSITIONS.format(
        get_accounts_account_id['customerId'],
        create_account[0],
        name,
        symbol,
        shares_buy,
        pricePerShare
    ), headers={'Accept': 'application/json'})
    position_id = response.json()[0]['positionId']
    return {'response': response, 'positionId': position_id}


@pytest.fixture()
def post_sell_positions(get_accounts_account_id, create_account, post_buy_positions):
    response = requests.post(url=POST_CUSTOMERID_SELLPOSITIONS.format(
        get_accounts_account_id['customerId'],
        create_account[0],
        post_buy_positions['positionId'],
        shares_sell,
        pricePerShare
    ), headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def post_bill_pay(create_account):
    user = User().build()
    data_post = {
        "name": user['First_name'],
        "address": user['City'],
        "state": user['State'],
        "zipCode": user['Zip code'],
        "phoneNumber": user['Phone'],
        "accountNumber": accountNumber
    }
    response = requests.post(url=POST_BILLPAY.format(create_account[0], amount), json=data_post, headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_position_customer(get_accounts_account_id):
    response = requests.get(url=GET_POSITINS_CUSTOMERID.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


@pytest.fixture()
def get_position_star_date_end_date(post_buy_positions):
    response = requests.get(url=GET_POSITINS_POSITIONID_STARDATE_ENDDATE.format(
        post_buy_positions['positionId'],
        from_date,
        to_date
    ), headers={'Accept': 'application/json'})
    return response
