def teste_senha(senha):
    if 10 <= len(senha) <= 40:
        numero = minuscula = maiuscula = d_especial = aspas = False
        for caractere in senha:
            if caractere.isdigit():
                numero = True
            elif caractere.islower():
                minuscula = True
            elif caractere.isupper():
                maiuscula = True
            elif caractere in "!@#$%¨&*()-=+":
                d_especial = True
            elif caractere in "\" '":
                aspas = True
        if numero and minuscula and maiuscula and d_especial and not aspas:
            return True
        else:
            if not numero:
                print("A senha foi negada pois o requisito de conter número não foi atendido!")
            elif not minuscula:
                print("A senha foi negada pois o requisito de conter letra minúscula não foi atendido!")
            elif not maiuscula:
                print("A senha foi negada pois o requisito de conter letra maiúscula não foi atendido!")
            elif not d_especial:
                print("A senha foi negada pois o requisito de conter um digito especial não foi atendido!")
            elif aspas:
                print("A senha foi negada pois o requisito de não conter aspas não foi atendido!")
            return False
    else:
        if len(senha) < 10:
            print("Tamanho de senha insuficiente!")
        else:
            print("Tamanho de senha excedeu o limite máximo de caracteres")
        return False


senha = (str(input("Digite uma senha qualquer: ")))
if teste_senha(senha):
    print("A senha passou nos testes!")