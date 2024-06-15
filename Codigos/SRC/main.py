
import uuid
from Pessoa import Pessoa
from Cliente import Cliente
from Funcionario import Funcionario
from MenuCliente import MenuCliente
from MenuFuncionario import MenuFuncionario
from ClienteVip import ClienteVIP




def main():
    """
    Criando bancada de testes:
    """


    Funcionario1 = Funcionario(str(uuid.uuid4()), 'João', 'dautonico32@gmail.com')
    Cliente1 = Cliente(str(uuid.uuid4()), 'Marcos', 'joaovitorbatista12337@gmail.com')
    Cliente2 = Cliente(str(uuid.uuid4()), 'Joaquim', 'email.com')

    a = int(input('Digite 1 se quer testar Cliente ou 2 para testar funcionario'))
    match a:
        case 1:
            Cliente.criar_cliente(MenuCliente)
        case 2:
            Funcionario.criar_funcionario(MenuFuncionario)

if __name__ == "__main__":
    main()