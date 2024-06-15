import pandas as pd
from .cliente import Cliente

class ClienteVIP(Cliente):
    def __init__(self, cliente: Cliente) -> None:
        super().__init__(cliente.id, cliente.nome, cliente.email)
        self.status = "VIP"
        self.add_to_global_db()

    def add_to_global_db(self) -> None:
        self.create_directory()
        try:
            df = pd.read_excel('database/clientes_vip.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=["ID", "Nome", "Email", "Status"])

        if not ((df["Nome"] == self.nome) & (df["Email"] == self.email)).any():
            new_row = pd.DataFrame({"ID": [self.id], "Nome": [self.nome], "Email": [self.email], "Status": [self.status]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel('database/clientes_vip.xlsx', index=False)
