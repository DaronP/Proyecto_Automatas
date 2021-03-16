EPSILON = 'ε'

def lastpos(exp, item, alfa):
    last_p = []
    if item == EPSILON:
        last_p = 0

    if item == '*':
        kleene = []
        for k in range(exp.index(item)):
            lp_fp = firstpos(exp, exp[k], alfa)
            kleene.append(lp_fp)
        last_p = kleene[-1]
    
    if item == '|':
        lp_fp = firstpos(exp, exp[exp.index(item) - 1], alfa)
        lp_fp2 = firstpos(exp, exp[exp.index(item) - 2], alfa)
        last_p = lp_fp.union(lp_fp2)
        
    if item == '_':
        concat = []
        
        for item2 in range(exp.index(item)):
            if exp[item2] == '|':
                fp_concat = firstpos(exp, exp[item2 - 2], alfa)
                concat.append(fp_concat)
            else:
                fp_concat = firstpos(exp, exp[item2], alfa)
                concat.append(fp_concat)

        null_item = nullable(exp, exp[exp.index(item) - 1])
        if null_item:
            last_p = concat[-1].union(concat(-2))
        else:
            last_p = concat[-1]
    else:
        last_p = {exp.index(item)}

    return last_p


def firstpos(exp, item, alfa):
    first_p = []
    if item == EPSILON:
        first_p = 0

    if item == '*':
        kleene = []
        for k in range(exp.index(item)):
            lp_fp = firstpos(exp, exp[k], alfa)
            kleene.append(lp_fp)
        first_p = kleene[-1]
    
    if item == '|':
        lp_fp = firstpos(exp, exp[exp.index(item) - 1], alfa)
        lp_fp2 = firstpos(exp, exp[exp.index(item) - 2], alfa)
        first_p = lp_fp.union(lp_fp2)
        
    if item == '_':
        concat = []
        
        for item2 in range(exp.index(item)):
            if exp[item2] == '|':
                fp_concat = firstpos(exp, exp[item2 - 2], alfa)
                concat.append(fp_concat)
            else:
                fp_concat = firstpos(exp, exp[item2], alfa)
                concat.append(fp_concat)

        null_item = nullable(exp, exp[exp.index(item) - 2])
        if null_item:
            first_p = concat[-1].union(concat(-2))
        else:
            first_p = concat[-2]
    else:
        first_p = {exp.index(item)}

    return first_p

def nullable(exp, item):
    nullab = []
    if item == EPSILON:
        nullab = True

    if item == '*':
        nullab = True
    
    if item == '|':
        null_or1 = nullable(exp, exp[exp.index(item) - 1])
        null_or2 = nullable(exp, exp[exp.index(item) - 2])
        nullab = null_or1 or null_or2
        
    if item == '_':
        concat = []
        
        for item2 in range(exp.index(item)):
            if exp[item2] == '|':
                null_concat = nullable(exp, exp[item2 - 2])
                concat.append(null_concat)
            else:
                null_concat = nullable(exp, exp[item2])
                concat.append(null_concat)

        nullab = concat[-1] and concat[-2]
    else:
        nullab = False

    return nullab

def directo(expr, alfa):
    exp.append('#')
    exp.append('_')
    follow_pos = []
    nodos = {}

    #calculando el follow pos de cada elemento de la expresion
    #mega for
    for item in exp:
        if item in alfa or item == '#':
            nodos[exp.idex(item)]: item
        if item == '*':
            lista = []
            last_pos = lastpos(exp, item, alfa)

            for i in last_pos:
                fp = firstpos(exp, item, alfa)
                lista.append(fp)
            
            if len(last_pos) > 1:
                last_last_pos = []
                for i2 in last_pos:
                    last_last_pos.append(set().union(*lista))
                follow_pos.append(last_last_pos)
            else:
                fp = firstpos(exp, i, alfa)
                follow_pos.append(fp)
            

        if item == '_':
            l_pos = lastpos(exp, exp[exp.index(item) - 1], alfa)
            for pos in l_pos:
                if not follow_pos:
                    fpos_list = []

                    for item2 in range(exp.index(item)):
                        if exp[item2] in alfa:
                            fpos_list.append(firstpos(exp, exp[item2]))

                    fpos_list2 = []
                    for j in fpos_list:
                        fpos_list2.append(set().union(*fpos_list))

                    follow_pos.append(fpos_list2)

                    if type(follow_pos[-1]) is list:
                        lista = []

                        for k in range(len(follow_pos[-1])):
                            lista.append(follow_pos[-1][k].union(set().union(firstpos(exp, exp[exp.index(item) - 1], alfa)))
                        follow_pos.pop()
                        follow_pos.append(lista)

                else:
                    if type(follow_pos[-1]) is list:
                        lista2 = []

                        for k in range(len(follow_pos[-1])):
                            lista.append(follow_pos[-1][k].union(set().union(firstpos(exp, exp[exp.index(item) - 1], alfa)))
                        follow_pos.pop()
                        follow_pos.append(lista[0])
                        follow_pos.append(lista[1])

    direct_nodos = []
    if type(follow_pos[0]) is list:
        for i in range(len(follow_pos[0])):
            direct_nodos.insert(0, follow_pos[0][i])
        follow_pos.pop(1)

    for elem in follow_pos:
        if type(elem) is not list:
            direct_nodos.append(elem)

    
