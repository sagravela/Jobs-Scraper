import scrapy
from scrapy.loader import ItemLoader
from jobs.items import JobOffer

class LinkedinSpider(scrapy.spiders.CrawlSpider):
    """
    Spider for Linkedin

    Parameters:
        job (str): Job title
        location (str): Location
    """
    name = 'Linkedin'
    allowed_domains = ['linkedin.com']
    rules = (
        scrapy.spiders.Rule(
            scrapy.linkextractors.LinkExtractor(restrict_css='a.base-card__full-link', allow= r'/jobs'),
            callback='parse',
        ),
    )

    def __init__(self, job: str = None, location: str =None, *args, **kwargs):
        super(LinkedinSpider, self).__init__(*args, **kwargs)
        
        # Search job and location will be received from the command line
        url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={job.replace(" ", "%20")}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&start='
        self.start_urls = [url + str(i) for i in range(0, 1000, 25)] # 1000 is the limit of offers showed by Linkedin
        self.logger.info("Linkedin starting base url: {}0".format(url))

    def parse(self, response):
        # scrapy.shell.inspect_response(response, self)
        item = ItemLoader(item=JobOffer(), response=response)
        item.add_css('title', 'h1.top-card-layout__title::text')
        item.add_css('company', 'a.topcard__org-name-link::text')
        item.add_css('place', 'span.topcard__flavor--bullet::text')
        item.add_css('posted_at', 'span.posted-time-ago__text::text')
        item.add_css('applicants', 'h4.top-card-layout__second-subline', re=r'(\d+) applicants')
        item.add_css('description', 'div.show-more-less-html__markup')
        item.add_value('url', response.url)
        yield item.load_item()
