import datetime


SERVICE_URL = 'https://parabank.parasoft.com/parabank/services/bank'
URL_MAIN = f'https://parabank.parasoft.com/parabank/index.htm'

# GET
data_create_acc = (0, 0, 0)

date_today = datetime.date.today()
on_date = f'{date_today.month}-{date_today.day}-{date_today.year}'
from_date = '01-01-1990'
to_date = '01-01-2040'
amount = 100
month = 10
transaction_type = 'Debit'

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

GET_ACCOUNTID_TRANSACTIONS = f'{SERVICE_URL}/accounts/' + '{}/transactions'
GET_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_ACCOUNTID = f'{SERVICE_URL}' + '/accounts/{}'
GET_ACCOUNTID_TRANSACTIONS_AMOUNT = f'{SERVICE_URL}/accounts/' + '{}/transactions/amount/{}'
GET_ACCOUNTID_TRANSACTIONS_MONTH_TYPE = f'{SERVICE_URL}/accounts/' + '{}/transactions/month/{}/type/{}'
GET_ACCOUNTID_TRANSACTIONS_FROMDATE_TODATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/fromDate/{}/toDate/{}'
GET_ACCOUNTID_TRANSACTIONS_ONDATE = f'{SERVICE_URL}/accounts/' + '{}/transactions/onDate/{}'
GET_CUSTOMERID = f'{SERVICE_URL}/customers/' + '{}'
GET_CUSTOMER_CUSTOMERID_ACCOUNTS = f'{SERVICE_URL}/customers/' + '{}/accounts'
GET_POSITINS_CUSTOMERID = f'{SERVICE_URL}/customers/' + '{}/positions'
GET_POSITINS_STARDATE_ENDDATE = f'{SERVICE_URL}/positions/' + '{}/{}/{}'
GET_MISC = f'{SERVICE_URL}/login/' + '{}/{}'
GET_TRANSACTIONSID = f'{SERVICE_URL}/transactions/' + '{}'

# POST
POST_CREATE_ACCOUNT = f'{SERVICE_URL}/createAccount?customerId=' + '{}&newAccountType={}&fromAccountId={}'
POST_DEPOSIT = f'{SERVICE_URL}/deposit?accountId=' + '{}&amount={}'
POST_WITHDRAW = f'{SERVICE_URL}/withdraw?accountId=' + '{}&amount={}'
POST_TRANSFER = f'{SERVICE_URL}/transfer?fromAccountId=' + '{}&toAccountId={}&amount={}'
POST_UPDATE = f'{SERVICE_URL}/customers/update/' + '{}?firstName={}&lastName={}&street={}&city={}&state={}&zipCode={}&phoneNumber={}&ssn={}&username={}&password={}'
POST_REQUESTLOAN = f'{SERVICE_URL}/requestLoan?customerId=' + '{}&amount={}&downPayment={}&fromAccountId={}'
POST_CUSTOMERID_BUYPOSITIONS = f'{SERVICE_URL}/customers/' + '{}/buyPosition?accountId={}&name={}&symbol={}&shares={}&pricePerShare={}'
POST_CUSTOMERID_SELLPOSITIONS = f'{SERVICE_URL}/customers/' + '{}/sellPosition?accountId={}&positionId={}&shares={}&pricePerShare={}'
POST_BILLPAY = f'{SERVICE_URL}/billpay' + '?accountId={}&amount={}'

POST_CLEANDB = f'{SERVICE_URL}/cleanDB'
