import random
lives = 4
score = 0
number = random.randint(1,11)
print("==Geuss The Number==")
print("You have a limited number of tries!")
print("Any number between 1-10")
print("Let the games begin!!!")
print("===================================")

def guess_the_number():
  while True:    
    global number
    global lives
    global score
    guess = int(input("\nEnter a number:"))
    guess = int(guess)
   
    if lives == 0:
      print("GamE OveR!!")
      return
    else:     
      if guess == number:
        score += 1
        print("====You win the game!====")
        print("Wins " + str(score))
        lives = 4
        number = random.randint(1,11)
      elif guess < number:
        print("Number is greater")
        lives -= 1
        print("Lives remaining: ",lives)
      elif guess > number:
        print("Number is lower")
        lives -= 1
        print("Lives remaining: ",lives)
      
guess_the_number()