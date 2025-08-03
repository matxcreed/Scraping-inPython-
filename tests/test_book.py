import unittest
from scrapy.http import HtmlResponse
from books.spiders.book import BookSpider

class BookSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = BookSpider()
        self.example_html = """file:///C:/Users/matxz/Downloads/materials-web-scraping-with-scrapy-and-mongodb-%20(1)/books/tests/sample.html
        """
        self.response = HtmlResponse(
            url="https://books.toscrape.com",
            body=self.example_html,
            encoding="utf-8"
        )

    def test_parse_scrapes_all_items(self):
        """Test if the spider scrapes books and pagination links."""
        book_items = []
        pagination_requests = []

        self.assertEqual(len(book_items), 2)
        self.assertEqual(len(pagination_requests), 1)
        pass

    def test_parse_scrapes_correct_book_information(self):
        """Test if the spider scrapes the correct information for each book."""
        pass

    def test_parse_creates_pagination_request(self):
        """Test if the spider creates a pagination request correctly."""
        pass

if __name__ == "__main__":
    unittest.main()