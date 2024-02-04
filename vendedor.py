Nome = input('Nome do vendedor:')
Salário_fixo = float(input('Qual é o seu salário fixo:'))
Vendas = float (input('Quantas vendas foram feitas no mês:'))
Ganho = Salário_fixo + 0.15 * Vendas

print ('\n\n O nome do vendedor(a) é:{}\n O seu salário fixo é R$:{:.2f}\n O seu salário no fim do mês é R$:{:.2f}' .format(Nome,Salário_fixo,Ganho))

