# Initial variable to track game play
user_play = "y"

aux = 0 
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    numbers = int(input('How many numbers? '))
   
    count = 0
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    while count +aux   < (numbers  + aux + 1):
        # Print each number in the range
       
        print(count + aux)
        count +=1
        

    aux = count + aux 
    
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")