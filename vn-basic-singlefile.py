#!/usr/bin/env python3

#
# von Neumann - Arquitetura Básica
# Todos as classes em um mesmo arquivo
# PSCF - Prof. Luiz Lima Jr.
#
# Arquitetura formada de 3 componentes básicos:
#
# 1. Memória => RAM
# 2. CPU
# 3. Entrada e Saída (IO)
#

from abc import abstractmethod
import sys


class IO:
    def __init__(self, entrada = sys.stdin, saida=sys.stdout):
        # saída-padrão = tela (stdout)
        self.entrada = entrada
        self.saida = saida

    def output(self, s):
        print(s, end='', file=self.saida)


# Exceção (erro)
class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender

    def __repr__(self):
        return self.ender


class Memoria:
    def __init__(self, capacidade):
        self._capacidade = capacidade

    def verifica_endereco(self, ender):
        if (ender < 0) or (ender >= self._capacidade):
            raise EnderecoInvalido(ender)

    def tamanho(self):
        return self._capacidade

    # métodos abstratos devem ser sobrescritos pelas subclasses

    @abstractmethod
    def read(self, ender): pass

    @abstractmethod
    def write(self, ender, val): pass


class RAM(Memoria):
    def __init__(self, k):
        Memoria.__init__(self, 2**k)
        self.memoria = [0] * self.tamanho()

    def read(self, ender):
        super().verifica_endereco(ender)
        return self.memoria[ender]

    def write(self, ender, val):
        super().verifica_endereco(ender)
        self.memoria[ender] = val


class CPU:
    def __init__(self, mem, io):
        self.mem = mem
        self.io = io
        self.PC = 0
        self.A = self.B = self.C = 0

    def run(self, ender):
        self.PC = ender
        self.A = self.mem.read(self.PC)
        self.PC += 1
        self.B = self.mem.read(self.PC)
        self.PC += 1

        self.C = 1
        while self.A <= self.B:
            self.mem.write(self.A, self.C)
            self.io.output(f'> {self.A} = {self.C}\n')
            self.C += 1
            self.A += 1


def main():
    try:
        io = IO()
        ram = RAM(7)
        cpu = CPU(ram, io)

        ram.write(10, 120)
        ram.write(11, 130)
        cpu.run(10)
    except EnderecoInvalido as e:
        print(f'Endereço inválido: {e}', file=sys.stderr)


if __name__ == '__main__':
    main()
