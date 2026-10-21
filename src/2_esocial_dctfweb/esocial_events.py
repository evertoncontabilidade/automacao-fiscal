from datetime import datetime
import xml.etree.ElementTree as ET

def gerar_evento_s1200(empregador_cnpj, trabalhador_cpf, valor_prolabore):
    """
    Gera o XML do evento S-1200 (Remuneração de trabalhador) para o pró-labore no eSocial.
    """
    root = ET.Element("eSocial", xmlns="http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_02_00")
    
    evtRemun = ET.SubElement(root, "evtRemun", Id=f"ID1{empregador_cnpj}{datetime.now().strftime('%Y%m%d%H%M%S')}")
    
    # IdeEvento
    ideEvento = ET.SubElement(evtRemun, "ideEvento")
    ET.SubElement(ideEvento, "indRetif").text = "1"
    ET.SubElement(ideEvento, "indApuracao").text = "1"
    ET.SubElement(ideEvento, "perApur").text = datetime.now().strftime('%Y-%m')
    ET.SubElement(ideEvento, "tpAmb").text = "1" # 1 - Produção
    ET.SubElement(ideEvento, "procEmi").text = "1"
    ET.SubElement(ideEvento, "verProc").text = "1.0"
    
    # IdeEmpregador
    ideEmpregador = ET.SubElement(evtRemun, "ideEmpregador")
    ET.SubElement(ideEmpregador, "tpInsc").text = "1"
    ET.SubElement(ideEmpregador, "nrInsc").text = empregador_cnpj
    
    # IdeTrab
    ideTrab = ET.SubElement(evtRemun, "ideTrab")
    ET.SubElement(ideTrab, "cpfTrab").text = trabalhador_cpf
    
    # Remuneração (Pró-labore)
    info-rv = ET.SubElement(ideTrab, "infoRend")
    # Detalhes do vencimento da retirada do sócio
    
    xml_string = ET.tostring(root, encoding='utf-8', xml_declaration=True).decode('utf-8')
    return xml_string
