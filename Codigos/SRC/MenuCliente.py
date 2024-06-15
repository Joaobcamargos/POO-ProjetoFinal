from Codigos.INTERFACES.MenuInterface import MenuI
from Cliente import Cliente
from Funcionario import Funcionario
import uuid



class MenuCliente(MenuI):
    def iniciarMenu(self, cliente: Cliente,) -> None:
        b = True
        FuncionarioBase = Funcionario(str(uuid.uuid4()), 'Funcionário Base', 'base@empresa.com')
        while b:
            print(f'Olá, {cliente.nome}!')
            print('Digite 1 para solicitar uma fatura')
            print('Digite 2 para solicitar um recibo')
            print('Digite 3 para verificar seu histórico')
            print('Digite 0 para sair')

            caso = int(input())
            match caso:
                case 1:
                    cliente.solicitar_fatura(FuncionarioBase)
                case 2:
                    cliente.solicitar_recibo(FuncionarioBase)
                case 3:
                    cliente.mostrar_historico(FuncionarioBase)
                case 0:
                    print("Saindo do menu...")
                    b = False
                case _:
                    print('Opção inválida. Por favor, digite novamente.')

            if b:
                c = input('Você deseja continuar? [S/N]').upper()
                if c != 'S':
                    b = False
