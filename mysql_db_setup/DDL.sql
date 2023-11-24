CREATE DATABASE OSU_Project;

USE OSU_Project;

CREATE TABLE Customers(
	id INT AUTO_INCREMENT NOT NULL,
	first VARCHAR(50) NOT NULL,
	last VARCHAR(50) NOT NULL,
	street VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE Employees(
	id INT AUTO_INCREMENT NOT NULL,
	first VARCHAR(50) NOT NULL,
	last VARCHAR(50) NOT NULL,
	street VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE Movies(
	movie_id INT AUTO_INCREMENT NOT NULL,
	title VARCHAR(100) NOT NULL,
	stock INT NOT NULL,
	price INT NOT NULL,
	PRIMARY KEY (movie_id)
);
CREATE TABLE Actors(
	actor_id INT AUTO_INCREMENT NOT NULL,
	first VARCHAR(50) NOT NULL,
	last VARCHAR(50) NOT NULL,
	PRIMARY KEY (actor_id)
);
CREATE TABLE Orders(
	order_id INT AUTO_INCREMENT NOT NULL,
	customer_id INT,
	employee_id INT,
	order_date DATETIME NOT NULL,
	credit_card_num VARCHAR(16) NOT NULL,
	order_fulfilled BOOL NOT NULL DEFAULT 0,
	PRIMARY KEY (order_id),
	FOREIGN KEY (customer_id) REFERENCES Customers(id)
    ON DELETE CASCADE,
	FOREIGN KEY (employee_id) REFERENCES Employees(id)
	ON DELETE CASCADE 
);
CREATE TABLE Order_items(
    order_id INT NOT NULL,
    movie_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, movie_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
    ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
    ON DELETE CASCADE
);

CREATE TABLE Performances(
	performance_id INT AUTO_INCREMENT NOT NULL,
	movie_id INT,
	actor_id INT,
	PRIMARY KEY (performance_id),
	FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) 
    ON DELETE CASCADE,
	FOREIGN KEY (actor_id) REFERENCES Actors(actor_id)
    ON DELETE CASCADE
);

INSERT INTO Customers (first, last, street, city, state, phone)
VALUE ('YJ', 'Park', '2415 Chestnut St', 'Philadelphia', 'PA', '1234567890'),
('San', 'Davran', '1231 Maple St', 'New York City', 'NY', '0987654321'),
('Tupac', 'Shakur', '9807 Oak St', 'Los Angeles', 'CA', '3216540987');

INSERT INTO Employees (first, last , street, city, state, phone)
VALUE ('Erling', 'Haaland', '3211 Oakview St.', 'Manchester', 'UK', '1111111111'),
('Harry', 'Kane', '3453 Carnaby Street', 'London', 'UK', '2222222222'),
('Darwin', 'Nunez', '1315 Bristol St', 'Liverpool', 'UK', '3333333333');

-- start value is 1 for auto_increment
INSERT INTO Orders (customer_id, employee_id, order_date, credit_card_num, order_fulfilled)
VALUE ('1', '2', '2022-01-11','1111222233334444', 0),
('2', '1', '2022-01-12', '2222333344445555', 1),
('3', '2', '2022-01-01', '3333444455556666', 1),
('2', '3', '2022-01-04', '4444555566667777', 0),
('1', '2', '2022-01-04', '5555666677778888', 0);


INSERT INTO Movies (title, stock, price)
VALUE ('Aliens', 3, 12);

INSERT INTO Order_items (order_id, movie_id, quantity)
VALUE (1, 1, 2);

INSERT INTO Actors(first, last)
Value ('Sigourney', 'Weaver'),
('Michael', 'Biehn'),
('Carrie', 'Henn'),
('Paul', 'Reiser');

INSERT INTO Performances (movie_id, actor_id)
VALUE (1, 1);
