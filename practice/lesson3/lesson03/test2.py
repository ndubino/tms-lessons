import random
import json
import os

# Генерирует случайные числа для номеров счета и карты
def generate_random_digits(count) -> str:
    return ''.join([str(random.randint(0, 9)) for i in range(count)])

# Класс для описания банковского счета
class BankAccount:
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.card_number: str = generate_random_digits(16) if card_number is None else card_number
        self.account_number: str = generate_random_digits(20) if account_number is None else account_number

# Преобразует объект BankAccount в словарь для сохранения в JSON
def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    return {
        'card_holder': bank_account.card_holder,
        'money': bank_account.money,
        'card_number': bank_account.card_number,
        'account_number': bank_account.account_number
    }

# Сохраняет все счета в JSON файл
def save_accounts(bank_accounts: dict[str, BankAccount], file_name: str):
    data = {number: convert_bank_account_to_dict(account) for number, account in bank_accounts.items()}
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

# Загружает все счета из JSON файла
def load_accounts(file_name) -> dict[str, BankAccount]:
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return {number: BankAccount(**data) for number, data in json.load(file).items()}

# Класс для управления банковскими счетами
class Bank:
    def __init__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts or {}

    def open_account(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_number].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        self.bank_accounts[from_account_number].money -= money
        print(f'Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}')

# Класс-контроллер для взаимодействия с пользователем и управления банком
class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')
            action = int(input())
            if action == 0:
                save_accounts(self.bank.bank_accounts, self.data_file_name)
                print('До свидания!')
                break
            # Далее идут различные действия, которые можно выполнить в банке
            # ...

    # Показывает информацию по всем счетам
    def show_accounts(self):
        print('Ваши открытые счета:')
        for account_number, account in self.bank.bank_accounts.items():
            print(f'Cчёт: {account_number}')
            print(f'   Остаток на счету: {account.money}$')
            print(f'   Номер карты: {account.card_number}')
            print(f'   Держатель карты: {account.card_holder}')

if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
