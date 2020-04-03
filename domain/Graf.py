class Graf(object):

    def __init__(self):
        self.__length = 0
        self.__matrice = []

    def add_line(self, line):
        self.__matrice.append(line)

    def get_matrice(self):
        return self.__matrice

    def set_matrice(self, graf):
        self.__matrice = graf

    def set_length(self, value):
        self.__length = value

    def get_length(self):
        return self.__length

    def get_cost(self, i, j):
        return self.__matrice[i][j]