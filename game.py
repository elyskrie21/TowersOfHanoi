from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Set up the Game
num_disks = 0

while num_disks < 3:
  num_disks = int(input("\nHow many disks do you want to play with?\n"))

#Get User Input

        
#Play the Game