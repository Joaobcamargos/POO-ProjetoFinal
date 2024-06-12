
from Pessoa import Pessoa
from ClienteVip import ClienteVIP #FOI NECESSARIO PARA O SISTEMA DE UPGRADE
import pandas as pd




class Funcionario(Pessoa):
    def __init__(self, id: str, nome: str, email: str, telefone: str, idade: int, data_de_cadastro: str) -> None:
        super().__init__(id, nome, email, telefone, idade, data_de_cadastro)
        self.atividades = []  # Lista para registrar atividades
        self.add_to_global_db()
        self.create_personal_db()

    def enviar_fatura(self, cliente) -> None:
        if "Solicitou Fatura" in cliente.atividades:
            assunto = "Fatura solicitada"
            corpo_email = "Prezado cliente, segue em anexo a sua fatura solicitada. Att, Equipe da Empresa."
            self.enviar_email(cliente.nome, cliente.email, assunto, corpo_email)
            self.registrar_atividade("Enviou fatura")  # funciona bugadamente

    def enviar_recibo(self, cliente) -> None:
        if "Solicitou Recibo" in cliente.atividades:
            assunto = "Recibo solicitado"
            corpo_email = "Prezado cliente, segue em anexo o seu recibo solicitado. Att, Equipe da Empresa."
            self.enviar_email(cliente.nome, cliente.email, assunto, corpo_email)
            self.registrar_atividade("Enviou recibo")

    def enviar_upgrade(self, cliente) -> ClienteVIP:
        cliente.remove_from_global_db()
        cliente_vip = ClienteVIP(cliente)
        cliente_vip.add_to_global_db()

        cliente_vip.update_personal_db('Tornou-se VIP')
        print(f"{cliente.nome} foi promovido a cliente VIP!")
        return cliente_vip

    def registrar_atividade(self, atividade) -> None:
        self.atividades.append(atividade)
        self.update_personal_db(atividade)

    def add_to_global_db(self) -> None:
        try:
            df = pd.read_excel('funcionarios.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('funcionarios.xlsx', index=False)

    def create_personal_db(self) -> None:
        df = pd.DataFrame({"Atividade": []})
        df.to_excel(f'{self.nome}_atividades.xlsx', index=False)

    def update_personal_db(self, atividade) -> None:
        df = pd.read_excel(f'{self.nome}_atividades.xlsx')
        new_row = pd.DataFrame({"Atividade": [atividade]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(f'{self.nome}_atividades.xlsx', index=False)

    def ver_atividades_cliente(self, cliente_nome: str) -> None:
        try:
            df = pd.read_excel(f'{cliente_nome}_atividades.xlsx')
            print(f"Histórico de atividades do cliente {cliente_nome}:")
            print(df)
        except FileNotFoundError:
            print(f"Histórico de atividades para o cliente {cliente_nome} não encontrado.")

    def mostrar_historico(self) -> None:
        df = pd.read_excel(f'{self.nome}_atividades.xlsx')
        print(df)
