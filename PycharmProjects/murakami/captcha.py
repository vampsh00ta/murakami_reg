from config import Config
from twocaptcha import TwoCaptcha
config = {
            'server': '2captcha.com',
            'apiKey': "5231070f6df23711d2b2afb8dfb3d4d2",
            'callback': 'https://murakamiflowers.kaikaikiki.com/register/new',
            'defaultTimeout': 120,
            'recaptchaTimeout': 600,
            'pollingInterval': 10,
}
solver = TwoCaptcha(**config)

result = solver.recaptcha(sitekey="6LeoiQ4eAAAAAH6gsk9b7Xh7puuGd0KyfrI-RHQY",url = "https://murakamiflowers.kaikaikiki.com/register/new")
