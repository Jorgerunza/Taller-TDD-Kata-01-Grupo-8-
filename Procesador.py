
class Procesador:
        def contador (self,lista):
            if (lista == ''):
                return [0,0,0,0]
            else:
                numeros = str.split( lista, ',')
                numeros = [int(i) for i in numeros]
                respuesta =[len(numeros), min(numeros), max(numeros), numeros[0]]
                return respuesta
