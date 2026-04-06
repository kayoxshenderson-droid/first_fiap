nota_a = float(input("Coloque a sua Primeira Nota: "))
nota_b = float(input("Coloque a sua Segunda Nota: "))
nota_c = float(input("Coloque a sua Terceira Nota: "))
nota_d = float(input("Coloque a sua Quarta Nota: "))

media = nota_a + nota_b + nota_c + nota_d/4

if media >=7:
    print("Aprovado")
elif media >=5:
    print("Em Recuperação")
else:
    print("Reprovado")


