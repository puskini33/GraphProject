from database_api.graph_repository import GraphRepository
from database_api.base_repository import BaseRepository

local_graph = GraphRepository()
# connect to database and create cursor

# execute queries
local_graph.insert('Flora Graph')


# close database
local_graph.close_database()
