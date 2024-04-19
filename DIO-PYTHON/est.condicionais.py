maior_idade = 18
idade_epecial = 12


idade = int(input("informe sua idade: "))

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH.")

if idade < maior_idade: 
    print(" Ainda não pode tirar a CNH.")

if idade >= maior_idade:
    print("maior idade , pode tirar a CNH.")
else:
    print("ainda nao pode tirar a CNH. ")

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH. ")
elif idade == idade_epecial:
    print("pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else:
    print("ainda nao pode tirar a CNH.")
    