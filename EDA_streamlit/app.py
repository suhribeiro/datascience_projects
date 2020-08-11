import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # BARRA LATERAL - MENU
    st.sidebar.subheader('Passo 1')

    # Definindo separador do arquivo
    sep_options = ["(,) - Vírgula", "(;) - Ponto e Vírgula"]
    sep = st.sidebar.radio('Escolha o separador: ', sep_options)
    if sep == sep_options[0]:
        sep = ','
    if sep == sep_options[1]:
        sep = ';'

    # Carregando o arquivo
    file = st.sidebar.file_uploader('Selecione um arquivo .csv para carregar:', type=['csv'])
    if file is not None:
        df = pd.read_csv(file, delimiter=sep)
        st.sidebar.subheader('Passo 2')
        options_list = ('Conhecendo os dados', 'Análise Exploratória', 'Visualização dos dados')
        option = st.sidebar.radio('Escolha o tipo de análise:', options_list)

        num = df.dtypes[df.dtypes != 'object'].index  # Variáveis numéricas
        cat = df.dtypes[df.dtypes == 'object'].index  # Variáveis categóricas

        # SEÇÃO - CONHECENDO OS DADOS
        if option == options_list[0]:
            st.header('Conhecendo os dados carregados...')
            st.subheader('Visão geral')
            st.write('O arquivo carregado possui um total de ', df.shape[0], ' linhas e ', df.shape[1], ' colunas.')
            number = st.slider('Escolha abaixo quantas linhas quer visualizar como amostra', min_value=5, max_value=50)
            st.dataframe(df.head(number))

            st.subheader('Tipos de dados')
            st.write('Tipos de dados presentes no arquivo:')
            st.dataframe({'Tipo': df.dtypes.value_counts().index, 'Qtd': df.dtypes.value_counts().values})

            st.write('Tipos de dados por coluna:')
            st.dataframe({'Coluna': df.dtypes.index, 'Tipo': df.dtypes.values})

            st.subheader('Dados ausentes')
            aux = pd.DataFrame({'Coluna': df.isna().sum().index, 'Tipo': df.dtypes, 'Qtd. Nulos': df.isna().sum(),
                                '% Nulos': df.isna().sum() / df.shape[0] * 100})
            st.dataframe(aux)
            st.write('O arquivo possui um total de ', aux['Qtd. Nulos'].sum(), ' campos nulos.')
            # Evolução posterior - input de dados faltantes

            st.subheader('Registros duplicados')
            st.write('Existem ', df.duplicated().sum(), 'registros duplicados do dataframe.')
            # Evolução posterior - apagar registros duplicados e exibir.

        # SEÇÃO - EXPLORANDO OS DADOS
        if option == options_list[1]:
            st.header('Explorando os dados...')
            # Numéricas
            st.subheader('Variáveis numéricas')
            # Opções de análise
            eda_options = ('Exploração Univariada', 'Exploração Multivariada')
            eda_option = st.radio('Escolha o tipo de exploração:', eda_options)
            # Exploração Univariada
            if eda_option == eda_options[0]:
                column = st.selectbox('Selecione qual atributo deseja avaliar: ', num)
                if column is not None:
                    mean = st.checkbox('Média')
                    if mean:
                        st.write('A média aritimética simples é o resultado da soma de todos os valores da coluna selecionada dividida pelo número de registros. '
                                 'A média é uma das medidas de centralidades mais utilizadas. Deve-se tomar cuidado, pois ela é muito sensível a outliers.')
                        st.markdown(df[column].mean().round(2))
                    median = st.checkbox('Mediana')
                    if median:
                        st.write('A mediana é uma medida de centralidade que determina qual o valor ocupa o valor central dos registros ordenados de forma crescente.')
                        st.markdown(df[column].median().round(2))
                    mode = st.checkbox('Moda')
                    if mode:
                        st.write('A moda é o valor que mais aparece na lista de registros.')
                        st.markdown(df[column].mode()[0])
                    std = st.checkbox('Desvio Padrão')
                    if std:
                        st.write('O desvio padrão é uma medida que expressa o grau de dispersão de um conjunto de dados. Ou seja, quanto mais próximo de 0 for o desvio padrão, mais homogêneos são os dados.')
                        st.markdown(df[column].std().round(2))
                    skew = st.checkbox('Skewness')
                    if skew:
                        st.write('Skewness mede a assimetria na distribuição dos dados.')
                        st.markdown(df[column].skew().round(2))
                    kurtosis = st.checkbox('Kurtosis')
                    if kurtosis:
                        st.write('A curtose é uma medida de forma que caracteriza o achatamento da curva da função de distribuição de probabilidade')
                        st.markdown(df[column].kurtosis().round(2))
                    boxplot = st.checkbox('Boxplot')
                    if boxplot:
                        plt.figure(figsize=(8, 5))
                        sns.set(style="whitegrid")
                        ax = sns.boxplot(x=df[column])
                        st.pyplot()
            # Exploração Multivariada
            if eda_option == eda_options[1]:
                st.subheader('Correlação')
                corr = st.multiselect('Selecione os atributos:', num.values)
                st.write('Escolha um tipo de correlação')
                pearson = st.checkbox('Pearson')
                if pearson:
                    st.write('O coeficiente de correlação de Pearson (r), também chamado de correlação linear ou r de Pearson, é um grau de relação entre duas variáveis quantitativas e exprime o grau de correlação através de valores situados entre -1 e 1.')
                    res = df[corr].corr(method='pearson')
                    sns.heatmap(res, fmt='.2f', square=True, annot=True)
                    st.pyplot()
                spearman = st.checkbox('Spearman')
                if spearman:
                    st.write('Denominado pela letra grega rho (ρ), o coeficiente de correlação de postos de Spearman é uma medida de correlação não paramétrica também avaliado no intervalo entre -1 e 1.')
                    res = df[corr].corr(method='spearman')
                    sns.heatmap(res, fmt='.2f', square=True, annot=True)
                    st.pyplot()
                kendall = st.checkbox('Kendall')
                if kendall:
                    st.write('Expresso pela letra grega tau (τ), o coeficiente de correlação de Kendall é uma medida de associação para variáveis ordinais. Uma vantagem de tau sobre o coeficiente de Spearman é a possibilidade de ser generalizado para um coeficiente de correlação parcial.')
                    res = df[corr].corr(method='kendall')
                    sns.heatmap(res, fmt='.2f', square=True, annot=True)
                    st.pyplot()
            # Categóricas
            st.subheader('Variáveis categóricas')
            # aux = pd.DataFrame(df[cat])
            # st.write(aux)
            # st.dataframe(aux)
            st.write(df.describe(include=['O']))

            # SEÇÃO - VISUALIZAÇÃO DE DADOS
        if option == options_list[2]:
            # histograma
            st.subheader('Histograma')
            st.write('O histograma, também conhecido como distribuição de frequências, é a representação gráfica em colunas ou em barras de um conjunto de dados previamente tabulado e dividido em classes uniformes ou não uniformes')
            col_num = st.selectbox('Selecione a Coluna Numérica', num)
            st.markdown('Histograma da coluna: ' + str(col_num))
            sns.distplot(df[col_num])
            st.pyplot()

            # target
            st.subheader('Distribuição target')
            var = st.selectbox('Selecione a váriavel alvo(target): ', num, 1)
            st.subheader('Balanceamento de classes')
            sns.countplot(y=df[var])
            st.pyplot()
    st.sidebar.subheader('-')
    opt = st.sidebar.checkbox('Sobre')

    if opt:
        st.subheader('Sobre esta ferramenta: ')
        st.write('Essa é uma ferramenta simples para a realização de uma análise exploratória inicial de arquivos .csv')
        st.write(
            'O objetivo principal é explorar e conhecer os recursos disponibilizados pelo framework Streamlit, apresentado durante o bootcamp aceleradev Data Science - 2020.')
        st.subheader('Sobre a autora: ')
        st.write(
            'Graduada em Sistemas de informação e pós graduanda em Ciência de dados e Big Data, ambas pela PUC Minas, atuo na área de dados há mais de 5 anos. Procuro usar minhas habilidades e experiências para gerar informações que tragam mais valor ao negócio e colaborar com outras áreas dentro da organização.'
            'Possuo experiência com Python, SQL, AWS Cloud, Lambda funcions, SageMaker, Git, Dremio, Power BI, Airflow, Análise de dados, Business Intelligence, Machine Learning.')
        st.markdown('[Linkedin](https://www.linkedin.com/in/suellenrimel/)')
        st.markdown('[Github](https://github.com/suhribeiro)')

if __name__ == '__main__':
    main()
