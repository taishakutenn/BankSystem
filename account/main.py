from data_entry_app import DataEntryApp
from database import CreateAccount


class StartWork:
    def __init__(self):
        self.start = False

    def run(self):
        self.start = True
        self.get_user_input()

    def get_user_input(self):
        app = DataEntryApp()  # Создаем экземпляр класса DataEntryApp
        app.run()  # Запускаем GUI приложения

        data = app.get_data()  # Получаем данные из приложения
        print(data)

        name = data.get('name')
        surname = data.get('surname')  # Получаем фамилию из словаря
        patronymic = data.get('patronymic')  # Получаем отчество из словаря
        age = int(data.get('age'))  # Получаем возраст из словаря
        passport_data = data.get('passport_data')  # Получаем паспортные данные из словаря

        account = CreateAccount(name, surname, patronymic, age, passport_data)
        account.add_to_database()


if __name__ == "__main__":
    session = StartWork()
    session.run()
