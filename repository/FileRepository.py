from domain.Graf import Graf
import math

def euclideanDistance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

class FileRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__graf = Graf()
        self.__loadFromFile()
        #self.__createFromCoordonates()
        self.__outputFile = filename.split(".")[0] + "_solution.out"

    def get_graf(self):
        return self.__graf

    def set_graf(self, value):
        self.__graf = value


    def __loadFromFile(self):
        with open(self.__filename) as f:
            length = int(f.readline())
            print(str(length))
            self.__graf.set_length(length)
            for i in range(0, length):
                stringLine = f.readline()
                cmps = stringLine.split(",")
                line = [int(k.rstrip()) for k in cmps]
                self.__graf.add_line(line)

    def writeToFile(self, drum, cost):
        result = ""
        result += str(len(drum)) + '\n'
        for i in drum:
            result += str(i+1) + ' '
        result += '\n'
        result += str(cost) + '\n'

        g = open(self.__outputFile, "w+")
        g.write(result)
        g.close()

    def __createFromCoordonates(self):
        with open(self.__filename) as f:
            f.readline()
            f.readline()
            f.readline()
            length = int(f.readline().split(' ')[2])
            f.readline()
            f.readline()
            print(str(length))
            self.__graf.set_length(length)
            x = [0 for _ in range(length)]
            y = [0 for _ in range(length)]
            for i in range(0, length):
                stringLine = f.readline()
                cmps = stringLine.split(' ')
                x[int(cmps[0])-1] = float(cmps[1])
                y[int(cmps[0])-1] = float(cmps[2])
            for i in range(0, length):
                line = [0 for _ in range(length)]
                for j in range(0, length):
                    line[j] = euclideanDistance(x[i], y[i], x[j], y[j])
                self.__graf.add_line(line)
