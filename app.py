import constants
import math

teams = constants.TEAMS

team_players = constants.PLAYERS
panthers= []
bandits = []
warriors = []
exper = []
non_exper = []
def clean_data():
    
    for players in team_players:
        for key,value in players.items():
            if key == "experience" and value == "YES":
                players[key] = True
                exper.append(players)       
            elif key == "experience" and value == "NO":
                players[key] = False
                non_exper.append(players)
            if key == "height":
                players[key] = int(players[key].split()[0])

            if key == "guardians":
                players[key] = players[key].split(" and ")
            
            
       

def balance_teams():
    total_teams = [panthers,warriors,bandits]
    total_team_len = len(total_teams)
    for team_member in range(len(exper)):
        total_teams[team_member % total_team_len].append(exper[team_member])
        total_teams[team_member % total_team_len].append(non_exper[team_member])
    
    
def menu():
    print("\n")
    print("   A) Display Team Stats")
    print("   B) Quit\n")
    
    
    

def team_info(team):
    player_guardians = []
    player_name = []
    print(f"Total team : {len(team)}")

    avg_height = 0
    total_height = 0
    exper_count = 0
    non_exper_count = 0
    for index,exp in enumerate(team):

        total_height += exp['height']

        if exp['experience'] == True:
            exper_count += 1
        elif exp['experience'] == False:
            non_exper_count += 1

        

        name = exp['name']
        player_name.append(name)
        guardians = exp['guardians']
        player_guardians.extend(guardians)
        

    avg_height = total_height / len(team)

    print(f"Total Experiance : {exper_count}\nTotal inexperienced : {non_exper_count}\n")
    print("Average hight : {:.1f}".format(avg_height))
    print("Players on Team: ")
    print(", ".join(player_name))
    print("\nGuardians : ")
    print(", ".join(player_guardians))

  

def main():
    print("\n")
    print("\t\tBASKETBALL TEAM STATS TOOL\t\t\n")
    print("     ---- MENU ----")
   
    
    team_state = None
    clean_data()
    balance_teams()
    while True:
        menu()
        option = input("Enter an option : " )
        

        
        if option.lower() == "a":
            print("\nA) Panthers\nB) Bandits\nC) Warriors\n")
            team_state = input(" > ")
            if team_state.lower() == "a":
                team_info(panthers)         
            elif team_state.lower() == "b":
                team_info(bandits)
            elif team_state.lower() == "c":
                team_info(warriors)
        elif option.lower() == "b":
            break
        

    

if __name__ == "__main__":
    main()



