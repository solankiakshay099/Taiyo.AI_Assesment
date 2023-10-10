{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b1336eb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data extracted & saved in output.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "\n",
    "class Scraping:\n",
    "    def __init__(self, url, table_columns):\n",
    "        self.url = url\n",
    "        self.table_columns = table_columns\n",
    "\n",
    "    def scrape_data(self):\n",
    "        page = requests.get(self.url)\n",
    "\n",
    "        if page.status_code != 200:\n",
    "            print(\"Failed to retrieve the page\")\n",
    "            return\n",
    "\n",
    "        soup = BeautifulSoup(page.content, 'html.parser')\n",
    "        tenders_table = soup.find('table', {'id': 'activeTenders'})\n",
    "\n",
    "        if not tenders_table:\n",
    "            print(\"Active Tenders not found\")\n",
    "            return\n",
    "\n",
    "        tender_data = []\n",
    "\n",
    "        for row in tenders_table.find_all('tr'):\n",
    "            columns = row.find_all('td')\n",
    "\n",
    "            if len(columns) == len(self.table_columns):\n",
    "                tender_data.append([c.get_text() for c in columns])\n",
    "\n",
    "        df = pd.DataFrame(tender_data, columns=self.table_columns)\n",
    "        df.to_csv('Tenders.csv', index=False)\n",
    "        print(\"Data extracted & saved in Tenders.csv\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    url = 'https://etenders.gov.in/eprocure/app'\n",
    "    table_columns = ['Tender Title', 'Reference No', 'Closing Date', 'Bid Opening Date']\n",
    "    scraping = Scraping(url, table_columns)\n",
    "    scraping.scrape_data()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ca24122",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
