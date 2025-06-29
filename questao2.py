# Nodo da lista encadeada
class Estado:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

def funcao_hash(sigla):
    if sigla == 'DF':
        return 7
    else:
        return (ord(sigla[0]) + ord(sigla[1])) % 10

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  

    def inserir(self, sigla, nome_estado):
        posicao = funcao_hash(sigla)  
        novo_nodo = Estado(sigla, nome_estado)  
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo

    def imprimir(self):
        for i in range(10):
            print(f'Posição {i}:', end=' ')
            atual = self.tabela[i]
            if not atual:
                print('None')
            else:
                while atual:
                    print(f'{atual.sigla}', end=' -> ')
                    atual = atual.proximo
                print('None')

def main():
    estados = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    tabela = TabelaHash()

    print("Impressão da tabela hash antes de inserir qualquer informação:")
    tabela.imprimir()

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

    print("Impressão da tabela hash após inserir os 26 estados e o Distrito Federal - DF:")
    tabela.imprimir()

    # estado fictício com meu nome
    tabela.inserir('VZ', 'Victoria Zanella')
    print("impressão da tabela hash após inserir os 26 estados, Distrito Federal - DF e o estado fictício com meu nome completo:")
    tabela.imprimir()

if __name__ == "__main__":
    main()