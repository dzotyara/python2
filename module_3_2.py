
recipient = str(input("Введите почту: "))
message = str(input("Введите сообщение: "))
variants = (".com", ".ru", ".net")

def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    error_1 = (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    error_2 = ("Невозможно отправить письмо самому себе")
    success = (f"письмо успешно отправлено с адреса {sender} на адрес {recipient}\n\nсодержимое письма: \n {message}")

    if "@" not in recipient and sender:
        return error_1
    elif sender.endswith(variants) or recipient.endswith(variants):
        if sender != recipient:
            return success
        else:
            return error_2
    else:
        return error_1

print(send_email(message, recipient))