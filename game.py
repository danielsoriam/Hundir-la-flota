import numpy as np
import random
import welcome
import tablerosIniciales
import endofgame
import jugador1
import computadora
import tablerosingame
import time
print("******************************S#&@$%***!!!***%$@&#S*****************************")
print("**************************S&$*!!::::::::::::::::::!*$&S*************************")
print("***********************#$*!::::::::!!*******!!::::::::!*$#**********************")
print("********************S@*::::::!*%$@@@@@$$@#$@@@@@$%*!::::::*@S*******************")
print("******************#%!:::::*$@@@$*!!:::::*@::::!!*%$@@$*:::::!%#*****************")
print("****************S%:::::!$&@$*:::::::$&!:%@::::::::::!%@@%!:::::%S***************")
print("***************@!::::*@&$*:::::::::!$&*:%@:::::::::::::!$&$!::::!@**************")
print("*************S%::::!$&$!::::::::!*%$$$$%$&::::::::::::::::%&$!::::%S************")
print("************#!::::%&@!:::::::::!$$$$$$$$@#*:::::::::::::::::$&%::::!#***********")
print("***********#!::::$#*::::::::::::****$@%!$&!::::::::::::::::::*&$::::!&**********")
print("**********#!:::!@&!:::::::::::::%%%%$@%%@&!:::::::::::::::::::!@@::::!#*********")
print("*********S*::::@&!::::::!$*:::::::::$&*:%&::::::::::::::::::::::@@::::*S********")
print("*********$::::$#!::::::%&&&&%*%%%***@&*:%@:::::::::::::::::::::::&%::::$********")
print("********S!:::*#%::::::::!$@$$@###@$$&&*:%@:::::::::::::::!:::::::*&!:::!#*******")
print("********$::::@&::::::::::*$$$$$$$$$$&&*:%@::::::::::::!*$&@%::::::@$::::$*******")
print("*********:::!#%:::!*$*!::*%%%$$$$$$$&@$%@&%%%%%%%%%**@&&&&@%::::::*&!:::********")
print("*******S!:::*#!:::$&&&&%%%%%%$$$$@@@&@$$$@$$$$&###&$$@&$*!:::::::::&*:::!#******")
print("*******#!:::%#:::::!$@$$$$$$$$$$$@@@&@$$$$$$$$@&&&@$$$$!:::::::::::@%::::&******")
print("*******#!:::%#$$$$$$@&&&&&&&&&&&&&#&&@$$$$$$@&&&&&&&&&&&@$$$$$$$$$$&%::::&******")
print("*******#!:::%#!::::*$@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@$******!:::&*:::!#******")
print("*******S!:::!#*::::!$&&&####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@*:::!&!:::!S******")
print("********%::::@$::::::*@#####&&&&&&&&&&&&##&&&&&&&&&&&&&&&&&&$:::::%@::::%*******")
print("********&::::*#!!!::::!@&&&&&&&&&&&&&&&&##&&&&&&&&&&&&&&&&&$::::::&*::::@*******")
print("**********::::@&**!:::!%&##&$@###@$&##&$&S##$$&##&$&###$$&#!:!!::$$::::*S*******")
print("*********&!:::!&$**********************!$&**********************$@!::::&********")
print("**********$::::!&$**********************$&*********************$@!::::%*********")
print("***********$::::!&@%*%%$%**%$%%*%$$%**%$@&*%$$%**%$%%*%$$%*%%$@@!::::*S*********")
print("************$::::!$&@$$$@$$@@@$$@@$@$$@$&#$@@@@$$@@@$$@@@@$$@&$!::::*S**********")
print("*************@:::::*&&@$$$$$$$$$$$$$$$$$&#$$$$$$$$$$$$$$$$@&@*:::::*S***********")
print("**************&*:::::%&&@$$$$$$$$$$$$$$$&#$$$$$$$$$$$$$$@&@%::::::%S************")
print("***************S$!:::::%@&@@$$$$$$$$$$$$&#$$$$$$$$$$$@@&@*:::::::$**************")
print("*****************#$!:::::!%@&&@@@$$$$$$$@#$$$$$$@@@@@@%!:::::::!&***************")
print("*******************#$!::::::!*%$@@@@@@@@&#@@@@@@@$%*!:::::::::$S****************")
print("*********************S&%!::::::::!!**%%%%%%%**!!::::::::::::*&******************")
print("************************S&$*!:::::::::::::::::::::::::::::*&********************")
print("****************************S&$*::::::::::::::::::::::::!@**********************")
print("********************************&!::::::::::::::::::::*@S***********************")
print("*********************************&!:::::::::::::::::*&**************************")
print("***********************************::::::::::::::!$#****************************")
print("***********************************:::::::::::!*@S******************************")
print("***********************************:::::::::*@#*********************************")
print("***********************************::::::*@#************************************")
print("***********************************::!%@S***************************************")
print("**********************************%%&S******************************************)")
print('Bienvenidos jugadores!\n'
          'Has entrado en Hundir la Flota.\n'
          'El juego consiste en hundir los barcos del oponente antes que el oponente destruye los tuyos introduciendo coordenadas.')
print('\U0001F600', '\U0001F9E0','\U0001F6F8')
jugador = input('¡Por favor introduzca su nombre y prepárese para la batalla espacial! : ')

# Crea un tablero 10x10 vacío Para la computadora
tablero = tablerosIniciales.tablero

tablerosIniciales.crea_crucero(tablero)

tablerosIniciales.num_naves(2, tablerosIniciales.crea_lanzadera, tablero)

tablerosIniciales.num_naves(3, tablerosIniciales.crea_bombardero, tablero)

tablerosIniciales.num_naves(4, tablerosIniciales.crea_caza, tablero)

tablero_computadora = tablero.copy()

tableroVacio_computadora = np.full((10, 10), (' '))

time.sleep(3)
print(f'{jugador}, prepárese, le toca distribuir su flota sobre el tablero')
time.sleep(2)
print('3...')
time.sleep(2)
print('2...')
time.sleep(2)
print('1...')
time.sleep(2)
print('--------------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------------')
print('LISTOS!!', '\U0001F3C1')


# Crea un tablero 10x10 vacío Para el jugador 
tableroJug = tablerosIniciales.tableroJug

tablerosIniciales.crea_cruceroManual(tableroJug)

tablerosIniciales.num_naves(2, tablerosIniciales.crea_lanzaderaManual, tableroJug)

tablerosIniciales.num_naves(3, tablerosIniciales.crea_bombarderoManual, tableroJug)

tablerosIniciales.num_naves(4, tablerosIniciales.crea_cazaManual, tableroJug)

tablero_jugador = tableroJug.copy()

tableroVacio_jugador = np.full((10, 10), (' '))

jugador1.jugador1(tablero_jugador, tablero_computadora, tableroVacio_jugador, tableroVacio_computadora)
computadora.computadora(tablero_jugador, tablero_computadora, tableroVacio_jugador, tableroVacio_computadora)
endofgame.endgame(tablero_jugador, tablero_computadora)
print(f'{jugador}, Esperemos haya disfrutado del juego, todos los derechos reservados... ')
print('\U0001F609')
# tablerosingame.tableroingame()
# endofgame.endgame(tablerojugador, tablerocomputadora)