from database_api.graph_repository import GraphRepository
from database_api.base_repository import BaseRepository

local_graph = GraphRepository()
# connect to database and create cursor
connection, cursor = local_graph.open_database()

# execute queries
cursor.execute(local_graph.get_graph(1))
print(cursor.fetchall())
cursor.execute(local_graph.get_graph(5))
print(cursor.fetchall())

# commit and close database
local_graph.commit_to_database()




