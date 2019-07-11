This is a placeholder for various DB and DB migration testing scripts and some resources on this topic. 


Database Testing Checklist:

1. Data Integrity:

1.	To check whether the data is well arranged and logically placed in the database.
2.	Check if data is committed to database only when the operation is successfully completed
3.	Check if input data is not truncated while saving. Field length shown to user on page and in database schema should be same
4.	To evaluate the consistency of the data.
5.	To ensure that the data values are being placed correctly in their respective tables or columns.
6.	Verifying and validating the correctness & integrity of the data, stored in the database.
7.	To locate and get rid of redundant and useless data.
8.	Whether data reflecting at front-end and stored at back-end is correctly synchronised and updated.
9.	Whether the data or values, fetched from the front-end is being correctly and successfully getting stored at back-end.
10.	To check, if no data valued is present outside the table.
11.	Whether data outside the table, could be modified or not.
12.	Whether database is able to store or export blank or null value.
13.	Checking the compatibility of the data with the software and hardware, especially the outdated or obsolete one.
14.	Verify the data encryption (if any).
15.	Validate the DB behavior of any case of service failures (recovery, error handling Etc.).
16.	Check that each data item is located under the relevant column.
17.	Is there any irrelevant data in the software dedicated tables?
18.	Check that each table contains the relevant data.
19.	Try to insert invalid database values.

2. Stored Procedures:

1.	Whether the execution of stored procedures or functions are outputting correct and reliable result sets.
2.	Manual execution of the stored procedures, updates the database tables.
3.	To ensure that correct and standard coding conventions is adopted and followed for the stored procedures.
4.	Does input data is able to encompass all sort of loops and conditions.
5.	To ensure proper and standard error and exception handing mechanism.
6.	Verifying and validating the attributes and parameters associated with each procedure.
7.	Evaluating the working or execution of all stored procedures in the presence of blank or empty database.
8.	Validate that the data the affected by the procedure is changed as expected.
9.	Validate that all procedures are triggered when they supposed to run.
10.	Validate that all the conditions receive an appropriate date inputs.
11.	Validate that all procedures are created with the relevant code.
12.	Is there an appropriate error handling for a failed procedure?
13.	Validate that all the loops receive an appropriate date inputs.
14.	Validate the procedure's parameters (types, names, etc.).
15.	Test the SP while executing the code manually.
16.	Validate important code with SQL profiler.
17.	Validate that all procedures names
18.	Run tests with missing parameters.

3. Triggers:

1.	Similar to stored procedures, adoption and implementation of correct and standing conventions for triggers, by the developers is being evaluated.
2.	To ensure that the execution of a trigger updates the data in the database, successfully.
3.	If the triggers are being executed for the DML transaction.
4.	Checking the execution of a trigger in the event of addition or deletion or update in the data.
5.	To check whether the execution of a stored procedure is followed by the firing of a trigger.

4.Field Validation:

1.	Whether the database system is allowing the entry and storage of null data value or not.
2.	Check numeric fields with minimum, maximum, and float values
3.	Check that all columns are set with the relevant data type (Bigint, int, string Etc.)
4.	Check that all data is logically organized in the relevant DB tables.
5.	To ensure the appropriate and sufficient length of each field to import and accommodate respective data value of varying range.
6.	Verifying and validating the data type for each field against specified and given specifications.
7.	To check whether all identical fields have similar name throughout the database and tables.
8.	To locate any computed field(if any) in the database and tables.
9.	Check numeric fields with negative values (for both acceptance and non-acceptance)
10.	Check if radio button and dropdown list options are saved correctly in database
11.	Check if database fields are designed with correct data type and data length
12.	Input field leading and trailing spaces should be truncated before committing data to database
13.	Check values for table audit columns (like createddate, createdby, updatedate, updatedby, isdeleted, deleteddate, deletedby etc.) are populated properly
14.	Validate that “Allow Null” condition is not allowed in a place that result a software failure
15.	Validate that “Allow Null” condition is set when you need to allow it.
16.	Validate that mandatory fields are created, this issue is very important when you work with multiple tables that depends on each other.

