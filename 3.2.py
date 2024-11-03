def send_email(mes, mail,*, sender = "university.help@gmail.com"):
    check_mail = mail.split('.') # для проверки на окончание почты
    check_mail2 = sender.split('.')# для проверки на окончание почты
    end = ['ru', 'com', 'net']
    flag = False
    if '@' in ( mail and sender):
        if check_mail[-1] in end:
            if check_mail2[-1] in end:
                flag = True

                if flag == True:
                    if mail != sender:
                        if sender == "university.help@gmail.com":
                            print(f"Письмо успешно отправлено с адреса {sender} на адрес {mail}")
                        else:
                            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {mail}")
                    else :
                        print(f"Нельзя отправить письмо самому себе!")
                else:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {mail}")
            else:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {mail}")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {mail}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

"""Вывод на консоль:
Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!"""
