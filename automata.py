
class Automata:
    def __init__(self):
        self.alphabet = list()
        self.states = list()
        self.transitions = list()  # Lista de tuplas
        self.initial = None
        self.finals = list()

    # Adiciona um novo estado a lista de estados do autômato
    def add_state(self, new_state):
        self.states.append(new_state)
        self.states.sort()  # Ordenando os estados

    # Adiciona um símbolo para a lista de alfabetos
    def add_alphabet_symbol(self, new_symbol):
        self.alphabet.append(new_symbol)
        self.alphabet.sort()  # Ordenando o alfabeto

    # Adiciona uma transição ao autômato
    def add_transition(self, init, dest, letter):
        if letter in self.alphabet:  # Verificação de que se a letra está presente no alfabeto

            # Verificando se os estados estão na lista de estados do autômato
            if init in self.states and dest in self.states:
                """ Adicionando transição = Do estado "init" com a "letter" do alfabeto 
                    eu chego no estado "dest" """
                self.transitions.append((init, letter, dest))
                self.transitions.sort()  # Ordenando as transições
                return True

            else:
                return False  # Indicando que os estados não estão na lista de estados

        else:
            return False  # Indicando que não foi possível fazer a transição

    # Adiciona uma estado como estado inicial(podendo ser apenas um)
    def set_as_initial_state(self, state):
        if state in self.states and self.initial is None:
            self.initial = state
            return True

        return False

    # Seta os estados finais do autômato(podendo ser mais de um)
    def set_as_final_state(self, state):
        if state in self.states:
            self.finals.append(state)
            self.finals.sort()
            return True

        return False

    # Mostra os estados na tela do usuário e suas transições
    def states_to_string(self):
        str = ""
        for state in self.states:  # Percorrendo cada estado da lista de estados
            str = str + ("[ " + state + " ]")
            for trans in self.transitions:  # Verificando as transições do autômato
                # Indicando se o estado atual da iteração foi o estado de partida
                if trans[0] == state:
                    # trans[1] é a letra do alfabeto para percorrer o autômato
                    """ trans[2] é o estado de destino ao percorrer-se esta letra a partir 
                        do estado de partida"""
                    str = str + "--{ '" + trans[1] + "' }->" + "[ " + trans[2] + " ]"
                    str = str + "\t"

            str = str + "\n"

        return str

    # Método para percorrer o autômato utilizando-se de uma string de letras de seu alfabeto
    def string_transition(self, string):
        if self.initial is None:
            return "Autômato não possui estado inicial"

        current_state = self.initial  # Começando a percorrer do estado inicial
        for char in string:  # Percorrendo-se a String
            if char in self.alphabet:
                for trans in self.transitions:  # Percorrendo-se as transições
                    # Verificando o estado de partida e a letra para ele percorrer para um próx. estado
                    if trans[0] == current_state and trans[1] == char:
                        current_state = trans[2]  # Percorreu-se para o próximo estado
                        break  # Saindo do laço pois já gastou-se o caracter da string
            else:
                # Caso em que encontrou um caracter que não está na lista do alfabeto do autômato
                return "String não aceita pelo autômato"

        if current_state in self.finals:
            return "String aceita pelo autômato"
        else:
            return "String não aceita pelo autômato"


if __name__ == "__main__":

    automata = Automata()

    automata.add_alphabet_symbol("a")
    automata.add_alphabet_symbol("b")

    automata.add_state("1")
    automata.add_state("2")
    automata.add_state("3")

    automata.add_transition("1", "2", "a")
    automata.add_transition("1", "3", "b")

    automata.add_transition("2", "1", "b")
    automata.add_transition("2", "2", "a")

    automata.add_transition("3", "3", "b")
    automata.add_transition("3", "2", "a")

    automata.set_as_initial_state("1")
    automata.set_as_final_state("3")

    # Exemplo de string
    print(automata.string_transition("aaaabbbbbababaabbbaabbb"))

