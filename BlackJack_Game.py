# Este es mi primer juego en python
from os import system
import random 
from art import logo

def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(card_list):
  score = sum(card_list)
  if score == 21 and len(card_list) == 2:
  	return 0
  elif 11 in card_list and score > 21:
  	card_list.remove(11)
  	card_list.append(1)
  	return sum(card_list)
  return score

def compare(user,computer):
	if user == computer:
		return "Empate."
	elif	user > computer:
		return "Tu ganas. :)"
	else:
		return "La casa gana."


""" Comienza el codigo del juego """
def play_game():
	system("cls")
	print(logo)
	user_cards = []
	computer_cards = []
	is_game_over = False

	for _ in range (2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"Tus cartas son {user_cards}, tu puntaje es {user_score} ")
		print(f"La primer carta de la casa es: {computer_cards[0]} ")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
			if user_score == 0 and computer_score != 0:
				print(f"Tus cartas son {user_cards}, tu puntaje es de {user_score}. ")
				print("Tu ganas")
			else:
				print(f"Perdiste tus cartas son {user_cards}, tu puntaje es {user_score} ")
				print(f"Las cartas de la casa son {computer_cards}, el puntaje es de {computer_score}")
				print("La casa gana.")
		else:
			user_say = input ("Quieres otra carta? 'y' o 'n': ")
			if user_say == 'y':
				user_cards.append(deal_card())
				user_score = calculate_score(user_cards)
	  # 	  print(f"Tus cartas son {user_cards}, tu puntaje es {user_score} ")
		# 		print(f"La primer carta de la casa es ¨{computer_cards[0]} ")
			else:
				is_game_over = True

	# print("va la casa")

	while computer_score != 0 and computer_score < 17:
	  computer_cards.append(deal_card())
	  computer_score = calculate_score(computer_cards)

	  print(f"Tu mano final {user_cards}, tu puntaje final {user_score}")
	  print(f"Mano final de la casa {computer_cards},  el puntaje final de la casa {computer_score}")
	  print(compare(user_score, computer_score))

		
while input("Quieres jugar al blackjack? 'y' o 'n': ") == 'y':
	play_game()
