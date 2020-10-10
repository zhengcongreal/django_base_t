from django.test import TestCase

# Create your tests here.
with open("img/1.jpg", 'rb') as file:
    file_data = file.read()
print(file_data)
