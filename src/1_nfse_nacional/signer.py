from signxml import XMLSigner
from cryptography.hazmat.serialization.pkcs12 import load_key_and_certificates
import lxml.etree as ET

def assinar_dps(xml_content, caminho_pfx, senha_pfx):
    """
    Assina o XML da DPS utilizando o Certificado Digital A1 (.pfx).
    """
    with open(caminho_pfx, "rb") as f:
        pfx_data = f.read()
        
    private_key, certificate, additional_certificates = load_key_and_certificates(
        pfx_data, senha_pfx.encode()
    )
    
    # Converte o XML para o formato lxml exigido pelo signxml
    root = ET.fromstring(xml_content.encode('utf-8'))
    
    signer = XMLSigner(
        method=XMLSigner.methods.enveloped,
        signature_algorithm="rsa-sha256",
        digest_algorithm="sha256"
    )
    
    signed_root = signer.sign(
        root,
        key=private_key,
        cert=certificate,
        reference_uri="#infDPS"
    )
    
    return ET.tostring(signed_root, encoding='utf-8').decode('utf-8')
