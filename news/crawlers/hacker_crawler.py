from datetime import datetime
from requests_html import HTMLSession
from slugify import slugify
from news.models import Article


def crawl_one(url):

    with HTMLSession() as session:
        response = session.get(url)

    title = response.html.xpath(
        '/html[1]/body[1]/main[1]/div[1]/h1[1]/a[1]')[0].text
    paragraphs = response.html.xpath(
        '/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/p')
    text = "\n\n".join([paragraph.text for paragraph in paragraphs])
    date = response.html.xpath(
        '/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/span[1]')[0].text
    slug = slugify(title)
    pub_date = datetime.strptime(date, "%B %d, %Y")

    article, created = Article.objects.update_or_create(source=url, defaults={
                                            "slug":slug,
                                            "title":title,
                                            "text":text,
                                            "created":pub_date})
    


def crawl_urls():
    main_page = "https://thehackernews.com/"
    with HTMLSession() as session:
        response = session.get(main_page)

    urls = response.html.xpath(
        '//a[@class="story-link"]/@href')
    return urls


def crawl_site():
    urls = crawl_urls()
    for url in urls:
        crawl_one(url)
