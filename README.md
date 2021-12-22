# SeleniumManager
I'm fed up with always having to struggle unnecessarily when I have to use Selenium on a new machine, so I made this little python module for my personal use to simplify Selenium's utilisation in a new environment

## usage

0) Download SeleniumManager.py

1) Download and put with SeleniumManager.py the correct firefox geckodriver here: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

2) Install Selenium using, for example:
```bash
python -m pip install selenium
```

3) Launch Python in the repertory containing SeleniumManager.py and the geckodriver

4) Import Selenium Manager by doing in the python console
```python
import SeleniumManager
```
It will open the Firefox browser

. So you can:
- go to an url by typing directly in the opened browser or by typing in the python console
```python
SeleniumManager.get(string: url)
```

- get elements using css-selectors by doing
```python
SeleniumManager.find_elements(string: css-selector): SeleniumWebElement[]
```

- manipulate the obtained array as you want
```python
l = SeleniumManager.find_elements("ul#list li a")
result = map(lambda el: el.text, l)
print(l)
```
