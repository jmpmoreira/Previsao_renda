import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
     page_title="Previsao de renda",
     page_icon=":R$:",
     layout="wide",
)

st.write('# Análise Exploratória da Previsão de Renda')

renda = pd.read_csv('previsao_de_renda.csv')

#plots
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)


# Definir estilo de plotagem com fundo preto
sns.set_style("darkgrid")

st.write('## Gráficos variáveis bivariadas')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0], palette='BuGn')
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1], palette='RdBu')
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2], palette='Blues')
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3], palette='Greens')
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4], palette='Purples')
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5], palette='Reds')
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6], palette='Oranges')
sns.despine()
st.pyplot(plt)







