import xml.etree.ElementTree as ET
from datetime import datetime

def gerar_xml_dps(prestador_cnpj, tomador_cnpj, valor_servico, discriminacao):
    """
    Gera o XML da DPS (Declaração de Prestação de Serviço) no padrão da NFS-e Nacional.
    """
    root = ET.Element("DPS", xmlns="http://www.sped.fazenda.gov.br/nfse")

    infDPS = ET.SubElement(root, "infDPS", Id=f"DPS{datetime.now().strftime('%Y%m%d%H%M%S')}")

    # Identificação da DPS
    ET.SubElement(infDPS, "tpAmb").text = "1" # 1 - Produção, 2 - Homologação
    ET.SubElement(infDPS, "dhEmi").text = datetime.now().isoformat()

    # Prestador
    prestador = ET.SubElement(infDPS, "prest")
    ET.SubElement(prestador, "CNPJ").text = prestador_cnpj

    # Tomador
    tomador = ET.SubElement(infDPS, "toma")
    ET.SubElement(tomador, "CNPJ").text = tomador_cnpj

    # Valores e Serviço
    servico = ET.SubElement(infDPS, "serv")
    valores = ET.SubElement(servico, "valores")
    ET.SubElement(valores, "vServ").text = f"{valor_servico:.2f}"

    ET.SubElement(servico, "cTribNacional").text = "010101" # Exemplo de código de tributação nacional
    ET.SubElement(servico, "xLocPrestacao").text = "Rio de Janeiro"

    ET.SubElement(servico, "xDiscriminacao").text = discriminacao

    # Retorna o XML em formato string
    xml_string = ET.tostring(root, encoding='utf-8', xml_declaration=True).decode('utf-8')
    return xml_string
