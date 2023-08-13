description
===========

This projects focuses on the implementation of an Airbnb clone application
It involes the use of multiple technologies and is divided into parts such as:

-A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-A website (the front-end) that shows the final product to everybody: static and dynamic
-A database or files that store data (data = objects)
-An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

description of the command interpreter:
=======================================

The console will be used to:
-Create data models
-Manage (create, update, destroy, etc) objects
-Store and persist objects to a file (JSON file)

how to start it
===============

You can start the console by running python3 console.py in the terminal

how to use it
==============

You can use the console through it's in built commands such as:
create, show, all, destroy and update

examples
========

This is how you can create a new object by using the create command, show string representation of all instancess by using the all command and then destroy it with the destroy command

(hbnb) create BaseModel
733901b6-7ddc-4aa9-b523-75307362f2cd
(hbnb) all
["[BaseModel] (41e97835-7b51-4992-b9e2-42c58e60ff50) {'id': '41e97835-7b51-4992-b9e2-42c58e60ff50', 'created_at': datetime.datetime(2023, 8, 12, 17, 10, 52, 713340), 'updated_at': datetime.datetime(2023, 8, 12, 17, 10, 52, 713359)}", "[User] (6b138cc0-540f-48e6-84df-696d3f362137) {'id': '6b138cc0-540f-48e6-84df-696d3f362137', 'created_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647080), 'updated_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647093), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (f9d00242-2805-4080-a882-f1743349452c) {'id': 'f9d00242-2805-4080-a882-f1743349452c', 'created_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647564), 'updated_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647594), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (395f71f2-7165-4243-a59d-2057f23f546b) {'id': '395f71f2-7165-4243-a59d-2057f23f546b', 'created_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674372), 'updated_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674387), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (5176b54a-96c1-465f-acb3-40cadb9dbdcb) {'id': '5176b54a-96c1-465f-acb3-40cadb9dbdcb', 'created_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674925), 'updated_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674945), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (733901b6-7ddc-4aa9-b523-75307362f2cd) {'id': '733901b6-7ddc-4aa9-b523-75307362f2cd', 'created_at': datetime.datetime(2023, 8, 13, 1, 30, 15, 936657), 'updated_at': datetime.datetime(2023, 8, 13, 1, 30, 15, 936674)}"]
(hbnb) destroy BaseModel 733901b6-7ddc-4aa9-b523-75307362f2cd
(hbnb) all
["[BaseModel] (41e97835-7b51-4992-b9e2-42c58e60ff50) {'id': '41e97835-7b51-4992-b9e2-42c58e60ff50', 'created_at': datetime.datetime(2023, 8, 12, 17, 10, 52, 713340), 'updated_at': datetime.datetime(2023, 8, 12, 17, 10, 52, 713359)}", "[User] (6b138cc0-540f-48e6-84df-696d3f362137) {'id': '6b138cc0-540f-48e6-84df-696d3f362137', 'created_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647080), 'updated_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647093), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (f9d00242-2805-4080-a882-f1743349452c) {'id': 'f9d00242-2805-4080-a882-f1743349452c', 'created_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647564), 'updated_at': datetime.datetime(2023, 8, 12, 18, 21, 27, 647594), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (395f71f2-7165-4243-a59d-2057f23f546b) {'id': '395f71f2-7165-4243-a59d-2057f23f546b', 'created_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674372), 'updated_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674387), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (5176b54a-96c1-465f-acb3-40cadb9dbdcb) {'id': '5176b54a-96c1-465f-acb3-40cadb9dbdcb', 'created_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674925), 'updated_at': datetime.datetime(2023, 8, 12, 18, 22, 32, 674945), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
(hbnb)
