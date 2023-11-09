import pandas as pd
import openpyxl


def filtro(estado, conta, coluna):
    filtro = (tabela['UF'] == estado) & (tabela['Conta'] == conta) & (tabela['Coluna'] == coluna)
    return filtro

def filtro2(municipio, conta, coluna):
    filtro = (tabela['Instituição'] == municipio) & (tabela['Conta'] == conta) & (tabela['Coluna'] == coluna)
    return filtro

tabela = pd.read_excel(r"C:\Users\humbe\Downloads\municipios1.xlsx", engine='openpyxl')

contas = ['06 - Segurança Pública', '08 - Assistência Social', '09 - Previdência Social', '10 - Saúde', '12 - Educação']

estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

despesas = ['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas', 'Inscrição de Restos a Pagar Não Processados']

soma = 0


if __name__ == '__main__':
    print("MENU:")
    print("1. ESTADOS")
    print("2. MUNICIPIO")
    print("3. ESTADO")
    print("4. Sair")

    while True:
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Opção 1 selecionada")

            conta = input('Qual conta: ')
            despesa = input('Qual despesa: ')

            for i in range(len(estados)):
                valor = filtro(estados[i], conta, despesa)
                linha = tabela.loc[valor]
                print(f'Valores de {despesa} em {conta} no estado de {estados[i]}')
                print(linha)
                soma += linha['Valor'].sum()
                print(f'A soma total dessa despesa é {round(soma, 2)}')
                soma = 0

        elif escolha == "2":
            print("Opção 2 selecionada")
            conta = input('Qual Conta: ')
            despesa = input('Qual Despesa: ')
            municipio = input('Qual Municipio: ')

            valor = filtro2(municipio, conta, despesa)
            linha = tabela.loc[valor]
            custo = linha['Valor']
            print(f'Valores de {despesa} em {conta} na {municipio}')
            print(linha['Valor'])

        elif escolha == "3":
            print("Opção 3 selecionada")

            conta = input('Qual conta: ')
            despesa = input('Qual despesa: ')
            estado = input('Qual estado: ')

            valor = filtro(estado, conta, despesa)
            linha = tabela.loc[valor]
            print(f'Valores de {despesa} em {conta} no estado de {estado}')
            print(linha)
            soma += linha['Valor'].sum()
            print(f'A soma total dessa despesa é {round(soma, 2)}')
            soma = 0

        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")