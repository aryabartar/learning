CREATE TABLE sales(
    name VARCHAR(256),
    color VARCHAR(256),
    size VARCHAR(256),
    quantity INT
    
);

INSERT INTO sales VALUES ('product1', 'Red', 'Small', 2);
INSERT INTO sales VALUES ('product1', 'Blue', 'small', 3);
INSERT INTO sales VALUES ('product1', 'Black', 'Small', 0);
INSERT INTO sales VALUES ('product2', 'Red', 'Small', 12);
INSERT INTO sales VALUES ('product2', 'Blue', 'Small', 1);
INSERT INTO sales VALUES ('product2', 'Black', 'Small', 2);
INSERT INTO sales VALUES ('product3', 'Red', 'Small', 3);
INSERT INTO sales VALUES ('product3', 'Blue', 'Small', 4);
INSERT INTO sales VALUES ('product3', 'Black', 'Small', 5);
INSERT INTO sales VALUES ('product1', 'Red', 'Medium', 2);
INSERT INTO sales VALUES ('product1', 'Blue', 'Medium', 3);
INSERT INTO sales VALUES ('product1', 'Black', 'Medium', 0);
INSERT INTO sales VALUES ('product2', 'Red', 'Medium', 12);
INSERT INTO sales VALUES ('product2', 'Blue', 'Medium', 1);
INSERT INTO sales VALUES ('product2', 'Black', 'Medium', 2);
INSERT INTO sales VALUES ('product3', 'Red', 'Medium', 3);
INSERT INTO sales VALUES ('product3', 'Blue', 'Medium', 4);
INSERT INTO sales VALUES ('product3', 'Black', 'Medium', 5);


SELECT name, color, size, sum(quantity) 
FROM sales
group by rollup (name, color, size)
;