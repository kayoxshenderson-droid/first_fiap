# logica E (and)
verifica_email = True
verifica_senha = False

verifica_login = verifica_senha and verifica_email
print(verifica_login)

if verifica_login:
    print("Entra no programa")


# Loigca OU (or)

logica_ou = False or True
print(logica_ou)

# Operador de Negação

negacao = not False
print(negacao)

if not verifica_login:
    print("Loga Certo aii.....")
