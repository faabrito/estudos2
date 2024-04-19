conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_epecial = 450

if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    elif saque <= (saldo + cheque_epecial):
        print('saque realizado com uso de cheque especial!')
    else:
        print('nao foi realizado com uso de cheque especial!')

elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    else: 
        print('saldo insuficiente!')