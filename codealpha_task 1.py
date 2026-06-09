import random 

anime = ['haikyuu', 'attackontitan', 'drstone', 'tokyorevenger', 'demonslayer']
anime_name = random.choice(anime)

gussed_anime = []
wrong_attempt = 0
remaining_attempt = 6

print ("Welcome to the Hangman Game!")

while wrong_attempt < remaining_attempt:

  display_anime = ''
  for letter in anime_name :
      if letter in gussed_anime: 
        display_anime += letter + ''
      else:
        display_anime += "_"
  print("\n anime name:",display_anime)

  if '_' not in display_anime:
    print ("congo you guessed it right:",anime_name)
    break

  guess = input("enter the letter:").lower()

  if len(guess) != 1 or not guess.isalpha():
    print("please enter only one letter")
    continue

  if guess in gussed_anime :
    print("you already guess the letter") 
    continue   

  gussed_anime.append(guess) 

  if guess in anime_name:
        print("Correct!")
  else:
        wrong_attempt += 1
        print("Wrong guess!")
        print("Remaining chances:", remaining_attempt - wrong_attempt)

  if wrong_attempt == remaining_attempt:
    print("\n❌ Game Over!")
    print("The correct word was:", anime_name)