import random
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding the database...")

        # Create users
        for i in range(3):
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={"email": f"user{i}@example.com", "password": "password123"}
            )
        
        users = User.objects.all()

        # Create listings
        for i in range(5):
            Listing.objects.create(
                title=f"Listing {i}",
                description="A lovely place to stay!",
                price_per_night=random.randint(50, 200),
                host=random.choice(users)
            )

        listings = Listing.objects.all()

        # Create bookings
        for i in range(10):
            Booking.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                start_date="2023-01-01",
                end_date="2023-01-10",
                status=random.choice(['pending', 'confirmed', 'cancelled'])
            )

        # Create reviews
        for i in range(15):
            Review.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                rating=random.randint(1, 5),
                comment="Great place!"
            )

        self.stdout.write("Database seeding completed!")

