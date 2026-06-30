CREATE VIEW CustomerOrders AS

SELECT
    Customers.customer_name,
    Orders.order_id,
    Orders.order_date

FROM Customers

INNER JOIN Orders
ON Customers.customer_id = Orders.customer_id;