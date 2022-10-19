
#importing libraries
#you need to run "pip install pyserial" for this to work
import serial
import time
import random
scramble_moves = []
connection = serial.Serial('COM4', 250000) #connecting to COM4 at 250000 baudrate
def write_gcode(gcode):
    connection.write(bytes(gcode + '\n', encoding='utf-8')) #sending and encoding the gcode as ASCII text
    time.sleep(0.1) #adding a slight delay so the arduino doesn't get overloaded
    #oks = connection.read(size=300) #testing
    #print(oks) #testing
    

def setup():
    #enables relative positioning mode
    write_gcode('G91')
    #disables cold extrusion preventing
    write_gcode('M302 S0')
    print("Connected!")
    
    

#------------------------------------------------------------------------------------------------------------------------------------------------
def R():
    #moves the X 1mm at 900 minutes/mm
    write_gcode('G1 X1 F900')
    #tells the arduino that the X axis is at 0, because sometimes relative positioning mode doesnt work
    write_gcode('G92 X0')
    #adds "R" to scramble_moves, so you know how it was scrambled
    scramble_moves.append("R")


def RP():
    write_gcode('G1 X-1 F900')
    write_gcode('G92 X0')
    scramble_moves.append("R'")

def R2():
    write_gcode('G1 X2 F900')
    write_gcode('G92 X0')

    scramble_moves.append("R2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def L():
    write_gcode('G1 Y-1 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L")

def LP():
    write_gcode('G1 Y1 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L'")

def L2():
    write_gcode('G1 Y2 F900')
    write_gcode('G92 Y0')
    scramble_moves.append("L2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def F():
    write_gcode('G1 Z1 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F")

def FP():
    write_gcode('G1 Z-1 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F'")

def F2():
    write_gcode('G1 Z2 F900')
    write_gcode('G92 Z0')
    scramble_moves.append("F2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def B():
    #switches to extruder 0, because 3 of the motors are extruders, and they are called 0, 1, 2
    write_gcode('T0')
    write_gcode('G1 E-1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B")

def BP():
    write_gcode('T0')
    write_gcode('G1 E1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B'")

def B2():
    write_gcode('T0')
    write_gcode('G1 E2 F900')
    write_gcode('G92 E0')
    scramble_moves.append("B2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def U():
    write_gcode('T1')
    write_gcode('G1 E-1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("U")

def UP():
    write_gcode('T1')
    write_gcode('G1 E1 F900')
    write_gcode('G92 E0')
    scramble_moves.append("R'")

def U2():
    write_gcode('T1')
    write_gcode('G1 E2 F900')
    write_gcode('G92 E0')
    scramble_moves.append("U2")
#------------------------------------------------------------------------------------------------------------------------------------------------
def D():
    write_gcode('T2')
    write_gcode('G1 E-1 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D")

def DP():
    write_gcode('T2')
    write_gcode('G1 E1 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D'")

def D2():
    write_gcode('T2')
    write_gcode('G1 E2 F700')
    write_gcode('G92 E0')
    scramble_moves.append("D2")
#------------------------------------------------------------------------------------------------------------------------------------------------


#Making a list of the functions, so i can call them easier
moves = [R, RP, R2, L, LP, L2, F, FP, F2, B, BP, B2, U, UP, U2, D, DP, D2]
#A list of all the moves as a string
movesAsString = ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", "U", "U'", "U2", "D", "D'", "D2"] 
numofmoves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def scramble():
  #generate scramble 
  seventeen_scramblemoves = random.sample(numofmoves, 17)
  eight_scramblemoves = random.sample(numofmoves, 8)
  #execute the scramble 
   for i in seventeen_scramblemoves:
    moves[i]()
   for i in eight_scramblemoves:
    moves[i]()

def menu():
 print("""The commands you can use are as follows:\n
 Type send; GCODE to send gcode, with GCODE being the gcode you want to send\n
 Type scramble to scramble the cube\n
 Type cm; MOVE to do a custom move, with MOVE being the move you want to do, written in standard cube notation\n
 Type mm; MOVES to do multiple moves, with MOVES being the moves you want to do, written in standard cube notation\n
 Type help to see this menu again\n
 Type disconnect to disconnect from the arduino and exit the program\n""" )

   
    
    


connected = False
print("A Rubik's Cube Scrambler, Made by JmarbinGG")
menu()
#print(connection) #prints the connection for testing
#This is the menu
while True:
    if not connected:
        print("Please connect by typing connect. To disconnect, type disconnect")
    menuchoice = input(">")
    if menuchoice == 'scramble':
        scramble()
        print("Your scramble is: ", *scramble_moves, sep =' ')
        scramble_moves.clear()
    elif menuchoice.startswith('send;'):
        menuchoiceGCODE = menuchoice.replace('send; ', '')
        write_gcode(menuchoiceGCODE)
    elif menuchoice.startswith("cm;"):
      custommoveindex = menuchoice.replace('cm; ', '')
      if custommoveindex in movesAsString:
       custommoveindex = movesAsString.index(custommoveindex)
       moves[custommoveindex]()
      else:
        print("Invalid move")
    elif menuchoice == "help":
        menu()
    elif not connected and menuchoice == "connect":
        setup()
        connected = True
    elif menuchoice.startswith("mm;"):
        
        multipleMovesToBeDone = menuchoice.replace("mm; ", "").split(" ")
        multipleMovesToBeDoneInNumbers = []
        for i in multipleMovesToBeDone:
            i = movesAsString.index(i)
            multipleMovesToBeDoneInNumbers.append(i)
        for e in multipleMovesToBeDoneInNumbers:
            moves[e]()
    elif connected and menuchoice == 'disconnect':
        connection.close()
        connected = False
        break
