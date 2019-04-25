CREATE TABLE takes(
    ID VARCHAR(5),
    course_id VARCHAR(8),
    sec_id VARCHAR(8),
    semester VARCHAR(6), 
    year NUMERIC(4,0),
    grade VARCHAR(2), 
    PRIMARY KEY (ID, course_id, sec_id, semester, year),
    FOREIGN KEY (ID) REFERENCES student(ID),
    FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES student(course_id, sec_id, semester, year)

)
;