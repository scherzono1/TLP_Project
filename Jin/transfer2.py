def transferDFA(m, inputs_NFA, states_NFA, initial_NFA):
    closures = makeClosure(m, inputs_NFA, states_NFA, initial_NFA)
    result = tranferToDFA(closures, m, inputs_NFA)

    return result


def copy(list1):
    new = []
    for i in range(len(list1)):
        new.append(list1[i])

    return new


def confirmClosure(closures, closure):
    if len(closures) != closure:
        return False
    else:

        aux0 = copy(closure)
        aux1 = copy(closures)
        for i in range(len(aux0)):
            k = aux0[0]
            for j in range(len(aux1)):
                if aux1[j] == k:
                    aux1.remove(k)
                    break
            aux0.remove(k)

        if (len(aux0) == 0) and (len(aux1) == 0):
            return True
        else:
            return False


def confirmPackge(closures, closure):
    for i in range(len(closures)):
        for j in range(len(closures[i])):
            if confirmClosure(closures[i][j], closure):
                return True
            else:
                continue

    return False


def makeClosure(m, inputs, states, initial):
    closures = []
    closures.append([initial])
    for i in range(len(states)):
        closures.append([])
        for j in range(len(inputs)):
            if m[i][j] != '.':
                aux = []
                for k in range(len(m[i][j])):
                    if len(m[i][j][k]):
                        aux.append(m[i][j][k])
                if confirmPackge(closures, aux):
                    closures[i].append(aux)

    return closures


def transferClosure(closure, m, input, inputs):
    result = []
    numinput = 0

    for i in range(len(inputs)):
        if inputs[i] == input:
            numinput = i
            break

    for i in range(len(closure)):
        if m[i][numinput] != '.':
            for j in range(len(m[i][numinput])):
                result.append(m[i][numinput][j])

    return result


def checkPosition(closures, closure):
    for i in range(len(closure)):
        if confirmClosure(closures[i], closure):
            return i


def tranferToDFA(closures, m, inputs):
    DFA = []

    for i in range(len(closures)):
        for j in range(len(closures[i])):
            aux = []
            for k in range(len(closures[i][j])):
                for l in range(len(inputs)):
                    if len(transferClosure(closures[i][j][k], m, inputs[l], inputs)) > 0:
                        aux.append(transferClosure(closures[i][j][k], m, inputs[l], inputs))
                    else:
                        aux.append(['.'])
            DFA.append(aux)

    return DFA
