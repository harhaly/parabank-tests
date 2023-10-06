
class Response:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, 'Error status code'
        return self


class Response_json:
    'response with json'
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def resp_json(self):
        return self.response_json

    # def __str__(self):
    #     return(
    #         "Hi there"
    #     )
