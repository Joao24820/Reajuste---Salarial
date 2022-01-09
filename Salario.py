nome = str(input('Informe por favor o nome do funcionario: '))
sal = float(input('Diga por favor qual o salario do funcionario {} R$ '.format(nome)))

soma = sal * (15/100) + sal

print("O funcionario {} que recebe R$ {} com aumento de 15% , passa a receber R$ {:.2f} mensais ! "
      .format(nome, sal, soma))
