# Explore fundamental relational data concepts

## Understanding relational data

## Understand normalization

- Normalization is a term used by database professionals for a schema design process that minimizes data duplication and enforces data integrity.

- While there are many complex rules that define the process of refactoring data into various levels (or forms) of normalization, a simple definition for practical purposes is:

  1. Separate each entity into its own table.

  2. Separate each discrete attribute into its own column.

  3. Uniquely identify each entity instance (row) using a primary key.

  4. Use foreign key columns to link related entities.

- Typically, a relational database management system (RDBMS) can enforce referential integrity to ensure that a value entered into a foreign key field has an existing corresponding primary key in the related table – for example, preventing orders for non-existent customers.

## Explore SQL

- Although these SQL statements are part of the SQL standard, many database management systems also have their own additional proprietary extensions to handle the specifics of that database management system.

- Some popular dialects of SQL include:

  - Transact-SQL (T-SQL). This version of SQL is used by Microsoft SQL Server and Azure SQL services.

  - pgSQL. This is the dialect, with extensions implemented in PostgreSQL.

  - PL/SQL. This is the dialect used by Oracle. PL/SQL stands for Procedural Language/SQL.

## Describe database objects

### What is a view?
- A view is a virtual table based on the results of **SELECT** query. We can think of a view as a window on specified rows in one or more underlying tables.
```sql
CREATE VIEW Deliveries
AS
SELECT o.OrderNo, o.OrderDate,
       c.FirstName, c.LastName, c.Address, c.City
FROM Order AS o JOIN Customer AS c
ON o.Customer = c.ID;

SELECT OrderNo, OrderDate, LastName, Address
FROM Deliveries
WHERE City = 'Seattle';
```

### What is a stored procedure?
- A stored procedure defines SQL statements that can be run on command. Stored procedures are used to encapsulate programmatic logic in a database for actions that applications need to perform when working with data.
```sql
CREATE PROCEDURE RenameProduct
	@ProductID INT,
	@NewName VARCHAR(20)
AS
UPDATE Product
SET Name = @NewName
WHERE ID = @ProductID;
```

```sql
EXEC RenameProduct 201, 'Spanner';
```

### What is an index?
- An index helps you search for data in a table.
- When you create an index in a database, you specify a column from the table, and the index contains a copy of this data in a sorted order, with pointers to the corresponding rows in the table. When the user runs a query that specifies this column in the WHERE clause, the database management system can use this index to fetch the data more quickly than if it had to scan through the entire table row by row.

```sql
CREATE INDEX idx_ProductName
ON Product(Name);
```
- An index consumes storage space, and each time you insert, update, or delete data in a table, the indexes for that table must be maintained. This additional work can slow down insert, update, and delete operations. You must strike a balance between having indexes that speed up your queries versus the cost of performing other operations.

# Explore relational data in Azure
## [Describe Azure SQL services and capabilities](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)

## [Describe Azure services for open-source databases](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)
