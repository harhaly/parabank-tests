import pytest
import json


from src.baseclasses.response import Response, Response_json
from src.pydantic_schemas.get_accounts import *

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
    test_object = Response_json(get_customers_customerID_accounts)
    test_object.assert_status_code(200).validate(Accounts_accountsID)


def test_validate_accounts_accountsID(get_accounts_accountID):
    """
    Тест валидация /accounts/{accountId}
    :param get_accounts_accountID:
    :return:
    """
    test_object = Response_json(get_accounts_accountID['response'])
    test_object.assert_status_code(200).validate(Accounts_accountsID)


def test_validate_accountsID_transactions_amount(get_accounts_accountID_transactions_amount):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_accountID_transactions_fromdate_todate:
    :return:
    """
    test_object = Response_json(get_accounts_accountID_transactions_amount)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)



def test_validate_accountsID_transactions_fromdate_todate(get_accountID_transactions_fromdate_todate):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_accountID_transactions_fromdate_todate:
    :return:
    """
    test_object = Response_json(get_accountID_transactions_fromdate_todate)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)



def test_validate_accountsID_transactions_ondate(get_accountID_transactions_ondate):
    """
    Тест валидация /accounts/{accountId}/transactions/onDate/{onDate}
    :param get_accountID_transactions_ondate:
    :return:
    """
    test_object = Response_json(get_accountID_transactions_ondate)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)


def test_validate_misc_login(get_login_username_password):
    """
    Тест валидация /login/{username}/{password}
    :param get_login_username_password:
    :return:
    """
    test_object = Response_json(get_login_username_password)
    test_object.assert_status_code(200).validate(Post_custoner_info)


def test_validate_transtactions_transtactionID(get_transactions_transactionID):
    """
    Test validate /transactions/{transactionId}
    :param get_accountID_transactions:
    :return:
    """
    test_object = Response_json(get_transactions_transactionID)
    test_object.assert_status_code(200).validate(Accounts_accountsID_transactions)


def test_validate_customer_customerid_accounts(get_customer_customerid_accounts):
    """
    Тест валидация customer_customerid_accounts
    :param get_customers_id:
    :return:
    """
    test_object = Response_json(get_customer_customerid_accounts)
    test_object.assert_status_code(200).validate(Accounts_accountsID)


def test_validate_customer_customerid(get_customer_customerid):
    """
    Тест: валидация на значения в полях json customer_customerid_accounts
    :param get_customer_customerid:
    :return:
    """
    test_object = Response_json(get_customer_customerid)
    test_object.assert_status_code(200)
    test_object.validate(Post_custoner_info)


def test_validate_transactions_month_type(get_accountID_transactions_month_type):
    """
    Тест: валидация на значения в полях json get_accountID_transactions_month_type
    :param get_accountID_transactions_month_type:
    :return:
    """
    test_object = Response_json(get_accountID_transactions_month_type)
    test_object.assert_status_code(200)
    test_object.validate(Accounts_accountsID_transactions)


