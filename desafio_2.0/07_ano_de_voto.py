ano_nascimeto = int(input("Qual ano voce nasceu?: "))
ano_atual = int(input("Qual o ano atual?: "))
idade_sua = ano_atual-ano_nascimeto

if idade_sua >=18:
    print("Seu voto é obrigatorio este ano")
elif idade_sua >=16 and 17:
    print("voto Opcional este ano")
else:
    print("Voto proibido este ano")