#Luiz Henrique

import sys

lstvertices = []
lstedges = []
dictionary = {}
filledlist = []
ordlist = []
finallist = []


def menu():
    print("-=" * 30)
    print("select an option")
    print("-=" * 30)
    print('Full list: ',filledlist)

    choice = input(
        """A: Add vertice. \nB: Add edge. \nC: Mathematical representation of the graph. \nD: Graph representation. \nE: Show degree of a vertice. \nF: List vertices adjacent to a given vertice. \nG: Check for the existence of an edge between certain vertices (adjacent). \nH: Using the Kruskall method. \nQ: Quit/Log Out. \nChoose an option: """).upper().strip()
    print()
    if choice == "A":
        addvertices()
    elif choice == "B":
        addedge()
    elif choice == "C":
        showmath()
    elif choice == "D":
        showgraph()
    elif choice == 'E':
        showdegree()
    elif choice == 'F':
        showneighbor()
    elif choice == 'G':
        showconnection()
    elif choice == 'H':
        kruskall()
    elif choice == "Q":
        sys.exit
    else:
        print('Just enter the cited options provided [A/B/C/D/E/F/G/Q]')
        print('try again...')
        menu()


def wannastop():
    op = str(input('do you wish to continue ? [S/N] ').upper().strip())
    if op == 'S':
        menu()
    elif op == 'N':
        sys.exit()
    else:
        print('Type only S or N ...')
        wannastop()


def addvertices():
    vrt = str(input('Type the vertice: ').upper().strip())
    lstvertices.append(vrt)
    print(lstvertices)
    dictionary[vrt] = []
    print(dictionary)
    menu()


def addedge():
    edge_init = str(input('Enter the initial vertice: ').upper().strip())
    edge_final = str(input('Enter the final vertice: ').upper().strip())
    cost = int(input('Enter the cost of this edge: '))
    if edge_init not in lstvertices or edge_final not in lstvertices:
        print('vertex does not exist.')
    else:
        dictionary[edge_init].append(edge_final)
        dictionary[edge_final].append(edge_init)
        filledlist.append(edge_init)
        filledlist.append(edge_final)
        filledlist.append(cost)
    menu()

def showneighbor():
    vrt1 = str(input('Type the vertice: ').upper().strip())
    print('The adjacent vertices of ',vrt1,'are:')
    for e in dictionary[vrt1]:
        print(e)
    wannastop()

def showconnection():
    vrt1 = str(input('Type the vertice: ').upper().strip())
    vrt2 = str(input('Type the other vertice: ').upper().strip())
    if vrt2 in dictionary[vrt1]:
        print(vrt1,' e ',vrt2,' are adjacent')
    else:
        print(vrt1,' e ',vrt2,'are not adjacent')
    wannastop()

def showmath():
    newlist = []
    for i in dictionary.keys():
        newlist.append(i)
    print(f'follow the vertices -> {newlist}')
    print(f'follow the edges -> {dictionary}')
    wannastop()


def showdegree():
    degree = 0
    vertices = str(input('Enter the name of the vertice you want: ').strip().upper())
    newlist3 = dictionary.copy()
    print(vertices)
    print(newlist3)
    if vertices in newlist3:
        for e in newlist3:
            for n in newlist3[e]:
                if vertices == n:
                    degree += 1
        print(f'the vertice {vertices} has degree {degree}.')
    else:
        print('vertice does not exist.')
    wannastop()


def showgraph():
    newlist2 = [dictionary.copy()]
    for d in newlist2:
        for k, v in d.items():
            print(f'Vertice {k} -> {v}')
    wannastop()

def kruskall():
    global cont, cont1
    n = len(filledlist)
    menor = []
    lstcmp = []
    for i in range(2,n,3):
        menor.append(filledlist[i])
    menor.sort()
    j = 2
    while j < n:
        if menor[0] == filledlist[j]:
            ordlist.append(filledlist[j-2])
            ordlist.append(filledlist[j-1])
            ordlist.append(filledlist[j])
            menor.pop(0)
            filledlist.pop(j-2)
            filledlist.pop(j-2)
            filledlist.pop(j-2)
            j=2
        else:
            j+=3
        if len(menor) == 0 or len(filledlist) == 0:
            break
    n1 = len(ordlist)
    k=0
    print('construction of the final graph: ')
    while k <= n1:
        n2 = len(finallist)
        print('final graph -> ', finallist)
        if n2 == 0:
            finallist.append(ordlist[k])
            lstcmp.append(ordlist[k])
            finallist.append(ordlist[k+1])
            lstcmp.append(ordlist[k+1])
            finallist.append(ordlist[k+2])
            k=3
        elif sorted(lstvertices) != sorted(lstcmp):
            for h in finallist:
                cont = 0
                if ordlist[k] == h:
                    cont+=1
                cont1 = 0
                if ordlist[k+1] == h:
                    cont1+=1
            flag=0
            if cont<3:
                finallist.append(ordlist[k])
                flag=1
            flag1=0
            if cont1<3:
                finallist.append(ordlist[k+1])
                flag1=1
            if flag == 1 and flag1 == 1:
                finallist.append(ordlist[k+2])
            aux = ordlist[k]
            aux1 = ordlist[k+1]
            if aux not in lstcmp:
                lstcmp.append(aux)
            if aux1 not in lstcmp:
                lstcmp.append(aux1)
            k += 3
        else:
            break
    print('--------------Kruskal--------------')
    print('formatted as follows: [ inicial vertice, final vertice, path cost... ]')
    print(finallist)
    print('-----------------------------------')
    wannastop()


if __name__ == '__main__':
    menu()
