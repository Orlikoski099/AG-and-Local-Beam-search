class cidade:
    def __init__(self, name, custo):
        self.nome = name
        self.custo = custo

    def __str__(self):
        return f"{self.nome},{self.custo}"


class list:
    def __init__(self, vertices=None):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        

    def criaCaminho(self, u, v, custo):
        self.grafo[u - 1].append([v, custo])

    def mostraGrafo(self):
        for i in range(self.vertices):
            print(f"{i+1}", end=" ")
            for j in self.grafo[i]:
                print(f"{j} ->", end=" ")
            print(" ")

    def printFile(self):
        file = open("SI/Teste.txt", "a")
        for i in range(self.vertices):
            for j in self.grafo[i]:
                file.write(str(j), ",")
            file.write("\n")
        file.close

    def readFile(self, name="SI/Teste.txt"):
        v = 0
        file = open(name, "r")
        for i in range(self.vertices):
            str = file.readline()
            for a in str.split(";"):
                v = 0
                for b in a.split(","):
                    if v == 0:
                        c = b
                    elif v == 1:
                        self.criaCaminho(i + 1, int(c), int(b))
                        v = 0
                    v = v + 1


teste = list(5)

teste.readFile()

teste.mostraGrafo()

"""
[2, 50][3, 30][4, 26][5, 37]

[1, 50][3, 32][4, 10][5, 20]

[1, 30][2, 32][4, 15][5, 16]

[1, 26][2, 10][3, 15][5, 40]

[1, 37][2, 20][3, 16][4, 40]
"""
