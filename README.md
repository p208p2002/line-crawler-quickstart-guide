# Line crawler quickstart guide
## Demo
![](https://raw.githubusercontent.com/p208p2002/line-crawler-quickstart-guide/master/assets/demo.gif)
## Prepare
```
chromedriver.exe # driver for control browser
ophjlpahpchlmihnnnihgmmeilfjmjjc.crx # Line-Web App Page
main.py # demo program
```
### Chromedriver
[Download chromedriver](https://chromedriver.chromium.org/) that compatible with your chrome
version


### Line packege
1. Install [CRX Downloader]((https://chrome.google.com/webstore/detail/crx-extractordownloader/ajkhmmldknmfjnmeedkbkkojgobmljda?utm_source=chrome-ntp-icon)) from Chrome App Store

2. Goto [Line-Web App Page]((https://chrome.google.com/webstore/detail/line/ophjlpahpchlmihnnnihgmmeilfjmjjc?utm_source=chrome-ntp-icon)) at Chrome App Store

3. Downlaod **Line-Web App Page** with **CRX Downloader** extention

![](https://raw.githubusercontent.com/p208p2002/line-crawler-quickstart-guide/master/assets/crx_downloader.png)

## Start Up
### Install Packages
```
$ pip install -r requirements.txt
```
### main.py
```
$ python main.py
```

## Development
use F12 open development tool and maunal parse html first, then code what you want.
![](https://raw.githubusercontent.com/p208p2002/line-crawler-quickstart-guide/master/assets/dev_tool.png)

### Development Resource
- [Selenium](https://www.selenium.dev/documentation/en/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
