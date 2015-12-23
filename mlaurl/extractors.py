def extractem(doc, extractors):
    pass



def extract_xpath_selector(htmldoc, selector):
    pass

def extract_text_string(htmldoc, regex):
    pass

def extract_url_pattern(url, regex):
    pass



EXTRACTORS = {
    'title': [
        ('og_title', """head/meta[@property="og:title"]/@content""", 'xpath'),
        ('twitter_title', """head/meta[@property="twitter:title"]/@content""", 'xpath'),
        ('itemprop_name', """head/meta[@itemprop="name"]/@content""", 'xpath'),
        ('head_title', """head/title/text()""", 'xpath'),
        ('h1#title', """body/h1[contains(@id, "title")]/text()""", 'xpath'),
        ('h1.title', """body/h1[contains(@class, "title")]/text()""", 'xpath'),
        ('first_h1', """body/h1[1]/text()""", 'xpath')
    ]
}
