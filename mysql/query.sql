-- DELIMITER //
-- CREATE FUNCTION dept_count2 (dept_name VARCHAR(20)) 
-- RETURNS INT 
-- BEGIN
--     DECLARE temp INT;
--     SELECT * 
--     FROM instructor
--     RETURN 12;
-- END //
-- DELIMITER ;


DELIMITER //
CREATE FUNCTION func4 (dept_name VARCHAR(20), ID INT) RETURNS INT
  BEGIN
  	DECLARE tt INT;	
    DECLARE tt1 INT;
    SELECT count(*) INTO tt1
    FROM department
    WHERE department.dept_name=dept_name; 
    SELECT count(*) INTO tt
    FROM department
    WHERE department.dept_name=dept_name;
    RETURN tt;
  END //
DELIMITER ;


-- CREATE FUNCTION F_TEST(PID INT) RETURNS VARCHAR
-- BEGIN
-- /*DECLARE VALUES YOU MAY NEED, EXAMPLE:
--   DECLARE NOM_VAR1 DATATYPE [DEFAULT] VALUE;
--   */
--   DECLARE NAME_FOUND VARCHAR DEFAULT "";

--     SELECT name INTO NAME_FOUND FROM instructor WHERE ID = PID;
--   RETURN NAME_FOUND;
-- END;

-- CREATE FUNCTION hello(id INT) RETURNS VARCHAR(20)
-- RETURN 'FOO';