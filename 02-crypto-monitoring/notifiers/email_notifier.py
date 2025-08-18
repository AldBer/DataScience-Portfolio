import smtplib
from email.message import EmailMessage
import requests

def enviar_alerta(subject, body):
    # Configurações de Email
    msg = EmailMessage()
    msg['Subject'] = f'🚨 Crypto Alert: {subject}'
    msg['From'] = 'aldo.bernardi@gmail.com'
    msg['To'] = 'aldo.bernardi@gmail.com'
    msg.set_content(body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('aldo.bernardi@gmail.com', 'ivrz umll dlhb jdzt')
        smtp.send_message(Atualizacao Crypto)

# Exemplo de trigger
if variacao > 0.05:  # 5% de variação
    enviar_alerta("BTC subiu 5%!", f"Preço atual: ${preco_atual}")