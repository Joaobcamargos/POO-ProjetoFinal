from Codigos.interfaces.menu_interface import MenuI
from Codigos.models.funcionario import Funcionario
from Codigos.models.cliente import Cliente
from models.cliente_vip import ClienteVIP
import uuid
import pandas as pd

class MenuFuncionario(MenuI):
    def iniciarMenu(self, funcionario: Funcionario) -> None:
        b = True
        while b:
            print(f'Olá, {funcionario.nome}!')
            print('Digite 1 para ver o banco de dados dos clientes')
            print('Digite 2 para ver o banco de dados dos clientes Vips')
            print('Digite 3 para ver a atividade de um cliente específico')
            print('Digite 4 para ver seu histórico')
            print('Digite 5 para enviar um upgrade')
            print('Digite 0 para sair')

            caso = int(input())
            match caso:
                case 1:
                    funcionario.verificar_clientes()
                case 2:
                    funcionario.verificar_clientes_vips()
                case 3:
                    a = input("Digite o nome do cliente: ")
                    funcionario.ver_atividades_cliente(a)
                case 4:
                    funcionario.mostrar_historico()
                case 5:
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
