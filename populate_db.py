import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasknest.settings')
import django
django.setup()

from faker import Faker
import random
from users.models import CustomUser
from tasks.models import Project, Task, TaskDetail

# Function to populate the database


def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Projects
    projects = [Project.objects.create(
        name=fake.bs().capitalize(),
        description=fake.paragraph(),
        start_date=fake.date_this_year()
    ) for _ in range(5)]
    print(f"Created {len(projects)} projects.")

    # Create Employees
    custom_users = [CustomUser.objects.create(
        username=fake.user_name(),
        email=fake.email(),
        password='password123' # You might want to use a more secure way to set passwords
    ) for _ in range(10)]
    print(f"Created {len(custom_users)} custom users.")

    # Create Tasks
    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED'])
        )
        task.assigned_to.set(random.sample(custom_users, random.randint(1, 3)))
        tasks.append(task)
    print(f"Created {len(tasks)} tasks.")

    # Create Task Details
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
    print("Populated TaskDetails for all tasks.")
    print("Database populated successfully!")


if __name__ == "__main__":
    populate_db()
