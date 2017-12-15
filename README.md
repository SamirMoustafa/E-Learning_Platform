# Requirements 
*1- registration system for students
*2- registration system for instructors
*3- Instructors add one or more course/s
*4- cource/s can have a specific or all students
*5- Student could access one or more courses
*6- Course have one or more chapters
*7- Course have a description
*8- Course have a external links
*9- Course have a files
*10 - there is an admin account
*11- Admin can make instructors
*12- Admin can add,delete and edit students and instructors
# Installation
Assuming you use virtualenv (Anaconda), follow these steps to download and run the
application in this directory:

    $ git clone https://github.com/SamirMoustafa/SoftwareProject.git
    $ cd SoftwareProject
    $ source activate py27
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

* Initial data supports 3 types of users for testing purposes:
    * User (username=user, password=letmein123)
    * Professor (username=professor, password=letmein123)
    * Admin (username=admin, password=letmein123)
    * Visit http://127.0.0.1:8000/

# Compatibility
* Python 2.7
* Django 1.9
* SQLite, PostgreSQL, MySQL

# Notes
* this project is a part of a cource in my college :)
