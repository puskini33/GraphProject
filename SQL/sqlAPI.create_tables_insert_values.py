import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'graph.db')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


conn = db_connect()  # connect to the database
c = conn.cursor()  # instantiate a cursor object


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


def insert_values_into_tables():
    c.execute('''INSERT INTO graph (id, name) VALUES (1, 'Test_Graph');''')
    c.execute('''INSERT INTO node (id, name, graph_id) 
                VALUES (1, 'a', 1), (2, 'b', 1), (3, 'c', 1), (4, 'd', 1), (5, 'e', 1)''')
    c.execute('''INSERT INTO edge (id, name, cost, node_start_id, node_end_id, graph_id) 
                VALUES (1, 'ab', 23, 1, 2, 1), (2, 'bc', 4, 2, 3, 1), (3, 'cd', 5, 3, 4, 1), 
                (4, 'de', 100, 4, 5, 1), (5, 'ea', 45, 5, 1, 1);''')


create_tables()
insert_values_into_tables()
conn.commit()  # save to the database
conn.close()   # close the database

