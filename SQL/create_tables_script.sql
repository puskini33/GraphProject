CREATE TABLE if not exists node (
	id integer primary key,
	name text,
	graph_id integer,
	FOREIGN KEY(graph_id) REFERENCES graph(id));


CREATE TABLE if not exists edge (
       id integer primary key, 
	name text,
	cost integer, 
	start_node_id integer,
	end_node_id integer,
	graph_id integer,
	FOREIGN KEY(graph_id) REFERENCES graph(id),
	FOREIGN KEY(start_node_id) REFERENCES node(id),
	FOREIGN KEY(end_node_id) REFERENCES node(id));


CREATE TABLE if not exists graph (
	id integer primary key,
	name text);