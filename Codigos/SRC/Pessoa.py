import smtplib
import email.message
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, id: str, nome: str, email: str) -> None:
        self.id = id
        self.nome = nome
        self.email = email


    def enviar_email(self, nome_destino: str, email_destino: str, assunto: str, corpo_email: str) -> None:
        msg = email.message.Message()
        msg['Subject'] = assunto
        msg['From'] = 'jjoaopoo@gmail.com'  # Substitua pelo seu email
        msg['To'] = email_destino
        password = 'pwpizdopbjoifitb'  # Use a senha de aplicativo gerada no Gmail
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')

    @abstractmethod
    def mostrar_historico(self) -> None:
        pass