import pandas as pd
import uuid
from .pessoa import Pessoa
from typing import Type
from Codigos.interfaces.cliente_interface import ClienteI

class Cliente(Pessoa,ClienteI):
    def __init__(self, id: str, nome: str, email: str) -> None:
        """
        Inicializa o cliente, adiciona ao banco de dados global e cria o banco de dados pessoal.
        Args:
            id (str): ID do cliente.
            nome (str): Nome do cliente.
            email (str): Email do cliente.
        """
        super().__init__(id, nome, email)
        self.atividades = []
        self.add_to_global_db()
        self.create_personal_db()

    def solicitar_fatura(self, funcionario) -> None:
        """
        Solicita uma fatura ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por enviar a fatura.
        """
        self.registrar_atividade("Solicitou Fatura")
        funcionario.enviar_fatura(self)

    def solicitar_recibo(self, funcionario) -> None:
        """
        Solicita um recibo ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por enviar o recibo.
        """
        self.registrar_atividade("Solicitou Recibo")
        funcionario.enviar_recibo(self)

    def cancelar_assinatura(self) -> None:
        """
        Cancela a assinatura do cliente.
        """
        self.registrar_atividade("Solicitou cancelamento")

    def registrar_atividade(self, atividade) -> None:
        """
        Registra uma atividade na lista de atividades e atualiza o banco de dados pessoal.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        self.atividades.append(atividade)
        self.update_personal_db(atividade)

    def add_to_global_db(self) -> None:
        """
        Adiciona o cliente ao banco de dados global de clientes.
        """
        self.create_directory()
        try:
            df = pd.read_excel('database/clientes.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('database/clientes.xlsx', index=False)

    def remove_from_global_db(self) -> None:
        """
        Remove o cliente do banco de dados global de clientes.
        """
        try:
            df = pd.read_excel('database/clientes.xlsx')
            df = df[~((df["Nome"] == self.nome) & (df["Email"] == self.email))]
            df.to_excel('database/clientes.xlsx', index=False)
        except FileNotFoundError:
            pass

    def create_personal_db(self) -> None:
        """
        Cria um banco de dados pessoal para o cliente.
        """
        df = pd.DataFrame({"Atividade": []})
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def update_personal_db(self, atividade) -> None:
        """
        Atualiza o banco de dados pessoal do cliente com uma nova atividade.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        new_row = pd.DataFrame({"Atividade": [atividade]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def solicitar_upgrade(self, funcionario) -> None:
        """
        Solicita um upgrade para ClienteVIP ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por realizar o upgrade.
        """
        self.registrar_atividade('Solicitou Upgrade')
        return funcionario.enviar_upgrade(self)


    def criar_cliente() -> object:
        """
        Cria um novo cliente e inicia o menu de cliente.
        Importando a biblioteca dentro do método para evitar bug de importação circular.
        Returns:
            Cliente: Novo cliente criado.
        """
        from Codigos.menus.menu_cliente import MenuCliente
        nome1 = input('Nome do cliente: ')
        email1 = input('E-mail do cliente: ')
        while not Cliente.validar_email(email1) or Cliente.email_existe(email1):
            email1 = input('Você digitou um email com a formatação errada ou um email já existente. Por favor, digite um novo email: ')
        cliente1 = Cliente(str(uuid.uuid4()), nome1, email1)
        menu=MenuCliente()
        menu.iniciarMenu(cliente1)
        return cliente1

    def mostrar_historico(self) -> None:
        """
        Mostra o histórico de atividades do cliente.
        """
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        print(df)
