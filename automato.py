def load_automaton(project):
    transitions = {} 
    with open(project, 'r') as arc:
        initial_state = arc.readline().strip()  # remove espaços em branco
        alphabet = set(arc.readline().split())  # símbolos alfanuméricos em conjunto
        states = set(arc.readline().split())  # estados em conjunto
        final_state = set(arc.readline().split())  # estado final

        for linha in arc:
            totens = linha.split()  # quebra a linha
            original_state, symbol, destiny_state = totens[0], totens[2], totens[1]
            if original_state not in transitions:
                transitions[original_state] = {}  # dicionário para as transições do estado original
            if totens[2] == '&' or '&&' or '&&&' or '&&&&':
                totens[2] = 'a'
            transitions[original_state][symbol] = destiny_state  # Define a transição entre o estado original e o estado destino

    return initial_state, alphabet, states, final_state, transitions


def is_accepted(automaton, word):
    current_states = {automaton[0]}  # estado inicial é o primeiro a ser verificado
    next_states = set()
    for symbol in word:
        if symbol not in automaton[1]:  # Se o símbolo não estiver no alfabeto, a palavra é rejeitada
            return False
        for state in current_states:
            if state in automaton[4] and symbol in automaton[4][state]:
                next_states.add(automaton[4][state][symbol])  # Adiciona os próximos estados possíveis
        current_states, next_states = next_states, set()  # Atualiza os estados
    # Verifica se algum estado atual é um estado final
    return any(state in automaton[3] for state in current_states)

def main():
    automaton = load_automaton("exemplo.txt")

    word = input("Digite uma palavra: ")
    if is_accepted(automaton, word): 
        print("OK!")
    else:
        print("Not OK!")

if __name__ == "__main__":
    main()
