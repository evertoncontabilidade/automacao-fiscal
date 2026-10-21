import requests

def transmitir_dps(xml_assinado, ambiente="1"):
    """
    Envia a DPS assinada para a API da NFS-e Nacional.
    Ambiente: "1" para Produção, "2" para Homologação (Testes).
    """
    # URLs oficiais do Ambiente de Dados Nacional (ADN) da Receita Federal
    if ambiente == "1":
        url = "https://nfse.receita.economia.gov.br/api/v1/dps"
    else:
        url = "https://homologacao.nfse.receita.economia.gov.br/api/v1/dps"
    
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/json"
    }
    
    try:
        # Envio da requisição POST com o XML assinado
        response = requests.post(
            url, 
            data=xml_assinado.encode('utf-8'), 
            headers=headers,
            timeout=30
        )
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
