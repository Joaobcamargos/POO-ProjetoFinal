import pandas as pd
import uuid
from .pessoa import Pessoa
from typing import Type

class Cliente(Pessoa):
    def __init__(self, id: str, nome: str, email: str) -> None:
        super().__init__(id, nome, email)
        self.atividades = []
        self.add_to_global_db()
        self.create_personal_db()

    def solicitar_fatura(self, funcionario) -> None:
        self.registrar_atividade("Solicitou Fatura")
        funcionario.enviar_fatura(self)

    def solicitar_recibo(self, funcionario) -> None:
        self.registrar_atividade("Solicitou Recibo")
        funcionario.enviar_recibo(self)

    def cancelar_assinatura(self) -> None:
        self.registrar_atividade("Solicitou cancelamento")

    def registrar_atividade(self, atividade) -> None:
        self.atividades.append(atividade)
        self.update_personal_db(atividade)

    def add_to_global_db(self) -> None:
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
        try:
            df = pd.read_excel('database/clientes.xlsx')
            df = df[~((df["Nome"] == self.nome) & (df["Email"] == self.email))]
            df.to_excel('database/clientes.xlsx', index=False)
        except FileNotFoundError:
            pass

    def create_personal_db(self) -> None:
        df = pd.DataFrame({"Atividade": []})
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def update_personal_db(self, atividade) -> None:
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        new_row = pd.DataFrame({"Atividade": [atividade]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def solicitar_upgrade(self, funcionario) -> None:
        self.registrar_atividade('Solicitou Upgrade')
        return funcionario.enviar_upgrade(self)

    @staticmethod
    def criar_cliente(menu: Type["MenuCliente"]) -> object:
        from Codigos.menus.menu_cliente import MenuCliente

        menu = MenuCliente()
        nome1 = input('Nome do cliente: ')
        email1 = input('E-mail do cliente: ')
        while email1.count('@') != 1:
            email1 = input('Caracteres invalidos coloque apenas 1 arroba. E-mail do cliente: ')
        cliente1 = Cliente(str(uuid.uuid4()), nome1, email1)
        menu.iniciarMenu(cliente1)
        return cliente1

    def mostrar_historico(self) -> None:
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        print(df)
