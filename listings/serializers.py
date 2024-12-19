# listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'price_per_night', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer()  # Nested serializer for the listing

    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'start_date', 'end_date', 'created_at']

