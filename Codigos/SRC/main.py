
import uuid
from Pessoa import Pessoa
from Cliente import Cliente
from Funcionario import Funcionario
from ClienteVip import ClienteVIP




def main():
    cliente1 = Cliente(str(uuid.uuid4()), "João", "joao@email.com", "123456", 30, "01/01/2024")
    funcionario1 = Funcionario(str(uuid.uuid4()), "Maria", "maria@email.com", "654321", 25, "01/01/2024")

    cliente1.solicitar_fatura(funcionario1)
    cliente1.solicitar_recibo(funcionario1)
    cliente1.cancelar_assinatura()

    print("Histórico de atividades do cliente:")
    cliente1.mostrar_historico()

    print("\nHistórico de atividades do funcionário:")
    funcionario1.mostrar_historico()

    cliente2 = Cliente(str(uuid.uuid4()), "Ronaldinho", "joaovitorbatista12337@gmail.com", "123456", 30, "01/01/2024")
    cliente2.solicitar_fatura(funcionario1)
    cliente2.solicitar_recibo(funcionario1)
    cliente2 = cliente2.solicitar_upgrade(funcionario1)
    cliente2.solicitar_fatura(funcionario1)

    print("Histórico de atividades do cliente 2 após upgrade:")
    cliente2.mostrar_historico()
    cliente2.acesso_exclusivo()  #BUGADO
    cliente2.atendimento_prioritario() #BUGADO

    print("\nHistórico de atividades do funcionário após cliente2:")
    funcionario1.mostrar_historico()
    print('Funcionario 1 vendo historio do cliente1')

    funcionario1.ver_atividades_cliente('Ronaldinho')


if __name__ == "__main__":
    main()