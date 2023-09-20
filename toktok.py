import requests


username = "your lambdatest username"
access_token = "$w%7pxC#+hhx%b0xl&_q"


def test_get_lambdatest_all_builds():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/builds" % (username, access_token)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200