from ram import Memoria

class Cache(Memoria):
    def __init__(self, tamanho, ram):
        Memoria.__init__(self, tamanho)
        self.ram = ram
        self.memoria = [0] * self.tamanho()
    
    def read(self, endereco):
        self.ram.verifica_endereco(endereco)
        for val in self.memoria:
            if(val == endereco):
                print(f'Cache HIT: {endereco}')
                return self.ram.read(endereco)
        
        print(f'Cache MISS: {endereco}')
        j = endereco
        for i in range(len(self.memoria)):
            self.memoria[i] = j
            j = j + 1
        
        return self.ram.read(endereco)

    def write(self, endereco, val):
        self.ram.verifica_endereco(endereco)
        for val in self.memoria:
            if(val == endereco):
                print(f'Cache HIT: {endereco}')
                return self.ram.write(endereco, val)
        
        print(f'Cache MISS: {endereco}')
        j = endereco
        for i in range(len(self.memoria)):
            self.memoria[i] = j
            j = j + 1
        
        return self.ram.write(endereco, val)