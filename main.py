from Automata import *

# main
f = open(".automata.mat", "w")
a = readAutomata(f)
printAutomata(a)
m = mirrorAutomata(a)
printAutomata(m)
#print('Write down a word to test the automata:')
#input_string = str(input())
#while input_string != 'end':
#    if (testAutomata(automata, states, inputs, final_states,input_string) == True):
#        print('correct word!')
#    else:
#        print('wrong')
#    print('Write down another word to test the automata:')
#    input_string = str(input())
