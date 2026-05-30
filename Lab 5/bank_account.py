class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self.balance:      # <-- ЗАКОММЕНТИРОВАТЬ ЭТУ СТРОКУ
            raise ValueError("Недостаточно средств на счёте")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть больше нуля")
        if amount > self.balance:
            raise ValueError("Недостаточно средств для перевода")
        self.withdraw(amount)
        target_account.deposit(amount)

    def apply_interest(self, rate):
        if rate <= 0:
            raise ValueError("Процентная ставка должна быть больше нуля")
        interest = self.balance * rate / 100
        self.balance += interest
