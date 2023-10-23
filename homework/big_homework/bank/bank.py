import random

def get_random_digits(count):
    return ''.join(str(random.randint(0, 9)) for _ in range(count))

class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.bank_accounts = {}

    def open_account(self, card_holder):
        new_account = BankAccount(card_holder)
        self.bank_accounts[new_account.account_number] = new_account
        return new_account

    def add_money(self, account_number, money):
        if account_number in self.bank_accounts:
            self.bank_accounts[account_number].money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        if from_account_number in self.bank_accounts and to_account_number in self.bank_accounts:
            self.bank_accounts[from_account_number].money -= money
            self.bank_accounts[to_account_number].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        if from_account_number in self.bank_accounts:
            self.bank_accounts[from_account_number].money -= money
            print(f"Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}")


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print("Здравствуйте, наш банк открылся!")

        while True:
            print("\nВыберите действие:")
            print("0. Завершить программу")
            print("1. Открыть новый счёт")
            print("2. Просмотреть открытые счета")
            print("3. Положить деньги на счёт")
            print("4. Перевести деньги между счетами")
            print("5. Совершить платёж")

            choice = input("\nВаш выбор: ")



