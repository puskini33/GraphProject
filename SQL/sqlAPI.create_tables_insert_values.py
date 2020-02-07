def create_tables():
    c.execute('''CREATE TABLE if not exists node (
                id integer primary key, name text, graph_id integer, FOREIGN KEY(graph_id) REFERENCES graph(id));''')
    c.execute('''CREATE TABLE if not exists edge (id integer primary key, name text, cost integer, 
                node_start_id integer, node_end_id integer,	graph_id integer,
                FOREIGN KEY(graph_id) REFERENCES graph(id),
                FOREIGN KEY(node_start_id) REFERENCES node(id),
                FOREIGN KEY(node_end_id) REFERENCES node(id));''')
    c.execute('''CREATE TABLE if not exists graph (
                id integer primary key,	name text);''')


# create CRUD functions with parameters for values



create_tables()

conn.commit()  # save to the database
conn.close()   # close the database

