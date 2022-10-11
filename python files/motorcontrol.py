

import serial
import time
import random
scramble_moves = []
connection = serial.Serial('COM4', 250000)
def write_gcode(gcode):
    connection.write(bytes(gcode + '\n', encoding='utf-8'))
    time.sleep(0.1)
    #oks = connection.read_until(expected='\n',size=100)
    #print(oks)
    

def setup():
     
    write_gcode('G91')
    
    write_gcode('M302 S0')
    
    

#------------------------------------------------------------------------------------------------------------------------------------------------
def R():
    write_gcode('G0 X1 F900')
    write_gcode('G92 X0')
    scramble_moves.append("R")


def RP():
    write_gcode('G0 X-1 F900')
    write_gcode('G92 X0')
    scramble_moves.append("R'")

def R2():
    write_gcode('G0 X2 F900')
    write_gcode('G92 X0')

    scramble_moves.append("R2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def L():
    write_gcode('G0 Y-1 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L")

def LP():
    write_gcode('G0 Y1 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L'")

def L2():
    write_gcode('G0 Y2 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def F():
    write_gcode('G0 Z1 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F")

def FP():
    write_gcode('G0 Z-1 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F'")

def F2():
    write_gcode('G0 Z2 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def B():
    write_gcode('T0')
    write_gcode('G0 E-1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B")

def BP():
    write_gcode('T0')
    write_gcode('G0 E1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B'")

def B2():
    write_gcode('T0')
    write_gcode('G0 E2 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def U():
    write_gcode('T1')
    write_gcode('G0 E-1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("U")

def UP():
    write_gcode('T1')
    write_gcode('G0 E1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("R'")

def U2():
    write_gcode('T1')
    write_gcode('G0 E2 F900')
    write_gcode('G92 E0')
    scramble_moves.append("U2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def D():
    write_gcode('T2')
    write_gcode('G0 E-1 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D")

def DP():
    write_gcode('T2')
    write_gcode('G0 E1 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D'")

def D2():
    write_gcode('T2')
    write_gcode('G0 E2 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D2")
#------------------------------------------------------------------------------------------------------------------------------------------------



moves = [R, RP, R2, L, LP, L2, F, FP, F2, B, BP, B2, U, UP, U2, D, DP, D2]
movesAsString = ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", "U", "U'", "U2", "D", "D'", "D2"]
numofmoves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

scramblemoves = random.sample(numofmoves, 17)
def scramble():
   for i in scramblemoves:
    moves[i]()


   
    
    


write_gcode('G91')

write_gcode('M302 S0')
print(connection)
print(connection.name)

while True:
    menuchoice = input("Choose something, e")
    if menuchoice == 'scramble':
        scramble()
        print("Your scramble is: ", *scramble_moves, sep =' ')
        scramble_moves.clear()
    elif menuchoice == 'R':
        R()
    elif menuchoice != "scramble" and menuchoice != ' ':
         custommoveindex = movesAsString.index(menuchoice)
         custommoveindex = custommoveindex + 1
         moves[custommoveindex]()
                
    elif menuchoice == '':
        connection.close()
        break