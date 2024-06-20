import pandas as pd
import smtplib
import email.message
from abc import ABC, abstractmethod
from Codigos.interfaces.pessoa_interface import PessoaI
import os
import re

class Pessoa(PessoaI,ABC):
    def __init__(self, id: str, nome: str, email: str) -> None:
        """
        Inicializa a classe base Pessoa.
        Args:
            id (str): ID da pessoa.
            nome (str): Nome da pessoa.
            email (str): Email da pessoa.
        """
        self.id = id
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    def enviar_email(self, nome_destino: str, email_destino: str, assunto: str, corpo_email: str) -> None:
        """
        Envia um email para o destinatário especificado.
        Args:
            nome_destino (str): Nome do destinatário.
            email_destino (str): Email do destinatário.
            assunto (str): Assunto do email.
            corpo_email (str): Corpo do email.
        """
        msg = email.message.Message()
        msg['Subject'] = assunto
        msg['From'] = 'jjoaopoo@gmail.com'  # Deveria ser configurável
        msg['To'] = email_destino
        password = 'pwpizdopbjoifitb'  # Deveria ser armazenada de forma segura (ex: variáveis de ambiente)
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        # Configuração e envio do email
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        print('Email enviado')

    @abstractmethod
    def mostrar_historico(self) -> None:
        """
        Método abstrato para mostrar o histórico de atividades da pessoa.
        Deve ser implementado nas classes derivadas.
        """
        pass

    def create_directory(self) -> None:
        """
        Cria os diretórios necessários para armazenar os bancos de dados, se não existirem.
        """
        if not os.path.exists('database'):
            os.makedirs('database')
        if not os.path.exists('database/atividades'):
            os.makedirs('database/atividades')

    def validar_email(email: str) -> bool:
        """
        Valida se o email tem a formatação correta.
        Args:
            email (str): Email a ser validado.
        Returns:
            bool: True se o email é válido, False caso contrário.
        """
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao, email) is not None

    def email_existe(email: str) -> bool:
        """
        Verifica se o email já existe no banco de dados de clientes ou funcionários.
        Args:
            email (str): Email a ser verificado.
        Returns:
            bool: True se o email já existe, False caso contrário.
        """
        arquivos = ['database/clientes.xlsx', 'database/funcionarios.xlsx']

        for arquivo in arquivos:
            try:
                df = pd.read_excel(arquivo)
                if email in df['Email'].values:
                    return True
            except FileNotFoundError:
                print(f"Arquivo {arquivo} não encontrado.")
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo}: {e}")

        return False

