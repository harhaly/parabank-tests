[README_ru](https://github.com/harhaly/parabank-tests/blob/master/README.md)
[Allure report](https://harhaly.github.io/parabank-tests/) | [Test case en](https://docs.google.com/spreadsheets/d/1Iu9yCDM-MTTyn3iIlj5q4Fvj2hpqVeY_/edit?usp=sharing&ouid=118116959263751703136&rtpof=true&sd=true) | [Test case ru](https://docs.google.com/spreadsheets/d/1J38to9NF8jPsy_bGJksiUTfMSK13hjPi/edit?usp=sharing&ouid=118116959263751703136&rtpof=true&sd=true)

<h1 align="center">
  <a href="https://parabank.parasoft.com/parabank/index.htm" title="Demo sire">
    <img alt="Logo" src="https://github.com/harhaly/parabank-tests/blob/master/documents/logo.gif?raw=true" width="200px" height="50px" />
  </a>
</h1>

## What is this?

A test suite for the Parabank demo site [Parabank](https://parabank.parasoft.com/parabank/admin.htm) and [Swagger Parabank REST API](https://parabank.parasoft.com/parabank/api-docs/index.html). The focus is on API testing and some UI testing. This is a personal project for educational purposes.

The tests are created using the pytest framework and utilize Requests for testing HTTP requests, Pydantic for defining schemas, and Selenium WebDriver for UI testing (Chrome only). Allure and GitHub Actions were used for [generating reports](https://harhaly.github.io/parabank-tests/). 

## Project Structure

The variables required to initialize test functions (`@pytest.fixture`) are stored in `configuration.py`. The account registration process through the UI is performed since ParaBank does not provide API registration. The process returns the variables necessary for the subsequent tests.

If some tests fail, other linked tests may also fail. For instance, the fixture `create_account` is an example of this. The tests are categorized into GET and POST requests.

## Setup

- Install Python 3.10.
- Clone this repository and navigate to it.
- Install the env package, run the following command
    ```
    sudo apt install python3-venv
    ``` 
- Create a virtual environment for Python:
    ```
    python -m venv venv
    ```
- Navigate to the directory you created and activate the virtual environment:
    ```
    source ./bin/activate
    ```
- Establishing Dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running tests

Tests can be run individually or in predefined groups. Basic commands:
- Running all tests: 
	```
	pytest tests/users
	```
- Running tests of GET-requests:
	```
	pytest tests/users/test_get_accounts.py
	``` 
- Running tests of POST-requests:
	```
	pytest tests/users/test_post.py
	```
- Running a specific test:
	```
	pytest tests/users/test_get_accounts.py::TestGet::test_validate_accounts_accounts_id
	```

## Initiating Allure report generation

### Local report

To generate reports, you must have the Allure application installed on your system. Reports can be run locally or via GitHub Actions.

1. Create a local report:
	```
	pytest --alluredir=\\allure_result tests
	```
2. Enter the following command:
	```
	allure serve 
	```
The HTML report will be automatically generated and opened in the default browser.

### GitHub Actions

1. Clone this repository into your GitHub account. Locate the file responsible for GitHub Actions. — `.github/workflows/run_test.yml`.
2. To add a secret TOKEN to your account, follow the link provided:
`https://github.com/{account_name}/{repository_name}/settings/pagesb.com/settings/tokens`
3. To run a test of your choice, navigate to the Actions tab and select Automated Test. Then, select Run Workflow.
4. To access the generated test, please follow the link.
`https://github.com/{account_name}/{repository_name}/settings/pages`

## TODO

Although many goals have been achieved, there are still additional features that I would like to add in the future when time permits.  

- [ ] Add various parameters to API requests.
- [ ] Remove import time.sleep.
- [ ]  Integration into Jenkins.
- [ ] Create a template and an example of a test case.
- [ ] Create a template and an example bug report.

## Links and Documentation on the Topic
* [Tested website](https://parabank.parasoft.com/parabank/admin.htm)
* [Tested API](https://parabank.parasoft.com/parabank/api-docs/index.html)
