from os import system

def menu():
	system("cls")
	print("""
	PUBGM Tournament Registration
	[1]. See All Players
	[2]. Add New Players
	[3]. Looking For Players
	[4]. Delete Player
	[Q}. Quit
		""")

def header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_answer(char):
	if char.upper() =="Y":
		return True
	else:
		return False

def data(player=None, ID=True, all_data=False):
	if player != None and all_data==False:
		print(f"NAMA : {player}")
		print(f"ID : {players[player]['ID']}")
	elif ID == False and all_data == False:
		print(f"NAMA : {player}")
	elif all_data == True:
		for every_player in players:
			nama = every_player
			ID = players[every_player]["ID"]
			print(f"NAMA : {nama} - ID : {ID}")

def view_players():
	header("Registered Player List")
	if not_empty(players):
		data(all_data=True)
	else:
		print("Sorry There Are No Registered Players Yet")
	input("Press ENTER to return to the MENU")

def add_player():
	header("Add New Players")
	nama = input("NAMA \t: ")
	ID = input("ID \t: ")
	respond = input(f"Are You Sure You Want To Save Contacts : {nama} ? (Y/N) ")
	if verify_answer(respond):
		players[nama] = {
			"ID" : ID
		}
		print("Saved Player Data")
	else:
		print("Cancel Saved Data")
	input("Press ENTER to return to the MENU")

def search(player):
	if player in players:
		return True
	else:
		return False

def find_player():
	header("Looking For Players")
	nama = input("Player Name Wanted : ")
	exists = search(nama)
	if exists:
		print("Data Found")
	else:
		print("Data Missing")
	input("Press ENTER to return to the MENU")

def delete_player():
	header("Delete Player")
	nama = input("Player Name To Be Deleted : ")
	exists = search(nama)
	if exists:
		data(player=nama)
		respond = input(f"Sure You Want To Delete {nama} ? (Y/N) ")
		if verify_answer(respond):
			del players[nama]
			print("Player Data Has Been Deleted")
		else:
			print("Undelete Player Data")
	else:
		print("Data Missing")
	input("Press ENTER to return to the MENU")

def check_player_input(char):
	char = char.upper()
	if char == "Q":
		print("GOODBYE...")
		return True
	elif char == "1":
		view_players()
	elif char == "2":
		add_player()
	elif char == "3":
		find_player()
	elif char == "4":
		delete_player()

players = {
	"BTRXRyzen" : {
		"ID" : "0987654321"
	},
	"BTRXLuxxy" : {
		"ID" : "1234567890"
	}
}

stop = False

while not stop:
	menu()
	player_input = input("Pilihan : ").upper()
	stop = check_player_input(player_input)
