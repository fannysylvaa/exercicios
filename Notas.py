Nome = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota da prova:'))
nota2 = float(input('Digite a segunda nota da prova: '))
nota3 = float(input('Digite a terceira nota da prova:'))
media =(nota1+nota2+nota3)/3

if media >=7:
    print('Nome do Aluno: {}\nSua média é de: {:.2f}\n APROVADO!'.format(Nome,media))
else:
    print('Nome do Aluno: {}\nSua média é de: {:.2f}\n REPROVADO!'.format(Nome,media))


