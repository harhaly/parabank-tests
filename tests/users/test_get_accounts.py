import allure

from src.baseclasses.response import ResponseJson
from src.pydantic_schemas.get_accounts import *


@allure.feature('Tests get request')
class TestGet:
    @allure.title('Get accountId transactions')
    def test_validate_accounts_accounts_id_transactions(self, get_accounts_account_id_transactions):
        test_object = ResponseJson(get_accounts_account_id_transactions)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)

    @allure.title('Get customerId account')
    def test_validate_customers_customer_id_accounts(self, get_customers_customer_id_accounts):
        test_object = ResponseJson(get_customers_customer_id_accounts)
        test_object.assert_status_code(200).validate(AccountsAccountsID)

    @allure.title('Get accountId')
    def test_validate_accounts_accounts_id(self, get_accounts_account_id):
        test_object = ResponseJson(get_accounts_account_id['response'])
        test_object.assert_status_code(200).validate(AccountsAccountsID)

    @allure.title('Get transactions amount')
    def test_validate_accounts_id_transactions_amount(self, get_accounts_account_id_transactions_amount):
        test_object = ResponseJson(get_accounts_account_id_transactions_amount)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)

    @allure.title('Get transactions from date to date')
    def test_validate_accounts_id_transactions_from_date_to_date(self, get_account_id_transactions_from_date_to_date):
        test_object = ResponseJson(get_account_id_transactions_from_date_to_date)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)

    @allure.title('Get transactions on date')
    def test_validate_accounts_id_transactions_on_date(self, get_account_id_transactions_on_date):
        test_object = ResponseJson(get_account_id_transactions_on_date)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)

    @allure.title('Get misc login')
    def test_validate_misc_login(self, get_login_username_password):
        test_object = ResponseJson(get_login_username_password)
        test_object.assert_status_code(200).validate(PostCustomerInfo)

    @allure.title('Get transactions transactionId')
    def test_validate_transaction_transaction_id(self, get_transactions_transaction_id):
        test_object = ResponseJson(get_transactions_transaction_id)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)

    @allure.title('Get customerId account')
    def test_validate_customer_customer_id_accounts(self, get_customer_customer_accounts):
        test_object = ResponseJson(get_customer_customer_accounts)
        test_object.assert_status_code(200).validate(AccountsAccountsID)

    @allure.title('Get customerId')
    def test_validate_customer_customer_id(self, get_customer_customer):
        test_object = ResponseJson(get_customer_customer)
        test_object.assert_status_code(200).validate(PostCustomerInfo)

    @allure.title('Get transactions type')
    def test_validate_transactions_month_type(self, get_account_id_transactions_month_type):
        test_object = ResponseJson(get_account_id_transactions_month_type)
        test_object.assert_status_code(200).validate(AccountsAccountsIDTransactions)
