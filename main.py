import os
from dotenv import load_dotenv
from src.1_nfse_nacional.dps_generator import gerar_xml_dps
from src.1_nfse_nacional.signer import assinar_dps
from src.1_nfse_nacional.api_client import transmitir_dps_com_certificado
from src.3_pgdas.pgdas_automation import apurar_simples_nacional

# Carrega as variáveis de ambiente locais (.env)
load_dotenv()

def executar_rotina_mensal():
    print("--- INICIANDO AUTOMAÇÃO FISCAL (MUNICÍPIO DO RIO DE JANEIRO / NACIONAL) ---")
    
    # 1. Dados obtidos do ambiente
    cnpj = os.getenv("CNPJ_PRESTADOR", "00000000000100")
    caminho_cert = os.getenv("CERT_PATH", "config/seu_certificado.pfx")
    senha_cert = os.getenv("CERT_PASSWORD", "sua_senha")
    
    # 2. Exemplo de Emissão de NFS-e Nacional
    print("\n[Etapa 1] Gerando e transmitindo NFS-e Nacional...")
    xml_dps = gerar_xml_dps(
        prestador_cnpj=cnpj,
        tomador_cnpj="11111111000111",
        valor_servico=1500.00,
        discriminacao="Serviços prestados de contabilidade e consultoria na construção civil."
    )
    
    # Nota: No ambiente real, aqui invocará a função assinar_dps e transmitir_dps_com_certificado
    print("XML da DPS gerado com sucesso.")
    
    # 3. Exemplo de Apuração PGDAS
    print("\n[Etapa 3] Executando rotina do Simples Nacional (PGDAS)...")
    apurar_simples_nacional(cnpj, "2026-08")
    
    print("\n--- ROTINA FINALIZADA COM SUCESSO ---")

if __name__ == "__main__":
    executar_rotina_mensal()
