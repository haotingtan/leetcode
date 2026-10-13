# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT customerID
    FROM Orders o
    WHERE o.customerID = c.id
)