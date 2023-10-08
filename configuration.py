
SERVICE_URL = 'https://parabank.parasoft.com/parabank/services/bank'
URL_MAIN = f'https://parabank.parasoft.com/parabank/index.htm'

global account_id
account_id = 0
from_date = '01-01-1990'
to_date = '01-01-2040'
on_date = '10-08-2023'

transactionsID = 14476
amount = 111
fromAccount = 20337
toAccount = 20448
transaction_type = "CREDIT" # хз что тут
month = "10" # хз что тут


newAccountType = 0
log = 'asda'
user_name = log
password = log
a = 'a'

customers_id = 15209

GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS = f'{SERVICE_URL}/accounts/' + '{}/transactions'
GET_CUSTOMERS_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_ACCOUNTS_ACCOUNTID = f'{SERVICE_URL}' + '/accounts/{}'

GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/' + '{}/transactions/amount/{}'
#GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/{account_id}/transactions/month/{month}/type/{transaction_type}'
GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/fromDate/{}/toDate/{}'
GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/onDate/{}'

GET_CUSTOMER_CUSTOMERID = f'{SERVICE_URL}/customers/{customers_id}'
GET_CUSTOMER_CUSTOMERID_POSITIONS = f'{SERVICE_URL}/customers/' + '{}/positions'
GET_CUSTOMER_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/{customers_id}/accounts'

#GET_POSITINS_CUSTOMERID = f'{SERVICE_URL}/customers/{customers_id}/positions'

GET_MISC = f'{SERVICE_URL}/login/' + '{}/{}'

GET_TRANSACTIONS_TRANSACTIONSID = f'{SERVICE_URL}/transactions/{transactionsID}'
GET_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/{account_id}/transactions/amount/{amount}'
GET_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/{account_id}/transactions/fromDate/{from_date}/todate/{to_date}'

POST_CREATE_ACCOUNT = f'{SERVICE_URL}/createAccount?customerId={customers_id}&newAccountType={newAccountType}&fromAccountId={account_id}'
POST_DEPOSIT = f'{SERVICE_URL}/deposit?accountId={account_id}&amount={amount}'
POST_WITHDRAW = f'{SERVICE_URL}/withdraw?accountId={account_id}&amount={amount}'
POST_TRANSFER = f'{SERVICE_URL}/transfer?fromAccountId={fromAccount}&toAccountId={account_id}&amount={amount}'
#POST_BILLPAY = f'{SERVICE_URL}'
POST_UPDATE = f'{SERVICE_URL}/customers/update/{customers_id}?firstName={a}&lastName={a}&street={a}&city={a}&state={a}&zipCode={a}&phoneNumber={a}&ssn={a}&username={a}&password={a}'
POST_REQUESTLOAN = f''