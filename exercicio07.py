nomes = ["joão", "maria","felix","jose","igor"]
senhas = [12345,54321,147852,258741,159753]
login = input("digite o nome do usuario: ")
senha = int(input("digite a senhas: "))
for x in range(len(nomes)):
    if login ==nomes[x]:
        if senha ==senhas[x]:
            print("login efetuado com sucesso")
        else:
            print("usuario ou senha incorreto")
    if login!=nomes[x]:
        print("senha ou login incorreto")
        break