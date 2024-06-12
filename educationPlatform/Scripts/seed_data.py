import os
import sys
import django
import csv
from collections import defaultdict
from datetime import datetime
# Setting up Django environment
baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(baseDir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educationPlatform.settings')
django.setup()

# Import your User model
from Uol.models import *

# Path to the CSV file
usersData = os.path.join(baseDir, '..', 'Assets', 'Users.csv')

"""
def seed_users():
    with open(usersData, mode='r') as file:
        cvReader = csv.DictReader(file)
        for row in cvReader:
            user, created = User.objects.get_or_create(
                userName=row['userName'],
                defaults={
                    'email': row['email'],
                    'role': row['role'],
                    'joinDate': row['joinDate']
                }
            )
            if created:
                print(f"Added a new user: {user.userName}")
            else:
                print(f"User already exists: {user.userName}")

if __name__ == "__main__":
    seed_users()

coursesData = os.path.join(baseDir, '..', 'Assets','CoursesModule.csv')

def seed_courses():
    with open(coursesData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            instructor = User.objects.get(userName=row['Instructor'])
            course, created = Course.objects.get_or_create(
                id=row['Code'],
                defaults={
                    'modelName': row['ModuleName'],
                    'writtenExam': row['Writtenexam'],
                    'category': row['Category'],
                    'instructor': instructor,
                    'publishDate': row['publishDate']
                }
            )
            if created:
                print(f"Added a new course {course.modelName}")
            else:
                print(f"Course already exists: {course.modelName}")

if __name__ == "__main__":
    seed_courses()


"""

enrollmentsData = os.path.join(baseDir, '..', 'Assets', 'Enrollment.csv')

def seed_enrollments():
    with open(enrollmentsData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            user = User.objects.get(id=row['user'])
            course = Course.objects.get(id=row['course'])
            enrollmentDate = datetime.strptime(row['enrollmentDate'], "%d/%m/%Y").date()
            enrollment, created = Enrollment.objects.get_or_create(
                id=row['ID'],
                defaults={
                    'user': user,
                    'course': course,
                    'enrollmentDate': enrollmentDate,
                    'progress': row['progress'],
                    'status': row['status']
                }
            )
            if created:
                print(f"Added a new enrollment for user {user.userName} in course {course.modelName}")
            else:
                print(f"Enrollment already exists for user {user.userName} in course {course.modelName}")

if __name__ == "__main__":
    seed_enrollments()