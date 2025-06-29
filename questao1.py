class Nodo:
    def __init__(self, cor, numero):
        self.cor = cor  # "A" ou "V"
        self.numero = numero  # número do paciente
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 0
        self.contador_amarelo = 200

    def inserirSemPrioridade(self, nodo):
        """
            Insere o nodo no final da lista.
        """

        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        """
            Insere o nodo depois do último com cor 'A' e antes do primeiro 'V'.
        """

        if not self.head or self.head.cor == 'V':
            # caso a lista estiver vazia ou o primeiro for verde:
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            anterior = None
            while atual and atual.cor == 'A':
                anterior = atual
                atual = atual.proximo
            # novo nodo após os amarelos e antes dos verdes
            nodo.proximo = atual
            anterior.proximo = nodo

    def inserir(self):
        """
            Solicita a cor do cartão e insere conforme prioridade.
        """
        while True:
            cor = input("\n--- INSERIR PACIENTE ---\nDigite a cor do cartão: \nA) Amarelo \nV) Verde\nSAIR) Voltar ao menu\n")
            cor = cor.upper()

            while cor not in ['A', 'V', 'SAIR']:
                cor = input("ERRO - Opção inválida. Digite apenas 'A', 'V' ou 'SAIR':\n")

            if cor == 'SAIR':
                break

            elif cor == 'V':
                self.contador_verde += 1
                numero = self.contador_verde
                print(f"Inserido cartão Verde número {numero}.")

            elif cor == 'A':
                self.contador_amarelo += 1
                numero = self.contador_amarelo
                print(f"Inserido cartão Amarelo número {numero}.")

            novo_nodo = Nodo(cor, numero)

            if not self.head:
                self.head = novo_nodo
            elif cor == 'V':
                self.inserirSemPrioridade(novo_nodo)
            elif cor == 'A':
                self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        """
            Imprime toda a lista de espera em ordem.
        """

        print("\n--- VISUALIZAR LISTA ---\n")
        atual = self.head
        if not atual:
            print("Nenhum paciente na fila para atendimento!")
            return
        while atual:
            print(f"{atual.cor}{atual.numero}", end=" -> ")
            atual = atual.proximo
        print("Fim")

    def atenderPaciente(self):
        """
            Atende (remove) o primeiro paciente da fila e imprime uma mensagem.
        """

        print("\n--- ATENDER PACIENTE ---")
        
        if not self.head:
            print("\nNenhum paciente na fila para atendimento!")
        else:
            paciente = self.head
            self.head = self.head.proximo
            print(f"\nChamando paciente cartão {paciente.cor}{paciente.numero} para atendimento.")


def main():
    fila = ListaEncadeada()

    while True:
        print("\n--- MENU --- ")
        print("1. Inserir paciente")
        print("2. Exibir fila")
        print("3. Atender paciente")
        print("4. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            fila.inserir()
        elif op == '2':
            fila.imprimirListaEspera()
        elif op == '3':
            fila.atenderPaciente()
        elif op == '4':
            print("\n--- ENCERRANDO ---")
            break
        else:
            print(f"\nA opção {op} é inválida. Tente novamente.")

if __name__ == "__main__":
    main()