from requests_pkcs12 import Session

def transmitir_dps_com_certificado(xml_assinado, caminho_pfx, senha_pfx, ambiente="1"):
    """
    Envia a DPS assinada para a API da NFS-e Nacional utilizando 
    o Certificado Digital A1 (.pfx) para autenticação mútua (mTLS).
    Ambiente: "1" para Produção, "2" para Homologação (Testes).
    """
    if ambiente == "1":
        url = "https://nfse.receita.economia.gov.br/api/v1/dps"
    else:
        url = "https://homologacao.nfse.receita.economia.gov.br/api/v1/dps"
    
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/json"
    }
    
    # Criamos uma sessão segura utilizando o certificado A1 (.pfx)
    session = Session()
    session.pkcs12_filename = caminho_pfx
    session.pkcs12_password = senha_pfx
    
    try:
        # Envio da requisição POST autenticada com o certificado da empresa
        response = session.post(
            url, 
            data=xml_assinado.encode('utf-8'), 
            headers=headers,
            timeout=30
        )
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
