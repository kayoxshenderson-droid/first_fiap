#  Estrutura condicional simples

# nota = 8.0
# if nota < 6:
#     print(f"sua nota é {nota}")
#
# print("FIM")
#  ----------------------------------------------------------
# Estrutura condicional composta

# nota = 5.0
# if nota < 4:
#     print(f"sua nota é {nota}")
#     print("Voçê foi REPROVADO")
# else:
#     print("Passou")
#
# print("FIM")
#  ----------------------------------------------------------

# Estrutura condicional Encadeada

nota = 9.0
if nota < 4:
    print("Você foi REPROVADO")
else:
    if nota < 6:
        print("Recuperacao")
    else:
        print("Aprovado")


print("FIM")

# Estrutura condicional Encadeada V2

nota = 9.0
if nota < 4:
    print("Você foi REPROVADO")
elif nota < 6:
     print("Recuperacao")
else:
    print("Aprovado")


print("FIM")

#  ----------------------------------------------------------