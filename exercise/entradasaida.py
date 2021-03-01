#Entrada e saída de Dados de uma pessoa:
nome = input("Digíte seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = bool(input("Digite 'M' para sexo Masculino e 'F' para sexo Feminino"))
print("Meu nome é", nome, "e minha idade é" ,idade , "tendo o sexo", sexo )
#1
nome = input("Informe seu nome completo: ")
print("Obrigado por responder à pergunta",nome)
#2
bebida = input("Qual bebida você prefere?\n 1) Água\n 2) Cerveja\n 3) Vinho\n 4) Leite\n Informe o número: ")
print("Você escolheu a opção", bebida)
#3
ano_nascimento = int(input("Informe o ano de nascimento com 4 dígitos: "))
idade = 2018 - ano_nascimento
print("Você tem", idade, "anos.")
#4
salario_minimo = float(input("Informe o valor do salário mínimo: "))
pretensao = float(input("Quantos salários você gostaria de ganhar? "))
print("Você pretende ganhar R$", salario_minimo * pretensao)
#5
salario = float(input("Informe o valor do seu salário: "))
salario_minimo = float(input("Informe o valor do salário mínimo: "))
idade = int(input("Informe sua idade (apenas número): "))
resultado = salario > (salario_minimo * 2) and idade > 18
print("O resultado foi", resultado)
