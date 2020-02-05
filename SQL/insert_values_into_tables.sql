INSERT INTO graph (id, name)
VALUES (1, 'Test_Graph');

INSERT INTO node (id, name, graph_id)
VALUES (1, 'a', 1), (2, 'b', 1), (3, 'c', 1), (4, 'd', 1), (5, 'e', 1);

INSERT INTO edge (id, name, cost, node_start_id, node_end_id, graph_id)
VALUES (1, 'ab', 23, 1, 2, 1), (2, 'bc', 4, 2, 3, 1), (3, 'cd', 5, 3, 4, 1), (4, 'de', 100, 4, 5, 1), (5, 'ea', 45, 5, 1, 1);

-- Display -> graph.name , node_start.name, node_end.name, edge.cost
SELECT graph.name AS graph_name, 
node_start.name AS node_start_name, 
node_end.name AS node_end_name, 
edge.cost AS edge_cost
FROM edge
JOIN graph
ON edge.graph_id = graph.id
JOIN node AS node_start
ON edge.node_start_id = node_start.id
JOIN node AS node_end
ON edge.node_end_id = node_end.id;