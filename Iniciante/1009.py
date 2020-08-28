if __name__ == "__main__":
    nome = str(input())
    salario = float(input())
    vendas_total = float(input())

    total = salario + ((15/100)*vendas_total)

    print(f'TOTAL = R$ {total:.2f}')
