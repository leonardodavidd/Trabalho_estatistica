from dash import Dash, html, dcc, Input,Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Book3.xlsx")


fig = px.bar(df, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group")
opcoes = list(df['Modelo do carro vendido'].unique())
opcoes.append("Todas as vendas")


app.layout = html.Div(children=[
    html.H1(children='Faturamento Loja de Carros'),
    html.H2(children='Gráfico com o Faturamento de Todas as Vendas'),

    html.Div(children='''
        Este gráfico mostra o valor líquido do faturamento
    '''),
    
    dcc.Dropdown(opcoes, value='Ano de cada carro', id='lista_lojas'),
    dcc.Graph(
        id='gráfico_quantidade_vendas',
        figure=fig
    )
])


@app.callback(
    Output('gráfico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as vendas":
        fig = px.bar(df, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group")
    else:
        tabela_filtrada = df.loc[df['Modelo do carro vendido'] == value,:]
        fig = px.bar(tabela_filtrada, x="Nome", y="Valor do carro vendido", color="Modelo do carro vendido", barmode="group")
    return fig


if __name__ == '__main__':
    app.run(debug=True)


