INSERT INTO customer VALUES ( 'cdi00' , 'customer name0' , 'Tehran' , 'Enghelab');
INSERT INTO customer VALUES ( 'cdi01' , 'customer name1' , 'Ardabil' , 'Valiasr');
INSERT INTO customer VALUES ( 'cdi02' , 'customer name2' , 'Tehran' , 'Valiasr');
INSERT INTO customer VALUES ( 'cdi03' , 'customer name3' , 'Ardabil' , 'Valiasr');
INSERT INTO customer VALUES ( 'cdi04' , 'customer name4' , 'Ardabil' , 'Enghelab');
INSERT INTO customer VALUES ( 'cdi05' , 'customer name5' , 'Ardabil' , 'Valiasr');
INSERT INTO customer VALUES ( 'cdi06' , 'customer name6' , 'Tehran' , 'Valiasr');
INSERT INTO customer VALUES ( 'cdi07' , 'customer name7' , 'Tehran' , 'Enghelab');
INSERT INTO customer VALUES ( 'cdi08' , 'customer name8' , 'Ardabil' , 'Valiasr');

INSERT INTO branch VALUES ( 'bran0' , 'branch name0' , 'Tehran');
INSERT INTO branch VALUES ( 'bran1' , 'branch name1' , 'Ardabil');
INSERT INTO branch VALUES ( 'bran2' , 'branch name2' , 'Tehran');
INSERT INTO branch VALUES ( 'bran3' , 'branch name3' , 'Ardabil');

INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi00", "bran2","00001", "560");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi01", "bran1", "00002","1");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi01", "bran3", "00003","52");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi03", "bran2", "00004","120");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi04", "bran1", "00005","534");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi04", "bran2", "00006","200");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi04", "bran3", "00007","100");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi05", "bran1", "00008","99");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi07", "bran2", "00009",0);
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi08", "bran0", "00010",800);
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi08", "bran1", "00011","4");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi08", "bran2", "00012","100");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi08", "bran3", "00013","60");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi08", "bran4", "00014","50");
INSERT INTO deposit(c_id,b_id, a_id ,balance) VALUES ("cdi09", "bran0", "00015","10");

