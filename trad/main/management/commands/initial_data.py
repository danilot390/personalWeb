from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import *
from about.models import *

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Create or get a superuser
        username = 'admin'  # Choose your desired username
        email = 'admin@example.com'  # Choose your desired email
        password = 'admin_password'  # Choose your desired password

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            user=User.objects.filter(username=username).first()
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))

        # Create a new company
        new_company, created = Company.objects.get_or_create(
            name='Trad',
            slang='Trad',
            defaults={
                'slogan': 'Nothing is deemed impossible; we merely require a bit more time',
                'description': "One day, I embarked on a journey to establish an international company. Starting solo in my hometown, there were moments when the dream felt overwhelming, and thoughts of giving up crossed my mind. Yet, fueled by a resilient determination, I persisted. Today, with a dedicated team by my side, our shared goal is to create exceptional solutions. Drawing from diverse experiences, we bring unique expertise to programming, resulting in remarkable and efficient solutions. Whether you seek to elevate your brand's presence or require a tailored system for any purpose, we stand as your optimal choice for all things internet-related.",
                'mission': 'Crafting optimal technological solutions for our clients, delivering top-tier software to propel their personal or organizational accomplishments. Achieved through the utilization of cutting-edge technologies and the expertise of seasoned professionals.',
                'vision': 'Strive to become one of the premier software development entities worldwide.',
                'background': "One day, I embarked on a journey to establish an international company. Starting solo in my hometown, there were moments when the dream felt overwhelming, and thoughts of giving up crossed my mind. Yet, fueled by a resilient determination, I persisted. Today, with a dedicated team by my side, our shared goal is to create exceptional solutions. Drawing from diverse experiences, we bring unique expertise to programming, resulting in remarkable and efficient solutions. Whether you seek to elevate your brand's presence or require a tailored system for any purpose, we stand as your optimal choice for all things internet-related.",
                'email': 'danilot390@gmail.com',
                'phone_number': '+353831780104',
                'location': 'Dublin, Ireland',
            }
        )

        # Create or get an employee for the superuser
        employee, created = Employee.objects.get_or_create(
            user=user,
            company=new_company,
            defaults={'position': "CEO", 'duties': ""}
        )

        # Create services for the new company
        services_data = [
            {'service': 'Web Application Development', 'slug': 'webapp', 'description': 'Creating dynamic web applications involves...', 'resumen': 'Crafting interactive web applications with coding and design...'},
            {'service': 'Custom Website Development', 'slug': 'website', 'description': 'Building tailor-made websites from scratch to meet specific requirements and design preferences.', 'resumen': 'Creating unique and tailored websites through custom development...'},
            {'service': 'E-commerce', 'slug': 'ecommerce', 'description': 'Designing and developing online stores and e-commerce platforms, including shopping cart functionality, payment gateways, and inventory management.', 'resumen': 'Conducting business transactions online, E-commerce involves buying and selling products or services through electronic platforms, streamlining commercial activities.'},
            {'service': 'Full Stack Development', 'slug': 'fullstack', 'description': 'Creating the user interface and user experience elements of a website using technologies like HTML, CSS, and JavaScript, the team specializes in creating visually captivating and user-friendly websites. On the other hand, implementing server-side logic, databases, and server configurations to ensure the functionality and data management of a website; you may require one or both of them.', 'resumen': 'Full Stack Development involves creating both frontend and backend of web applications, encompassing a range of technologies for comprehensive, end-to-end solutions.'},
            {'service': 'Website Maintenance and Support', 'slug': 'support', 'description': 'Providing ongoing support, updates, and maintenance services to ensure the smooth functioning of websites.', 'resumen': 'Providing ongoing support, updates, and maintenance services to ensure the smooth functioning of websites.'},
            {'service': 'Database Design and Management', 'slug': 'datab', 'description': 'Providing ongoing support, updates, and maintenance services to ensure the smooth functioning of websites.', 'resumen': 'Providing ongoing support, updates, and maintenance services to ensure the smooth functioning of websites.'},
        ]

        for service_data in services_data:
            ServiceCompany.objects.get_or_create(company=new_company, **service_data)

        # Create social links for the new company
        social_links_data = [
            {'name': 'LinkedIn', 'slug': 'linkedin', 'url': 'https://www.linkedin.com/in/danilo-tito-7313931a7/'},
            {'name': 'GitHub', 'slug': 'git', 'url': 'https://github.com/danilot390'},
            {'name': 'Facebook', 'slug': 'facebook', 'url': 'https://www.facebook.com/danilo.titorodriguez'},
            {'name': 'Instagram', 'slug': 'instagram', 'url': 'https://www.instagram.com/daniloatitorodriguez/'},
        ]

        for social_link_data in social_links_data:
            SocialCompany.objects.get_or_create(company=new_company, **social_link_data)


        # Create social links for the user
        for social_link_data in social_links_data:
            SocialUser.objects.get_or_create(user=user, **social_link_data)

        self.stdout.write(self.style.SUCCESS('Initial dates created successfully'))

        
        