from src.generators_user.generate_user import User


SERVICE_URL = 'https://parabank.parasoft.com/parabank/services/bank'
URL_MAIN = f'https://parabank.parasoft.com/parabank/index.htm'


log = 'asda'
account_id = 13677
customers_id = 12545
transactionsID = 14476
amount = 111
transaction_type = "CREDIT" # хз что тут
month = "10" # хз что тут
from_date = '01-01-1990'
to_date = '01-01-2040'
on_date = '10-05-2023'
user_name = log
password = log


SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS = f'{SERVICE_URL}/accounts/{account_id}/transactions'
SERVICE_URL_GET_CUSTOMERS_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/{customers_id}/accounts'
SERVICE_URL_GET_ACCOUNTS_ACCOUNTID = f'{SERVICE_URL}/accounts/{account_id}'
SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/{account_id}/transactions/amount/{amount}'
SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/{account_id}/transactions/month/{month}/type/{transaction_type}'
SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/{account_id}/transactions/fromDate/{from_date}/toDate/{to_date}'
SERVICE_URL_GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE = f'{SERVICE_URL}/accounts/{account_id}/transactions/onDate/{on_date}'

SERVICE_URL_GET_CUSTOMER_CUSTOMERID = f'{SERVICE_URL}/customers/{customers_id}'
SERVICE_URL_GET_CUSTOMER_CUSTOMERID_POSITIONS = f'{SERVICE_URL}/customers/{customers_id}/positions'
SERVICE_URL_GET_CUSTOMER_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/{customers_id}/accounts'

SERVICE_URL_GET_POSITINS_CUSTOMERID = f'{SERVICE_URL}/customers/{customers_id}/positions'

SERVICE_URL_GET_MISC = f'{SERVICE_URL}/login/{user_name}/{password}'

SERVICE_URL_GET_TRANSACTIONS_TRANSACTIONSID = f'{SERVICE_URL}/transactions/{transactionsID}'
SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS = f'{SERVICE_URL}/accounts/{account_id}/transactions'
SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/{account_id}/transactions/amount/{amount}'
SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/{account_id}/transactions/month/{month}/type/{transaction_type}'
SERVICE_URL_GET_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/{account_id}/transactions/fromDate/{from_date}/todate/{to_date}'
