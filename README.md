YTS Scraping

This project is a web scraper built with Python and Scrapy to extract information from YTS and store it in a MongoDB database.
Its main goal is to demonstrate how to implement a complete scraping workflow with pagination and custom user-agent to simulate a real browser.
✨ Features

    Structured scraping using Scrapy.

    Automatic pagination to crawl multiple result pages.

    Custom User-Agent to avoid basic blocks.

    MongoDB storage for the scraped data.

    Designed for learning purposes by hobbyists and students.

📦 Requirements

    Python 3.9+

    MongoDB installed and running

    Python libraries:

        scrapy

        pymongo

Install dependencies with:

pip install -r requirements.txt

pip install scrapy pymongo

🚀 Usage

    Clone this repository:

git clone https://github.com/matxcreed/YTS-Scraping.git
cd YTS-Scraping

    Set up your MongoDB connection in the project configuration file (e.g., settings.py).

    Run the scraper:

scrapy crawl movie

    Check your MongoDB database to confirm the data has been saved.


📚 Inspiration

I’ve always wanted to learn how to extract data from a website in a structured way.
This project is the result of experimenting with web scraping, data storage, and best practices using Scrapy.
⚠️ Legal Disclaimer

This project was created for educational purposes only.
Improper use of scraping techniques may violate a website’s Terms of Service.
The author is not responsible for any misuse of this code.

