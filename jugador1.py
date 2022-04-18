import computadora
import time
import sys

def jugador1(tablerojugador, tablerocomputadora, tablerovacio1, tablerovacio2):
    while 'O' in tablerojugador and 'O' in tablerocomputadora:
        try:
            while True:
                print('Tablero de acción, guarda el historial de disparos\n', tablerovacio1)
                x = input('Es tu turno! Escoja la coordenada "x": ')
                if x.lower() == 'esc':
                    print('Bandera blanca, nos rendimos!!', '\U0001F3F3')
                    sys.exit('Se ha rendido, ganan las máquinas otra vez..., es un día triste para la humanidad')
                while 1>0:
                    try:
                        x = int(x)
                        break
                    except:
                        print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                        x = input('Introduzca la coordenada "x" para disparar: ')
                if x < 0 or x > 9:
                    print('Coordenada recibida errónea, introduce valores entre 0 y 9')
                    continue
                y = input('Es tu turno! Escoja la coordenada "y": ')
                while 1>0:
                    try:
                        y = int(y)
                        break
                    except:
                        print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                        y = input('Introduzca la coordenada "y" para disparar: ')
                if y < 0 or y > 9:
                    print('Coordenada recibida errónea, introduce valores entre 0 y 9')
                    continue
                
                if tablerojugador[x,y] == 'O':
                    tablerojugador [x,y] = 'X'
                    tablerovacio1[x,y] = 'X'
                    print(f'¡TOCADO en {x},{y}!')
                    print('\U0001F525')
                    print()
                    print('Dispara otra vez!')
                    print(tablerovacio1)
                    time.sleep(5)
                    
                elif tablerojugador[x,y] == ' ':
                    tablerojugador[x,y] = '-'
                    tablerovacio1[x,y] = '-'
                    print(f'¡Fallo en {x},{y}!')
                    print('\U0001F622')
                    print()
                    print(tablerovacio1)
                    time.sleep(5)
                    computadora.computadora(tablerojugador,tablerocomputadora,tablerovacio1,tablerovacio2)
                    break

                else:
                    print('Try again player!')
                    continue
        except:
            print('Error')
            continue