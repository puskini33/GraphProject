INSERT INTO graph (id, name)
VALUES (1, 'Test_Graph');

INSERT INTO node (id, name, x_coord, y_coord, graph_id)
VALUES (1, 'a', 123, 156, 1), (2, 'b', 136, 190, 1), (3, 'c', 234, 456, 1), (4, 'd', 234, 322, 1), (5, 'e', 190, 234, 1);

INSERT INTO edge (id, name, cost, node_start_id, node_end_id, graph_id)
VALUES (1, 'ab', 23, 1, 2, 1), (2, 'bc', 4, 2, 3, 1), (3, 'cd', 5, 3, 4, 1), (4, 'de', 100, 4, 5, 1), (5, 'ea', 45, 5, 1, 1);
