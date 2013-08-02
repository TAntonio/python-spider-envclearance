import cookielib
import mechanize
from spiders import config

__author__ = 'Tuly'


class Config(object):
    HEADERS = "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20130626 Firefox/17.0 Iceweasel/17.0.7"
    USER_AGENT = ('User-Agent', HEADERS)

    def __init__(self):
        pass


class BrowserUtil(object):
    def __init__(self):
        self.browser = None

    def fetchData(self):
        self.browser = self.createBrowser([Config.USER_AGENT])

    def createBrowser(self, headers):
        browser = mechanize.Browser()
        browser.set_cookiejar(cookielib.LWPCookieJar())

        # Browser options
        browser.set_handle_equiv(True)
        browser.set_handle_gzip(True)
        browser.set_handle_redirect(True)
        browser.set_handle_referer(True)
        browser.set_handle_robots(True)

        # Follows refresh 0 but not hangs on refresh > 0
        browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #browser.set_debug_http(True)
        #browser.set_debug_redirects(True)
        #browser.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        browser.addheaders = headers

        return browser