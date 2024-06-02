import pytest

from helpers.api_helper import *
from solution import Solution

solution = Solution()


class TestBaseHttpResponse:
    def test_http_ok_on_main_page(self):
        assert get_page().status_code == 200

    def test_http_text_non_empty(self):
        assert get_page().text

    def test_http_ok_on_result_page(self):
        assert post_form({'data': '1 2 3'}).status_code == 200

    def test_content_type_text_html(self):
        assert get_page().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_content_type_app_json(self):
        assert post_form({'data': '1 2 3'}).headers['Content-Type'] == 'application/json'


class TestAPIResultResponse:
    def test_valid_example(self):
        nums = '2 3 -2 4'
        assert post_form({'data': nums}).json()['res'] == 6

    @pytest.mark.parametrize('data', [
        pytest.param('1', id='nums.length=min'),
        pytest.param('1 1', id='nums.length=min+1'),
        pytest.param('1 ' * (2 * 10 ** 4 - 1), id='nums.length=max-1'),
        pytest.param('1 ' * (2 * 10 ** 4), id='nums.length=max'),
    ])
    def test_nums_length_in_range(self, data):
        assert post_form({'data': data}).json()['res'] == 1

    @pytest.mark.parametrize('data', [
        pytest.param('', id='nums.length=min-1'),
        pytest.param('1 ' * (2 * 10 ** 4 + 1), id='nums.length=max+1'),
    ])
    def test_nums_length_out_of_range(self, data):
        assert post_form({'data': data}).status_code == 400

    @pytest.mark.parametrize('data', [
        pytest.param('8 8 0 -10', id='num[i]=min'),
        pytest.param('8 8 0 -9', id='num[i]=min+1'),
        pytest.param('8 8 0 9', id='num[i]=max-1'),
        pytest.param('8 8 0 10', id='num[i]=max'),
    ])
    def test_num_value_in_range(self, data):
        assert post_form({'data': data}).json()['res'] == 64

    @pytest.mark.parametrize('data', [
        pytest.param('8 8 0 -11', id='nums[i]=min-1'),
        pytest.param('8 8 0 11', id='nums[i]=max+1'),
    ])
    def test_num_value_out_of_range(self, data):
        assert post_form({'data': data}).status_code == 400

    def test_product_in_range_max(self):
        nums = '2 ' * 31
        assert post_form({'data': nums}).json()['res'] == 2 ** 31

    @pytest.mark.parametrize('data', [
        pytest.param('2 ' * 32, id='product=max'),
        pytest.param('2 ' * 33, id='product=max+1'),
    ])
    def test_product_out_of_range(self, data):
        assert post_form({'data': data}).status_code == 400

    @pytest.mark.parametrize('data', [
        pytest.param('fg dj d meow d', id='string'),
        pytest.param('None 1 1 0', id='none'),
        pytest.param('2.5 1 1 1.5', id='float'),
        pytest.param('true true false true', id='bool'),
    ])
    def test_num_value_invalid_type(self, data):
        assert post_form({'data': data}).status_code == 400

    def test_invalid_data_key(self):
        nums = '2 3 -2 4'
        assert post_form({'nums': nums}).status_code == 400

    def test_empty_request(self):
        nums = '2 3 -2 4'
        assert post_form({}).status_code == 400
