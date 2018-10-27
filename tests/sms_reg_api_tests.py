import string
import unittest
from random import choice, randint

import sms_reg_api
from sms_reg_api.sms_reg import Sms
'''
Api_key сменен, попытка
использовать ключ из тестов
не увенчается успехом.
'''


class SmsTest(unittest.TestCase):
    def test_auth_error(self):
        with self.assertRaises(sms_reg_api.exceptions.BadToken):
            for _ in range(10):
                Sms(''.join([choice(string.ascii_uppercase + string.digits) for _ in range(randint(1, 10000))]))

    def test_auth_normal(self):
        self.assertTrue(Sms('2d08p37k6bkwjpj1pqgwdsbg9nuy2g1y'))

    def test_balance(self):
        self.assertTrue(Sms('2d08p37k6bkwjpj1pqgwdsbg9nuy2g1y').balance())

    def test_get_operations(self):
        self.assertTrue(Sms('2d08p37k6bkwjpj1pqgwdsbg9nuy2g1y').get_operations())


if __name__ == "__main__":
    unittest.main()
