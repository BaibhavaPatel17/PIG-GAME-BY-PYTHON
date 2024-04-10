import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)


    return roll

while True:
  players = input("Enter The Number Of Players (2-4) : ")
  if players.isdigit():
     players = int(players)
     if 2 <= players <= 4:
      break
     else:
        print("Must Be Between 2 - 4 players.")
  else:
   print("Input Must Be a Number ")
     
print(players) 

max_score = 50
player_scores = [0 for _ in range (players)]

while max(player_scores) < max_score:
   print("Lets Begain The game\n")
   for player_idx in range(players):
       print("\nplayer number",player_idx + 1,"turn has just started !\n")
       print("your totla score is ",player_scores[player_idx],"\n")
       current_score = 0
       while True:  
          should_roll = input("Would You like To Roll? if yes  press (Y), if no press (n) :")
          if should_roll.lower()!="y":
            break
   
          value = roll()
          if value ==1:
           print("you got the value 1 , your turn over")
           current_score =0
           break
          else:
           current_score +=value
           print("you got the value :",value)  
          print("your current score is:",current_score) 
       player_scores[player_idx] += current_score
       print("your total score is : ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player number", winning_idx +1,
      "is the Winner With A score of :", max_score)    