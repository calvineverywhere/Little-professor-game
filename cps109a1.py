'''
Math problem guessing game 
This program will generate 10 math problems for 
the user to solve dependng on the level 1,2,3(easy, meduim, hard).
For example, if the program shows
1+2= , the user will probably answer 3. But if the user
didnt answer 3 and but the incorrect answer, if program will display 
wrong.And after three incorrect answers for the same problem , the 
program will show the correct answer. For example, 1+4=5 or 2+2=4.
the user will get 1 score if the answer is correct.
And finally, the program will display the score. 
'''

#import the random module to generate random
import random

#define the main function
def main():
    
    greeting = "hello"
    
    #ask the user to type hello
    response = input("type 'hello' to the program: ")
    
    #(comparing)check if the user's response is not hello using a while loop
    while response.lower() != greeting:
        
        #if the response is not hello, ask the user to type it again 
        response = input("Incorrect. Please type 'hello' back: ")
       
    #printing the message   
    print("Perfect! You typed 'hello' back. Now the program will start")

    #call_get_level_function
    level = get_the_level()

    #get the score and print 
    print("Score" , generate_integer(level))


#define a function to get the level
def get_the_level():
    
    #Loop until a valid enter is entered
    while True:
        try:
            #ask the user to put level 
            level = int(input("Level: "))
            
            #and check if it is between 1 to 3
            if level in {1,2,3}:
                
                #if it is valid, break and exit
                break 
            
        #handling the error, for example even if the input is invalid 
        # we continue the loop
        except ValueError:
            pass
        
    #return the valid game level 
    return level

#define a function to generate random math problems to calculate score
def generate_integer(level):
    
    #initialize score to zero
    score = 0
    
    #generating 10 problems depending on the level 
    for ten in range(1,11):
        
        #for level 1
        if level == 1:
            
            #generate the number between 1 and 9 for the first number 
            x = random.randint(0,9)
            
            #generate the number between 1 and 9 for the second number
            y = random.randint(0,9)
            
        #for level 2
        elif level == 2:
            
            #generate the number between 10 and 99 for the first number
            x = random.randint(10, 99)
            
            #generate the number between 10 and 99 for the second number
            y = random.randint(10, 99)
            
        #for level 3
        else:
            
            #generate the number between 100 and 999 for the first number
            x = random.randint(100, 999)
            
            #generate the number between 100 and 999 for the second number
            y = random.randint(100, 999)
            
        #initialize the count to zero
        count = 0
        
        #give the users 3 chances to enter the correct answer
        while count < 3:
            
            try:
                #ask the user to input the answer for the problem.
                guess  = int(input(f"{x} + {y} = "))
                
                #check if the answer is correct
                if guess == x + y:
                    #add 1 to score if the answer is correct
                    score += 1
                    #exit the loop 
                    break
                
                else:
                    #print 'nah' to show if it is wrong'
                    print("nah")
                    
                    #add 1 to count
                    count += 1
                    
                    # If the user has made three attempts, type the correct answer
                    if count == 3:
                        
                        #print the correct answer
                        print(f"{x} + {y} = {x + y}")
                        
                        #exit the loop
                        break
                    
            except ValueError:
                #print 'nah' to show that the answer is wrong 
                print("nah")
                
                #add 1 to count
                count += 1
                
                #continue the loop
                pass
    #return the final score 
    return  score

if __name__ == '__main__':
    #call the main function
    main()
