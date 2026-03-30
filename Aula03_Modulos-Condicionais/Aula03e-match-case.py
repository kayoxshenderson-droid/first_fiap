escolha_usuario = 1

match escolha_usuario:
    case 0:
        status = "Sair programa"
    case 1:
        status = "Entrar no Programa"
    case _:
        status = "Erro"

print(status)