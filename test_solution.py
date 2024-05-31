from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_max_product_example_1(self):
        solution = Solution()
        nums = [2, 3, -2, 4]
        max_product = solution.maxProduct(nums)
        self.assertEqual(6, max_product)

    def test_max_product_example_2(self):
        solution = Solution()
        nums = [-2, 0, -1]
        max_product = solution.maxProduct(nums)
        self.assertEqual(0, max_product)

    def test_nums_length_in_range(self):
        solution = Solution()
        data = {
            'nums.length=min': [1],
            'nums.length=min+1': [1, 1],
            'nums.length=max-1': [1] * (2 * 10 ** 4 - 1),
            'nums.length=max': [1] * (2 * 10 ** 4),
        }
        for n in data:
            with self.subTest(nums=n):
                self.assertEqual(1, solution.maxProduct(data[n]))

    def test_nums_length_out_of_range(self):  # ToDo добавить обработку выхода за границы
        solution = Solution()
        data = {
            'nums.length=min-1': [],
            'nums.length=max+1': [1] * (2 * 10 ** 4 + 1),
        }
        for n in data:
            with self.subTest(nums=n):
                with self.assertRaises(AssertionError):
                    solution.maxProduct(data[n])

    def test_num_value_in_range(self):
        solution = Solution()
        data = {
            'num[i]=min': [8, 8, 0, -10],
            'num[i]=min+1': [8, 8, 0, -9],
            'num[i]=max-1': [8, 8, 0, 9],
            'num[i]=max': [8, 8, 0, 10],
        }
        for n in data:
            with self.subTest(nums=n):
                self.assertEqual(64, solution.maxProduct(data[n]))

    def test_num_value_out_of_range(self):
        solution = Solution()
        data = {
            'nums[i]=min-1': [8, 8, 0, -11],
            'nums[i]=max+1': [8, 8, 0, 11],
        }
        for n in data:
            with self.subTest(nums=n):
                with self.assertRaises(AssertionError):
                    solution.maxProduct(data[n])

    def test_product_in_range_max(
            self):  # отрицательную границу можно не проверять, так как она не достяжима по свойству умножения
        solution = Solution()
        nums = [2] * 31
        max_product = solution.maxProduct(nums)
        self.assertEqual(2 ** 31, max_product)

    def test_product_out_of_range(self):
        solution = Solution()
        data = {
            'product=max': [2] * 32,
            'product=max+1': [2] * 33
        }
        for n in data:
            with self.subTest(nums=n):
                with self.assertRaises(AssertionError):
                    solution.maxProduct(data[n])

    def test_num_value_is_string(self):
        solution = Solution()
        nums = ['a', 'b', 'c', '.', 'fjhgjek', '1']
        self.assertRaises(TypeError, solution.maxProduct, nums)
