-- Group 126 Project Step 3 Database CRUD Queries
-- Team Members: San Davran, Young-Joon Park
-- ------------------------------------------------------

-- Dropdown menus
--   Populate Employee dropdown
SELECT Employees.employee_id, Employees.first, Employees.last FROM Employees;
--   populate Customers dropdown, unlikely to use
SELECT Customers.customer_id, Customers.first, Customers.last FROM Customers;

-- Join queries for readability
SELECT Order_items.order_id, Order_items.movie_id,
                CONCAT_WS(', ', Movies.title, Movies.price) AS 'Movie Detail', 
                Order_items.quantity
                FROM Order_items
                INNER JOIN Movies ON Movies.movie_id=Order_items.movie_id;
SELECT Order_items.order_id, Order_items.movie_id,
                CONCAT_WS(', ', Movies.title, Movies.price) AS 'Movie Detail', 
                Order_items.quantity
                FROM Order_items
                INNER JOIN Movies ON Movies.movie_id=Order_items.movie_id
                WHERE Order_items.movie_id=%s AND Order_items.order_id='%s';

SELECT Orders.order_id, 
                CONCAT_WS(', ', Customers.first, Customers.last) AS 'Customer Name', 
                CONCAT_WS(', ', Employees.first, Employees.last) AS 'Employee Name',
                Orders.order_date, Orders.credit_card_num, Orders.order_fulfilled
                FROM Orders
                INNER JOIN Customers ON Orders.customer_id = Customers.id
                INNER JOIN Employees ON Orders.employee_id = Employees.id;
SELECT Orders.order_id, 
                CONCAT_WS(', ', Customers.first, Customers.last) AS 'Customer Name', 
                CONCAT_WS(', ', Employees.first, Employees.last) AS 'Employee Name',
                Orders.order_date, Orders.credit_card_num, Orders.order_fulfilled
                FROM Orders
                   INNER JOIN Customers ON Orders.customer_id = Customers.id
                INNER JOIN Employees ON Orders.employee_id = Employees.id
                WHERE Orders.order_id='%s';
-- Search functionality
SELECT * FROM Employees WHERE first LIKE :firstQuery OR last LIKE :lastQuery;

-- Employees-----------------------
--   Populate Table
SELECT Employees.employee_id, Employees.first, Employees.last, Employees.street, Employees.city, Employees.state, Employees.phone
FROM Employees;
--   Add Employee
INSERT INTO Employees (first, last, street, city, state, phone) 
Values (:employeeFirst, :employeeLast, :employeeStreet, :employeeCity, :employeeState, :employeePhone);
--   Delete Employee
DELETE FROM Employees WHERE id = :employeeId;
--   Update Employee
UPDATE Employees SET first = :employeeFirst, last = :employeeLast, street = :employeeStreet, city = :employeeCity, state = :employeeState, phone = :employeePhone
WHERE employee_id = :employeeId;

-- Orders -----------------------
--   Populate Table
SELECT order_id, customer_id, employee_id, credit_card_num, order_date, order_fulfilled
FROM Orders;
--   Add Orders
INSERT INTO Orders (customer_id, employee_id, credit_card_num, order_date, order_fulfilled) 
Values (:cidFromDrop, :eidFromDrop, :creditCardNum, :orderDate, :orderFulfilled);
--   Delete Orders
DELETE FROM Orders WHERE order_id = :orderId;
--   Update Orders
UPDATE Employees SET first = :employeeFirst, last = :employeeLast, street = :employeeStreet, city = :employeeCity, state = :employeeState, phone = :employeePhone
WHERE id = :employeeId;

-- Customers
--   Populate Table
SELECT customer_id, first, last, street, city, state, phone
FROM Customers;
--   Add Customers
INSERT INTO Customers (first, last, street, city, state, phone)
Values (:customerFirst, :customerLast, :customerStreet, :customerCity, :customerState, :customerPhone);
--   Delete Customers
DELETE FROM Customers WHERE customer_id = :customerId;
--   Update Customers
UPDATE Customers SET first = :customerFirst, last = :customerLast, street = :customerStreet, city = :customerCity, state = :customerState, phone = :customerPhone
WHERE id = :employeeId;

-- Movies
--   Populate Table
SELECT movie_id, title, stock, price
FROM Movies;
--   Add Movie
INSERT INTO Movies (title, stock, price)
Values (:movieTitle, :movieStock, :moviePrice);
--   Delete Movie
DELETE FROM Moviess WHERE movie_id = :movieId;
--   Update Movie
UPDATE Movies SET title = :movieTitle, stock = :movieStock, price = :moviePrice
WHERE movie_id = :movieId;

-- Actors
--   Populate Table
SELECT actor_id, first, last
FROM Actors;
--   Add Actor
INSERT INTO Actors (first, last)
Values (:actorFirst, :actorLast);
--   Delete Actor
DELETE FROM Actors WHERE actor_id = :actorId;
--   Update Actor
UPDATE Actors SET first = :actorFirst, last = :actorLast
WHERE actor_id = :actorId;

-- Performances
--   Populate Table
SELECT performance_id, Movies.title, Actors.name
FROM Performances
INNER JOIN Movies ON Performances.movie_id=Movies.id
INNER JOIN Actors ON Performances.actor_id=Actors.id;
--   Add Performance
INSERT INTO Performances (movie_id, actor_id)
Values (:midFromDropdown, :aidFromDropdown);
--   Delete Performance
DELETE FROM Performances WHERE performance_id = :perfromanceId;
--   Update Performance
UPDATE Performances SET movie_id = :midFromDropdown, actor_id = :aidFromDropdown
WHERE performance_id = :performanceId;

-- Order_items
--   Populate Table
SELECT order_id, movie_id, quantity
FROM Order_items;
--   Search Table
SELECT order_id, movie_id, quantity
FROM Order_items
WHERE order_id = :orderId;
--   Add Order_items
INSERT INTO Order_items (order_id, movie_id, quantity)
Values (:orderId, :movieId, :quantity);
--   Delete Order_items
DELETE FROM Order_items WHERE order_id = :orderId AND movie_id AND :movieId;
--   Update Order_items
UPDATE Order_items SET movie_id = :midFromDropdown, quantity = :quantity
WHERE order_id = :orderId AND movie_id =:midFromDropdown;

