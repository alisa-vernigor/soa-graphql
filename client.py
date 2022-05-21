from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://0.0.0.0:8000/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


# Provide a GraphQL query
queryActiveGames = gql(
    """
    query {
        activeGames
    }
"""
)

queryFinishedGames = gql(
    """
    query {
        finishedGames
    }
"""
)

while True:
    command = input("Input command: ")

    if command == 'activeGames':
        result = client.execute(queryActiveGames)
        print(result)
    elif command == 'finishedGames':
        result = client.execute(queryFinishedGames)
        print(result)
    elif command == 'scoreboard':
        room_id = int(input("Input room_id: "))
        result = client.execute(
            gql(
                f"query {{"
                f"    scoreboard(roomId: {room_id}) {{"
                f"        nickname"
                f"        isAlive"
                f"        role"
                f"    }}"
                f"}}"
            )
        )
        print(result)
    elif command == 'addComment':
        room_id = int(input("Input room_id: "))
        comment = input("Input comment: ")
        result = client.execute(
            gql(
        f"mutation {{"
	    f"    addComment(roomId: {room_id}, comment:  \"{comment}\") {{"
        f"        roomId"
        f"        comments"
        f"}}"
        f"}}"))
        print(result)
    elif command == 'finish':
        break
