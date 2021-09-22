#Les comparto el código que realice para el ejercicio que habia propuesto en clase el profesor, cualquier sugerencia
#es recibida o error
#Autor: Miguel Angel Ramirez Echeverry
import threading
from sys import argv
import datetime

class Hilo(threading.Thread):
    def __init__(self, nombreHilo, data):
        threading.Thread.__init__(self, name=nombreHilo, target=Hilo.run)
        self.limiteInicial = data[0]
        self.limiteFinal = data[1]
        self.suma = 0

    @property
    def obtenerSuma(self):
        return self.suma

    def __str__(self) -> str:
        return f"limite Inicial:{self.limiteInicial},  limite final:{self.limiteFinal}, suma:{self.suma}"

    def run(self):
        for i in range(self.limiteInicial, self.limiteFinal+1):
            self.suma += i

def mostrarSuma(lista):
    total = 0
    for el in lista:
        total += el.obtenerSuma
    return total

if __name__ == "__main__":
    #sumar los primeros 100 números con 10 hilos, los datos se pasan desde la terminal y son parametrizables
    cantidadNumeros = int(argv[1]) #100
    cantidadHilos = int(argv[2]) #10

    #lo que voy a incrementar
    contador =  cantidadNumeros // cantidadHilos
    inicial, final = (1, contador)
    hilos  = []

    #para medir la eficiencia
    tiempo_inicial = datetime.datetime.now()

    for i in range(cantidadHilos):
        t = Hilo(f"hilo:{i+1}",(inicial, final))
        t.start()
        inicial  = final + 1
        final += contador
        hilos.append(t)

    for el in hilos:
        el.join()

    tiempo_final = datetime.datetime.now()

    print(f"Tiempo transcurrido:{tiempo_final.second - tiempo_inicial.second}")

    print(f"La suma de todos los hilos es:{mostrarSuma(hilos)}")


    

        
