CREATE TABLE customer(
    c_id VARCHAR(5) PRIMARY KEY,
    c_name VARCHAR(128),
    c_city VARCHAR(128),
    c_street VARCHAR(128)
)
;

CREATE TABLE branch(
    b_id VARCHAR(5) PRIMARY KEY,
    b_name VARCHAR(128) UNIQUE, 
    b_city VARCHAR(128)
)
;

CREATE TABLE deposit(
    c_id VARCHAR(5),
    b_id VARCHAR(5),
    a_id CHAR(5),
    balance NUMERIC(10,0),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (a_id),
    FOREIGN KEY (c_id) REFERENCES customer(c_id),
    FOREIGN KEY (b_id) REFERENCES branch(b_id)
)
;

CREATE TABLE transfer(
    a_id CHAR(5),
    c_id VARCHAR(5),
    amount NUMERIC(10,0),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (c_id) REFERENCES customer(c_id),
    FOREIGN KEY (a_id) REFERENCES deposit(a_id)
)
;

CREATE TABLE transaction(
    a_id CHAR(5),
    type VARCHAR(120) CHECK (type="deposit" or type="withdraw"),
    amount NUMERIC(10,0),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (a_id) REFERENCES deposit(a_id)
)
;