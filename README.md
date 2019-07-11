This is a placeholder for various DB and DB migration testing scripts and some resources on this topic. 


<b><p>Database Testing Checklist:</p></b>

<b>1. Data Integrity:</b>
<ul>
	<li>1.	To check whether the data is well arranged and logically placed in the database.</li>
	<li>2.	Check if data is committed to database only when the operation is successfully completed</li>
	<li>3.	Check if input data is not truncated while saving. Field length shown to user on page and in database schema should be same</li>
	<li>4.	To evaluate the consistency of the data.</li>
	<li>5.	To ensure that the data values are being placed correctly in their respective tables or columns.</li>
	<li>6.	Verifying and validating the correctness & integrity of the data, stored in the database.</li>
	<li>7.	To locate and get rid of redundant and useless data.</li>
	<li>8.	Whether data reflecting at front-end and stored at back-end is correctly synchronised and updated.</li>
	<li>9.	Whether the data or values, fetched from the front-end is being correctly and successfully getting stored at back-end.</li>
	<li>10.	To check, if no data valued is present outside the table.</li>
	<li>11.	Whether data outside the table, could be modified or not.</li>
	<li>12.	Whether database is able to store or export blank or null value.</li>
	<li>13.	Checking the compatibility of the data with the software and hardware, especially the outdated or obsolete one.</li>
	<li>14.	Verify the data encryption (if any).</li>
	<li>15.	Validate the DB behavior of any case of service failures (recovery, error handling Etc.).</li>
	<li>16.	Check that each data item is located under the relevant column.</li>
	<li>17.	Is there any irrelevant data in the software dedicated tables?</li>
	<li>18.	Check that each table contains the relevant data.</li>
	<li>19.	Try to insert invalid database values.</li>
	<li></li>	
</ul>

<b>2. Stored Procedures:</b>
<ul>
	<li>1.	Whether the execution of stored procedures or functions are outputting correct and reliable result sets.</li>
	<li>2.	Manual execution of the stored procedures, updates the database tables.</li>
	<li>3.	To ensure that correct and standard coding conventions is adopted and followed for the stored procedures.</li>
	<li>4.	Does input data is able to encompass all sort of loops and conditions.</li>
	<li>5.	To ensure proper and standard error and exception handing mechanism.</li>
	<li>6.	Verifying and validating the attributes and parameters associated with each procedure.</li>
	<li>7.	Evaluating the working or execution of all stored procedures in the presence of blank or empty database.</li>
	<li>8.	Validate that the data the affected by the procedure is changed as expected.</li>
	<li>9.	Validate that all procedures are triggered when they supposed to run.</li>
	<li>10.	Validate that all the conditions receive an appropriate date inputs.</li>
	<li>11.	Validate that all procedures are created with the relevant code.</li>
	<li>12.	Is there an appropriate error handling for a failed procedure?</li>
	<li>13.	Validate that all the loops receive an appropriate date inputs.</li>
	<li>14.	Validate the procedure's parameters (types, names, etc.).</li>
	<li>15.	Test the SP while executing the code manually.</li>
	<li>16.	Validate important code with SQL profiler.</li>
	<li>17.	Validate that all procedures names</li>
	<li>18.	Run tests with missing parameters.</li>
	<li>19.	Stored procedures should not be named with prefix “sp_”</li>
</ul>

<b>3. Triggers:</b>

<ul>
	<li>1.	Similar to stored procedures, adoption and implementation of correct and standing conventions for triggers, by the developers is being evaluated.</li>
	<li>2.	To ensure that the execution of a trigger updates the data in the database, successfully.</li>
	<li>3.	If the triggers are being executed for the DML transaction.</li>
	<li>4.	Checking the execution of a trigger in the event of addition or deletion or update in the data.</li>
	<li>5.	To check whether the execution of a stored procedure is followed by the firing of a trigger.</li>

</ul>

<b>4.Field Validation:</b>


<ul>
	<li>1.	Whether the database system is allowing the entry and storage of null data value or not.</li>
	<li>2.	Check numeric fields with minimum, maximum, and float values</li>
	<li>3.	Check that all columns are set with the relevant data type (Bigint, int, string Etc.)</li>
	<li>4.	Check that all data is logically organized in the relevant DB tables.</li>
	<li>5.	To ensure the appropriate and sufficient length of each field to import and accommodate respective data value of varying range.</li>
	<li>5.	To ensure the appropriate and sufficient length of each field to import and accommodate respective data value of varying range.</li>
	<li>6.	Verifying and validating the data type for each field against specified and given specifications.</li>
	<li>7.	To check whether all identical fields have similar name throughout the database and tables.</li>
	<li>8.	To locate any computed field(if any) in the database and tables.</li>
	<li>9.	Check numeric fields with negative values (for both acceptance and non-acceptance)</li>
	<li>10.	Check if radio button and dropdown list options are saved correctly in database</li>
	<li>11.	Check if database fields are designed with correct data type and data length</li>
	<li>12.	Input field leading and trailing spaces should be truncated before committing data to database</li>
	<li>13.	Check values for table audit columns (like createddate, createdby, updatedate, updatedby, isdeleted, deleteddate, deletedby etc.) are populated properly</li>
	<li>14.	Validate that “Allow Null” condition is not allowed in a place that result a software failure</li>
	<li>15.	Validate that “Allow Null” condition is set when you need to allow it.</li>
	<li>16.	Validate that mandatory fields are created, this issue is very important when you work with multiple tables that depends on each other.</li>
