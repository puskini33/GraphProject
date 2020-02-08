from database_api.graph_repository import GraphRepository
from database_api.base_repository import BaseRepository

local_graph = GraphRepository()
# connect to database and create cursor
connection = local_graph.connection

# execute queries
print(local_graph.insert(13, 'Flora Graph'))


# close database
local_graph.close_database()




