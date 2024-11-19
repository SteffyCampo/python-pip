import random

def choose_option():
  options = ("piedra", "papel", "tijera")
  user_option = input("Escoja piedra, papel o tijera => ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("La opción ingresada no es válida")
    return None, None
    #continue

  computer_option = random.choice(options)

  print("User option => ", user_option)
  print("Computer option => ", computer_option)
  return user_option, computer_option

def choose_winner(user_wins, computer_wins):
  if user_wins == 2:
    print("EL GANADOR ES EL USUARIO")
    exit()
  if computer_wins == 2:
    print("EL GANADOR ES LA COMPUTADORA")
    exit()
  

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Es un empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Ganaste!, piedra gana a tijera")
      user_wins += 1
    else:
      print("Perdiste!, papel gana a piedra")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("Perdiste!, piedra gana a tijera")
      computer_wins += 1
    else:
      print("Ganaste!, tijera gana a papel")
      user_wins += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("Perdiste!, tijera gana a papel")
      computer_wins += 1
    else:
      print("Ganaste!, papel gana a piedra")
      user_wins +=1
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  round = 1

  while True:
    print("*" * 30)
    print("ROUNDS", round)
    print("*" * 30)
  
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
   
    round += 1

    user_option, computer_option =  choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    choose_winner(user_wins, computer_wins)
    

    
    

run_game()
