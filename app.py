import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="EC2 Streamlit projeto",
    page_icon="🚀"
)

st.title('Análise Financeira com Streamlit')

@st.cache_data
def load_data():
    df = pd.read_csv('MS_Financial Sample.csv', sep=';')
    df.columns = df.columns.str.strip()
    # Limpar e converter 'Units Sold'
    df['Units Sold'] = pd.to_numeric(df['Units Sold'].astype(str).str.replace(',', '').str.strip(), errors='coerce')
    return df

df = load_data()

st.write("### Preview dos dados")
st.dataframe(df.head())

# GRÁFICO 1. Unidades vendidas por segmento
units_por_segmento = df.groupby('Segment', as_index=False)['Units Sold'].sum()

chart1 = alt.Chart(units_por_segmento).mark_bar(color='skyblue').encode(
    x=alt.X('Segment', sort='-y', title='Segmento'),
    y=alt.Y('Units Sold', title='Unidades Vendidas'),
    tooltip=['Segment', 'Units Sold']
).properties(
    width=600,
    height=400,
    title='Unidades vendidas por segmento'
)

st.altair_chart(chart1, use_container_width=True)

# GRÁFICO 2. Distribuição das faixas de desconto
descontos = df['Discount Band'].value_counts().reset_index()
descontos.columns = ['Discount Band', 'Count']

pie = alt.Chart(descontos).mark_arc().encode(
    theta=alt.Theta(field='Count', type='quantitative'),
    color=alt.Color(field='Discount Band', type='nominal'),
    tooltip=['Discount Band', 'Count']
).properties(
    width=400,
    height=400,
    title='Distribuição das faixas de desconto'
)

st.altair_chart(pie, use_container_width=False)

# GRÁFICO 3. Top 10 produtos por unidades vendidas
unidades_por_produto = df.groupby('Product', as_index=False)['Units Sold'].sum()
unidades_por_produto = unidades_por_produto.sort_values('Units Sold', ascending=False).head(10)

chart3 = alt.Chart(unidades_por_produto).mark_bar(color='orange').encode(
    x=alt.X('Product', sort='-y', title='Produto'),
    y=alt.Y('Units Sold', title='Unidades Vendidas'),
    tooltip=['Product', 'Units Sold']
).properties(
    width=700,
    height=400,
    title='Top 10 produtos por unidades vendidas'
).configure_axisX(
    labelAngle=45
)

st.altair_chart(chart3, use_container_width=True)