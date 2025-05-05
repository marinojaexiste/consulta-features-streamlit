import streamlit as st
import pandas as pd

st.title("Consulta de Features e Projetos")

uploaded_file = st.file_uploader("Faça o upload do arquivo Excel", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        # Renomear colunas para padronizar
        df.columns = ['Designer Responsável', 'Projeto', 'Features', 'Qual subsistema a feature consome?']

        # Substituir valores nulos por "Sem dados para exibir"
        df = df.fillna("Sem dados para exibir")

        st.success("Arquivo carregado com sucesso!")

        # Opções no menu lateral
        st.sidebar.title("Menu de Consulta")
        opcao = st.sidebar.radio("Escolha uma opção", [
            "Listar features por projeto",
            "Consultar projetos por feature",
            "Consultar designer por projeto",
            "Consultar subsistema por feature",
            "Consultar features por subsistema"
        ])

        if opcao == "Listar features por projeto":
            projeto = st.selectbox("Selecione o projeto", df["Projeto"].unique())
            resultado = df[df["Projeto"] == projeto]["Features"].unique()
            st.write("Features no projeto:")
            st.write(resultado)

        elif opcao == "Consultar projetos por feature":
            feature = st.selectbox("Selecione a feature", df["Features"].unique())
            resultado = df[df["Features"] == feature]["Projeto"].unique()
            st.write("Projetos que contêm a feature:")
            st.write(resultado)

        elif opcao == "Consultar designer por projeto":
            projeto = st.selectbox("Selecione o projeto", df["Projeto"].unique())
            resultado = df[df["Projeto"] == projeto]["Designer Responsável"].unique()
            st.write("Designer responsável pelo projeto:")
            st.write(resultado)

        elif opcao == "Consultar subsistema por feature":
            feature = st.selectbox("Selecione a feature", df["Features"].unique())
            resultado = df[df["Features"] == feature]["Qual subsistema a feature consome?"].unique()
            st.write("Subsistema consumido pela feature:")
            st.write(resultado)

        elif opcao == "Consultar features por subsistema":
            subsistema = st.selectbox("Selecione o subsistema", df["Qual subsistema a feature consome?"].unique())
            resultado = df[df["Qual subsistema a feature consome?"] == subsistema]["Features"].unique()
            st.write("Features que consomem o subsistema:")
            st.write(resultado)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
