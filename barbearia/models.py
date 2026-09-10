# Modelo POO que representa um agendamento e faz a conversão para o banco.


class Agendamento:
    """Representa um agendamento da barbearia."""

    def __init__(
        self, cliente, telefone, servico, preco, barbeiro, data, horario,
        status="Agendado", id=None
    ):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def exibir(self):
        """Retorna um resumo legível do agendamento."""
        return (
            f"{self.cliente} — {self.servico} com {self.barbeiro} | "
            f"{self.data} às {self.horario} | {self.status}"
        )

    def converte_tupla(self):
        """Converte o objeto em tupla, na ordem das colunas da tabela."""
        return (
            self.cliente, self.telefone, self.servico, self.preco,
            self.barbeiro, self.data, self.horario, self.status
        )

    @staticmethod
    def reverte_tupla(tupla):
        """Converte uma tupla da tabela em um objeto Agendamento."""
        return Agendamento(
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbeiro=tupla[5],
            data=tupla[6],
            horario=tupla[7],
            status=tupla[8],
            id=tupla[0]
        )
