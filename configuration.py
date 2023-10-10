
SERVICE_URL = 'https://parabank.parasoft.com/parabank/services/bank'
URL_MAIN = f'https://parabank.parasoft.com/parabank/index.htm'

global account_id
account_id = 0
global data
data = (0, 0, 0)
on_date = '10-10-2023'
from_date = '01-01-1990'
to_date = '01-01-2040'
amount = 100

GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS = f'{SERVICE_URL}/accounts/' + '{}/transactions'
GET_CUSTOMERS_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_ACCOUNTS_ACCOUNTID = f'{SERVICE_URL}' + '/accounts/{}'

GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/' + '{}/transactions/amount/{}'
#GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/{account_id}/transactions/month/{month}/type/{transaction_type}'
GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/fromDate/{}/toDate/{}'
GET_ACCOUNTS_ACCOUNTID_TRANSACTIONS_ONDATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/onDate/{}'

GET_CUSTOMER_CUSTOMERID = f'{SERVICE_URL}/customers/' + '{}'
GET_CUSTOMER_CUSTOMERID_POSITIONS = f'{SERVICE_URL}/customers/' + '{}/positions'
GET_CUSTOMER_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'

# positionID from post
#GET_POSITINS_CUSTOMERID = f'{SERVICE_URL}/customers/{customers_id}/positions'
#GET_POSITINS_POSITIONID_STARDATE_ENDDATE = f'{SERVICE_URL}/positions/{positionId}/{startDate}/{endDate}

GET_MISC = f'{SERVICE_URL}/login/' + '{}/{}'

GET_TRANSACTIONS_TRANSACTIONSID = f'{SERVICE_URL}/transactions/' + '{}'


fromAccount = 20337
newAccountType = 0
a = 'a'
customers_id = 15209

POST_CREATE_ACCOUNT = f'{SERVICE_URL}/createAccount?customerId={customers_id}&newAccountType={newAccountType}&fromAccountId={account_id}'
POST_DEPOSIT = f'{SERVICE_URL}/deposit?accountId={account_id}&amount={amount}'
POST_WITHDRAW = f'{SERVICE_URL}/withdraw?accountId={account_id}&amount={amount}'
POST_TRANSFER = f'{SERVICE_URL}/transfer?fromAccountId={fromAccount}&toAccountId={account_id}&amount={amount}'
#POST_BILLPAY = f'{SERVICE_URL}'
POST_UPDATE = f'{SERVICE_URL}/customers/update/{customers_id}?firstName={a}&lastName={a}&street={a}&city={a}&state={a}&zipCode={a}&phoneNumber={a}&ssn={a}&username={a}&password={a}'
#POST_REQUESTLOAN = f''
#POST_CUSTOMERID_BUYPOSITIONS = ''
#POST_CUSTOMERID_SELPOSITIONS = ''
