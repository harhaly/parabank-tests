import allure
import pytest
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from configuration import *
from src.generators_user.generate_user import User


@allure.step('Create account')
@pytest.fixture
def create_account():

    global data_create_acc
    if data_create_acc['Password'] != 0:
        return data_create_acc

    # clean database
    requests.post(url=POST_CLEAN_DB)

    # selenium setup
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(URL_MAIN)
    browser.implicitly_wait(5)

    with allure.step('Create all fields'):
        user = User().build()
        # user = User().get_username('aaaa').get_password_confirm('ffff').build()

    with allure.step('Registration'):
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
    with allure.step('Click button registration'):
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input').click()

    with allure.step('Find account_id'):
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[2]/a').click()
        time.sleep(2)
        account_id = browser.find_element(By.CLASS_NAME, 'ng-binding').text
        time.sleep(2)

    with allure.step('Create second account'):
        browser.find_element(By.LINK_TEXT, 'Open New Account').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div/input').click()
        to_account = browser.find_element(By.CLASS_NAME, 'ng-binding').text
        time.sleep(2)

    # create transactions
    with allure.step('Transaction'):
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[3]/a').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="amount"]').send_keys(amount)
        dropdown = browser.find_element(By.ID, 'toAccountId')
        se = Select(dropdown)
        se.select_by_visible_text(to_account)
    with allure.step('Button click transaction'):
        browser.find_element(By.CLASS_NAME, 'button').click()

    # find transactionID
    with allure.step('Find transaction'):
        browser.find_element(By.LINK_TEXT, 'Find Transactions').click()
        browser.find_element(By.XPATH, '//*[@id="criteria.onDate"]').send_keys(on_date)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div[5]/button').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[2]/a').click()
        time.sleep(2)
    with allure.step('Save find element'):
        transactions_id = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]').text

    # close browser
    browser.quit()

    data_create_acc = {'account_id': account_id,
                       'Password': user['Password'],
                       'Username': user['Username'],
                       'to_account': to_account,
                       'transactions_id': transactions_id
                       }
    return data_create_acc

    # attach = browser.get_screenshot_as_png()
    # allure.attach(attach, name=f'ScreenShot {datetime.datetime.today()}', attachment_type=allure.attachment_type.PNG)


