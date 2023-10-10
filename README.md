# Taiyo.AI_Assesment
This is my submission
The task was to create a web scraper using Python to extract data from the E-procurement Government of India website (https://etenders.gov.in/eprocure/app) specifically, information about active tenders. The goal was to scrape details such as the tender title, reference number, closing date, and bid opening date and save this data in a CSV file.

Initialization: I created a Python class named Scraping that accepts the target URL and the expected table columns for the tender data as parameters.
Scraping Data: I sent a GET request to the specified URL using the requests library and checked if the request was successful (HTTP status code 200). If the request failed, I printed an error message and exited.
Parsing HTML: I used BeautifulSoup to parse the HTML content of the page, allowing me to navigate and extract data from the webpage's structure.
Finding the Active Tenders Table: I located the HTML table with the ID "activeTenders" on the page, as this table contained the tender data I needed.
Iterating through Rows: I iterated through the rows of the table, extracted data from each row, and ensured that the number of columns in a row matched the expected number to maintain consistency.
Storing Data: I stored the extracted tender data in a list.
Saving to CSV: Finally, I used the Pandas library to create a DataFrame from the extracted data and saved it to a CSV file named "Tenders.csv."
This approach effectively completed the task of web scraping, allowing me to obtain and store the required tender data from the E-procurement Government of India website in a structured CSV format.
