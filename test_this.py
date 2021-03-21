from secrets import my_login, my_password
from main import my_driver, YaAuth


class TestThis:
    def setup_class(self):
        self.driver = my_driver
        self.yd = YaAuth(self.driver)

    def teardown_class(self):
        self.yd.close()

    def test_go_to_auth_page(self):
        assert self.yd.go_to_auth_page()

    def test_input_bad_login(self):
        self.yd.go_to_auth_page()
        assert not self.yd.input_login('#!@#')

    def test_input_proper_login(self):
        self.yd.go_to_auth_page()
        assert self.yd.input_login(my_login)

    def test_input_bad_passw(self):
        self.yd.go_to_auth_page()
        self.yd.input_login(my_login)
        assert not self.yd.input_password('#!@#')

    def test_input_proper_passw(self):
        self.yd.go_to_auth_page()
        self.yd.input_login(my_login)
        assert self.yd.input_password(my_password)


