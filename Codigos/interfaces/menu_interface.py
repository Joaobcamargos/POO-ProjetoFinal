from abc import ABC, abstractmethod


class MenuI(ABC):
    @abstractmethod
    def iniciarMenu(self, objeto: object) -> None:
        """
        Método abstrato que deve ser implementado pelas subclasses para iniciar o menu de interação.

        Args:
            objeto (object): O objeto para o qual o menu está sendo iniciado. Pode ser uma instância de qualquer classe.
        """
        pass
