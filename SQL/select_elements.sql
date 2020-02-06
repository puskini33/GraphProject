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
ON edge.node_start_id = node_start.id
JOIN node AS node_end
ON edge.node_end_id = node_end.id;


-- With a select display only graph 1 with all it's nodes and edges
SELECT graph.name AS graph_name, node.name AS node_name, edge.name AS edge_name
FROM node
JOIN graph
ON node.graph_id = graph.id
JOIN edge
ON edge.node_start_id = node.id
WHERE graph.name = 'Test_Graph1';


-- display only node2 from first graph and all the edges that are connected to it
SELECT node.name AS node_name, 
edge.name AS edge_name,
graph.name AS graph_name
FROM node
JOIN graph
ON node.graph_id = graph.id
JOIN edge
ON edge.node_start_id = node.id
WHERE node.id = 2;