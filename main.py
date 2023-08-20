from ram import EnderecoInvalido, Memoria, RAM
from cpu import CPU
from es import IO
from cache import Cache
import sys

def main():
    try:
        io = IO(sys.stdin, sys.stdout)
        ram = RAM(7)
        cache = Cache(8, ram)
        cpu = CPU(cache, io)
        
        inicio = 10
        ram.write(inicio, 118)
        ram.write(inicio + 1, 130)
        cpu.run(inicio)
    except EnderecoInvalido as e:
        print("Endereço inválido:", e.ender, file=sys.stderr)

if __name__ == '__main__':
    main()