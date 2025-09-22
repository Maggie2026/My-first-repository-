-- SCHEMA + SAMPLE DATA

-- PAYMENTS table
CREATE TABLE payments (
    checkNumber VARCHAR(50),
    paymentDate DATE,
    amount DECIMAL(10,2)
);

INSERT INTO payments VALUES
('CHK101', '2025-01-05', 1500.00),
('CHK102', '2025-01-12', 2300.50),
('CHK103', '2025-02-01', 500.75);

-- ORDERS table
CREATE TABLE orders (
    orderNumber INT,
    orderDate DATE,
    requiredDate DATE,
    status VARCHAR(50)
);

INSERT INTO orders VALUES
(1001, '2025-01-10', '2025-01-20', 'In Process'),
(1002, '2025-01-12', '2025-01-22', 'Shipped'),
(1003, '2025-01-15', '2025-01-25', 'In Process');

-- EMPLOYEES table
CREATE TABLE employees (
    employeeNumber INT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    jobTitle VARCHAR(50)
);

INSERT INTO employees VALUES
(101, 'John', 'Doe', 'john.doe@example.com', 'Sales Rep'),
(102, 'Jane', 'Smith', 'jane.smith@example.com', 'Manager'),
(103, 'Mike', 'Brown', 'mike.brown@example.com', 'Sales Rep');

-- OFFICES table
CREATE TABLE offices (
    officeCode INT,
    city VARCHAR(50),
    phone VARCHAR(50),
    addressLine1 VARCHAR(100),
    country VARCHAR(50)
);

INSERT INTO offices VALUES
(1, 'New York', '212-555-1234', '123 NY Street', 'USA'),
(2, 'London', '+44 20 7946 0958', '45 London Road', 'UK');

-- PRODUCTS table
CREATE TABLE products (
    productCode VARCHAR(50),
    productName VARCHAR(50),
    quantityInStock INT,
    buyPrice DECIMAL(10,2)
);

INSERT INTO products VALUES
('P001', 'Product A', 50, 10.50),
('P002', 'Product B', 30, 8.25),
('P003', 'Product C', 20, 12.00),
('P004', 'Product D', 15, 7.75),
('P005', 'Product E', 10, 9.50),
('P006', 'Product F', 25, 11.00);


-- ASSIGNMENT QUERIES

-- 1. Payments
SELECT checkNumber, paymentDate, amount
FROM payments;

-- 2. Orders 'In Process' sorted by orderDate DESC
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- 3. Employees with jobTitle 'Sales Rep'
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- 4. All offices
SELECT *
FROM offices;

-- 5. Products sorted by buyPrice ASC, limit 5
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
