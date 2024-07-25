import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_object.data import Urls
from page_object.helpers import Helpers


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    driver.get(Urls.URL)
    yield driver
    driver.quit()

@pytest.fixture()
def user_credentials():
    # генерируем email, password, name
    def generate_payload():
        email = Helpers.generate_random_string(5)
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()

@pytest.fixture()
def return_data_pass(user_credentials):

    user = user_credentials

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=user)
    r = response.json()

    # создаём список, чтобы метод мог его вернуть
    data_pass = {}

    #def registration(data):
    data_pass['email'] = user['email']
    data_pass['password'] = user['password']
    data_pass['name'] = user['name']
    data_pass['accessToken'] = r['accessToken']

    #registration(user)
    # возвращаем список
    yield data_pass
    response = requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': data_pass['accessToken']})

