import sys
import re 
from cola import Cola 
import random
class proceso:
    def __init__(self,archivo,info_estado):
        self.id = 0
        self.archivo_path=archivo
        self.estado = False # ejecutando - bloqueado 
        self.contador= 1
        self.info_estado1 = False # 0 inicio -  1 completo - 2 falta      
    


class despacher(proceso):
    def __init__(self,proceso):
        self.proceso=proceso
        self.bcp = [0]
        self.info_estado= True
        self.memoria= 0
        self.bloqueado= True


    def print(self):
        with open(self.proceso,'r') as file:
            print("archivo ->",self.proceso,"\n",file.read())
            print("BCP = ",self.bcp)
            print("estado_info=", self.info_estado)

    def cambiar_estados(self):
        if(self.info_estado == True):
            self.info_estado = False
        else:
            self.info_estado = True  

    def proceso2(self,n,contador_intrucciones,salida,objeto,cola2):
        Memoria = (random.randrange(6000,9999))
        with open(self.proceso,"r") as file :
            lineas = [linea.split() for linea in file]  
        i = 0
        Memoria = self.memoria
        for linea in lineas:
            while (n >= i):
                if (len(lineas[i])==2): #para el caso de Intruccion normal
                    i = i+1 
                    contador_intrucciones = contador_intrucciones+1
                    salida.write ("\n" + str(contador_intrucciones) + "   I    "+ str(self.proceso) + "  "+str(Memoria))
                    Memoria = Memoria +1
                else:
                    i=i +1 
                    #finalizar proceso
        if (self.info_estado == True):
                contador_intrucciones = contador_intrucciones+1
                salida.write("\n" +str(contador_intrucciones) +"  PUSH_Listo " + "   "+str(self.proceso) + "  Dispatcher  101")
        else:
            i = i + 1
        return (contador_intrucciones)

    def exec(self,n,contador_intrucciones,salida,objeto,cola2): #debe ingresar el proceso y el limite de intrucciones , y el numero de intruccion en el cual va 
        Memoria = (random.randrange(6000,9999))
        with open(self.proceso,"r") as file :
            lineas = [linea.split() for linea in file]  
        i = 0
        
        for linea in lineas:
            while (n > i):
                try:
                    if (len(lineas[i])==2): #para el caso de Intruccion normal         
                        i = i+1 
                        contador_intrucciones = contador_intrucciones+1
                        salida.write ("\n" + str(contador_intrucciones) + "   I    "+ str(self.proceso) + "  "+str(Memoria))
                        Memoria = Memoria +1
                        
                    elif(len(lineas[i])==3):
                        i = i+1
                        contador_intrucciones = contador_intrucciones+1
                        
                        salida.write("\n" + str(contador_intrucciones) + "  ES 7    " + str(self.proceso) +" "+ str(Memoria))
                        contador_intrucciones = contador_intrucciones+1                        
                        
                        salida.write("\n" +str(contador_intrucciones) +"  ST " + "   "+str(self.proceso) + "  Dispatcher  100")
                        i = n 
                        self.memoria = Memoria 
                        self.info_estado = False
                        self.bloqueado = False
                        cola2.agregar(self)
                        break 
                    else:
                        i = i+1
                        #finalizar proceso
                except ValueError:
                    print("errr")

            if (self.info_estado == True):
                contador_intrucciones = contador_intrucciones+1
                salida.write("\n" +str(contador_intrucciones) +"  PUSH_Listo " + "   "+str(self.proceso) + "  Dispatcher  101")
                break
            else:
                print(" ")
                
        return (contador_intrucciones)


    def crear_proceso(self,cola1): # 
            obj = proceso(self.proceso, True)
            obj.info_estado = 1
            cola1.agregar(obj)    
            return cola1

    def activar(self,proceso1,cola1,cola2):
        new = cola1.desencolar()
        if(self.bcp[0]==0):
            print("BCP vacia")
            self.bcp[0]= proceso1
            print("saque de cola listo a ", proceso1, "ahora meto al !procesador! ")
            print("el bcp[0] = ",self.bcp[0])
        #falta temporizador
        else:
            aux = self.bcp[0]
            self.bcp.remove()
            cola2.agregar(aux)
            self.bcp.append(proceso1)
    
    def activar_bloqueados(self,cola1,cola2,new):
            aux = cola1.desencolar()
            cola2.agregar(aux)            

    def salir(self):
        if(self.proceso.info_estado == 1):
            aux = self.bcp.remove()
            return aux
        else:
            ("el proceso de aun no acaba")        