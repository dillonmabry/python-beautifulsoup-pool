# python-beautifulsoup-pool
Python web scraping utilizing Python multiprocessing pooling techniques to output a .txt file with all posts from a forum thread with multiple pages.

This particular file will scrape a forum post related to all posts concerning form 4 ATF (Alcohol-Tobacco-Firearms) wait times for raw data source for further processing time calculations in a data processing engine (Spark, etc...)

| FIELD | DESC |
| ------ | ------ |
| PATH | Base project path |
| BASE_URL | Base URL of the Forum/Thread you wish to scrape |
| NUM_PAGES | The total number of pages in the thread/topic |
| POOL_SIZE | The max pool size of your multiprocessing |
