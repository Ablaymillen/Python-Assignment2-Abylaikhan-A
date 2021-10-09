from requests_html import HTMLSession

# constant variables
X_PATH_NEWS = r'//*[@id="fusion-app"]/div/div[5]/section[1]/div[2]'
WEB_PAGE = 'https://www.coindesk.com/data/'
FULL_INFO = 'div.currency-detailstyles__AboutSectionWrapper-e9ov1h-4'
COIN_PAGE = 'https://www.coindesk.com/price/'

# coin class
class Coin:
    def __init__(self, name):
        self.name = name

    # close connection session
    def close_con(self, request):
        request.session.close()

    # open connection session
    def open_con(self, url):
        return HTMLSession().get(url)

    # get news on specific coin from website
    def get_news(self):
        # making request to the website
        url = COIN_PAGE + self.name.lower()
        request = self.open_con(url)
        # load webpage for dynamic scrapping
        # timeout - essentially how much time program will wait for answer from web site
        request.html.render(sleep=1, timeout=100)
        # find required items by scrapping and print them to the console
        news = request.html.xpath(X_PATH_NEWS, first=True)
        for item in news.absolute_links:
            r = HTMLSession().get(item)
            desc = r.html.find('div.at-headline', first=True).text
            date = r.html.find('span.Typography__StyledTypography-sc-1xaoczh-0', first=True).text
            short = r.html.find('div.at-text', first=True).text
            print(f"Title '\n'{desc}")
            print(f"Date of publication {date}")
            print(f"Short description '\n' {short}")
        self.close_con(request)

    # information on specific coin
    def get_info(self):
        # url request
        url = COIN_PAGE + self.name.lower()
        request = self.open_con(url)
        # load webpage for dynamic scrapping
        # timeout - essentially how much time program will wait for answer from web site
        request.html.render(sleep=1, timeout=10)
        # get required item and print it to the console
        info = request.html.find(FULL_INFO, first=True).text
        print(f"Information on coin: '\n' {info}")
