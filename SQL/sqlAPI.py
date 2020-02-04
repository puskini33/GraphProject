import sqlite3
conn = sqlite3.connect("E:\PYTHON\code\GraphProject\SQL\graph.db")

c = conn.cursor()


def create_tables():
    c.execute('''CREATE TABLE node
                (id integer primary key, arch1_id integer, arch2_id integer)''')
    c.execute('''CREATE TABLE arch
                (id integer primary key, length integer, nod1_id integer, nod2_id integer)''')
    c.execute('''CREATE TABLE graph
                (id integer primary key)''')
    c.execute('''CREATE TABLE graph_node_arch
                (id integer primary key, graph_id integer, node_id integer)''')


conn.commit()
conn.close()

