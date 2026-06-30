INSERT INTO Customers VALUES
(1,'Alice','alice@example.com','9876543210'),
(2,'Bob','bob@example.com','9876543211'),
(3,'Charlie','charlie@example.com','9876543212');

INSERT INTO Products VALUES
(101,'Laptop','Electronics',55000),
(102,'Mouse','Electronics',800),
(103,'Keyboard','Electronics',1500);

INSERT INTO Orders VALUES
(1001,1,'2026-06-25'),
(1002,2,'2026-06-26');

INSERT INTO OrderItems VALUES
(1,1001,101,1),
(2,1001,102,2),
(3,1002,103,1);

INSERT INTO Payments VALUES
(1,1001,'UPI',56600),
(2,1002,'Card',1500);