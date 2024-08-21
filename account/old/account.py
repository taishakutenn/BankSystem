import random
import psycopg2
from account_gui import DataEntryApp


class StartWork:
    def __init__(self):
        self.start = False

    def run(self):
        self.start = True
        self.get_user_input()

    def get_user_input(self):
        app = DataEntryApp
        app.run(self)

        data = app.get_data(self)
        print(data)
        name = data.get('name')
        print(name)
        surname = input("Введите фамилию пользователя: ")
        patronymic = input("Введите отчество пользователя: ")
        age = int(input("Введите возраст пользователя: "))
        passport_data = input("Введите серию и номер паспорта пользователя: ")

        account = CreateAccount(name, surname, patronymic, age, passport_data)
        account.add_to_database()


class CreateAccount:
    def __init__(self, name, surname, patronymic, age, passport_data):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.passport_data = passport_data
        self.card_balance = 0
        self.card_id = self.create_card_id()

        # Создаём коннект к базе данных
        self.connection = psycopg2.connect(
            dbname="Accaunts",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            options="-c client_encoding='windows-1251"
        )

    def __del__(self):
        self.connection.close()

    def add_to_database(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''
            INSERT INTO Accounts(first_name, second_name, third_name, age, passport_details, card_balance, card_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (self.name, self.surname, self.patronymic, self.age, self.passport_data, self.card_balance,
                  self.card_id))

            self.connection.commit()

    def create_card_id(self):
        return random.randint(100000000, 999999999)


if __name__ == "__main__":
    session = StartWork()
    session.run()
