import psycopg2


class ATM:
    def __init__(self):
        # Создаём коннект к базе данных
        self.connection = psycopg2.connect(
            dbname="Accaunts",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            options="-c client_encoding='windows-1251'"
        )

        self.get_card_number()

    def get_card_number(self):
        while True:
            self.card_id = input("Введите айди карты: ")

            with self.connection.cursor() as cursor:
                cursor.execute('''
                SELECT card_id
                FROM accounts
                WHERE card_id = %s
                ''', (self.card_id,))

                result = cursor.fetchone()

                if not result:
                    print("ОШИБКА: ТАКОЙ КАРТЫ НЕ СУЩЕСТВУЕТ")
                else:
                    break

    def display_actions(self):
        print("1: Проверить баланс карты.")
        print("2: Положить деньги на карту.")
        print("3: Снять деньги с карты.")
        print("4: Выход.")

    def get_card_balance(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''
            SELECT card_balance
            FROM accounts
            WHERE card_id = %s
            ''', (self.card_id,))

            self.balance = cursor.fetchone()

        print(self.balance)

    def put_money_on_card(self):
        while True:
            money = float(input("Введите количество денег: "))

            with self.connection.cursor() as cursor:
                cursor.execute('''
                UPDATE accounts
                SET card_balance = card_balance + %s
                WHERE card_id = %s
                ''', (money, self.card_id))

                if cursor.rowcount > 0:
                    self.connection.commit()
                    print("Операция успешно завершена")
                    break
                else:
                    print("ПРОИЗОШЛА ОШИБКА, ПОПРОБУЙТЕ СНОВА")

    def withdraw_money_from_card(self):
        while True:
            withdraw_money = float(input("Введите количество денег: "))

            with self.connection.cursor() as cursor:
                cursor.execute('''
                            UPDATE accounts
                            SET card_balance = card_balance - %s
                            WHERE card_id = %s
                            ''', (withdraw_money, self.card_id))

                if cursor.rowcount > 0:
                    self.connection.commit()
                    print("Операция прошла успешшно")
                    break
                else:
                    print("ПРОИЗОШЛА ОШИБКА, ПОПРОБУЙТЕ СНОВА")

    def run(self):
        self.display_actions()

        while True:
            action = int(input("Введите номер действия: "))

            if action == 1:
                self.get_card_balance()
                print("Ссесия закончена, досвидания")
                break

            elif action == 2:
                self.put_money_on_card()
                print("Ссесия закончена, досвидания")
                break

            elif action == 3:
                self.withdraw_money_from_card()
                print("Ссесия закончена, досвидания")
                break

            elif action == 4:
                print("Вы закончили ссесию, досвидания")
                break

            else:
                print("ОШИБКА: ТАКОГО ДЕЙСТВИЯ НЕТ, ПОПРОБУЙТЕ СНОВА")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
