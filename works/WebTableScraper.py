import cookielib
import mechanize
from bs4 import BeautifulSoup
from utils.Csv import Csv
from utils.Regex import Regex

__author__ = 'Tuly'


class Config(object):
    HEADERS = "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20130626 Firefox/17.0 Iceweasel/17.0.7"
    USER_AGENT = ('User-Agent', HEADERS)

    def __init__(self):
        pass


class WebTableScrapper(object):
    def __init__(self):
        self.browser = None
        self.url = "http://environmentclearance.nic.in/Search.aspx"
        self.statuses = []
        self.categories = []
        self.years = []
        self.states = []
        self.csvDataHeader = ['Status', 'Category', 'Year', 'State', 'Serial No', 'Proposal details', 'Location',
                              'Important Date', 'Category', 'Company Proponent']
        self.regex = Regex()
        dupCsvReader = Csv()
        self.dupCsvRows = dupCsvReader.readCsvRow('env_clearance.csv')
        self.csvWriter = Csv('env_clearance.csv')
        if self.csvDataHeader not in self.dupCsvRows:
            self.csvWriter.writeCsvRow(self.csvDataHeader)
            self.dupCsvRows.append(self.csvDataHeader)

    def scrapData(self):
        self.browser = self.createBrowser([Config.USER_AGENT])
        self.browser.set_handle_robots(True)
        self.scrapDataByState('UPEC', 'MIN', '2011', 'Gujarat')
        exit(1)
        data = self.browser.open(self.url, None, 60).read()
        if data is not None:
            soup = BeautifulSoup(data)
            self.statuses = self.populateDropDownValues(soup, 'ddlstatus', '0')
            self.categories = self.populateDropDownValues(soup, 'ddlcategory', '-All Category-')
            self.years = self.populateDropDownValues(soup, 'ddlyear', '-All Years-')
            self.states = self.populateDropDownValues(soup, 'ddlstate', '-All State-')

            for status in self.statuses:
                self.scrapDataByStatus(status)
                exit(1)

    def populateDropDownValues(self, soup, idValue, ignoreValue):
        listItem = []
        allStatusList = soup.find('select', {'id': idValue})
        if allStatusList is not None:
            for status in allStatusList.find_all('option'):
                if status.get('value') != ignoreValue:
                    listItem.append(status.get('value'))
        return listItem


    def scrapDataByStatus(self, status):
        for category in self.categories:
            self.scrapDataByCategory(status, category)
            exit(1)

    def scrapDataByCategory(self, status, category):
        for year in self.years:
            self.scrapDataByYear(status, category, year)
            exit(1)

    def scrapDataByYear(self, status, category, year):
        for state in self.states:
            self.scrapDataByState(status, category, year, state)
            exit(1)

    def scrapDataByState(self, status, category, year, state):
        self.browser.open(self.url)
        self.browser.select_form(name="form1")
        self.browser["ddlstatus"] = [status]
        self.browser["ddlcategory"] = [category]
        self.browser["ddlyear"] = [year]
        self.browser["ddlstate"] = [state]
        res = self.browser.submit()
        content = res.read()

        if content is not None:
            content = self.regex.replaceData('\r+', ' ', content)
            content = self.regex.replaceData('\n+', ' ', content)
            content = self.regex.replaceData('\s+', ' ', content)
            soup = BeautifulSoup(content)
            table = soup.find('table', {'class': 'ez1'})
            if table:
                for row in table.find_all('tr'):
                    cols = row.find_all('td')
                    if cols is not None and len(cols) > 7:
                        csvData = [status, category, year, state, cols[0].text, cols[1].text, cols[2].text,
                                   cols[3].text, cols[4].text, cols[5].text,
                                   cols[6].text]
                        print csvData
                        if csvData not in self.dupCsvRows:
                            self.csvWriter.writeCsvRow(csvData)
                            self.dupCsvRows.append(csvData)


    def createBrowser(self, headers):
        browser = mechanize.Browser()
        browser.set_cookiejar(cookielib.LWPCookieJar())

        # Browser options
        browser.set_handle_equiv(True)
        browser.set_handle_gzip(False)
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


if __name__ == '__main__':
    var = WebTableScrapper()
    var.scrapData()