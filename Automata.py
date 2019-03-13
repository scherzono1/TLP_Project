class Automata:
    def __init__(self,matrix,states,inputs,final_states,initial_state):
        self.matrix = matrix
        self.states = states
        self.inputs = inputs
        self.final_states = final_states
        self.initial_state = initial_state
        self.newStates=[]

def readAutomata():
    states = []
    inputs = []
    final_states= []
    initial_state = []
    mat = []
    # deletes comments in file
    f = open(".automata.mat", "w")
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
    
    # reads initial states
    initial_state_line = f.readline()
    for i in range (len(initial_state_line)-1):
        initial_state.append(initial_state_line[i])
    
    # reads final states
    final_states_line = f.readline()
    for i in range (len(final_states_line)-1):
        final_states.append(final_states_line[i])

    # fills automata_matrix
    for i in range(number_states):
        mat.append([])
        s = f.readline()
        for j in range(number_inputs):
            mat[i].append([])
            mat[i][j].append(s[j])
    
    return Automata(mat,states,inputs,final_states,initial_state)

def testAutomata(automata, states, inputs, final_states,input_string):
    accepted = True 
    for i in input_string:
        if (belongs_to_list(i, inputs) == False):
            return False
    ans = search_automata(automata, states, input_string, 0, 0, len(input_string) - 1, final_states)
    return ans


def search_automata(automata, states, inputs, s, i, max_i, final_states):
    cur_input = inputs[i]
    if i + 1 > max_i:
        if (belongs_to_list(automata[s][cur_input]), final_states) == True:
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


def mirrorAutomata(a):
    print('Making mirror...')
    m = []
    #copies the dimensions of original automata matrix
    for i in range (len(a.matrix)):
        m.append([])
        for j in range (len(a.matrix[i])):
            m[i].append([])
    
    #find the mirrored indexes with its corresponding location
    #in the original automata and adds theem to a list
    indexes = []
    for i in range (len(a.matrix)): 
        indexes.append ( search_mirror(a.states[i],a) )
    

    #shows all the found indexes to be copied to mirror
    print('FOUND INDEXES FOR MIRROR:')
    printMatrix(indexes) 
    
    #puts the found indexes along with the appropiate state
    #in the mirror matrix
    for i in range( len(indexes) ):
        for j in range (len(indexes[i])):
            m[i][indexes[i][j][1]].append(indexes[i][j][0])
    #puts the corresponding '.' char in the empty lists
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (len(m[i][j]) == 0):
                m[i][j].append('.')
    return Automata(m,a.states,a.inputs,a.initial_state,a.final_states)

def search_mirror(target,a):
    res = []
    for i in range (len(a.matrix)):
        for j in range(len(a.matrix[i])):
            if a.matrix[i][j] == [ target ]:
                res.append([a.states[i],j])
    return res

def printAutomata(a):
    print('STATES:')
    print (a.states)
    print('INPUTS:')
    print (a.inputs)
    print('FINAL STATES:')
    print (a.final_states)
    print('INITIAL STATE:')
    print (a.initial_state)
    print('MATRIX:')
    printMatrix(a.matrix)

def printMatrix(m):
    mat = ''
    for i in range (len(m)):
        for j in range (len(m[i])):
            mat += str ( m[i][j] )
        mat += '\n'
    print (mat)

def test(a):
    print('Write down a word to test the automata:')
    input_string = str(input())
    while input_string != 'end':
        if (testAutomata(a.matrix, a.states, a.inputs, a.final_states,input_string) == True):
            print('correct word!')
        else:
            print('wrong')
        print('Write down another word to test the automata:')
        input_string = str(input())
def NFAtoDFA(a):
    while True:
        new = []
        newmatrix = []
        for i in range ( len(a.matrix) ):
            for j in range ( len(a.matrix[i]) ):
                if len(a.matrix[i][j]) > 1:
                    new.append(a.matrix[i][j])
        if(len(new) == 0):
            break
        print('found:')
        print(new)
        newstates=[]
        print('new states are: ')
        for i in range(len(new)):
            newstates.append(concat(new[i]))
        print(newstates)
        for i in range (len(new)):
            newmatrix.append([])
            for j in range(len(a.matrix[0])):
                newmatrix[i].append([])
        print('concatenated new states...')
        for i in range (len (new)):
            for c in new[i]:
                for k in ( a.matrix[a.states.index(c)] ):
                    if k != ['.']:
                        newmatrix[i][a.matrix[a.states.index(c)].index(k)] = k
        for i in range (len (newmatrix)):
            for j in range(len(newmatrix[i])):
                if len(newmatrix[i][j]) == 0:
                    newmatrix[i][j] = ['.']
        for i in range (len(new)):
            a.matrix.append(newmatrix[i])
        for i in range (len(a.matrix)):
            for j in range(len(a.matrix[i])):
                if len(a.matrix[i][j])>1:
                    a.matrix[i][j]=concat(a.matrix[i][j])
        a.newstates = new
        printMatrix(a.matrix)

def concat(l):
    new = []
    string = ''
    for c in l:
        string+=c
    new.append(string)
    return new
