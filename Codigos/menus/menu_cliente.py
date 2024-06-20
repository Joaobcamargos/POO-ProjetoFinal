from Codigos.interfaces.menu_interface import MenuI
from Codigos.models.cliente import Cliente
from Codigos.models.funcionario import Funcionario
import uuid

class MenuCliente(MenuI):
    def iniciarMenu(self, cliente: Cliente) -> None:
        """
        Inicia o menu de interações para o cliente.
        Args:
            cliente (Cliente): Instância do cliente que está utilizando o menu.
        """
        b = True
        FuncionarioBase = Funcionario(str(uuid.uuid4()), 'Funcionário Base', 'base@empresa.com')

        while b:
            print(f'Olá, {cliente.nome}!')
            print('Escolha uma das opções: \n')
            print('1 - Solicitar uma fatura')
            print('2 - Solicitar um recibo')
            print('3 - Verificar seu histórico')
            print('0 - Sair')

            try:
                caso = int(input())  # Input do usuário para selecionar uma opção
            except ValueError:
                print('Opção inválida. Por favor, digite novamente.')
                continue

            match caso:
                case 1:
                    cliente.solicitar_fatura(FuncionarioBase)
                case 2:
                    cliente.solicitar_recibo(FuncionarioBase)
                case 3:
                    cliente.mostrar_historico()
                case 0:
                    print("Saindo do menu...")
                    b = False
                case _:
                    print('Opção inválida. Por favor, digite novamente.')

            if b:
                c = input('Você deseja continuar? [S/N]').upper()
                if c != 'S':
                    b = False
