#3
"""Создайте систему управления банковскими счетами, которая позволяет создавать, управлять и выполнять
операции с банковскими счетами различных клиентов.
1.	Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента)
    и id (уникальный идентификатор клиента).
2.	Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты
    account_number (номер счета), balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
    Класс также должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить
    или снять деньги со счета.
3.	Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts,
    который является словарем, где ключами являются номера счетов, а значениями - объекты типа BankAccount.
    Класс также должен иметь методы create_account(client, initial_balance) для создания нового счета
    и get_account(account_number) для получения счета по его номеру.
4.	Добавьте в класс Bank методы для выполнения переводов между счетами
    (transfer(sender_account, receiver_account, amount)), а также для получения
    общего баланса клиента (get_total_balance(client)), который включает сумму денег на всех его счетах.
5.	Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег
    или отсутствие счета при переводе.
"""

class Bank:
    def __init__(self):
        self.accounts={}

    def create_account(self,client, initial_balance):
        account=BankAccount(client, initial_balance)
        self.accounts[account.account_number]=account
        return account
    def get_account(self,account_number):
        return self.accounts.get(account_number,'')
    def transfer(self, sender_account, receiver_account, amount):
        send=self.get_account(sender_account)
        receiver = self.get_account(receiver_account)
        # нет счета
        if send and receiver:
            if send.withdraw(amount):
                receiver.deposit(amount)
                print('Транзакция успешна')
        else:
            print('Неверно указаны счета')
    def get_total_balance(self,client):
        print(f'{client.name} на счетах имеет {sum([elem.balance for elem in self.accounts.values() if elem.client==client])}')
class BankAccount:
    def __init__(self, client,account_number, balance=0):
        self.client=client
        self.account_number=account_number
        self.balance=balance
    def deposit(self, sum):
        self.balance+=sum

    def withdraw(self, sum):
        if self.balance<sum:
            print('Не хватает средств на счете. Операция не выполнена')
            return False
        else:
            self.balance-=sum
            return True

class Client:
    def __init__(self, name, id):
        self.name=name
        self.id=id

client1=Client('Рая', 55)
client2=Client('Иван', 32)
bank=Bank()

account1=bank.create_account(client1,'111111111')
account1.deposit(500)
account2=bank.create_account(client1,'222222222')
account2.deposit(900)
account3=bank.create_account(client2,'333333333')
account3.deposit(200)
print('проверка на отсутствие счета')
bank.transfer(account1.account_number,'33333333',150)
print('проверка на отсутствие средств')
bank.transfer(account1.account_number,account3.account_number,600)
print('прошда транзакция')
bank.transfer(account1.account_number,account3.account_number,300)

bank.get_total_balance(client1)
bank.get_total_balance(client2)