5. Constraints:

1.	Whether the primary key and the foreign key constraints is specified and created for each table or not.
2.	Proper and valid referencing of foreign key between the database table has been done or not.
3.	Whether the null value is being accepted as a valid input both for the primary and the foreign key.
4.	To ensure primary key data type of a table is same as to that of corresponding foreign key of other table.

6. Transactions:

1.	To check out whether the correct transaction is being executed or not.
2.	To ensure that the data is being committed on the successful execution of the transaction.
3.	To check that if the data is rollback in the event of transaction failure along with the involvement of multiple variants of database.
4.	To check whether the transactions are fulfilling the ACID (Atomicity, Consistency, Isolation, Durability) properties.
5.	To ensure that all the transactions is being called upon & executed by the TRANSACTION Keyword.

7. Indexes

1.	To check the presence of clustered and non-clustered indexes to fulfil the necessary need for a given table as per the business requirements.
2.	To evaluate the size and length of the indexes.
3.	Naming conventions for the indexes.
4.	Index names should be given as per the standards e.g. IND_<Tablename>_<ColumnName>
5.	Tables should have primary key column
6.	Null values should not be allowed for Primary key column
7.	Check if all table constraints like Primary key, Foreign key etc. are implemented correctly
8.	Validate that all indexes are created when it can increase the system performance.

8.Performance

1.	Database performance in terms of time taken, for the execution of lesser number of queries for small set of records.
2.	Database performance in terms of time taken, for the execution of queries pertaining to comparatively large set of records.
3.	Performance of database in the event of simultaneous and concurrent access to data by multiple users.
4.	To verify and validate the normalization of the database.
5.	Time in retrieving or updating the data or records.
9. Security
1.	Verifying & validating the access and no access to database by authorized and non-authorized users, respectively.
2.	Verifying & validating the different permission granted to each different role, assigned for the database.
3.	Other security aspects comprises of evaluation of following features:
4.	Authentication.
5.	Confidentiality.
6.	Availability.
7.	Integrity.
8.	Resilience.

10.  Miscellaneous

1.	Data Redundancy
2.	Data Duplication
3.	Data Migration
4.	Database timely backup & recovery management and plan. (For every database add/update operation log should be added)
5.	Database logical names should be given according to database name (again this is not standard but helpful for DB maintenance)
6.	Database name should be given as per the application type i.e. test, UAT, sandbox, live (though this is not a standard it is helpful for database maintenance)
7.	Stored procedures should not be named with prefix “sp_”

11.	Database system-level tests

1.	Try to work when the storage is ‘0’ and the e database is in running state.
2.	Perform your tests on different versions (SQL 2005, 2008, 2012 etc.).
3.	Validate the software security model (User roles, permissions etc.).
4.	Validate the connection strings against SQL/Win authentications.
5.	Validate data migrations (Different Database, Cluster, etc.).
6.	Validate the behavior of the system against SQL injections.
7.	Validate date to DB when the server is loaded.
8.	Try to work when the database server is down.
9.	Try to work with difference instance.
10.	Validate restore and backup plans.

12.	Database and software integration (Client, web Etc.) 

1.	Validate that the user data is saved when the user “Apply” or “Submit” the changes.
2.	Try to insert “NULL” values on fields that doesn’t supposed to receive it.
3.	Validate that the user receives the current result when pulling data.
4.	Validate that transaction the data type boundaries (Minima Etc.)
5.	Validate that empty spaces are not committed to the database.
6.	Validate that the values displayed based on the database data.
7.	Try to insert UNICODE on Unicode character strings.
8.	Try to insert values that exceed the field boundaries.
9.	Validate that transactions the negative data values.
10.	Insert invalid date format on Date and time fields.
