import pytest


from src.baseclasses.response import Response, Response_json
from src.pydantic_schemas.get_accounts import *
from src.pydantic_schemas.get_customers import Post, Post_custoner_info, Post_customers_customersId_positions

def test_validate_accounts_accountsID_transactions(get_accounts_accountID_transactions):
    """
    Тест валидация /accounts/{accountId}/transactions
    :param get_accounts_accountID_transactions:
    :return:
    """
    print(get_accounts_accountID_transactions.text)
    test_object = Response_json(get_accounts_accountID_transactions)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)


def test_validate_customers_customerID_accounts(get_customers_customerID_accounts):
    """
    Тест валидация /customers/{customerId}/accounts
    :param get_customer_customerID_accounts:
    :return:
    """
    print(get_customers_customerID_accounts.text)
    test_object = Response_json(get_customers_customerID_accounts)
    test_object.assert_status_code(200).validate(Customers_customerID_accounts)


def test_validate_accounts_accountsID(get_accounts_accountID):
    """
    Тест валидация /accounts/{accountId}
    :param get_accounts_accountID:
    :return:
    """
    print(get_accounts_accountID['response'].text)
    test_object = Response_json(get_accounts_accountID['response'])
    test_object.assert_status_code(200).validate(Accounts_accountsID)


def test_validate_accountsID_transactions_amount(get_accounts_accountID_transactions_amount):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_accountID_transactions_fromdate_todate:
    :return:
    """
    print(get_accounts_accountID_transactions_amount.text)
    test_object = Response_json(get_accounts_accountID_transactions_amount)
    test_object.assert_status_code(200).validate(AccountID_transactions_fromdate_todate)



def test_validate_accountsID_transactions_fromdate_todate(get_accountID_transactions_fromdate_todate):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_accountID_transactions_fromdate_todate:
    :return:
    """
    print(get_accountID_transactions_fromdate_todate.text)
    test_object = Response_json(get_accountID_transactions_fromdate_todate)
    test_object.assert_status_code(200).validate(AccountID_transactions_fromdate_todate)



def test_validate_accountsID_transactions_ondate(get_accountID_transactions_ondate):
    """
    Тест валидация /accounts/{accountId}/transactions/onDate/{onDate}
    :param get_accountID_transactions_ondate:
    :return:
    """
    print(get_accountID_transactions_ondate.text)
    test_object = Response_json(get_accountID_transactions_ondate)
    test_object.assert_status_code(200).validate(AccountID_transactions_ondate)


def test_validate_misc_login(get_login_username_password):
    """
    Тест валидация /login/{username}/{password}
    :param get_login_username_password:
    :return:
    """
    print(get_login_username_password.text)
    test_object = Response_json(get_login_username_password)
    test_object.assert_status_code(200).validate(Post_custoner_info)


def test_validate_customersID_positions(get_customers_customerID_positions):
    """
    Тест валидация /customers/{customerId}/positions
    :param get_customers_customerID_positions:
    :return:
    """
    print(get_customers_customerID_positions)
    print(get_customers_customerID_positions.text)
    test_object = Response_json(get_customers_customerID_positions)
    test_object.assert_status_code(200).validate(CustomerID_positions)


def test_validate_transtactions_transtactionID(get_transactions_transactionID):
    """
    Test validate /transactions/{transactionId}
    :param get_accountID_transactions:
    :return:
    """
    print(get_transactions_transactionID.text)
    test_object = Response_json(get_transactions_transactionID)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)


def test_validate_customer_customerid_accounts(get_customer_customerid_accounts):
    """
    Тест валидация customer_customerid_accounts
    :param get_customers_id:
    :return:
    """
    print(get_customer_customerid_accounts.text)
    test_object = Response_json(get_customer_customerid_accounts)
    test_object.assert_status_code(200).validate(Post)


def test_validate_customer_customerid(get_customer_customerid):
    """
    Тест: валидация на значения в полях json customer_customerid_accounts
    :param get_customer_customerid:
    :return:
    """
    print(get_customer_customerid.text)
    test_object = Response_json(get_customer_customerid)
    test_object.assert_status_code(200)
    test_object.validate(Post_custoner_info)
