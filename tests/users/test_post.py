import pytest
from src.baseclasses.response import Response, ResponseJson
from src.pydantic_schemas.get_accounts import *


def test_post_create_account(post_create_account):
    """
    Тест валидация POST createAccount
    :param post_create_account:
    :return:
    """
    test_object = ResponseJson(post_create_account)
    test_object.assert_status_code(200).validate(AccountsAccountsID)


def test_post_deposit(post_deposit):
    """
    Тест валидация POST deposit
    :param post_deposit:
    :return:
    """
    test_object = Response(post_deposit)
    test_object.assert_status_code(200).validate_str()


def test_post_withdraw(post_withdraw):
    """
    Тест валидация POST withdraw
    :param post_withdraw:
    :return:
    """
    test_object = Response(post_withdraw)
    test_object.assert_status_code(200).validate_str()


def test_post_transfer(post_transfer):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    test_object = Response(post_transfer)
    test_object.assert_status_code(200).validate_str()


def test_post_update_info(post_update_info):
    """
    Тест валидация POST transfer
    :param post_update_info:
    :return:
    """
    test_object = Response(post_update_info['response'])
    test_object.assert_status_code(200).validate_str()


def test_request_loan(post_request_loan):
    """
    Тест валидация POST transfer
    :param post_request_loan:
    :return:
    """
    test_object = ResponseJson(post_request_loan)
    test_object.assert_status_code(200).validate(RequestLoan)


def test_buy_positions(post_buy_positions):
    """
    Тест валидация POST transfer
    :param post_buy_positions:
    :return:
    """
    print(post_buy_positions['response'].text)
    test_object = ResponseJson(post_buy_positions['response'])
    test_object.assert_status_code(200).validate(CustomerIDPositions)


def test_sell_positions(post_sell_positions):
    """
    Тест валидация POST transfer
    :param post_sell_positions:
    :return:
    """
    print(post_sell_positions.text)
    test_object = ResponseJson(post_sell_positions)
    test_object.assert_status_code(200).validate(CustomerIDPositions)


def test_bill_pay(post_bill_pay):
    print(post_bill_pay.text)
    test_object = ResponseJson(post_bill_pay)
    test_object.assert_status_code(200).validate(PostBillPay)


def test_position_customer(get_position_customer):
    test_object = ResponseJson(get_position_customer)
    test_object.assert_status_code(200).validate(CustomerIDPositions)


@pytest.mark.skip('Нет информации про star_date end_date. Либо не тот positionID')
def test_position_star_date_end_date(get_position_star_date_end_date):
    print(get_position_star_date_end_date.text)
    test_object = ResponseJson(get_position_star_date_end_date)
    test_object.assert_status_code(200).validate(PositionIDStartDateEndDate)

# # @pytest.skip
# # def test_bill_pay():
# #     pass
