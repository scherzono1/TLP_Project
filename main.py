import numpy as np
def readAutomata(f):
    global states,inputs
    #deletes comments in file
    forg = open("automata.mat","r")
    for s in forg:
        if(s[0]!='#'): 
            f.write(s)
    f.close()
    f = open(".automata.mat","r")
  
    number_inputs = int (f.readline())
    number_states = int (f.readline())
    
    #reads possible inputs of automata  
    inputs_line = f.readline()
    for i in range ( number_inputs ):
        inputs.append( inputs_line[i] )
    
    #reads possible states of automata
    states_line = f.readline()
    for i in range ( number_states ):
        states.append( states_line[i] )

    #fills automata_matrix
    mat = np.chararray((number_states,number_inputs), unicode = True)
    for i in range (number_states):
        s = f.readline()
        for j in range ( number_inputs ):
                mat[i][j] = s[j]
    return mat
    
#main
states = []
inputs = []
f = open(".automata.mat","w")
automata = readAutomata(f)
print(automata)
