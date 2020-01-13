import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
t1 = 24
e1 = 23
t2 = 22
e2 = 18
t3 = 3
e3 = 2
t4 = 17
e4 = 27

count = 0

in1 =26
in2 =19
in3 =13
in4 =6


GPIO.setwarnings(False)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

def distance(TRIG,ECHO):
    GPIO.setwarnings(False)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.setup(ECHO,GPIO.IN)
    
    GPIO.output(TRIG, False)
    time.sleep(0.000001)
    
    GPIO.output(TRIG, True)
    time.sleep(0.000001)
    GPIO.output(TRIG, False)
    pulse_start = 0 
    pulse_end   = 0
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    #if pulse_end > pulse_start:
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    #distance = round(distance, 2)
    return distance

def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    
def left():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def right():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
try:
    def can_exit(lst):
      maze = lst
      #Set goal before passing it to the search function
      maze[4][3] = 5
      return search(0,0, maze)

    n= 0
    def search(row, column, maze):
      print("visit", row, column)
      #Attempting to get a visual of where I am
      #state = maze[row][column]
      global n

      maze[row][column] = 2
      #n=n+1
      #for i in maze:
       # print(i)
      
      #ukuran array
      y = len(maze)
      #print(y)
      x = len(maze[row])
      #print(x)
      s=0.398887
      n=1.267
      r=3
      c=3
      global count
      if count == 0:
          stop()
          time.sleep(1)
          count =1
        
      if(row == 4 and column == 4):
          stop()
          time.sleep(1)
          print("finish", row, column)
      
      else:
 #1         
        if(row - 1 <= -1 and column - 1 <= -1): #pojok kiri atas
          if(maze[row + 1][column] == 0): #maju
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          elif(maze[row][column + 1] == 0): #kiri
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
#2
        elif(row + 1 >= y and column - 1 <= -1): #pojok kiri bawah
          if(maze[row][column + 1] == 0):
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
#3
        elif(row - 1 <= -1 and column + 1 >= x):
          if(maze[row + 1][column] == 0):
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
#4
        elif(row + 1 >= y and column + 1 >= x ): #ragu
          if(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
#5
        elif(row - 1 <= -1):
          if(maze[row + 1][column] == 0):
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          elif(maze[row][column + 1] == 0):
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
          # elif(maze[row][column - 1] == 0):
          #   column = column - 1
          #   print("kanan")
          #   search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
#6
        elif(column - 1 <= -1):
          if(maze[row + 1][column] == 0):
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          elif(maze[row][column + 1] == 0):
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          # elif(maze[row - 1][column] == 0):
          #   row = row - 1
          #   print("mundur")
          #   search(row, column, maze)
#7
        elif(row + 1 >= y):          #letak paling bawah -> tapi ragu
          # if(maze[row + 1][column] == 0):
          #   row = row + 1
          #   print("maju")
          #   search(row, column, maze)
          if(maze[row][column + 1] == 0):
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
#8
        elif(column + 1 >= x):          #ragu
          if(maze[row + 1][column] == 0): #finish
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          # elif(maze[row][column + 1] == 0):
          #   column = column + 1
          #   print("kiri")
          #   search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
#9
        else:
          if(maze[row + 1][column] == 0):
            row = row + 1
            forward()
            time.sleep(n)
            print("maju")
            search(row, column, maze)
          elif(maze[row][column + 1] == 0):
            column = column + 1
            left()
            time.sleep(s)
            forward()
            time.sleep(n)
            right()
            time.sleep(s)
            print("kiri")
            search(row, column, maze)
          elif(maze[row][column - 1] == 0):
            column = column - 1
            right()
            time.sleep(s)
            forward()
            time.sleep(n)
            left()
            time.sleep(s)
            print("kanan")
            search(row, column, maze)
          elif(maze[row - 1][column] == 0):
            row = row - 1
            print("mundur")
            search(row, column, maze)
        
    can_exit([
        [0, 1, 0, 0, 0, 1], 
        [0, 1, 0, 1, 0, 1], 
        [0, 1, 0, 1, 0, 1], 
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1]
    ])
    
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
