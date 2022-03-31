
from bs4 import BeautifulSoup
import requests as r
from config import Config
from captcha import result
from twocaptcha import TwoCaptcha

import concurrent

from capmonster_python import RecaptchaV2Task
from python3_anticaptcha import CustomResultHandler

from python3_anticaptcha import NoCaptchaTaskProxyless

s = r.Session()


header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36'
}



solver = TwoCaptcha(Config.captcha_api)
result = solver.recaptcha(sitekey=Config.public_key,
                          url=Config.url_site)
print(result)
with open("mail.txt","r") as file:
    mails = file.readlines()
for mail in mails:
    try:
        page = s.get(Config.url_site, headers=header).text

        soup = BeautifulSoup(page, 'html.parser')
        auth_token = soup.find('input')['value']
        # custom_result = CustomResultHandler.CustomResultHandler(
        #     anticaptcha_key=Config.captcha_api
        # )
        #
        # result = NoCaptchaTaskProxyless.NoCaptchaTaskProxyless(anticaptcha_key=Config.captcha_api) \
        #     .captcha_handler(websiteURL=Config.url_site,
        #                      websiteKey=Config.public_key)


        params = {
            "authenticity_token": auth_token,
            "t": "new",
            "email": mail,
            # "g-recaptcha-response": result['solution']['gRecaptchaResponse'],
            "g-recaptcha-response": result['code'],
            "commit": "SEND REGISTRATION MAIL"
        }

        send = s.post(Config.url_reg, params=params, headers=header)

        print(send, send.text)
    except:
        print("error")

