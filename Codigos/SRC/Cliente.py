
from Pessoa import Pessoa
import pandas as pd

class Cliente(Pessoa):
    def __init__(self, id: str, nome: str, email: str, telefone: str, idade: int, data_de_cadastro: str) -> None:
        super().__init__(id, nome, email, telefone, idade, data_de_cadastro)
        self.atividades = []  # Lista para registrar atividades
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
        try:
            df = pd.read_excel('clientes.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('clientes.xlsx', index=False)

    def remove_from_global_db(self) -> None:
        try:
            df = pd.read_excel('clientes.xlsx')
            df = df[~((df["Nome"] == self.nome) & (df["Email"] == self.email))]
            df.to_excel('clientes.xlsx', index=False)
        except FileNotFoundError:
            pass

    def create_personal_db(self) -> None:
        df = pd.DataFrame({"Atividade": []})
        df.to_excel(f'{self.nome}_atividades.xlsx', index=False)

    def update_personal_db(self, atividade) -> None:
        df = pd.read_excel(f'{self.nome}_atividades.xlsx')
        new_row = pd.DataFrame({"Atividade": [atividade]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(f'{self.nome}_atividades.xlsx', index=False)

    def solicitar_upgrade(self, funcionario) -> None:
        self.registrar_atividade('Solicitou Upgrade')
        return funcionario.enviar_upgrade(self)

    def mostrar_historico(self) -> None:
        df = pd.read_excel(f'{self.nome}_atividades.xlsx')
        print(df)