@allure.step('Response get accountId transactions, need account id from fixture @create_account')
@pytest.fixture
def get_accounts_account_id_transactions(create_account):
    response = requests.get(url=GET_ACCOUNT_TRANSACTIONS.format(create_account['account_id']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get accountId, need account id from fixture @create_account')
@pytest.fixture
def get_accounts_account_id(create_account):
    response = requests.get(url=GET_ACCOUNT.format(create_account['account_id']), headers={'Accept': 'application/json'})
    customer = response.json()['customerId']
    return {'response': response, 'customerId': customer}


@allure.step('Response get transactions_amount, need account id from fixture @create_account')
@pytest.fixture
def get_accounts_account_id_transactions_amount(create_account):
    response = requests.get(url=GET_ACCOUNT_TRANSACTIONS_AMOUNT.format(create_account['account_id'], amount), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get customerId account, need customer id from fixture @get_accounts_account_id')
@pytest.fixture
def get_customers_customer_id_accounts(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMER_ACCOUNTS.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get transactions moth type, need account id from fixture @create_account')
@pytest.fixture()
def get_account_id_transactions_month_type(create_account):
    response = requests.get(url=GET_ACCOUNT_TRANSACTIONS_MONTH_TYPE.format(create_account['account_id'], month, transaction_type), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get transactions from date to date type, need account id from fixture @create_account')
@pytest.fixture
def get_account_id_transactions_from_date_to_date(create_account):
    response = requests.get(url=GET_ACCOUNT_TRANSACTIONS_FROM_DATE_TO_DATE.format(create_account['account_id'], from_date, to_date), headers={'Accept': 'application/json'})
    return response


# need user_name password
@allure.step('Response get login username, password, need log/pass from fixture @create_account')
@pytest.fixture
def get_login_username_password(create_account):
    response = requests.get(url=GET_MISC.format(create_account['Username'], create_account['Password']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get transactionsId, need transactionId from fixture @create_account')
@pytest.fixture()
def get_transactions_transaction_id(create_account):
    response = requests.get(url=GET_TRANSACTIONS.format(create_account['transactions_id']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get transaction ondate, need account id from fixture @create_account')
@pytest.fixture()
def get_account_id_transactions_on_date(create_account):
    response = requests.get(url=GET_ACCOUNT_TRANSACTIONS_ON_DATE.format(create_account['account_id'], on_date), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get customer account, need customerId from fixture @get_accounts_account_id')
@pytest.fixture
def get_customer_customer_accounts(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMER_CUSTOMER_ACCOUNTS.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response get customer customerId, need customerId from fixture @get_accounts_account_id')
@pytest.fixture
def get_customer_customer(get_accounts_account_id):
    response = requests.get(url=GET_CUSTOMER.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


# test_POST
@allure.step('Response post create account, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def post_create_account(create_account, get_accounts_account_id):
    response = requests.post(url=POST_CREATE_ACCOUNT.format(get_accounts_account_id['customerId'], newAccountType, format(create_account['account_id'])), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post deposit, need account id from fixture @create_account')
@pytest.fixture()
def post_deposit(create_account):
    response = requests.post(url=POST_DEPOSIT.format(create_account['account_id'], amount), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post withdraw, need account id from fixture @create_account')
@pytest.fixture()
def post_withdraw(create_account):
    response = requests.post(url=POST_WITHDRAW.format(create_account['account_id'], amount), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post transfer, need account id, second accountId from fixture @create_account')
@pytest.fixture()
def post_transfer(create_account):
    response = requests.post(url=POST_TRANSFER.format(create_account['account_id'], create_account['to_account'], amount), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post update info, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def post_update_info(get_accounts_account_id):
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


@allure.step('Response post request loan, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def post_request_loan(get_accounts_account_id, create_account):
    response = requests.post(url=POST_REQUEST_LOAN.format(
        get_accounts_account_id['customerId'],
        amount,
        downPayment,
        create_account['account_id']
    ), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post buy position, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def post_buy_positions(get_accounts_account_id, create_account):
    response = requests.post(url=POST_CUSTOMER_BUY_POSITIONS.format(
        get_accounts_account_id['customerId'],
        create_account['account_id'],
        name,
        symbol,
        shares_buy,
        pricePerShare
    ), headers={'Accept': 'application/json'})
    position_id = response.json()[0]['positionId']
    return {'response': response, 'positionId': position_id}


@allure.step('Response post sell position, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def post_sell_positions(get_accounts_account_id, create_account, post_buy_positions):
    response = requests.post(url=POST_CUSTOMER_SELL_POSITIONS.format(
        get_accounts_account_id['customerId'],
        create_account['account_id'],
        post_buy_positions['positionId'],
        shares_sell,
        pricePerShare
    ), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post bill pay, need account id from fixture @create_account')
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
    response = requests.post(url=POST_BILL_PAY.format(create_account['account_id'], amount), json=data_post, headers={'Accept': 'application/json'})
    return response


@allure.step('Response post position customer, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def get_position_customer(get_accounts_account_id):
    response = requests.get(url=GET_POSITIONS_CUSTOMER.format(get_accounts_account_id['customerId']), headers={'Accept': 'application/json'})
    return response


@allure.step('Response post position start date and date, need customerId from fixture @get_accounts_account_id')
@pytest.fixture()
def get_position_start_date_end_date(post_buy_positions):
    response = requests.get(url=GET_POSITIONS_STAR_DATE_END_DATE.format(
        post_buy_positions['positionId'],
        from_date,
        to_date
    ), headers={'Accept': 'application/json'})
    return response