</ul>

<b>5. Constraints:</b>


<ul>
	<li>1.	Whether the primary key and the foreign key constraints is specified and created for each table or not.</li>
	<li>2.	Proper and valid referencing of foreign key between the database table has been done or not.</li>
	<li>3.	Whether the null value is being accepted as a valid input both for the primary and the foreign key.</li>
	<li>4.	To ensure primary key data type of a table is same as to that of corresponding foreign key of other table.</li>			
</ul>

<b>6. Transactions:</b>


<ul>
	<li>1.	To check out whether the correct transaction is being executed or not.</li>
	<li>2.	To ensure that the data is being committed on the successful execution of the transaction.</li>
	<li>3.	To check that if the data is rollback in the event of transaction failure along with the involvement of multiple variants of database.</li>
	<li>4.	To check whether the transactions are fulfilling the ACID (Atomicity, Consistency, Isolation, Durability) properties.</li>
	<li>5.	To ensure that all the transactions is being called upon & executed by the TRANSACTION Keyword.</li>
</ul>

<b>7. Indexes</b>


<ul>
	<li>1.	To check the presence of clustered and non-clustered indexes to fulfil the necessary need for a given table as per the business requirements.</li>
	<li>2.	To evaluate the size and length of the indexes.</li>
	<li>3.	Naming conventions for the indexes.</li>
	<li>4.	Index names should be given as per the standards e.g. IND_<Tablename>_<ColumnName></li>
	<li>5.	Tables should have primary key column</li>
	<li>6.	Null values should not be allowed for Primary key column</li>
	<li>7.	Check if all table constraints like Primary key, Foreign key etc. are implemented correctly</li>
	<li>8.	Validate that all indexes are created when it can increase the system performance.</li>
</ul>

<b>8.Performance</b>


<ul>
	<li>1.	Database performance in terms of time taken, for the execution of lesser number of queries for small set of records.</li>
	<li>2.	Database performance in terms of time taken, for the execution of queries pertaining to comparatively large set of records.</li>
	<li>3.	Performance of database in the event of simultaneous and concurrent access to data by multiple users.</li>
	<li>4.	To verify and validate the normalization of the database.</li>
	<li>5.	Time in retrieving or updating the data or records.</li>
</ul>


<b>9. Security</b>

<ul>
	<li>1.	Verifying & validating the access and no access to database by authorized and non-authorized users, respectively.</li>
	<li>2.	Verifying & validating the different permission granted to each different role, assigned for the database.</li>	
	<li>3.	Authentication.</li>
	<li>4.	Confidentiality.</li>
	<li>5.	Availability.</li>
	<li>6.	Integrity.</li>
	<li>7.	Resilience.</li>
	<li></li>
	<li></li>							
</ul>


<b>10.  Miscellaneous</b>

<ul>
	<li>1.	Data Redundancy</li>
	<li>2.	Data Duplication</li>
	<li>3.	Data Migration</li>
	<li>4.	Database timely backup & recovery management and plan. (For every database add/update operation log should be added)</li>
	<li>5.	Database logical names should be given according to database name (again this is not standard but helpful for DB maintenance)</li>
	<li>6.	Database name should be given as per the application type i.e. test, UAT, sandbox, live (though this is not a standard it is helpful for database maintenance)</li>

</ul>

<b>11.	Database system-level tests</b>

<ul>
	<li>1.	Try to work when the storage is ‘0’ and the e database is in running state.</li>
	<li>2.	Perform your tests on different versions (SQL 2005, 2008, 2012 etc.).</li>
	<li>3.	Validate the software security model (User roles, permissions etc.).</li>
	<li>4.	Validate the connection strings against SQL/Win authentications.</li>
	<li>5.	Validate data migrations (Different Database, Cluster, etc.).</li>
	<li>6.	Validate the behavior of the system against SQL injections.</li>
	<li>7.	Validate date to DB when the server is loaded.</li>
	<li>8.	Try to work when the database server is down.</li>
	<li>9.	Try to work with difference instance.</li>
	<li>10.	Validate restore and backup plans.</li>
</ul>

<b>12.	Database and software integration (Client, web Etc.)</b> 

<ul>
	<li>1.	Validate that the user data is saved when the user “Apply” or “Submit” the changes.</li>
	<li>2.	Try to insert “NULL” values on fields that doesn’t supposed to receive it.</li>
	<li>3.	Validate that the user receives the current result when pulling data.</li>
	<li>4.	Validate that transaction the data type boundaries (Minima Etc.)</li>
	<li>5.	Validate that empty spaces are not committed to the database</li>
	<li>6.	Validate that the values displayed based on the database data.</li>
	<li>7.	Try to insert UNICODE on Unicode character strings.</li>
	<li>8.	Try to insert values that exceed the field boundaries.</li>
	<li>9.	Validate that transactions the negative data values.</li>
	<li>10.	Insert invalid date format on Date and time fields.</li>
</ul>





