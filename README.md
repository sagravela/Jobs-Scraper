# Job Scraper App
The Job Scraper App is a tool designed to connect to various job websites, retrieve job offer information, and filter the results based on keywords provided by the user. The app leverages the *Scrapy* framework to efficiently scrape job listings and present the most relevant opportunities according to the user's preferences.

## Usage
Help:
```bash
python search_jobs.py --help
```

Searching for jobs:
```bash
python search_jobs.py --search search_term --location location
```
> **Keywords** could be supplied through a 'keywords.txt' file in the root of the project, a sample format is attached. They are divided between keywords to be included and to be excluded in the job title.  
Remember to write them one per line and they are considered case insensitive.  

Where:
- `--search_term` is the job title or keyword to search for.
- `--location` is the location to search for the job.

Spider can be runned standalone by Scrapy CLI:
```bash
scrapy crawl spider_name -a job=job_name -a location=location -O file_name.format
```
This will run the spider scraping all the jobs without filtering.

### Filtering Notes
The app filter by the search term and keywords (if they are provided) looking them up in the job title. If any of them matches, the job is considered relevant.  
A recommendation of use is to **provide other names of the role (even translations) as keywords to filter the results**.

>**NOTE**: The jobs offer are sorted by applicants number (ascending order) and posted date (descending order).

## Further Improvements
- Add support for different job websites: this can be done adding new spiders by new web site and concatenating the results.
- AI filtering: the app already filter by keywords, but it can be improved futher using a generation LLM and a fixed prompt given by the user according to their preferences. The AI will flag which jobs are relevant to the user.
- Improve performance: the app can scrape data faster by decreasing `DOWNLOAD_DELAY` and deactivating `AUTOTHROTTLE_ENABLED` but it will require more resources to avoid getting blocked by the website. For instance, including proxy services. 
