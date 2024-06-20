from abc import ABC, abstractmethod
class PessoaI(ABC):

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    @abstractmethod
    def email(self):
        pass

    @email.setter
    @abstractmethod
    def email(self, email):
        pass

    @abstractmethod
    def enviar_email(self, nome_destino: str, email_destino: str, assunto: str, corpo_email: str) -> None:
        """
        Envia um email para o destinatário especificado.
        Args:
            nome_destino (str): Nome do destinatário.
            email_destino (str): Email do destinatário.
            assunto (str): Assunto do email.
            corpo_email (str): Corpo do email.
        """
        pass

    @abstractmethod
    def mostrar_historico(self) -> None:
        """
        Método abstrato para mostrar o histórico de atividades da pessoa.
        Deve ser implementado nas classes derivadas.
        """
        pass

    @abstractmethod
    def create_directory(self) -> None:
        """
        Cria os diretórios necessários para armazenar os bancos de dados, se não existirem.
        """
        pass


    @abstractmethod
    def validar_email(email: str) -> bool:
        """
        Valida se o email tem a formatação correta.
        Args:
            email (str): Email a ser validado.
        Returns:
            bool: True se o email é válido, False caso contrário.
        """
        pass

    @abstractmethod
    def email_existe(email: str) -> bool:
        """
        Verifica se o email já existe no banco de dados de clientes ou funcionários.
        Args:
            email (str): Email a ser verificado.
        Returns:
            bool: True se o email já existe, False caso contrário.
        """
        pass
