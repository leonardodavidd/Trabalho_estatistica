# Importe as bibliotecas necessárias
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Carregue seus dados
df = pd.read_excel("Book3.xlsx")

# Defina um modelo de cores escuro
dark_template = 'plotly_dark'

# Defina um modelo de cores branco para o primeiro gráfico
white_template = 'plotly'

# Defina um estilo CSS para a cor do texto do menu
menu_style = {'color': 'black'}

fig = px.bar(df, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group", template=dark_template)
opcoes = list(df['Modelo do carro vendido'].unique())
opcoes.append("Todas as vendas")

fig2 = px.pie(names=['Média', 'Mediana', 'Moda', 'Desvio Padrão'],
             values=[65892, 42500, 100000, 55825],
             title='Gráficos da Média, Mediana, Moda, Desvio Padrão de todas as vendas que foram realizadas no mês',
             template=dark_template)

fig3 = px.line(x=['Curtose', 'Assimetria'],
              y=[-0.057, 0.95],
              title='Gráficos da Curtose e Assimetria de todas as vendas que foram realizadas no mês',
              template=dark_template)

fig4 = px.bar(x=['Lucro Líquido'],
              y=[1845000],
              title='Gráfico do lucro Líquido dia 01/01/2020 até 28/01/2020',
              template=dark_template)

fig5 = px.box(x=['Previsão Futura'],
               y=[2397653],
               title='Gráfico de Previsão futura do faturamento do lucro líquido do dia 01/02/2020 até 28/02/2020',
               template=dark_template)

app.layout = html.Div(style={'backgroundColor': '#1f2630', 'color': 'white'}, children=[
    html.H1(style={'textAlign': 'center'}, children='Faturamento Loja de Carros'),
    html.H2(style={'textAlign': 'center'}, children='Gráfico com o Faturamento de Todas as Vendas'),

    html.Div(children='''
        Este gráfico mostra o valor líquido do faturamento
    ''', style={'textAlign': 'center'}),

    dcc.Dropdown(options=[{'label': option, 'value': option} for option in opcoes], value='Ano de cada carro', id='lista_lojas', style=menu_style),
    dcc.Graph(
        id='gráfico_quantidade_vendas',
        figure=fig
    ),
    dcc.Graph(
        id='gráfico_quantidade_vendas_bottom',
        figure=fig2
    ),
    dcc.Graph(
        id='gráfico_quantidade_vendas_bottom2',
        figure=fig3
    ),
    dcc.Graph(
        id='gráfico_quantidade_vendas_bottom3',
        figure=fig4
    ),
    dcc.Graph(
        id='gráfico_quantidade_vendas_bottom4',
        figure=fig5
    )

])

@app.callback(
    Output('gráfico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as vendas":
        fig = px.bar(df, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group", template=dark_template)
    else:
        tabela_filtrada = df.loc[df['Modelo do carro vendido'] == value, :]
        fig = px.bar(tabela_filtrada, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group", template=dark_template)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)