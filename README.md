# Flask App - Gorak's Galactic Store

## Overview
This project is a Flask application for Gorak's Galactic Store, a fictional interstellar business model that sells human movies to an alien species. The Flask app has been deployed on AWS and features a fully functional user interface for managing movie orders, customers, and employees.

## Technical Aspects
- **Language:** Python (Flask Framework)
- **Deployment:** AWS (Amazon Web Services)
- **Database:** MySQL (hosted on Amazon RDS)
- **Containerization:** Docker

## Database Relationships
The application's database consists of several interrelated entities, designed to support the business operations of Gorak's Galactic Store.

### Entities and Their Relationships
- **Customers:** Represents customers who order movies. Each customer can place multiple orders.
- **Employees:** Gorkian agents who fulfill the orders. Each employee is assigned to specific orders.
- **Orders:** Records of orders placed by customers. An order is linked to a customer and an employee who fulfills it.
- **Order Items:** Junction table between orders and movies, detailing the movies ordered and their quantities.
- **Movies:** Represents the movies available for sale. Includes details like title, stock, and price.
- **Performances:** A junction table that resolves the many-to-many relationship between movies and actors.
- **Actors:** Represents actors featured in the available movies.
![Entities' Relationship](documents/entity_relationship.png)
### Database Schema
The database schema has been designed to handle relationships between these entities effectively. For example, the `Orders` table has foreign keys referencing the `Customers` and `Employees` tables, establishing a direct link between these entities. Similarly, `Order Items` serves as a junction table between `Orders` and `Movies`, capturing the many-to-many relationship.

## Deployment and Usage
The Flask application is containerized using Docker, ensuring easy deployment and scalability. The Docker container includes all necessary dependencies and can be readily deployed on any platform supporting Docker, including AWS.

To access the application:
- Visit [Gorak's Galactic Store on AWS]().
- Utilize the user-friendly interface to interact with the database, such as placing orders, managing movies, or viewing actor performances.

For further information on the project, including the detailed API documentation and a guide on how to interact with the web application, please refer to the [CRUD Documentation PDF](documents/CRUD_documentation.pdf).
