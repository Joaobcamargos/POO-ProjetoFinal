from abc import ABC, abstractmethod
class ClienteI(ABC):

    @abstractmethod
    def solicitar_fatura(self, funcionario) -> None:
        """
        Solicita uma fatura ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por enviar a fatura.
        """
        pass

    @abstractmethod
    def solicitar_recibo(self, funcionario) -> None:
        """
        Solicita um recibo ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por enviar o recibo.
        """
        pass

    @abstractmethod
    def cancelar_assinatura(self) -> None:
        """
        Cancela a assinatura do cliente.
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
        Adiciona o cliente ao banco de dados global de clientes.
        """
        pass

    @abstractmethod
    def remove_from_global_db(self) -> None:
        """
        Remove o cliente do banco de dados global de clientes.
        """
        pass

    @abstractmethod
    def create_personal_db(self) -> None:
        """
        Cria um banco de dados pessoal para o cliente.
        """
        pass

    @abstractmethod
    def update_personal_db(self, atividade: str) -> None:
        """
        Atualiza o banco de dados pessoal do cliente com uma nova atividade.
        Args:
            atividade (str): Atividade a ser registrada.
        """
        pass

    @abstractmethod
    def solicitar_upgrade(self, funcionario) -> None:
        """
        Solicita um upgrade para ClienteVIP ao funcionário.
        Args:
            funcionario (Funcionario): Funcionário responsável por realizar o upgrade.
        """
        pass

    @abstractmethod
    def criar_cliente() -> object:
        """
        Cria um novo cliente e inicia o menu de cliente.
        Returns:
            Cliente: Novo cliente criado.
        """
        pass

    @abstractmethod
    def mostrar_historico(self) -> None:
        """
        Mostra o histórico de atividades do cliente.
        """
        pass
