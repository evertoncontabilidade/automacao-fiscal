import requests

def consultar_e_transmitir_dctfweb(cnpj_empresa, periodo_apuracao):
    """
    Realiza a comunicação com os serviços da Receita Federal para 
    verificar e consolidar a DCTFWeb da competência.
    """
    # URL base dos webservices oficiais de apuração previdenciária / DCTFWeb
    url = f"https://www.gov.br/esocial/api/v1/dctfweb/apuracao/{periodo_apuracao}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
