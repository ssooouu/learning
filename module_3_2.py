def send_email(message, recipient, sender = "university.help@gmail.com"):
    found = ('.com', '.ru', '.net')
    n = []
    if sender.endswith(found) is False:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    elif sender != sender[0]:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}r на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email(
