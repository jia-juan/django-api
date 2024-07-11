import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()

from user.models import User
from demo.models.product import Product
from demo.models.customer import Customer

fake = Faker()


def create_fake_users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            password='password123'  # 你可以生成更複雜的密碼
        )
        user.is_superuser = False
        user.is_staff = False
        user.save()
        users.append(user)
    return users


def create_fake_customers(users):
    for user in users:
        Customer.objects.create(
            user=user,
            phone_number=fake.phone_number(),
            address=fake.address()
        )


def create_fake_products(num_products=20):
    for _ in range(num_products):
        Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=round(random.uniform(10.0, 1000.0), 2),
            stock_quantity=random.randint(1, 100)
        )


if __name__ == '__main__':
    users = create_fake_users(10)  # 生成 10 個假用戶
    create_fake_customers(users)  # 為每個用戶創建一個 Customer
    create_fake_products(20)  # 生成 20 個假產品
