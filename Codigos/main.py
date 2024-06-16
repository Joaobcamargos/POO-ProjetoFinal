import uuid
from models.cliente import Cliente
from models.funcionario import Funcionario
from menus.menu_cliente import MenuCliente
from menus.menu_funcionario import MenuFuncionario

def main():
    """
    Criando algumas instâncias iniciais(opcional) e inicia os menus a partir da entrada
    """
    Funcionario1 = Funcionario(str(uuid.uuid4()), 'João', 'dautonico32@gmail.com')
    Cliente1 = Cliente(str(uuid.uuid4()), 'Marcos', 'joaovitorbatista12337@gmail.com')
    Cliente1.solicitar_fatura(Funcionario1)
    Cliente2 = Cliente(str(uuid.uuid4()), 'Joaquim', 'email.com')

    a = int(input('Digite 1 se quer testar Cliente ou 2 para testar funcionario'))
    match a:
        case 1:
            Cliente.criar_cliente(MenuCliente)
        case 2:
            Funcionario.criar_funcionario(MenuFuncionario)

if __name__ == "__main__":
    main()
