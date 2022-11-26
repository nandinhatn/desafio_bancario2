menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuario
[a] Abrir Conta
[b] Listar Contas
[u] Listar Usuários
[q] Sair

=>"""
saldo =0
limite =500
extrato =""
numero_saque =0
LIMITE_SAQUES =3
usuarios =[]
contas =[]

def listar_usuarios(usuarios):
    print('>>>>listar usuarios >>>>')
    for indice,usuario in  enumerate(usuarios):
        print(f" {indice} : Nome: {usuario['nome']}, Endereco: {usuario['endereco']}, CPF : {usuario['cpf']}, Data de Nascimento :{usuario['data_nascimento']} \n")
    


def listar_contas(contas):
    print('>>>>listar contas >>>>')
    for indice, conta in enumerate(contas):
        print(f"{indice}: Agência: {conta['agencia']}, CPF :{conta['usuario']}, Numero da Conta : {conta['numero_conta']} ")


def depositar(valor,saldo,extrato):
    if valor<0:
        print("o valor digitado é inválido")
    else:
        saldo += valor
        print(f"Deposito realizado com sucesso saldo atual R$ {saldo:.2f}")
        extrato += f" Deposito realizado  R$ {valor:.2f} \n"
        print(extrato)
        return  extrato, saldo

def sacar(valor_saque, extrato , saldo, numero_saque):
        if valor_saque>saldo:
            print("Operação não permitida - SALDO INSUFICIENTE")
            return saldo, extrato, numero_saque
        elif  numero_saque>=3:
             print("Operação não permitida - SEU LIMITE DE SAQUES ESGOTOU")
             return saldo, extrato, numero_saque
        elif valor_saque> 500:
             print("Operação não permitida - O LIMITE DE SAQUE É DE R$ 500,00")
             return saldo, extrato, numero_saque
        elif valor_saque < 0:
            print("Valor inválido")
            return saldo, extrato, numero_saque
        else:
            saldo -= valor_saque
            print(f"""Saque  no valor de R$ {valor_saque:.2f} realizado com sucesso""")
            extrato += f""" Saque Realizado no valor de R$ {valor_saque:.2f} \n"""
            numero_saque += 1
            return saldo, extrato, numero_saque

def tirar_extrato(saldo, extrato):
     print("<<<<<<<<<<<<<<<<<<extrato<<<<<<<<<<<<<<<<<<")
     if extrato=="":
        print("Não foram realizadas movimentações")
        return extrato
     else:
            print(f"""{extrato}""")
            print(f"""Saldo : R$ {saldo:.2f}""")
            print("<<<<<<<<<<<<<<<<<<<<")
            return extrato

def criar_usuario(usuarios):
    print('entrei')
    cpf = int(input ("Informe CPF"))
    cpf_existe=verificar_cpf_existente(cpf,usuarios)
    if cpf_existe== True:
        print('cpf já está cadastrado')
        return
    else:      
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe sua data de nascimento: ")
        endereco = input(" Informe o endereço :")
        usuario = dict( nome= nome, data_nascimento=data_nascimento , endereco=endereco,cpf=cpf)
        print('Usuário inserido com sucesso')
        return usuario

def verificar_cpf_existente(cpf,usuarios):
    for usuario in usuarios:
        if usuario['cpf']==cpf:
            return True
        else:
            return False

def abrir_conta(usuarios,contas):
    #verificar a conta , verifcar os usarios
    cpf = int(input("Informe o CPF: "))
    consulta=verificar_cpf_existente(cpf,usuarios)
    if consulta == True:
        numero_agencia = '0001'
        numero_conta = len(contas) + 1
        nova_conta = dict(usuario = cpf, agencia= numero_agencia, numero_conta=numero_conta)
        print('Conta inserida com sucesso')
        return nova_conta
    else:
        print("<<<< é preciso cadastrar um usuário")
        return


while True :
    opcao = input(menu)
    if opcao=='d':
        valor = int(input("Digite o valor para o depósito "))
        extrato, saldo=depositar(valor, saldo, extrato)
         
            
    elif opcao =='s':
        valor_saque = int(input("Digite o valor para sacar: "))
        saldo, extrato, numero_saque = sacar(valor_saque= valor_saque, extrato= extrato, saldo=saldo,numero_saque=numero_saque)
        
    elif opcao == 'e':
        extrato = tirar_extrato(saldo, extrato=extrato)
    
    elif opcao =='c':
        usuarios.append(criar_usuario(usuarios))
    
    elif opcao =='a':
        print(">>>>> Abertura de Conta <<<<<<<<<")
        contas.append(abrir_conta(usuarios,contas))
    
    elif opcao=='u':
        listar_usuarios(usuarios)
    
    elif opcao=='b':
        listar_contas(contas)


       

       
   
    elif opcao =='q':
         break
    else:
        print("opcao invalida , por favor selecione novamente a operação desejada")
