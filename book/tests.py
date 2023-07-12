from django.test import TestCase
from django.test import Client


# Create your tests here.
class BookTestCase(TestCase):
    def test_get_all_book(self):
        response = Client().get("/book")
        print(response.content)

        self.assertEqual(len(response.content), 11)
