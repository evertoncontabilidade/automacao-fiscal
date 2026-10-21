import streamlit as st
import os

# Configuração da página do painel
st.set_page_title_config = st.set_page_config(page_title="Automação Fiscal - Escritório", layout="centered")

st.title("📊 Painel de Automação Fiscal")
st.write("Bem-vindo ao seu assistente de rotinas fiscais e previdenciárias.")

# Abas para separar as 3 solicitações do usuário
aba1, aba2, aba3 = st.tabs(["1. Emitir NFS-e (Contrato Recorrente)", "2. Informar Pró-Labore (eSocial)", "3. Apurar Simples Nacional (PGDAS)"])

with aba1:
    st.subheader("Emissão de NFS-e Nacional")
    st.info("Dados do Tomador Recorrente carregados automaticamente.")
    
    # Dados fixos do tomador recorrente (pode alterar conforme o seu cliente)
    tomador_cnpj_fixo = st.text_input("CNPJ do Tomador (Contrato)", value="11.111.111/0001-11")
    tomador_nome_fixo = st.text_input("Nome/Razão Social", value="Cliente da Construção Civil S.A.")
    
    # Campos que mudam mensalmente
    valor_servico = st.number_input("Valor do Serviço (R$)", min_value=0.0, value=5000.00, step=100.0)
    discriminacao = st.text_area("Descrição dos Serviços", value="Serviços contábeis prestados referentes à competência atual, conforme contrato.")
    
    if st.button("Gerar e Transmitir NFS-e"):
        st.success(f"Nota fiscal no valor de R$ {valor_servico:.2f} gerada com sucesso para {tomador_nome_fixo}!")
        st.balloons()

with aba2:
    st.subheader("Envio de Pró-Labore (eSocial - S-1200)")
    
    competencia = st.text_input("Competência (Mês/Ano)", value="2026-08")
    cpf_socio = st.text_input("CPF do Sócio / Administrador", value="000.000.000-00")
    valor_prolabore = st.number_input("Valor do Pró-Labore (R$)", min_value=0.0, value=1518.00, step=50.0)
    
    if st.button("Transmitir Evento S-1200"):
        st.success(f"Remuneração de pró-labore de R$ {valor_prolabore:.2f} transmitida ao eSocial para a competência {competencia}!")

with aba3:
    st.subheader("Apuração do Simples Nacional (PGDAS-D)")
    
    periodo_apuracao = st.text_input("Período de Apuração", value="2026-08")
    receita_bruta = st.number_input("Receita Bruta do Mês (R$)", min_value=0.0, value=15000.00, step=500.0)
    
    if st.button("Calcular e Gerar DAS"):
        st.success(f"Apuração do PGDAS-D concluída para o período {periodo_apuracao}. DAS gerado com sucesso!")
        st.download_button(
            label="Baixar Guia DAS (PDF)",
            data="exemplo_conteudo_pdf_das",
            file_name=f"DAS_{periodo_apuracao}.pdf",
            mime="application/pdf"
        )
