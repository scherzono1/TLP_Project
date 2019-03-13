from Automata import *

a = readAutomata()
print('## original automata ##')
printAutomata(a)
m = mirrorAutomata(a)
print('## mirror automata (maybe not DFA) ##')
printAutomata(m)
d = NFAtoDFA(m)
print('## DFA of mirror automata ##')
printAutomata(d)
#test(a)
