import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("Иван Иванов", 1000)
        self.account2 = BankAccount("Пётр Петров", 500)

    def test_account_creation(self):
        self.assertEqual(self.account1.owner, "Иван Иванов")
        self.assertEqual(self.account1.get_balance(), 1000)

    def test_deposit(self):
        self.account1.deposit(200)
        self.assertEqual(self.account1.get_balance(), 1200)

    def test_deposit_zero_or_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(0)
        with self.assertRaises(ValueError):
            self.account1.deposit(-100)

    def test_withdraw(self):
        self.account1.withdraw(300)
        self.assertEqual(self.account1.get_balance(), 700)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(2000)

    def test_withdraw_zero_or_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(0)
        with self.assertRaises(ValueError):
            self.account1.withdraw(-50)

    def test_transfer(self):
        self.account1.transfer(self.account2, 400)
        self.assertEqual(self.account1.get_balance(), 600)
        self.assertEqual(self.account2.get_balance(), 900)

    def test_transfer_with_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(self.account2, 2000)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Некорректный счёт", -100)

    def test_apply_interest(self):
        self.account1.apply_interest(10)
        self.assertEqual(self.account1.get_balance(), 1100)

    def test_apply_interest_negative_rate(self):
        with self.assertRaises(ValueError):
            self.account1.apply_interest(-5)


if __name__ == "__main__":
    unittest.main()
