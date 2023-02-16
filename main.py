# Obter os nomes das opções e seus respectivos valores como input
nome_opcao1 = input("Digite o nome da opção 1: ")
valor_opcao1 = float(input("Digite o valor da opção 1: "))
nome_opcao2 = input("Digite o nome da opção 2: ")
valor_opcao2 = float(input("Digite o valor da opção 2: "))
nome_opcao3 = input("Digite o nome da opção 3: ")
valor_opcao3 = float(input("Digite o valor da opção 3: "))

# Calcular a taxa de retorno esperada de cada opção
taxa_opcao1 = valor_opcao1 - 1
taxa_opcao2 = valor_opcao2 - 1
taxa_opcao3 = valor_opcao3 - 1

# Calcular o investimento ideal em cada opção
investimento_opcao1 = (taxa_opcao1 * valor_opcao3 - taxa_opcao3) / (taxa_opcao1 * taxa_opcao3 - taxa_opcao2 ** 2)
investimento_opcao2 = (taxa_opcao2 * (investimento_opcao1 * taxa_opcao1 + taxa_opcao3)) / taxa_opcao3
investimento_opcao3 = (investimento_opcao1 + investimento_opcao2) * (-1 * taxa_opcao2) / taxa_opcao3

# Calcular o investimento total e imprimir os resultados
investimento_total = investimento_opcao1 + investimento_opcao2 + investimento_opcao3
print(f"Investimento ideal em {nome_opcao1}: R$ {round(investimento_opcao1, 2)}")
print(f"Investimento ideal em {nome_opcao2}: R$ {round(investimento_opcao2, 2)}")
print(f"Investimento ideal em {nome_opcao3}: R$ {round(investimento_opcao3, 2)}")
print(f"Investimento total: R$ {round(investimento_total, 2)}")
