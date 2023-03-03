
BBC Article Scrapper:

Use Selenium with PYTHON in headless mode on Django framework with Docker to scrape BBC.com
Update all scrapped details into mysql table

Steps:
1. Fetch all Article links on home page of www.bbc.com
2. Scrapper each article link in sperate thread and fetch title and body the topic.
3. Populate MYSQL table with URL, Title & Body
4. Display all the fetched articles on Home Page with scrapped time


Usage:
1. Clone the repo
2. cd to cloned repo dir
3. docker-compose up
4. open url http://localhost:8000