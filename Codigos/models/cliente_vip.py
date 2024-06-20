import pandas as pd
from .cliente import Cliente

class ClienteVIP(Cliente):
    def __init__(self, cliente: Cliente) -> None:
        """
        Inicializa o ClienteVIP com os dados de um Cliente existente.
        Args:
            cliente (Cliente): Cliente a ser promovido a VIP.
        """
        super().__init__(cliente.id, cliente.nome, cliente.email)
          # Inicializa o atributo 'status' antes de adicionar ao banco de dados
        self.add_to_global_db()

    def add_to_global_db(self) -> None:
        """
        Adiciona o cliente VIP ao banco de dados global de clientes VIPs.
        """
        self.create_directory()
        try:
            df = pd.read_excel('database/clientes_vip.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email", "Status"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('database/clientes_vip.xlsx', index=False)

    def mostrar_historico(self) -> None:
        """
        Mostra o histórico de atividades do cliente VIP.
        """
        super().mostrar_historico()

    def acesso_exclusivo(self) -> None:
        """
        Informa que o cliente VIP tem acesso exclusivo.
        """
        print(f"{self.nome} tem acesso exclusivo!")

    def atendimento_prioritario(self) -> None:
        """
        Informa que o cliente VIP tem atendimento prioritário.
        """
        print(f"{self.nome} tem atendimento prioritário!")