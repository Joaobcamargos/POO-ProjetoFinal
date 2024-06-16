
import pandas as pd
import uuid
from .pessoa import Pessoa
from .cliente_vip import ClienteVIP
from typing import Type
class Funcionario(Pessoa):
    def __init__(self, id: str, nome: str, email: str) -> None:
        """
        Inicializa o funcionário e adiciona ao banco de dados global e cria o banco de dados pessoal.
        Args:
            id (str): ID do funcionário.
            nome (str): Nome do funcionário.
            email (str): Email do funcionário.
        """
        super().__init__(id, nome, email)
        self.atividades = []
        self.add_to_global_db()
        self.create_personal_db()

    def enviar_fatura(self, cliente) -> None:
        """
        Envia uma fatura para o cliente se solicitado.
        Args:
            cliente (Cliente): Cliente que solicitou a fatura.
        """
        assunto = "Fatura solicitada"
        corpo_email = "Prezado cliente, segue em anexo a sua fatura solicitada. Att, Equipe da Empresa."
        self.enviar_email(cliente.nome, cliente.email, assunto, corpo_email)
        self.registrar_atividade("Enviou fatura")

    def enviar_recibo(self, cliente) -> None:
        """
        Envia uma fatura para o cliente se solicitado.
        Args:
            cliente (Cliente): Cliente que solicitou a fatura.
        """
        assunto = "Recibo solicitado"
        corpo_email = "Prezado cliente, segue em anexo o seu recibo solicitado. Att, Equipe da Empresa."
        self.enviar_email(cliente.nome, cliente.email, assunto, corpo_email)
        self.registrar_atividade("Enviou recibo")

    def enviar_upgrade(self, cliente) -> ClienteVIP:
        """
        Envia um upgrade para o cliente, transformando-o em ClienteVIP.
        Args:
           cliente (Cliente): Cliente a ser promovido a VIP.
        Returns:
           ClienteVIP: Novo cliente VIP.
        """
        cliente.remove_from_global_db()
        cliente_vip = ClienteVIP(cliente)
        cliente_vip.add_to_global_db()

        cliente_vip.update_personal_db('Tornou-se VIP')
        print(f"{cliente.nome} foi promovido a cliente VIP!")
        return cliente_vip

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
        Adiciona o funcionário ao banco de dados global de funcionários.
        """
        self.create_directory()
        try:
            df = pd.read_excel('database/funcionarios.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('database/funcionarios.xlsx', index=False)

    def create_personal_db(self) -> None:
        """
        Cria um banco de dados pessoal para o funcionário.
        """
        df = pd.DataFrame({"Atividade": []})
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def update_personal_db(self, atividade) -> None:
        """
        Atualiza o banco de dados pessoal do funcionário com uma nova atividade.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        new_row = pd.DataFrame({"Atividade": [atividade]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(f'database/atividades/{self.nome}_atividades.xlsx', index=False)

    def ver_atividades_cliente(self, cliente_nome: str) -> None:
        """
         Mostra as atividades de um cliente específico.
         Args:
            cliente_nome (str): Nome do cliente.
        """
        try:
            df = pd.read_excel(f'database/atividades/{cliente_nome}_atividades.xlsx')
            print(f"Histórico de atividades do cliente {cliente_nome}:")
            print(df)
        except FileNotFoundError:
            print(f"Histórico de atividades para o cliente {cliente_nome} não encontrado.")

    def verificar_clientes(self) -> None:
        """
        Mostra o banco de dados de clientes.
        """
        try:
            df = pd.read_excel('database/clientes.xlsx')
            print("Banco de Dados de Clientes:\n", df)
        except FileNotFoundError:
            print("Banco de dados de clientes não encontrado.")

    def verificar_clientes_vips(self) -> None:
        """
        Mostra o banco de dados de clientes VIPs.
        """
        try:
            df = pd.read_excel('database/clientes_vip.xlsx')
            print("Banco de Dados de Clientes VIPs:\n", df)
        except FileNotFoundError:
            print("Banco de dados de clientes VIPs não encontrado.")

    @staticmethod
    def criar_funcionario(menu: Type["MenuFuncionario"]) -> object:
        """
        Cria um novo funcionário e inicia o menu de funcionário.
        Args:
            menu (Type[MenuFuncionario]): Classe do menu de funcionário.
        Returns:
            Funcionario: Novo funcionário criado.
        """
        from Codigos.menus.menu_funcionario import MenuFuncionario
        menu = MenuFuncionario()
        nome1 = input('Nome do funcionario: ')
        email1 = input('E-mail do funcionario: ')
        funcionario1 = Funcionario(str(uuid.uuid4()), nome1, email1)
        menu.iniciarMenu(funcionario1)
        return funcionario1

    def mostrar_historico(self) -> None:
        """
        Mostra o histórico de atividades do funcionário.
        """
        df = pd.read_excel(f'database/atividades/{self.nome}_atividades.xlsx')
        print(df)
