import strawberry

@strawberry.type
class Player:
    role: str
    is_alive: str
    nickname: str

@strawberry.type
class Game:
    room_id: int
    comments: list[str]
    scoreboard: list[Player]

active_games = []
finished_games = []
room_id_to_game = dict()

def get_active_games():
    return active_games

def get_finished_games():
    return finished_games

def get_scoreboard_by_room_id(room_id: int):
    return room_id_to_game[room_id].scoreboard

@strawberry.type
class Query:
    active_games: list[int] = strawberry.field(resolver=get_active_games)
    finished_games: list[int] = strawberry.field(resolver=get_finished_games)
    scoreboard: list[Player] = strawberry.field(resolver=get_scoreboard_by_room_id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_comment(self, room_id: int, comment: str)->Game:
        room_id_to_game[room_id].comments.append(comment)
        return room_id_to_game[room_id]


active_games = [1, 2]
player1 = Player(nickname="Alice", is_alive=True, role="Queen")
player2 = Player(nickname="Bob", is_alive=False, role="King")

game1 = Game(room_id=1, comments=["al"], scoreboard=[player1])
game2 = Game(room_id=2, comments=["bo"], scoreboard=[player2])

room_id_to_game[1] = game1
room_id_to_game[2] = game2
print(room_id_to_game)

schema = strawberry.Schema(query=Query, mutation=Mutation)