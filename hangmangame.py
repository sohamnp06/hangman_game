import random


words = [
    "apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat", "ice",
    "kite", "lion", "monkey", "notebook", "orange", "pencil", "queen", "robot", "snake",
    "umbrella", "violin", "whale", "xylophone", "yogurt", "zebra", "anchor", "bridge",
    "eagle", "forest", "guitar", "hill", "island", "jacket", "kangaroo", "lamp", 
    "ocean", "pirate", "quilt", "river", "sun", "train", "unicorn", "vase", "window",
    "yawn", "zoo", "art", "ball", "circle", "dance", "earth", "feather", "gold",
    "idea", "jewel", "key", "leaf", "magic", "nest", "owl", "paint", "quiet", "rain",
    "star", "turtle", "under", "voice", "wind", "exit", "young", "zone", "alligator",
    "candle", "desk", "engine", "fan", "garden", "hammer", "ink", "jungle", "kite",
    "mirror", "net", "opera", "piano", "queen", "rope", "shell", "tower", "uniform"
]



secret_word=random.choice(words).upper()
guessed_word=[]
prev_guess=[]
leftout_letters=set(secret_word)
lifeline=5

print(f"WORD CONTAINS TOTAL {len(secret_word)} LETTERS \n")

while len(leftout_letters) != 0 and lifeline !=0:
  word_list = [letter if letter in guessed_word else '_' for letter in secret_word]
  print(' '.join(word_list))
  answer=input("\nENTER GUESSED LETTER : ").upper()

  if answer in guessed_word:
    lifeline-=1
    print(f"{answer} WAS ALREADY ENTERED")
    print(f"LIFELINE REMAINING : {lifeline}\n")

  elif answer in secret_word:
    guessed_word.append(answer)   
    leftout_letters.remove(answer)

  else:
    lifeline-=1
    prev_guess.append(answer)
    pg=','.join(prev_guess)
    print(f"SORRY WRONG GUESS\nPREVIOUS GUESSES: {pg}")
    print(f"LIFELINE REMAINING : {lifeline}\n")


if lifeline == 0:
  print(f"\nCORRECT ANSWER WAS: {secret_word}")
  print("SORRY BETTER LUCK NEXT TIME")

else:
  print("CONGRATULATIONS!!!...YOU GUESSED THE WORD CORRECTLY")












