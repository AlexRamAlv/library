from django.test import TestCase
from django.urls import reverse

from books.models import Book

# Create your tests here.


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Alexander Ramirez",
            isbn="123456789123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "An excellent subtitle")
        self.assertEqual(self.book.author, "Alexander Ramirez")
        self.assertEqual(self.book.isbn, "123456789123")

    def test_book_listView(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An excellent subtitle")
        self.assertTemplateUsed(response, "book_list.html")
