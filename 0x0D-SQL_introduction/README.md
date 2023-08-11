0x0D. SQL - Introduction

In this project, i learnt about databases, what they are for and how to properly manage them.

More Info
Comments for your SQL file:

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

Use “container-on-demand” to run MySQL
In the container, credentials are root/root

	Ask for container Ubuntu 20.04
	Connect via SSH
	OR connect via the Web terminal
	In the container, you should start MySQL before playing with it:

$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$

In the container, credentials are root/root

File: 0-list_databases.sql: Write a script that lists all databases of your MySQL server.

File: 1-create_database_if_missing.sql: Write a script that creates the database hbtn_0c_0 in your MySQL server.
	If the database hbtn_0c_0 already exists, your script should not fail
	You are not allowed to use the SELECT or SHOW statements

File: 2-remove_database.sql: Write a script that deletes the database hbtn_0c_0 in your MySQL server.
	If the database hbtn_0c_0 doesn’t exist, your script should not fail
	You are not allowed to use the SELECT or SHOW statements

File: 3-list_tables.sql: Write a script that lists all the tables of a database in your MySQL server.
	The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

File: 4-first_table.sql: Write a script that creates a table called first_table in the current database in your MySQL server.
	first_table description:
		id INT
		name VARCHAR(256)
	The database name will be passed as an argument of the mysql command
	If the table first_table already exists, your script should not fail
	You are not allowed to use the SELECT or SHOW statements

File: 5-full_table.sql: Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
	The database name will be passed as an argument of the mysql command
	You are not allowed to use the DESCRIBE or EXPLAIN statements

File: 6-list_values.sql: Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
	All fields should be printed
	The database name will be passed as an argument of the mysql command

File: 7-insert_value.sql: Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
	New row:
		id = 89
		name = Best School
	The database name will be passed as an argument of the mysql command

File: 8-count_89.sql: Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
	The database name will be passed as an argument of the mysql command

File: 9-full_creation.sql: Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
	second_table description:
		id INT
		name VARCHAR(256)
		score INT
	The database name will be passed as an argument to the mysql command
	If the table second_table already exists, your script should not fail
	You are not allowed to use the SELECT and SHOW statements
	Your script should create these records
		id = 1, name = “John”, score = 10
		id = 2, name = “Alex”, score = 3
		id = 3, name = “Bob”, score = 14
		id = 4, name = “George”, score = 8

File: 10-top_score.sql: Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
	Results should display both the score and the name (in this order)
	Records should be ordered by score (top first)
	The database name will be passed as an argument of the mysql command

File: 11-best_score.sql: Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
	Results should display both the score and the name (in this order)
	Records should be ordered by score (top first)
	The database name will be passed as an argument of the mysql command

File: 12-no_cheating.sql: Write a script that updates the score of Bob to 10 in the table second_table.
	You are not allowed to use Bob’s id value, only the name field
	The database name will be passed as an argument of the mysql command

File: 13-change_class.sql: Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
	The database name will be passed as an argument of the mysql command

File: 14-average.sql: Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
	The result column name should be average
	The database name will be passed as an argument of the mysql command

File: 15-groups.sql: Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
	The result should display:
		the score
		the number of records for this score with the label number
	The list should be sorted by the number of records (descending)
	The database name will be passed as an argument to the mysql command

File: 16-no_link.sql: Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

	Don’t list rows without a name value
	Results should display the score and the name (in this order)
	Records should be listed by descending score
	The database name will be passed as an argument to the mysql command
	In this example, new data have been added to the table second_table.
