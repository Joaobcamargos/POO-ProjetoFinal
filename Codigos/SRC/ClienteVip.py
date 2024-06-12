from Cliente import Cliente
import pandas as pd
class ClienteVIP(Cliente):
    def __init__(self, cliente: Cliente) -> None:
        super().__init__(cliente.id, cliente.nome, cliente.email, cliente.telefone, cliente.idade,
                         cliente.data_de_cadastro)
        self.status = "VIP"
        self.add_to_global_db()

    def solicitar_upgrade(self, funcionario) -> None:
        print("Cliente já é VIP")

    def add_to_global_db(self) -> None:
        try:
            df = pd.read_excel('clientes_vip.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('clientes_vip.xlsx', index=False)

    def mostrar_historico(self) -> None:
        super().mostrar_historico()

    def acesso_exclusivo(self) -> None:
        print(f"{self.nome} tem acesso exclusivo!")

    def atendimento_prioritario(self) -> None:
        print(f"{self.nome} tem atendimento prioritário!")
