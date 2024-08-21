import customtkinter as ctk


class DataEntryApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("250x400")
        self.app.title("ATM")
        self.app.resizable('false', 'false')
        self.app.grid_columnconfigure(0, weight=1)

        self.entry_data = {}

        # Вывод текста
        label = ctk.CTkLabel(self.app, text="Введите ваши данные", font=("Arial", 19))
        label.pack(pady=20)

        self.input_data()

    def input_data(self):
        data_for_input = ['Имя', 'Фамилия', 'Отчество', 'Возраст', 'Серия и номер паспорта']
        self.entry_widgets = []

        for i in range(5):
            entry = ctk.CTkEntry(self.app, placeholder_text=f"{data_for_input[i]}", width=180, height=30)
            entry.pack(pady=10)
            self.entry_widgets.append(entry)

        submit_button = ctk.CTkButton(self.app, text="Отправить", command=self.submit)
        submit_button.pack(pady=20)

    def submit(self):
        dataes = ['name', 'surname', 'patronymic', 'age', 'passport_data']
        for i, entry in enumerate(self.entry_widgets):
            self.entry_data[f"{dataes[i]}"] = entry.get()
        self.app.quit()  # Закрываем приложение после отправки данных

    def run(self):
        self.app.mainloop()

    def get_data(self):
        return self.entry_data
