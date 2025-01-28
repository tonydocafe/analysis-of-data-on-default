# -*- coding: utf-8 -*-
# Importação da biblioteca pandas
import pandas as pd

# Carregar o arquivo Excel
data = pd.read_excel("default of credit card clients.xls", skiprows=1)

# Visualizar os primeiros 5 dados do conjunto
print("Visualizando os primeiros dados do conjunto:")
print("\n")
print("PAY_* = O a 6,pagamento -2(antecipado) -1(Pontual) 0(nenhum atraso)")
print("BILL_AMT* = 1 a 6, fatura do mês atual até 6 meses atrás")
print("PAY_AMT* = 1 a 6, valor pago do mês atual até 6 meses atrás")
print("\n")
# Caso queira ver todas as colunas, descomente a linha abaixo:
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

# Mostrar as primeiras 10 linhas
print(data.head(10))