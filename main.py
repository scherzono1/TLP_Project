import numpy as np


def readAutomata(f):
    global states, inputs, final_states
    # deletes comments in file
    forg = open("automata.mat", "r")
    for s in forg:
        if (s[0] != '#'):
            f.write(s)
    f.close()
    f = open(".automata.mat", "r")

    number_inputs = int(f.readline())
    number_states = int(f.readline())

    # reads possible inputs of automaton
    inputs_line = f.readline()
    for i in range(number_inputs):
        inputs.append(inputs_line[i])

    # reads possible states of automaton
    states_line = f.readline()
    for i in range(number_states):
        states.append(states_line[i])
    # reads final states
    final_states_line = f.readline()
    for c in final_states_line:
        final_states.append(c)

    # fills automata_matrix
    mat = np.chararray((number_states, number_inputs), unicode=True)
    for i in range(number_states):
        s = f.readline()
        for j in range(number_inputs):
            mat[i][j] = s[j]
    return mat


def drawAutomata(states, inputs, automata):
    # function to draw an automaton. to me able to vizualize it
    return 0


def testAutomata(automata, states, inputs, final_states):
    accepted = True
    input_string = str(input())
    for i in input_string:
        if (belongs_to_list(i, inputs) == False):
            return False
    ans = search_automata(automata, states, input_string, 0, 0, len(input_string) - 1, final_states)
    return ans


def search_automata(automata, states, inputs, s, i, max_i, final_states):
    cur_input = int(inputs[i])
    if i + 1 > max_i:
        if belongs_to_list(str(automata[s][cur_input]), final_states) == True:
            return True
        else:
            return False
    if automata[s][cur_input] == '.': return False
    s = states.index(automata[s][cur_input])
    return search_automata(automata, states, inputs, s, i + 1, max_i, final_states)


def belongs_to_list(char, test):
    belongs = False
    for c in test:
        if (c == char):
            belongs = True
    return belongs


# main
states = []
inputs = []
final_states = []
f = open(".automata.mat", "w")
automata = readAutomata(f)
print('inputs:')
print(inputs)
print('states:')
print(states)
print('automata:')
print(automata)
print('Write down a word to test the automata:')
if (testAutomata(automata, states, inputs, final_states) == True):
    print('correct word!')
else:
    print('wrong')
