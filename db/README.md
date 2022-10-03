# Usage

Install the dependencies (in the Docker container)

```bash
$ pip3 install flask sqlalchemy flask_sqlalchemy flask_bcrypt
```

Start the `python` interpreter

```bash
$ python
```

Import the models

```python
>>> from db.models import *
```

Create tables from the schema and initialize the database with default values (to be run only once)

```python
>>> db.create_all()
>>> init_db()
Database initialized
```

## Working with the `Student` table

Query all students in the database

```python
>>> Student.query.all()
[<Student homer>]
```

Let's create a new student `Lisa` (Note the field `last_name` is optional)

```python
>>> lisa = Student(first_name='Lisa', username='lisa', email='lisa@simpson.com')
>>> lisa.set_password('supersecret')
```

Save it to the database

```python
>>> db.session.add(lisa)
>>> db.session.commit()
>>> Student.query.all()
[<Student homer>, <Student lisa>]
```

Now, filter all students with `username` lisa, and display their properties

```python
>>> s = Student.query.filter_by(username='lisa').first()
>>> s.id
2
>>> s.first_name
'Lisa'
>>> s.username
'lisa'
>>> s.email
'lisa@simpson.com'
>>> s.enrollments
[]
>>> s.joined
datetime.datetime(2021, 8, 15, 9, 15, 38, 777176)
>>> s.password_hash
'$2b$12$Xtf8YcZ71jyouCKoitlJFu4BQJNPsY5ffDZEdn1UOptKyiu7w7MJ.'
```

There is a helper method `check_password` for comparing the stored password hash against the user supplied plaintext (useful for the login page)

```python
>>> s.check_password('wrongpassword')
False
>>> s.check_password('supersecret')
True
```

Updating an entry is as simple as changing a Python variable and then commiting the changes

```python
>>> s.last_name = 'Simpson'
>>> db.session.add(s)
>>> db.session.commit()
```

## Working with the `Course` table

Display all level 4 courses

```python
>>> level4 = Course.query.filter_by(level=4).all()
>>> for course in level4:
...     print(course.name)
... 
Introduction to Programming I
Introduction to Programming II
Computational Mathematics
Discrete Mathematics
Fundamentals of Computer Science
How Computers Work
Algorithms and Data Structures I
Web Development
```

Courses can be quickly queried by their unique ID

```python
>>> c = Course.query.get(1)
>>> c.name
'Introduction to Programming I'
```

To see the list of students enrolled in the selected course, use the `enrollments` property

```python
>>> c.enrollments
[<Enrollment (homer, Introduction to Programming I, 82.0)>]
```

## Working with the `Enrollment` table

Enrollment table stores three objects. A student, the course they are enrolled in, and a corresponding grade.

To see a list of students enrolled in at least one module:

```python
>>> for entry in Enrollment.query.all(): print(entry)
... 
<Enrollment (homer, Introduction to Programming I, 82.0)>
<Enrollment (homer, Object Oriented Programming, 91.0)>
<Enrollment (homer, Machine Learning and Neural Networks, 76.0)>
<Enrollment (homer, Final Project, 66.0)>
```

Let's add existing student `Lisa` to the module `Introduction to Programming I` with a grade `95`

Create a new `Grade` entry

```python
>>> g = Grade(midterm_score=90, final_score=100, module_score=95)
```
Fetch the `Course` we are interested in

```python
>>> c = Course.query.get(1)
```

Create a new `Enrollment` object, and commit it to the database

```python
>>> e = Enrollment(student=lisa, course=c, grade=g)
>>> db.session.add(e)
>>> db.session.commit()
```

Alternatively, it is also possible to add the `Enrollment` object from within the `Student` object

```python
>>> lisa.enrollments.append(e)
>>> db.session.commit()
```
