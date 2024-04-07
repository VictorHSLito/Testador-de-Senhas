import re


def teste_senha(senha):
    if 10 <= len(senha) <= 40:
        numero = minuscula = maiuscula = d_especial = aspas = False
        for caractere in senha:
            if re.search("[a-z]", caractere):
                minuscula = True
            elif re.search("[A-Z]", caractere):
                maiuscula = True
            elif re.search("[0-9]", caractere):
                numero = True
            elif re.search("[!@#$%¨&*()-=+]", caractere):
                d_especial = True
            elif re.search("[\" ']", caractere):
                aspas = True
        if numero and minuscula and maiuscula and d_especial and not aspas:
            return True
        else:
            if not minuscula:
                print("Senha inválida! A senha não possui caractere minúsculo!")
            elif not maiuscula:
                print("Senha inválida! A senha não possui caractere maiúsculo!")
            elif not numero:
                print("Senha inválida! A senha não possui número!")
            elif not d_especial:
                print("Senha inválida! A senha não possui caractere especial!")
            elif aspas:
                print("Senha inválida! A senha contêm aspas!")
            return False
    else:
        if len(senha) < 10:
            print("Tamanho de senha insuficiente!")
        else:
            print("Tamanho de senha excedeu o limite máximo de caracteres")


senha = str(input("Digite uma senha: "))
if teste_senha(senha):
    print("Senha válida!")