# Título - Sistema de Vendas
# Seção Cadastrar venda
    #Campo Data
    #Campo Vendedor
    #Campo Produto
    #Campo Quantidade
    #Campo Valor
    #Botão cadastrar venda
        #quando clicar -> adicionar a venda na tabela e atualizar Dashboard
# Seção Vendas Cadastradas
    # Tabela com Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto

# pip install streamlit pandas plotly (terminal, caso seja primeira execução)

import streamlit as st
import pandas as pd
import plotly.express as px

#Carregar base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data", max_value="today")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica de cadastro
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0 or vendedor == "":
        st.warning ("Preencha todos os campos corretamente")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        #print(nova_venda)
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada")


# Seção de visualizar as Vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Seção de Dashboard
st.write("## Dashboard")
# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas,x="vendedor", y="valor", color="produto")#, color_discrete_map=['#EF553B','#448899','#FF7891'])
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)