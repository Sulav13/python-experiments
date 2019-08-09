# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of
# robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and 
# original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2


x=0
y=0
while True:
   dir = input("enter the direction step: ")
   if not dir:
     break
   dir, steps = dir.split(' ')
   if dir == "left":
       x = x - int(steps)
   elif dir == "right":
       x = x + int(steps)
   elif dir == "up":
       y = y + int(steps)
   elif dir == "down":
       y = y - int(steps)
   else:
     pass
distance = (x**2 + y**2)**(1/2)
print("the output is: ",int(distance))