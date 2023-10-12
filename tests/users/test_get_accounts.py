
from src.baseclasses.response import ResponseJson
from src.pydantic_schemas.get_accounts import *


def test_validate_accounts_accounts_id_transactions(get_accounts_account_id_transactions):
    """
    Тест валидация /accounts/{accountId}/transactions
    :param get_accounts_account_id_transactions:
    :return:
    """
    print(get_accounts_account_id_transactions.text)
    test_object = ResponseJson(get_accounts_account_id_transactions)
    test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)


def test_validate_customers_customer_id_accounts(get_customers_customer_id_accounts):
    """
    Тест валидация /customers/{customerId}/accounts
    :param get_customers_customer_id_accounts:
    :return:
    """
    test_object = ResponseJson(get_customers_customer_id_accounts)
    test_object.assert_status_code(200).validate(AccountsAccountsID)


def test_validate_accounts_accounts_id(get_accounts_account_id):
    """
    Тест валидация /accounts/{accountId}
    :param get_accounts_account_id:
    :return:
    """
    test_object = ResponseJson(get_accounts_account_id['response'])
    test_object.assert_status_code(200).validate(AccountsAccountsID)


def test_validate_accounts_id_transactions_amount(get_accounts_account_id_transactions_amount):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_accounts_account_id_transactions_amount:
    :return:
    """
    test_object = ResponseJson(get_accounts_account_id_transactions_amount)
    test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)


def test_validate_accounts_id_transactions_from_date_to_date(get_account_id_transactions_from_date_to_date):
    """
    Тест валидация /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}
    :param get_account_id_transactions_from_date_to_date:
    :return:
    """
    test_object = ResponseJson(get_account_id_transactions_from_date_to_date)
    test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)


def test_validate_accounts_id_transactions_on_date(get_account_id_transactions_on_date):
    """
    Тест валидация /accounts/{accountId}/transactions/onDate/{onDate}
    :param get_account_id_transactions_on_date:
    :return:
    """
    test_object = ResponseJson(get_account_id_transactions_on_date)
    test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)


def test_validate_misc_login(get_login_username_password):
    """
    Тест валидация /login/{username}/{password}
    :param get_login_username_password:
    :return:
    """
    test_object = ResponseJson(get_login_username_password)
    test_object.assert_status_code(200).validate(PostCustomerInfo)


def test_validate_transaction_transaction_id(get_transactions_transaction_id):
    """
    Test validate /transactions/{transactionId}
    :param get_transactions_transaction_id):
    :return:
    """
    test_object = ResponseJson(get_transactions_transaction_id)
    test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)


def test_validate_customer_customer_id_accounts(get_customer_customer_accounts):
    """
    Тест валидация customer_customer_id_accounts
    :param get_customer_customer_accounts:
    :return:
    """
    test_object = ResponseJson(get_customer_customer_accounts)
    test_object.assert_status_code(200).validate(AccountsAccountsID)


def test_validate_customer_customer_id(get_customer_customer):
    """
    Тест валидация customer_customer_id_accounts
    :param get_customer_customer:
    :return:
    """
    test_object = ResponseJson(get_customer_customer)
    test_object.assert_status_code(200)
    test_object.validate(PostCustomerInfo)


def test_validate_transactions_month_type(get_account_id_transactions_month_type):
    """
    Тест валидация get_accountID_transactions_month_type
    :param get_account_id_transactions_month_type:
    :return:
    """
    test_object = ResponseJson(get_account_id_transactions_month_type)
    test_object.assert_status_code(200)
    test_object.validate(AccountsAccountsIDTransactions)
