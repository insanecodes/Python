import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phone_number = phonenumbers.parse("Enter Number")
# Indian phone number example: 91**********

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
print(timezone.time_zones_for_number(phone_number))
