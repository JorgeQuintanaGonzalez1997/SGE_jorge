import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import hashlib
import csv

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.users_data = self.load_users("users.csv")

        # Campo de usuario
        self.add_widget(Label(text="Usuari:"))
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        # Campo de contraseña
        self.add_widget(Label(text="Contrasenya:"))
        self.password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.password_input)

        # Botón comprobar
        self.check_button = Button(text="Comprovar")
        self.check_button.bind(on_press=self.check_credentials)
        self.add_widget(self.check_button)

        # Etiqueta de resultado
        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def load_users(self, filepath):
        """Carga usuarios y contraseñas desde un archivo CSV."""
        users_data = {}
        try:
            with open(filepath, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        username, password_hash = row
                        users_data[username] = password_hash
        except FileNotFoundError:
            print(f"Error: El archivo {filepath} no existe.")
        return users_data

    def check_credentials(self, instance):
        """Comprueba si las credenciales son correctas."""
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        # Hash de la contraseña ingresada
        password_hash = hashlib.sha1(password.encode()).hexdigest()

        if username in self.users_data and self.users_data[username] == password_hash:
            self.result_label.text = "OK"
        else:
            self.result_label.text = "ERROR"


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    LoginApp().run()