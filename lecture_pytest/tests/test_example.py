import pytest


@pytest.mark.skip('цей тест поки що не дописаний')
def test_one():
    assert 1 == 1


def test_two():
    assert True


number = [1, 2, 4, 5, 3.3]
@pytest.mark.parametrize('digit', number)


def test_three(digit):
    assert type(digit) is int


class TestLogin:

    def test_login_1(self):
        print('Hello, test_login_1')
        pass

    @pytest.mark.smoke
    @pytest.mark.api
    def test_login_2(self):
        assert 1 == 1

    @pytest.mark.xfail
    def test_login_multiple(self):
        first_result = 5 < 6
        second_result = 1 > 0
        third_result = 0 == 0
        assert all([first_result, second_result, third_result])


class TestBasket:
    @pytest.mark.api
    def test_basket_1(self):
        pass

    @pytest.mark.smoke
    def test_basket_2(self):
        pass

    def test_basket_3(self):
        pass
