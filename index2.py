# @title Texto de título padrão
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'Book3.xlsx'
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='Sheet1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='Planilha4')


lucro_dos_vendedores = df_dia_1.groupby(['Nome']).sum()
lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()


#arquivo_excel_2 = 'Pasta 3.xlsx'#
#df_dia_2 = pd.read_excel(arquivo_excel_2, sheet_name='exemplo')#
#df_todas_as_planilhas = pd.concat([df_dia_1,df_dia_2])#
#aqui em baixo estamos a mostrar os dados das 2 planilhas concatenadas#
#print(df_todas_as_planilhas['MARCA'])#
relatorio_bonito = lucro_dos_vendedores.loc[:,"Valor do carro vendido": "Score de vendas"]
print(relatorio_bonito)
relatorio_bonito.plot(kind='bar')
plt.title('Valor que cada cliente vendeu')
plt.show()



relatorio_bonito = lucro_dos_vendedores.loc[:,"Média": "Desvio Padrão"].sum()
relatorio_bonito.plot(kind='line')
plt.title('Média, Mediana, Moda, Desvio Padrão')
plt.show()


valormedia = lucro_dos_vendedores.loc[:,"Média"]
valormediana = lucro_dos_vendedores.loc[:,"Mediana"]
valormoda = lucro_dos_vendedores.loc[:,"Moda"]
valordesvio = lucro_dos_vendedores.loc[:,"Desvio Padrão"]

paises = 'Média','Moda','Mediana', 'Desvio'
tamanho = (63689, 100000, 35000, 56079)
explode = (0, 0.1, 0, 0.5)
fig1, ax1 = plt.subplots()
ax1.pie(tamanho, explode=explode, labels=paises, autopct = '%1.1f%%', shadow=True,startangle = 90)
ax1.axis('equal')
plt.show()

relatorio_bonito = lucro_dos_vendedores.loc[:,"Curtose": "Assimetria"].sum()
relatorio_bonito.plot(kind='bar')
plt.title('Curtose, Assimetria')
plt.show()

relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Lucro Líquido 01/01/2020 até 28/01/2020 "]
relatorio_bonito2.plot(kind='area')
plt.title('Lucro Líquido')
plt.show()

relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Previsão"]
relatorio_bonito2.plot(kind='box')
plt.title('Previsão Futura dia 01/02/2020 até 28/02/2020')
plt.show()