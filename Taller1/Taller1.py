import sys
import re 
from p import despacher 
from cola import Cola

n = int(sys.argv[1])
probabilidad = int(sys.argv[2])
entrada = sys.argv[3]
salida = sys.argv[4]
cola1 = Cola()
cola2 = Cola()
contador_intrucciones= 1
end = 'a'
aux1 = 1

with open(entrada,'r') as f:
    texto = f.read()
    f.seek(0)
matches = re.findall(r'proceso[0-9]*', texto)
#
print (matches)
proceso = 103
while ( end != 's'):
    for match_num in matches:
        with open(salida,"r+") as f1:
            new = match_num + '.txt' # 
            desp = despacher(new) # se carga proceso a despacher
            desp.crear_proceso(cola1) # se agrega proceso a la cola 
            contenido = f1.read()
            f1.write("\n" +str(contador_intrucciones) + "  PULL    " + "Dispatcher     102 " )
            contador_intrucciones= contador_intrucciones+1
            f1.write("\n" +str(contador_intrucciones) + "  LOAD    " + str(new) + " Dispatcher 103")
            contador_intrucciones= contador_intrucciones+1 
            f1.write("\n" +str(contador_intrucciones) + "  EXEC    " +str(new)+ " Dispatcher 104")
            contador_intrucciones=desp.exec(n,contador_intrucciones,f1,new,cola2)
            if ( cola2.is_empty == None):
                print(" ")
            else:
                if ( aux1 > 1):  
                    aux = cola2.desencolar()
                    if (aux != None):

                        contador_intrucciones = contador_intrucciones+1
                        f1.write("\n" +str(contador_intrucciones) +"  PUSH_Bloqueado " + "   "+aux.proceso + "  Dispatcher  101")
                        contador_intrucciones= contador_intrucciones+1
                        f1.write("\n" +str(contador_intrucciones) + "  PULL    " + "Dispatcher     102 " )
                        contador_intrucciones= contador_intrucciones+1
                        f1.write("\n" +str(contador_intrucciones) + "  LOAD    " + str(aux.proceso) + " Dispatcher 103")
                        contador_intrucciones= contador_intrucciones+1 
                        f1.write("\n" +str(contador_intrucciones) + "  EXEC    " +str(aux.proceso)+ " Dispatcher 104")
                        contador_intrucciones=aux.proceso2(n,contador_intrucciones,f1,aux.proceso,cola2)
                    else:
                        print("procesos no existe en cola ")
                else:
                    aux1 = aux1 + 1
                
            #desp.proceso2(str(new),new)
            
            contador_intrucciones= contador_intrucciones+1 
            aux1=1+1
            end = 's'



            
        
        