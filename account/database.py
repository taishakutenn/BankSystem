import psycopg2
import random


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
            options="-c client_encoding='windows-1251'"
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
