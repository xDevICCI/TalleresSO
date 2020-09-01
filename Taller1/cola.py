class Cola:
    def __init__(self):
        self.items=[]

    def agregar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            print("cola vacia")
    def is_empty(self):
        return None
    
    def imprimir(self):
        print (self.items)


