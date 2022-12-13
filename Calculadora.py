class Calculadora():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getsoma(self):
        return self.n1 + self.n2

    def getsub(self):
        return self.n1 - self.n2

    def getmult(self):
        return self.n1 * self.n2

    def getdiv(self):
        return self.n1 / self.n2
