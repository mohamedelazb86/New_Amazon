import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from faker import Faker
from products.models import Product,Brand


def seed_brand(n):
    fake=Faker()
    image=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_brand/{image[random.randint(0,9)]}'
        )
        

def seed_product(n):
    fake=Faker()
    flag=['New','Sale','Feature']
    image=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    brand=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag[random.randint(0,2)],
            price=round(random.uniform(5.55,99.99),2),
            image=f'photo_product/{image[random.randint(0,9)]}',
            sku=random.randint(100,10000000),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brand[random.randint(0,len(brand)-1)],
            quantity=random.randint(5,1500)
        )
    
#seed_brand(200)
seed_product(1500)