#1. import random module
#This program will allocate teams randomly
#2. Create a list of every genius
#3. Use the module to shuffle a list
#4. Loop through list and display each team members name
#5. using if statement to see if the user is happy with new teams
# if not it will shuffle again

import random #import random module
#create list of players in player variable
players = ["Devon", "Kauri", "Isaiah",
        "Braylen","Taymur", "Xavier",  
        "Taqari", "Kenlon", "Marshawn",        
        "Nahum", "Kamari", "Kristopher",
        "Joseph", "Darren", "Walter",
        "Jeffrey", "Nishad", "Maximus",
        "Ja’Den", "Joaquin", "Jarmauri",
        "Eustace", "Semaj", "Avery",]

def PickTeams(players): #create our funtion
    random.shuffle(players) #Shuflle this list of players
    team1 = players[:len(players) // 2]#put 1st half of team players
    teamCaption1 = team1[random.randrange(0, 12)]#randomly assign team caption

    print("Team 1:")
    print("Team 1 Capatin: " + teamCaption1)
    for player in team1:
        print(player)

    team2 = players[:len(players) // 2:]
    teamCaption2 = team2[random.randrange(0, 12)]

    print("\nTeam 2:")
    print("Team 2 Capatin: " + teamCaption2)
    for player in team2:
        print(player)
    
PickTeams(players)
