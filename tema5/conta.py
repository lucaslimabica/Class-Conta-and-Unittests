# 31.03.24 - TP5 - a82451 - Lucas de Lima Bica

class Conta:
    """Classe que representa uma conta bancária."""

    def __init__(self, titular, taxa_de_juro_prazo=0, saldo=0):
        self._titular = titular.title()
        self._taxa_de_juro_prazo = max(0, taxa_de_juro_prazo)
        self._saldo = max(0, saldo)

    def __str__(self):
        return f"Conta de {self._titular}, com um saldo de €{self._saldo} e taxa de juro a prazo de {self._taxa_de_juro_prazo} %"

    @property
    def titular(self):
        """Devolve o titular da conta."""
        return self._titular

    @titular.setter
    def titular(self, valor):
        """Guarda uma string formatada em "title".
        (e.g., 'luigi vercotti' -> 'Luigi Vercotti)"""
        self._titular = valor.title()

    @property
    def taxa_de_juro_prazo(self):
        """Devolve a taxa de juro a prazo."""
        return self._taxa_de_juro_prazo

    @taxa_de_juro_prazo.setter
    def taxa_de_juro_prazo(self, valor):
        """Guarda a taxa de juro a prazo.
        Deve ser numérica, em percentagem (0-100%).
        A taxa_de_juro não pode ser negativa, sendo que se for fornecido
        um valor negativo a taxa_de_juro é colocada a 0.
        """
        self._taxa_de_juro_prazo = max(0, valor)

    @property
    def saldo(self):
        """Devolve o saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Guarda o saldo. Deve ser numérico.
        O saldo não pode ser negativo, sendo que se for fornecido
        um valor negativo o saldo é colocado a 0.
        """
        self._saldo = max(0, valor)

    def capitaliza_juros(self):
        """Acrescenta os juros ao saldo.
        E.g., se saldo = 1000 e taxa_juro = 2 então saldo passa a 1020
        """
        juros = self._saldo * self._taxa_de_juro_prazo / 100
        self._saldo += juros

    def cobra_comissao_bancaria(self, valor):
        """O valor da comissão é retirado ao saldo.
        Se o saldo for maior do que a comissão então cobra tudo, senão
        cobra o equivalente ao existente em saldo.
        E.g.:
        saldo = 10 e comissão = 5 -> saldo = 5 e cobrado = 5
        saldo = 10 e comissão = 15 -> saldo = 0 e cobrado = 10

        :return: valor descontado ao saldo
        """
        cobrar = min(valor, self._saldo)
        self._saldo -= cobrar
        return cobrar

    def faz_levantamento(self, valor):
        """
        Subtrai ao saldo o valor desde que o saldo se mantenha positivo.
        :return: True se o levantamento foi possível, False caso contrário.
        """
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def faz_deposito(self, valor):
        """Acrescenta ao saldo o valor"""
        self._saldo += valor


if __name__ == "__main__":
    conta = Conta("Quim")
    print(conta.titular, conta.taxa_de_juro_prazo, conta.saldo)
