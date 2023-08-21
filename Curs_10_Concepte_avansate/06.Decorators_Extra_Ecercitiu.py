def require_login(method):
    def wrapper(self, *args, **kwargs):
        if not self.loggedin:
            print("Access nepermis! Utilizatorul nu este logat!")
            return
        return method(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.loggedin = False

    def login(self, email, parola):
        if self.email == email and self.parola == parola:
            self.loggedin = True
            print("Utilizatorul s-a logat cu succes!")
        else:
            print("Email sau parola incorecta!")

    @require_login
    def get_info(self):
        return {
            "nume": self.nume,
            "email": self.email,
            "data_nasterii": self.data_nasterii
        }

    def log_out(self):
        if self.loggedin:
            self.loggedin = False  # Resetam starea de autentificare
            print("Utilizatorul a fost delogat!")
        else:
            print("Utilizatorul nu este logat!")


user = User("Ion", "ion@itfactory.it", "parola", 1993)
print(user.get_info())
user.login("ion@itfactory.it", "parola")
user.log_out()

