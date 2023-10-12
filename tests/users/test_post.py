import pytest
from src.baseclasses.response import Response, Response_json
from src.pydantic_schemas.get_accounts import *


def test_post_createAccount(post_createAccount):
    """
    Тест валидация POST createAccount
    :param post_createAccount:
    :return:
    """
    test_object = Response_json(post_createAccount)
    test_object.assert_status_code(200).validate(Accounts_accountsID)


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
    :param post_deposit:
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
    :param post_transfer:
    :return:
    """
    test_object = Response(post_update_info['response'])
    test_object.assert_status_code(200).validate_str()


def test_requestloan(post_requestloan):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    test_object = Response_json(post_requestloan)
    test_object.assert_status_code(200).validate(RequestLoan)


def test_buypositions(post_buypositions):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    print(post_buypositions['response'].text)
    test_object = Response_json(post_buypositions['response'])
    test_object.assert_status_code(200).validate(CustomerID_positions)


def test_sellpositions(post_sellpositions):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    print(post_sellpositions.text)
    test_object = Response_json(post_sellpositions)
    test_object.assert_status_code(200).validate(CustomerID_positions)


def test_billpay(post_billpay):
    print(post_billpay.text)
    test_object = Response_json(post_billpay)
    test_object.assert_status_code(200).validate(Post_billpay)


def test_position_customer(get_position_customer):
    test_object = Response_json(get_position_customer)
    test_object.assert_status_code(200).validate(CustomerID_positions)


@pytest.mark.skip('Нету инфы про stardate enddate Либо не правильный positinID')
def test_position_stardate_enddate(get_position_stardate_enddate):
    print(get_position_stardate_enddate.text)
    test_object = Response_json(get_position_stardate_enddate)
    test_object.assert_status_code(200).validate(PositionId_startDate_endDate)

# # @pytest.skip
# # def test_billpay():
# #     pass
#
#

