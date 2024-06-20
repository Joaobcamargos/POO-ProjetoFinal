from Codigos.interfaces.menu_interface import MenuI
from Codigos.models.funcionario import Funcionario
from Codigos.models.cliente import Cliente
import uuid
import pandas as pd

class MenuFuncionario(MenuI):

    def iniciarMenu(self, funcionario: Funcionario) -> None:
        """
        Inicia o menu de funcionário.
        Args:
            funcionario (Funcionario): Funcionário para o qual o menu será iniciado.
        """
        b = True
        while b:
            print(f'Olá, {funcionario.nome}!')
            print('Escolha uma das opções: \n')
            print('1 - Ver atividades do cliente')
            print('2 - Ver banco de dados de clientes')
            print('3 - Ver banco de dados de clientes VIPs')
            print('4 - Solicitar upgrade de cliente para VIP')
            print('0 - Sair')

            try:
                op = int(input())
            except ValueError:
                print('Opção inválida. Por favor, digite novamente.')
                continue

            match op:
                case 1:
                    cliente_nome = input("Digite o nome do cliente para ver as atividades: ")
                    funcionario.ver_atividades_cliente(cliente_nome)
                case 2:
                    funcionario.verificar_clientes()
                case 3:
                    funcionario.verificar_clientes_vips()
                case 4:
                    cliente_nome = input("Digite o nome do cliente para upgrade: ")
                    cliente_email = input("Digite o email do cliente para upgrade: ")
                    try:
                        df = pd.read_excel('database/clientes.xlsx')
                        cliente_id = df.query(f'Nome == "{cliente_nome}" and Email == "{cliente_email}"')['ID'].values[0]
                        cliente = Cliente(cliente_id, cliente_nome, cliente_email)
                        funcionario.enviar_upgrade(cliente)
                    except (IndexError, FileNotFoundError):
                        print("Cliente não encontrado.")
                case 0:
                    print("Saindo do menu...")
                    b = False
                case _:
                    print('Opção inválida. Por favor, digite novamente.')

            if b:
                c = input('Você deseja continuar? [S/N]').upper()
                if c != 'S':
                    b = False
