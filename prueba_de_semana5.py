def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
      
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                introducir_puntuacion_comentario()
            elif num == 2:
                comprobar_resultado()
            elif num == 3:
                print('Finalizado')
                break  # Sentencia para finalizar el procesamiento
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

    
      
        
def introducir_puntuacion_comentario():
    while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = input()
                
                if point.isdecimal():
                    point = int(point)

                    if point < 1 or point > 5  :  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                        print('NO VALIDO, introduzca un puntuacion entre 1 y 5')
                    else:
                        print("Por favor introduzca un comentario")
                        comment = input()
                        guardar_post(point, comment)
                        break
                else:
                    print("Introduzca una puntuación en numeros")

def guardar_post(point, comment):
    post = (f"punto: {point} comentario: {comment}")
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')


def comprobar_resultado():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r")as read_file:
        print(read_file.read())


if __name__ == "__main__":
    main()