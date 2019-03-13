def recSearchStates(start_state, mat, closure, states_NFA, inputs_NFA):
    start = findState(states_NFA, start_state)
    closure.append(start_state)
    if mat[start][len(inputs_NFA) - 1] != ['.']:
        for i in range(len(mat[start][len(inputs_NFA) - 1])):
            recSearchStates(mat[start][len(inputs_NFA) - 1][i], mat, closure, states_NFA, inputs_NFA)

    return


def findState(states_NFA, element):
    for i in range(len(states_NFA)):
        if element == states_NFA[i]:
            return i


def insertClosures(mat, closure, states_NFA, inputs_NFA, s):
    recSearchStates(states_NFA[s], mat, closure, states_NFA, inputs_NFA)

    return 0


def make_NFA_Closures(mat, states_NFA, inputs_NFA):
    closures = []
    for i in range(len(states_NFA)):
        closures.append([])
        insertClosures(mat, closures[i], states_NFA, inputs_NFA, i)

    return closures


def formatPackge(pacakge):
    newPackge = []
    minAux = pacakge[0]

    while pacakge.size:
        for i in range(len(pacakge)):
            if pacakge[i] <= minAux:
                minAux = pacakge[i]

        newPackge.append(minAux)
        pacakge.remove(minAux)
        minAux = pacakge[0]

    return newPackge


def transferClosures(closure, mat, input_NFA):
    newPackge = []

    for i in range(len(closure)):
        if mat[i][len(input_NFA) - 1] != '.':
            for j in range(len(mat[closure[i]][input_NFA])):
                newPackge.append(mat[closure[i]][input_NFA][j])

    return formatPackge(newPackge)


def confirmPackge(packges, packge):
    for i in range(len(packges)):
        if comparePackge(packges[i], packge):
            return True

    return False


def findPackges(closures, inputs_NFA, mat):
    packges = []
    packges.append(closures[0])
    numPac = 0

    while 1:
        for i in range(len(inputs_NFA)):
            auxPac = transferClosures(closures[numPac], mat, inputs_NFA[i])
            if confirmPackge(packges, auxPac):
                continue
            else:
                packges.append(auxPac)

        numPac += 1
        if (numPac - 1) == len(packges):
            break

    return packges


def makeResultset(packges, inputs_NFA, mat):
    result_set = []
    result_set.append([])

    for i in range(len(packges)):
        for j in range(len(inputs_NFA) - 2):
            result_set[i][j] = transferClosures(packges[i], mat, inputs_NFA[j])

    return result_set


def comparePackge(packge1, packge2):
    if len(packge1) != len(packge2):
        return False
    else:
        for i in range(len(packge1)):
            if packge1[i] == packge2[i]:
                continue
            else:
                return False

        return True


def locatePackge(packges, packge):
    for i in range(len(packges)):
        if comparePackge(packges[i], packge):
            return i


def makeMatrix(packges, result_set):
    global num_inputs
    automaton = []
    automaton.append([])
    for i in range(len(automaton)):
        for j in range(len(automaton[0])):
            if result_set[i][j]:
                automaton[i][j] = locatePackge(packges, result_set[i][j])
            else:
                automaton[i][j] = '.'

    return automaton


def transferDFA(m, inputs_NFA, states_NFA):
    closures = make_NFA_Closures(m, states_NFA, inputs_NFA)
    packges = findPackges(closures, inputs_NFA, m)
    result_set = makeResultset(packges, inputs_NFA, m)
    final = makeMatrix(packges, result_set)

    return final
