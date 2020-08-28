if __name__ == "__main__":
    n_funcionario = int(input())    #Numero do funcionario
    h_trabalhadas = int(input())    #Numero de horas trabalhadas
    valor_h = float(input())        #Valor recebido por hora

    salario = h_trabalhadas * valor_h

    print(f'NUMBER = {n_funcionario}')
    print(f'SALARY = U$ {salario:.2f}')