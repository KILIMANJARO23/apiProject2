import allure
import requests

from utils.logger import Logger

"""Список HTTP методов"""

class HttpMethod:
    headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Cookie': 'chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; advref=brand_search:google-; advref_first=brand_search:google-; site_version=desktop; client_timestamp=1713694723; session=A53WpsneRNDlDxriGk0KwP; _ym_uid=1713694724702729101; _ym_d=1713694724; _ym_isad=1; _ym_visorc=b; rrpvid=193305643933410; _userGUID=0:lv9dlcf2:lqtGUaow4jPmGOT6DWkBwjmJ9aj_UfTc; rcuid=65c2400c014b856547d52ad5; _gcl_au=1.1.1187061320.1713694725; _ga=GA1.1.1012464355.1713694725; _ga=GA1.3.1012464355.1713694725; _gid=GA1.3.1448785252.1713694725; dSesn=7cef0071-65b0-f519-bb13-043de217e690; _dvs=0:lv9dlcf2:ZAq1BQvMxEd7pJqO5i3hUjDWuGcxTJK9; digi_uc=W1siY3YiLCIyOTA1ODYiLDE3MTM2OTQ4NTQ0MjRdLFsiY3YiLCI3MzUyMjkiLDE3MTM2OTQ4NjU4NTZdXQ==; _gali=city-list-modal; telemetryToken=A53WpsneRNDlDxriGk0KwPreET6ZpsSS1Cdy67F2ouEV; backendStart=1713695493811; backendEnd=1713695494308; system_id=bb91d90a3a2cf59b90128b1d15280596z1713695493; _ga_SFTLJVK4S7=GS1.1.1713694725.1.1.1713695493.60.0.0; backendEnd=1713695647691; backendStart=1713695647631; chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; client_timestamp=1713695064; session=4Ut5CIDtrv8XuCgjHv5XKU; site_version=desktop; system_id=f7602b15da0e1e257c95ed3ac17765d6z1713695647; telemetryToken=A53WpsneRNDlDxriGk0KwPUSLrqv0emoDdOl3BaPqhFv'
}

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethod.headers)
            Logger.add_response(result)
            return result



    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpMethod.headers)
            Logger.add_response(result)
            return result



    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethod.headers)
            Logger.add_response(result)
            return result



    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=HttpMethod.headers)
            Logger.add_response(result)
            return result
