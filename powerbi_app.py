import requests


report_url = "https://app.powerbi.com/reportEmbed?reportId=b022156d-d948-4094-9723-9294160e7c75&autoAuth=true&ctid=03c2eefa-aa8b-46a8-a766-941121ebc67c"


username = "custos@innovaagro.com.br"
password = "Cust0@2023br"


login_url = "https://login.microsoftonline.com/common/login"
login_data = {
    "loginfmt": username,
    "passwd": password,
    "RememberMe": "false"
}
session = requests.Session()
session.post(login_url, data=login_data)


response = session.get(report_url)


print(response.text)
