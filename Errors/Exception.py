""" x=10

if x>5:
    raise Exception("X 5'ten büyük") """

from click import password_option


def check_password(psw):
    import re
    if len(psw) <8:
        raise Exception("Parola En Az 7 Karakter Olmalı")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola Küçük Harf İçermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola Büyük Harf İçermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola Rakam İçermelidir")
    else:
        print("Parola Oluşturuldu")

password  ="12345678aB"        
try:
    check_password(password)
except Exception as ex:
    print(ex)
