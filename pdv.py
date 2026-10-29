# ALGORITMO DE PONTO DE VENDAS (PDV) - COM EXIBIÇÃO DETALHADA

resposta = input('Deseja fazer compras, digite S para SIM e N para NÃO qualquer outra resposta não sera valida : ')

# Listas de histórico
q_compra = []
desconto_max = []      
desconto_idade = []    
l_idade = []
v_final = []
v_original = []

if resposta.upper() == 'S':
    cont = 1
    
    while cont == 1:
        v_compra = float(input("Digite o valor da compra (ou 0 para encerrar): "))
        
        # Requisito 5: Encerra ao digitar 0
        if v_compra == 0:
            break
            
        # Requisito 7: Validação de valor negativo com continue
        if v_compra < 0:
            print("Aviso: Valor inválido! Digite um valor positivo.")
            continue

        idade = int(input("Digite a idade: "))
        
        # Requisito 7: Validação de idade negativa com continue
        if idade < 0:
            print("Aviso: Idade inválida! Digite uma idade positiva.")
            continue

      
        v_original.append(v_compra)
        l_idade.append(idade)

        valor_atual = v_compra

        # REGRA 1: Desconto por Idade (20% se idade >= 65)
        if idade >= 65:
            pct_idade = "20%"
            valor_atual = valor_atual * 0.80
        else:
            pct_idade = "0%"

        # REGRA 2: Desconto por Valor (10% extra se o valor acumulado > 100)
        if valor_atual > 100:
            pct_valor = "10%"
            valor_atual = valor_atual * 0.90
        else:
            pct_valor = "0%"

        desconto_idade.append(pct_idade)
        desconto_max.append(pct_valor)
        v_final.append(valor_atual)
        q_compra.append(1)

     
        print("\n--- DETALHAMENTO DA COMPRA ---")
        print(f"Valor (R$):         {v_compra:.2f}")
        print(f"Idade:              {idade}")
        print(f"Desconto idade:     {pct_idade}")
        print(f"Desconto valor:     {pct_valor}")
        print(f"Valor final:        R$ {valor_atual:.2f}\n")

    print("\nObrigado por comprar!")

elif resposta.upper() == 'N':
    print("Saindo do Programa")
else: 
    print("Resposta invalida")

# RESUMO FINAL DO DIA
if len(v_final) > 0:
    print("\n==========================================")
    print("             RESUMO DO DIA               ")
    print("==========================================")
    print(f"Quantidade de compras registradas: {len(q_compra)}")
    print(f"Total bruto:                     R$ {sum(v_original):.2f}")
    print(f"Total de descontos concedidos:   R$ {(sum(v_original) - sum(v_final)):.2f}")
    print(f"Total final arrecadado:          R$ {sum(v_final):.2f}")
    print("==========================================")