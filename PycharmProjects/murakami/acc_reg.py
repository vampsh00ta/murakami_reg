import requests as r
from bs4 import BeautifulSoup
from captcha import result
s = r.Session()
url = "https://murakamiflowers.kaikaikiki.com/register/register?t=bnt76Hxn7w6cCIqnsGshJZ--&u=uk_GwvXZ"
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36'
}

page = s.get(url,headers=header).text
class Var:
    t = ''
    u = ''
    token = ''

page = s.get(url,headers=header).text
soup = BeautifulSoup(page, 'html.parser')
for i in soup.find_all("input"):
    try:
        if i['name'] == "t":
            Var.t = i["value"]
        if  i['name'] == "u":
            Var.u = i["value"]
        if i["name"] ==  "authenticity_token":
            Var.token = i["value"]
    except:
        pass

params = {
    "authenticity_token": Var.token,
    "user[email]": "dolboeb148822814881@gmail.com",
    "user[name]": "Vlad",
    "user[metamask_wallet_address]": "0x1084C6c33901111B0e04035949964Cd348Db6bF3",
    "user[password]": "Terminator2020",
    "user[password_confirmation]": "Terminator2020",
    "g-recaptcha-response":result['code'],
    "t": Var.t,
    "u": Var.u,
    "commit": "Confirm"
}
send = s.post(url,params =params,headers=header)
print(send,send.text)