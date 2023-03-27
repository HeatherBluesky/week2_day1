# write code here 
class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0 # sets the teams to points from the beginning 

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_to_find):
        player_exists = False
        for player in self.players:
            if player == player_to_find:
                player_exists = True
        
        return player_exists
       
    def play_game(self, result):  # last 2 questions on the test, needed to add the self.points to the class and set to 0 to begin
        if result == True:
            self.points += 3 