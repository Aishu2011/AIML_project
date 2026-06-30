-- 1. SELECT
SELECT * FROM Customers;

-- 2. WHERE
SELECT * FROM Products
WHERE price > 1000;

-- 3. ORDER BY
SELECT * FROM Products
ORDER BY price DESC;

-- 4. GROUP BY
SELECT payment_method,
       SUM(amount) AS total_amount
FROM Payments
GROUP BY payment_method;

-- 5. INNER JOIN
SELECT
    Customers.customer_name,
    Orders.order_id,
    Orders.order_date
FROM Customers
INNER JOIN Orders
ON Customers.customer_id = Orders.customer_id;

-- 6. LEFT JOIN
SELECT
    Customers.customer_name,
    Orders.order_id
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;

-- 8. UNION

SELECT customer_name AS Name
FROM Customers

UNION

SELECT product_name
FROM Products;

-- 9. CASE

SELECT
    product_name,
    price,
    CASE
        WHEN price >= 50000 THEN 'Premium'
        WHEN price >= 1000 THEN 'Standard'
        ELSE 'Budget'
    END AS Category
FROM Products;

-- 10. Subquery

SELECT *
FROM Products
WHERE price >
(
    SELECT AVG(price)
    FROM Products
);

-- 11. CTE

WITH ProductAverage AS
(
    SELECT AVG(price) AS avg_price
    FROM Products
)

SELECT *
FROM Products
WHERE price >
(
    SELECT avg_price
    FROM ProductAverage
);

-- 12. ROW_NUMBER()

SELECT
    product_name,
    price,
    ROW_NUMBER() OVER
    (
        ORDER BY price DESC
    ) AS row_num
FROM Products;

-- 13. RANK()

SELECT
    product_name,
    price,
    RANK() OVER
    (
        ORDER BY price DESC
    ) AS ranking
FROM Products;

-- 14. DENSE_RANK()

SELECT
    product_name,
    price,
    DENSE_RANK() OVER
    (
        ORDER BY price DESC
    ) AS dense_rank
FROM Products;

-- 15. LAG()

SELECT
    order_date,
    amount,
    LAG(amount) OVER
    (
        ORDER BY order_date
    ) AS previous_amount
FROM Orders
JOIN Payments
ON Orders.order_id = Payments.order_id;

-- 16. LEAD()

SELECT
    order_date,
    amount,
    LEAD(amount) OVER
    (
        ORDER BY order_date
    ) AS next_amount
FROM Orders
JOIN Payments
ON Orders.order_id = Payments.order_id;