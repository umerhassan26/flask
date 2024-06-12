SELECT * FROM Customers WHERE CustomerID = 10;

SELECT * FROM Customers WHERE CustomerID > 10;

SELECT * FROM Customers WHERE CustomerID >= 10;

SELECT * FROM Customers WHERE CustomerID < 10;

SELECT * FROM Customers WHERE CustomerID <= 10;

SELECT * FROM Customers WHERE CustomerID <> 5;

SELECT * FROM Customers ORDER BY CustomerId DESC;

SELECT * FROM Customers ORDER BY City;

SELECT * FROM Customers WHERE Country = 'Germany' AND City = 'berlin';

SELECT * FROM Customers WHERE Country = 'Germany' OR City = 'berlin';

SELECT * FROM Customers WHERE NOT Country = 'Germany' ;

SELECT TOP 2 * FROM Customers ;

SELECT * FROM Customers WHERE Country IN ('Germany','UK','Sweden');

SELECT * FROM Customers LIMIT 10;

SELECT MAX(Price) FROM Products;

SELECT MIN(Price) FROM Products;

SELECT MIN(Price) AS min_price FROM Products;

SELECT COUNT(ProductName) FROM Products;

SELECT COUNT(ProductName) AS Total_products FROM Products;

SELECT sum(Price) FROM Products;

SELECT AVG(Price) FROM Products;

SELECT * FROM Products WHERE ProductID BETWEEN 10 AND 25 ;

SELECT * FROM Customers WHERE CustomerName LIKE 'a%';

SELECT * FROM Customers WHERE Country LIKE 'G__m__y';