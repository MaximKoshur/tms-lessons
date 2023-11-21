import json
import random
import os
import sqlite3

def get_random_digits(count):
    return "".join([str(random.randint(0, 9)) for i in range(0, count)])


class BankAccount:
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder = card_holder.upper()
        self.money: float = money
        self.card_number: str = get_random_digits(16) if card_number is None else card_number
        self.account_number: str = get_random_digits(20) if account_number is None else account_number


class Bank:
    def __init__(self, bank_accounts: list[BankAccount] = None):
        self.__bank_accounts: dict[str, BankAccount] = {
            account.account_number: account for account in bank_accounts or []}

    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        self.__bank_accounts[account.account_number] = account
        return account.account_number

    def __get_account(self, account_number: str) -> BankAccount:
        return self.__bank_accounts[account_number]


    def get_all_bank_accounts(self):
        return list(self.__bank_accounts.values())

    def add_money(self, account_number: str, money: float):
        target_account = self.__get_account(account_number)
        target_account.money += money


    def transfer_money(self, from_account_number, to_account_number, money):
        from_account = self.__get_account(from_account_number)
        to_account = self.__get_account(to_account_number)
        from_account.money -= money
        to_account.money += money


    def external_transfer(self, from_account_number, to_external_number, money):
        from_account = self.__get_account(from_account_number)
        from_account.money -= money

        print(f'Банк перевёл {money}$ с вашего счёта '
              f'{from_account_number} на внешний счёт '
              f'{to_external_number}')

class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)
    def run(self):
        print("Наш банк открылся")
        while True:
            print(
                "Выберите действие:\n0. Завершить программу\n1. Открыть новый счёт\n2. Просмотреть открытые счета\n3. "
                "Положить деньги на счёт\n4. Перевести деньги между счетами\n5. Совершить платёж")
            answer = input()
            if answer == '0':
                save_accounts(self.bank.get_all_bank_accounts(), self.data_file_name)
                print("До свидания!")
                break
            elif answer == '1':
                user = self.bank.open_account(input("Введите имя и Фамилию владельца:"))
                print(f'Счет {user} создан!')
            elif answer == '2':
                for i in self.bank.get_all_bank_accounts():
                    print(f"\nСчет: {i.account_number}")
                    print(f"    Деньги: {i.money}$")
                    print(f"    Номер карты: {i.card_number}")
                    print(f"    Владелец: {i.card_holder}\n")
            elif answer == '3':
                self.bank.add_money(input("Account number: "), int(input("Money: ")))
                print(f'Деньги переведены')
            elif answer == '4':
                self.bank.transfer_money(input("Account number: "), input("Account number: "), int(input("Money: ")))
                print(f'Деньги переведены')
            elif answer == '5':
                self.bank.external_transfer(input("Account number: "), input("Account number: "), int(input("Money: ")))
                print(f'Деньги переведены')
            else:
                print(f'Неверная операция')


def convert_bank_account_dict(obj: BankAccount) -> dict:
    return {
        "card_holder": obj.card_holder,
        "money": obj.money,
        "card_number": obj.card_number,
        "account_number": obj.account_number
    }


def save_accounts(obj: list[BankAccount], file_name: str):
    with sqlite3.connect('Bank.db') as connection:
        for i in obj:
            account = convert_bank_account_dict(i)
            result = connection.execute("INSERT INTO Bank VALUES(?, ?, ?, ?)",
                                        [account["card_holder"], account["money"], account["card_number"], account["account_number"]])


    # with open(file_name, "w") as data:
    #     save_users = {}
    #     for i in obj:
    #         user = {i.account_number: convert_bank_account_dict(i)}
    #         save_users.update(user)
    #     json.dump(save_users, data)


def load_accounts(file_name):
    with sqlite3.connect('Bank.db') as connection:
        result = connection.execute("SELECT * FROM Bank")
        return [BankAccount(
                card_holder=item[0],
                money=float(item[1]),
                card_number=item[2],
                account_number=item[3]
            ) for item in result.fetchall()]


    # if not os.path.exists(file_name):
    #     return []
    # with open(file_name, 'r') as file:
    #     data = json.load(file)
    #     return [BankAccount(
    #         card_holder=item["card_holder"],
    #         money=float(item["money"]),
    #         card_number=item["card_number"],
    #         account_number=item["account_number"]
    #     ) for item in data.values()]


if __name__ == '__main__':
    controller = Controller("data.json")
    controller.run()
