-- Display for each edge its nodes and the graph it belongs to
SELECT 
edge.name AS edge_name,
node_start.name AS node_start_name, 
node_end.name AS node_end_name,
graph.name AS graph_name
FROM edge
JOIN graph
ON edge.graph_id = graph.id
JOIN node AS node_start
ON edge.start_node_id = node_start.id
JOIN node AS node_end
ON edge.end_node_id = node_end.id;


-- With a select display only graph 1 with all it's nodes and edges
SELECT graph.name AS graph_name, node.name AS node_name, edge.name AS edge_name
FROM node
JOIN graph
ON node.graph_id = graph.id
JOIN edge
ON edge.start_node_id = node.id
WHERE graph.name = 'Test_Graph';


-- display only node2 from first graph and all the edges that are connected to it
SELECT node.name AS node_name, 
edge.name AS edge_name,
graph.name AS graph_name
FROM node
JOIN graph
ON node.graph_id = graph.id
JOIN edge
ON edge.start_node_id = node.id
WHERE node.id = 79;

-- Display -> graph.name , node_start.name, node_end.name, edge.cost
SELECT graph.name AS graph_name,
node_start.name AS node_start_name,
node_end.name AS node_end_name,
edge.cost AS edge_cost
FROM edge
JOIN graph
ON edge.graph_id = graph.id
JOIN node AS node_start
ON edge.start_node_id = node_start.id
JOIN node AS node_end
ON edge.end_node_id = node_end.id;


-- Display coordinates of edges
SELECT node.node_x_coord, node.node_y_coord
FROM edge
JOIN node
ON edge.start_node_id = node.id
;

-- Display all edges from a graph
SELECT edge.id, edge.name, edge.cost, edge.start_node_id, edge.end_node_id, edge.graph_id
FROM edge
JOIN node
ON edge.start_node_id = node.id OR edge.end_node_id = node.id
JOIN graph
ON edge.graph_id = graph.id
WHERE graph.id = 90;