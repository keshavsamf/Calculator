
import os



def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add(num_1, num_2):

 return num_1 + num_2

def subtract(num_1, num2):

  return num_1 - num_2

def multiply(num_1, num_2):
 
   return num_1 * num_2

def divide(num_1, num_2):

  return num_1 / num_2

clr()




print("\033[1;31;40m" + "# Made by " + "\033[1;32;40m" + "'KESHAVSAMF'")

print("\033[1;36;40m" + "What you want to do -\n" \
      "\033[1;31;40m" + "1. add\n" \
      "\033[1;32;40m" + "2. subtract\n" \
      "\033[1;33;40m" + "3. multiply\n" \
      "\033[1;37;40m" + "4. divide\n")


select = int(input("select any no. 1,2,3,4: "))




num_1 = float(input("please enter a no: "))

num_2 = float(input("please enter another no: "))



verify = input("\033[1;36;40m" + "press enter to continue ")

clr()

if select== 1:
   print(num_1, "+", num_2, "=",
         add(num_1, num_2))

elif select== 2:
    print(num_1, "-", num_2, "=",
      subtract(num_1, num_2))

elif select== 3:
    print(num_1, "*", num_2, "=",
      multiply(num_1, num_2))


elif select== 4:
   print(num_1, "/", num_2, "=",
    divide(num_1, num_2))



else:
    print("invalid input")
