import requests

token_acesso = 'EAAeBTZAEK2wsBQ6P7oNAZAGcTYeEhXyGOiOIQWkFzJKx7ZAdXE9DxZCX3OvsMzSPVe3rTZB5z8oWj4Jo5feELNSXSZA8FY9yZBUpym9WofkfjKCuoZAtttgOZARmnwxrhrT4ZCPBbQpNiv9X9dSFovtwzVLcgNBa2Eqg7SGDzdmwlp4TWDOEPrIDmvZCmsVZCxGGmpwZASwZB60oQHk1GGJqpkwVjFLvvNoqtVreR20wONRK3FoIIRwqi7PdQETFfqJOct7cXjHcndrHln2MxU2hY4z5pgXAZDZD'
id_numero = '1028372453690713'
numero_teste = '5527995700483'

def enviar_whatsapp(texto):
    url = f"https://graph.facebook.com/v18.0/{id_numero}/messages"
    
    headers = {
        "Authorization": f"Bearer {token_acesso}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": numero_teste,
        "type": "text",
        "text": {"body": texto}
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro: {response.status_code}")
        print(response.json())


enviar_whatsapp("Olá! Teste de API direto do Python.")