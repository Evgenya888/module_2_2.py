def send_email(message, recipient,sender = "university.help@gmail.com"):
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "urban.fan@mail.ru ":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    elif(str( recipient and sender)) != "@" or(str( recipient and sender)) != ".com"/".ru"/".net":
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")


send_email('messagje', 'vasyok1337@gmail.com')
send_email('messagje',' urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('messagje',' urban.student@mail.ru','urban.teacher@mail.uk')
send_email('messagje','urban.teacher@mail.ru', 'urban.teacher@mail.ru')
