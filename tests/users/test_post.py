import allure
import pytest

from src.baseclasses.response import Response, ResponseJson
from src.pydantic_schemas.get_accounts import *


@allure.feature('Tests post request')
class TestPost:

    @allure.title('Post create account')
    def test_post_create_account(self, post_create_account):
        test_object = ResponseJson(post_create_account)
        test_object.assert_status_code(200).validate(AccountsAccountsID)

    @allure.title('Post deposit')
    def test_post_deposit(self, post_deposit):
        test_object = Response(post_deposit)
        test_object.assert_status_code(200).validate_str()

    @allure.title('Post withdraw')
    def test_post_withdraw(self, post_withdraw):
        test_object = Response(post_withdraw)
        test_object.assert_status_code(200).validate_str()

    @allure.title('Post transfer')
    def test_post_transfer(self, post_transfer):

        test_object = Response(post_transfer)
        test_object.assert_status_code(200).validate_str()

    @allure.title('Post update info')
    def test_post_update_info(self, post_update_info):
        test_object = Response(post_update_info['response'])
        test_object.assert_status_code(200).validate_str()

    @allure.title('Post request loan')
    def test_request_loan(self, post_request_loan):
        test_object = ResponseJson(post_request_loan)
        test_object.assert_status_code(200).validate(RequestLoan)

    @allure.title('Post buy positions')
    def test_buy_positions(self, post_buy_positions):
        test_object = ResponseJson(post_buy_positions['response'])
        test_object.assert_status_code(200).validate(CustomerIDPositions)

    @allure.title('Post sell positions')
    def test_sell_positions(self, post_sell_positions):
        test_object = ResponseJson(post_sell_positions)
        test_object.assert_status_code(200).validate(CustomerIDPositions)

    @allure.title('Post bill pay')
    def test_bill_pay(self, post_bill_pay):
        test_object = ResponseJson(post_bill_pay)
        test_object.assert_status_code(200).validate(PostBillPay)

    @allure.title('Post positions customer')
    def test_position_customer(self, get_position_customer):
        test_object = ResponseJson(get_position_customer)
        test_object.assert_status_code(200).validate(CustomerIDPositions)

    @pytest.mark.skip('Нет информации про star_date end_date. Либо не тот positionID')
    @allure.title('Post positions stardate enddate')
    def test_position_start_date_end_date(self, get_position_star_date_end_date):
        print(get_position_star_date_end_date.text)
        test_object = ResponseJson(get_position_star_date_end_date)
        test_object.assert_status_code(200).validate(PositionIDStartDateEndDate)

