import datetime


SERVICE_URL = 'https://parabank.parasoft.com/parabank/services/bank'
URL_MAIN = f'https://parabank.parasoft.com/parabank/index.htm'

# GET
data_create_acc = {'account_id': 0,
                   'Password': 0,
                   'Username': 0,
                   'to_account': 0,
                   'transactions_id': 0
                   }
date_today = datetime.date.today()
on_date = f'{date_today.month}-{date_today.day}-{date_today.year}'
month = date_today.month
from_date = '01-01-1990'
to_date = '01-01-2040'
amount = 100
transaction_type = 'Debit'

GET_ACCOUNT_TRANSACTIONS = f'{SERVICE_URL}/accounts/' + '{}/transactions'
GET_CUSTOMER_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_ACCOUNT = f'{SERVICE_URL}' + '/accounts/{}'
GET_ACCOUNT_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/' + '{}/transactions/amount/{}'
GET_ACCOUNT_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/' + '{}/transactions/month/{}/type/{}'
GET_ACCOUNT_TRANSACTIONS_FROM_DATE_TO_DATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/fromDate/{}/toDate/{}'
GET_ACCOUNT_TRANSACTIONS_ON_DATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/onDate/{}'
GET_CUSTOMER = f'{SERVICE_URL}/customers/' + '{}'
GET_CUSTOMER_CUSTOMER_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_POSITIONS_CUSTOMER = f'{SERVICE_URL}/customers/' + '{}/positions'
GET_POSITIONS_STAR_DATE_END_DATE = f'{SERVICE_URL}/positions/' + '{}/{}/{}'
GET_MISC = f'{SERVICE_URL}/login/' + '{}/{}'
GET_TRANSACTIONS = f'{SERVICE_URL}/transactions/' + '{}'

# POST
newAccountType = 0
downPayment = 50
name = 'Apple'
symbol = 'App'
shares_buy = 10
shares_sell = 5
pricePerShare = 1
accountNumber = 13333  # под ?
startDate = 1  # под ?
endDate = 1  # под ?

POST_CREATE_ACCOUNT = f'{SERVICE_URL}/createAccount?customerId=' + '{}&newAccountType={}&fromAccountId={}'
POST_DEPOSIT = f'{SERVICE_URL}/deposit?accountId=' + '{}&amount={}'
POST_WITHDRAW = f'{SERVICE_URL}/withdraw?accountId=' + '{}&amount={}'
POST_TRANSFER = f'{SERVICE_URL}/transfer?fromAccountId=' + '{}&toAccountId={}&amount={}'
POST_UPDATE = f'{SERVICE_URL}/customers/update/' + '{}?firstName={}&lastName={}&street={}&city={}&state={}&zipCode={}&phoneNumber={}&ssn={}&username={}&password={}'
POST_REQUEST_LOAN = f'{SERVICE_URL}/requestLoan?customerId=' + '{}&amount={}&downPayment={}&fromAccountId={}'
POST_CUSTOMER_BUY_POSITIONS = f'{SERVICE_URL}/customers/' + '{}/buyPosition?accountId={}&name={}&symbol={}&shares={}&pricePerShare={}'
POST_CUSTOMER_SELL_POSITIONS = f'{SERVICE_URL}/customers/' + '{}/sellPosition?accountId={}&positionId={}&shares={}&pricePerShare={}'
POST_BILL_PAY = f'{SERVICE_URL}/billpay' + '?accountId={}&amount={}'

POST_CLEAN_DB = f'{SERVICE_URL}/cleanDB'
