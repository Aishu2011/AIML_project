CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
);

CREATE TABLE OrderItems (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id)
        REFERENCES Orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES Products(product_id)
);

CREATE TABLE Payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method TEXT,
    amount REAL,
    FOREIGN KEY (order_id)
        REFERENCES Orders(order_id)
);