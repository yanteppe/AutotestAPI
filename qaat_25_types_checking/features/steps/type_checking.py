import requests
from behave import *
from jsonschema import validate

from work_tasks.qaat_25_types_checking.schemas.schema_type_checking import correct_schema


@given("token authorization")
def tokenAuthorization(context):
    url = "http://discovery-stb3.ertelecom.ru/"
    api_path = "api/token/device"
    token_parameters = "?client_id=er_ottweb_device&timestamp=1500979473&device_id=123"

    request_token = requests.get(url + api_path + token_parameters)
    get_token = request_token.json()
    token = get_token["token"]
    return token


@when("send request")
def sendRequest(context):
    url = "http://discovery-stb3.ertelecom.ru/api/v3/pages/library"
    headers = {"X-Auth-Token": tokenAuthorization(context), "view": "stb3"}

    request = requests.get(url, headers=headers)
    response = request.json()
    return response


@then("validation response schema")
def validationSchema(context):
    validate(sendRequest(context=sendRequest), correct_schema)


@then("get all showcases types")
def getShowcases(context):
    responseJson = sendRequest(context)

    showcase_list = []
    for key_1 in responseJson["data"]["showcases"]:
        showcase_list.append(key_1["type"])

    return showcase_list


def getChekingTypes(value):
    responseJson = sendRequest(context=sendRequest)

    showcases_list = []
    item_list = []
    for i in responseJson["data"]["showcases"]:
        showcases_list.append(i["type"])

        for j in i["items"]:
            item_list.append(j["type"])
            break

    if value == 'showcase':
        return showcases_list
    elif value == "item":
        return item_list


expectedShowcas = getChekingTypes('showcase')
expectedItem = getChekingTypes('item')


@then('validation types showcases and items')
def validationTypes(context):
    responseJson = sendRequest(context=sendRequest)

    for expected_i in expectedShowcas:
        for actual_i in responseJson["data"]["showcases"]:

            if expected_i == actual_i["type"]:

                for expected_j in expectedItem:
                    for actual_j in expectedItem:

                        if actual_j == expected_j:
                            assert expected_j == actual_j
