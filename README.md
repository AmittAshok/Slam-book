# Slambook App- Two Tier appliaction 

This is a simple Flask app that interacts with a MySQL database. The app allows users to submit messages, which are then stored in the database and displayed on the frontend.

# Prerequisites
Before you begin, make sure you have the following installed:

Docker
Git (optional, for cloning the repository)

# Setup
  1.Clone this repository (if you haven't already):

  2.git clone https://github.com/your-username/your-repo-name.git
  
          cd your-repo-name
        
  3.Create a .env file in the project directory to store your MySQL environment variables:
  
        touch .env
        Open the .env file and add your MySQL configuration:

        MYSQL_HOST=mysql
        MYSQL_USER=your_username
        MYSQL_PASSWORD=your_password
        MYSQL_DB=your_database
# Usage

1.Start the containers using Docker Compose:

    docker-compose up --build
    
2.Access the slambook app in your web browser:

    Frontend: http://localhost
    Backend: http://localhost:5000
    
3.Create the messages table in your MySQL database:
  Use a MySQL client or tool (e.g., phpMyAdmin) to execute the following SQL commands:
  
    CREATE TABLE messages (
    CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    blood_group VARCHAR(10),
    location VARCHAR(255),
    hobbies TEXT
    );
    
4.Interact with the app:

      Visit http://localhost to see the frontend. You can submit new messages using the form.
      Visit http://localhost:5000/insert_sql to insert a message directly into the messages table via an SQL query.
      
5.Cleaning Up
To stop and remove the Docker containers, press Ctrl+C in the terminal where the containers are running, or use the following command:

docker-compose down
To run this two-tier application using without docker-compose

First create a docker image from Dockerfile

      docker build -t slambook
Now, make sure that you have created a network using following command

    docker network create slam-network
# Notes

This is a basic setup for demonstration purposes. In a production environment, you should follow best practices for security and performance.

Be cautious when executing SQL queries directly. Validate and sanitize user inputs to prevent vulnerabilities like SQL injection.

If you encounter issues, check Docker logs and error messages for troubleshooting.

