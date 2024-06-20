import uuid
from models.cliente import Cliente
from models.funcionario import Funcionario



def main():
    """
    Criando algumas instâncias iniciais e iniciando os menus
    """
    try:
        Funcionario1 = Funcionario(str(uuid.uuid4()), 'João', 'dautonico32@gmail.com')
        Cliente1 = Cliente(str(uuid.uuid4()), 'Marcos', 'joaovitorbatista12337@gmail.com')
        Cliente1.solicitar_fatura(Funcionario1)
        Cliente2 = Cliente(str(uuid.uuid4()), 'Joaquim', 'joaquim@example.com')

        while True:
            print("Digite 1 para testar Cliente ou 2 para testar Funcionario, 0 para sair:")
            try:
                choice = int(input())
                if choice == 1:
                    Cliente.criar_cliente()
                elif choice == 2:
                    Funcionario.criar_funcionario()
                elif choice == 0:
                    print("Encerrando o programa.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
