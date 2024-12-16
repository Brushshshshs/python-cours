#UrTube, Video, User.

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    class polzovatelya, sodergashiy atr : login, parol'
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветсыую, выберите действие: \n1 - вход\n2 - регистрация\n")
        user = User(input('Введите логин: '), password1 := input("Введите пароль на латыне (должен содержать не менне 8ми символов, включая заглавную, маленькую букву и цифру) : "),password2 := input("Повторите пароль: "))
        #Блок проверки пароля
        #
        #
        def upper(password):
            for c in password:
                if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    return True
            return False
        def lower(password):
            for c in password:
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    return True
            return False
        def number(password):
            for c in password:
                if c in '0123456789':
                    return True
            return False

        if password1 != password2:
            print("некорректный пароль, заново")
            exit()
        if len(password1) < 8:
            print("некорректный пароль, заново")
            exit()
        if not upper(password1):
            print("некорректный пароль, заново")
            exit()
        if not lower(password1):
            print("некорректный пароль, заново")
            exit()
        if not number(password1):
            print("некорректный пароль, заново")
            exit()

            # Блок проверки пароля окончен
            #
            #

        database.add_user(user.username, user.password)
        print (database.data)
