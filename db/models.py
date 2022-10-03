"""This module implements the database schema."""

from db import db
from sqlalchemy import event
from datetime import datetime
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash


class Enrollment(db.Model):
    """Implements the Enrollment model."""

    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=0)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=0)
    grade_id = db.Column(db.Integer, db.ForeignKey("grade.id"), nullable=0)

    __table_args__ = (db.UniqueConstraint(student_id, course_id),)

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")
    grade = db.relationship("Grade")

    def __repr__(self):
        return '<Enrollment ({0}, {1}, {2})>'.format(
            self.student.username,
            self.course.name,
            self.grade.module_score
        )


class Student(db.Model):
    """Implements the Student model."""

    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    joined = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    password_hash = db.Column(db.String(72), nullable=True)

    enrollments = db.relationship("Enrollment", back_populates="student")

    def set_password(self, plaintext, rounds=12):
        """Sets the password for the user. The password hash is created
        with the Bcrypt python library

        Args:
            plaintext: The plaintext password to hash
            rounds: Number of rounds to use for the bcrypt hashing
        """
        password_hash = generate_password_hash(plaintext, rounds)
        self.password_hash = password_hash.decode()

    def check_password(self, plaintext):
        """Check a plaintext password against a stored password hash.

        Args:
            plaintext: A plaintext password

        Returns:
            A boolean value indicating if the plaintext password matches the
            stored password hash.
        """
        return check_password_hash(self.password_hash, plaintext)

    def __repr__(self):
        return f'<Student {self.username}>'


class Course(db.Model):
    """Implements the Course model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    enrollments = db.relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f'<Course {self.name}>'


class Grade(db.Model):
    """Implements the Grade model."""

    id = db.Column(db.Integer, primary_key=True)
    midterm_score = db.Column(db.Float, nullable=False)
    final_score = db.Column(db.Float, nullable=False)
    module_score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Grade {self.module_score}>'


def init_db():
    """Fill up the database with default values."""

    # Create test student
    student = Student(
        first_name='Homer', last_name='Simpson',
        username='homer', email='homer@simpson.com'
    )
    student.set_password('secret')
    db.session.add(student)
    db.session.commit()

    # Create all courses
    course_list = [
        {'name': 'Introduction to Programming I', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Introduction to Programming II', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Computational Mathematics', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Discrete Mathematics', 'level': '4','weight': '1', 'credits': '15'},
        {'name': 'Fundamentals of Computer Science', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'How Computers Work', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Algorithms and Data Structures I', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Web Development', 'level': '4', 'weight': '1', 'credits': '15'},
        {'name': 'Object Oriented Programming', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Software Design and Development', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Programming with Data', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Agile Software Projects', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Computer Security', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Graphics Programming', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Algorithms and Data Structures II', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Databases, Networks and the Web', 'level': '5', 'weight': '3', 'credits': '15'},
        {'name': 'Machine Learning and Neural Networks', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Artificial Intelligence', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Virtual Reality', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Games Development', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Advanced Web Development', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Physical Computing and Internet of Things', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': '3D Graphics and Animation', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Mobile Development', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Interaction Design', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Natural Language Processing', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Intelligent Signal Processing', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Data Science', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Databases and Advanced Data Techniques', 'level': '6', 'weight': '5', 'credits': '15'},
        {'name': 'Final Project', 'level': '6', 'weight': '5', 'credits': '30'}
    ]

    for course in course_list:
        c = Course(**course)
        db.session.add(c)
    db.session.commit()

    # Enroll test student in 4 modules
    g1 = Grade(midterm_score=86.00, final_score=78.00, module_score=82.00)
    e1 = Enrollment(student=student, course=Course.query.get(1), grade=g1)
    db.session.add(e1)

    g2 = Grade(midterm_score=95.00, final_score=87.00, module_score=91.00)
    e2 = Enrollment(student=student, course=Course.query.get(9), grade=g2)
    db.session.add(e2)

    g3 = Grade(midterm_score=83.00, final_score=69.00, module_score=76.00)
    e3 = Enrollment(student=student, course=Course.query.get(17), grade=g3)
    db.session.add(e3)

    g4 = Grade(midterm_score=55.00, final_score=77.0, module_score=66.00)
    e4 = Enrollment(student=student, course=Course.query.get(30), grade=g4)
    db.session.add(e4)

    db.session.commit()
    print("Database initialized")
