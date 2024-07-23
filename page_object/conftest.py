import string
import random
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_object.data import Urls


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
def register_new_user():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_payload():
        email = generate_random_string(5)
        password = generate_random_string(10)
        name = generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()

@pytest.fixture()
def return_data_pass(register_new_user):

    user = register_new_user

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=user)
    r = response.json()

    # создаём список, чтобы метод мог его вернуть
    data_pass = {}

    def registration(data):
        data_pass['email'] = data['email']
        data_pass['password'] = data['password']
        data_pass['name'] = data['name']
        data_pass['accessToken'] = r['accessToken']

    registration(user)
    # возвращаем список
    yield data_pass
    response = requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': data_pass['accessToken']})

