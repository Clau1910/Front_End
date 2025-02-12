vendas = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

total = sum(vendas)

media = total / len(vendas)

Junior_vendas = max(vendas)
mes_max = vendas.index(Junior_vendas) + 1

print("Total anual de vendas:", total)
print("Média mensal de vendas:", media)
print("Mês com maior venda:", mes_max)