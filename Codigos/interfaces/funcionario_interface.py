from abc import ABC, abstractmethod
from typing import Type


class FuncionarioI(ABC):

    @abstractmethod
    def enviar_fatura(self, cliente) -> None:
        """
        Envia uma fatura para o cliente se solicitado.
        Args:
            cliente (Cliente): Cliente que solicitou a fatura.
        """
        pass

    @abstractmethod
    def enviar_recibo(self, cliente) -> None:
        """
        Envia um recibo para o cliente se solicitado.
        Args:
            cliente (Cliente): Cliente que solicitou o recibo.
        """
        pass

    @abstractmethod
    def enviar_upgrade(self, cliente) -> Type['ClienteVIP']:
        """
        Envia um upgrade para o cliente, transformando-o em ClienteVIP.
        Args:
           cliente (Cliente): Cliente a ser promovido a VIP.
        Returns:
           ClienteVIP: Novo cliente VIP.
        """
        pass

    @abstractmethod
    def registrar_atividade(self, atividade: str) -> None:
        """
        Registra uma atividade na lista de atividades e atualiza o banco de dados pessoal.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        pass

    @abstractmethod
    def add_to_global_db(self) -> None:
        """
        Adiciona o funcionário ao banco de dados global de funcionários.
        """
        pass

    @abstractmethod
    def create_personal_db(self) -> None:
        """
        Cria um banco de dados pessoal para o funcionário.
        """
        pass

    @abstractmethod
    def update_personal_db(self, atividade: str) -> None:
        """
        Atualiza o banco de dados pessoal do funcionário com uma nova atividade.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        pass

    @abstractmethod
    def ver_atividades_cliente(self, cliente_nome: str) -> None:
        """
        Mostra as atividades de um cliente específico.
        Args:
            cliente_nome (str): Nome do cliente.
        """
        pass

    @abstractmethod
    def verificar_clientes(self) -> None:
        """
        Mostra o banco de dados de clientes.
        """
        pass

    @abstractmethod
    def verificar_clientes_vips(self) -> None:
        """
        Mostra o banco de dados de clientes VIPs.
        """
        pass

    @abstractmethod
    def criar_funcionario() -> object:
        """
        Cria um novo funcionário e inicia o menu de funcionário.
        Importando a biblioteca dentro do método para evitar bug de importação circular.
        Returns:
            Funcionario: Novo funcionário criado.
        """
        pass

    @abstractmethod
    def mostrar_historico(self) -> None:
        """
        Mostra o histórico de atividades do funcionário.
        """
        pass
