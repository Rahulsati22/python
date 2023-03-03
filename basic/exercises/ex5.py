# playing rock paper scissor
import random
print("Rules of the games")
print()
print('Enter "Rock" for rock \nEnter "Paper" for Paper \nEnter "Gun" for Gun')
print("The game is between you and computer and the person that\nwill score 5 points first will be the winner")
list = ["Rock", "Scissor", "Paper"]
playerScore = 0
computerScore = 0
while (True):
    playerValue = input("Enter what you want to choose\n")
    computerValue = random.choice(list)
    print(computerValue)
    if (playerValue == "Rock" and computerValue == "Paper"):
        computerScore += 1
    if (playerValue == "Rock" and computerValue == "Scissor"):
        playerScore += 1
    if (playerValue == "Rock" and computerValue == "Rock"):
        continue

    if (playerValue == "Paper" and computerValue == "Paper"):
        continue
    if (playerValue == "Paper" and computerValue == "Scissor"):
        computerScore += 1
    if (playerValue == "Paper" and computerValue == "Rock"):
        playerScore += 1

    if (playerValue == "Scissor" and computerValue == "Paper"):
        playerScore += 1
    if (playerValue == "Scissor" and computerValue == "Scissor"):
        continue
    if (playerValue == "Scissor" and computerValue == "Rock"):
        computerScore += 1
    
    print(f"PlayerScore : {playerScore} and ComputerScore : {computerScore}")
    if (playerScore == 5):
        print("Player has won the match")
        break;
    if (computerScore == 5):
        print("Computer has won the match")
        break;
