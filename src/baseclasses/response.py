import allure


@allure.step('Response')
class Response:
    @allure.step('Initialization TEXT, STATUS CODE')
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        self.response_text = response.text

    @allure.step('Assert status code')
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, f'Error status code {self.response_status} != {status_code}'
        return self

    @allure.step('Validate response string')
    def validate_str(self, assert_test):
        assert self.response_text == assert_test, f'Error request text {self.response_text} != {assert_test}'
        return self


@allure.step('Response JSON')
class ResponseJson:
    @allure.step('Initialization response JSON, STATUS CODE')
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    @allure.step('Validate response JSON')
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)

    @allure.step('Assert status code')
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, 'Error status code'
        return self

    def resp_json(self):
        return self.response_json
