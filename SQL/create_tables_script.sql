CREATE TABLE if not exists node (
	id integer primary key,
	name text);


CREATE TABLE if not exists edge (
            id integer primary key, 
	name text
	length integer, 
	node_start integer, 
	node_end integer,
	FOREIGN KEY(node_start) REFERENCES node(id),
	FOREIGN KEY(node_end) REFERENCES node(id));


CREATE TABLE if not exists graph (
	id integer primary key,
	name text);

CREATE TABLE if not exists graph_node_arch (
	id integer primary key, 
	graph_id integer, 
	node_id integer,
	edge_id integer,
	FOREIGN KEY(graph_id) REFERENCES graph(id),
	FOREIGN KEY(node_id) REFERENCES node(id),
	FOREIGN KEY(edge_id) REFERENCES edge(id));