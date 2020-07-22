class Stack:
    s=[]
    def init(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def push(self, item):
        self.s.append(item)

    def sizeOfStack(self):
        return len(self.s)

    def peak(self):
        return self.s[len(self.s) - 1]

    def printStack(self):
        for i in range(len(self.s)):
            print(self.s[i])


def foo(string):
    global index, inpIndex, inp, s, flage

    print(string)

    if string[0] == 'r':  # do reducing
        temp = RulesTable[int(string[1:])]
        temp = temp.split("->")
        g = temp[1].split(" ")
        for i in range(len(g) * 2):
            label = s.pop()
        num = s.peak()

        s.push(temp[0])

        s.push(int(LR1Table[num][goto[temp[0]]]))
        index = (int(LR1Table[num][goto[temp[0]]]))



    else:  # do shifting
        s.push(inp[inpIndex])
        s.push(int(string[1:]))
        inpIndex += 1
        index = s.peak()


index = 0
inpIndex = 0  # input pointer
nodeNum = 0  # number of node for graphviz
flage = 1

s = Stack()

terminals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
nonterminals = ['S/', 'S', 'A', 'B', 'C', 'D', 'E', 'I', 'J', 'F', 'K', 'G', 'L', 'H']

action = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
          'm': 12, 'n': 13, 'o': 14, 'p': 15, '$': 16}
goto = {'S/': 17, 'S': 18, 'A': 19, 'B': 20, 'C': 21, 'D': 22, 'E': 23, 'I': 24, 'J': 25, 'F': 26, 'K': 27, 'G': 28,
        'L': 29, 'H': 30}
RulesTable = []
RulesTable.append("S/->S")
RulesTable.append("S->a A")
RulesTable.append("A->B b c C d c")
RulesTable.append("B->e f g c")
RulesTable.append("C->D C")
RulesTable.append("C->D")
RulesTable.append("D->E h c")
RulesTable.append("D->F h c")
RulesTable.append("D->G")
RulesTable.append("D->H h c")
RulesTable.append("E->a I")
RulesTable.append("I->J")
RulesTable.append("I->J j I")
RulesTable.append("J->j")
RulesTable.append("J->j k l")
RulesTable.append("F->j k K")
RulesTable.append("F->j k K m K")
RulesTable.append("K->j")
RulesTable.append("K->l")
RulesTable.append("G->n f j o K g L")
RulesTable.append("L->c b c C d n c")
RulesTable.append("H->p K")
print(RulesTable)
# rl(1) table
LR1Table = []

f = open("C:/Users/HP/Desktop/Input.csv") 

state = []
i = 0
for line in f:

    state = line.split(',')
    l5 = []

    for i in state:
        if i != '\n':
            l5.append(i)

    LR1Table.append(l5)
print(LR1Table)
# rules table

inp = input(" Enter string ")
inp += " $"
inp = inp.split(' ')

s.push(0)

temp = LR1Table[index][action[inp[inpIndex]]]

while (temp != "acc"):
    if temp == '':
        print("error")
        break
    print(temp)
    foo(temp)



    temp = LR1Table[index][action[inp[inpIndex]]]
if(temp == "acc"):
    print("STRING ACCEPTED")