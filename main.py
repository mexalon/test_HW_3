from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import my_login, my_password

my_driver = webdriver.Chrome()


class YaAuth:
    def __init__(self, driver):
        self.driver = driver
        self.good_login = None
        self.good_pass = None
        self.driver.implicitly_wait(3)

    def input(self, where, what):
        element = self.driver.find_element_by_xpath(where)
        element.clear()
        element.send_keys(what)
        element.submit()

    def close(self):
        self.driver.close()

    def go_to_auth_page(self):
        self.driver.get("https://passport.yandex.ru/auth/")
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.title_is("Авторизация"))
        return "Авторизация" in self.driver.title

    def input_login(self, login):
        xpath_l = '//*[@id="passp-field-login"]'
        xpoth_p = '//*[@id="passp-field-passwd"]'
        try:
            self.input(xpath_l, login)
            self.driver.find_element_by_xpath(xpoth_p)
            self.good_login = True
        except:
            self.good_login = False

        return self.good_login

    def input_password(self, password):
        xpath_p = '//*[@id="passp-field-passwd"]'
        try:
            self.input(xpath_p, password)
            wait = WebDriverWait(self.driver, 3)
            wait.until(EC.title_is('Яндекс.Паспорт'))
            self.good_pass = True
        except:
            self.good_pass = False
        return self.good_pass

    def am_i_in(self):
        return "Яндекс.Паспорт" in self.driver.title


if __name__ == '__main__':
    auth = YaAuth(my_driver)
    print(f"Страница авторизации - {auth.go_to_auth_page()}")
    print(f"Ввод логина - {auth.input_login(my_login)}")
    print(f"Ввод пароля - {auth.input_password(my_password)}")
    print(f"Авторизация - {auth.am_i_in()}")
    auth.close()
