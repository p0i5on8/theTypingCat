# The Typing Cat

theTypingCat automates the typing test on [theTypingCat.com](https://thetypingcat.com/) using [Selenium](https://selenium-python.readthedocs.io/)

## Requirements

Install the Selenium library for python
```bash
python3 -m pip install selenium
```

Open chrome, goto [chrome://settings/help](chrome://settings/help) and note down the chrome version   

![Chrome Version](chrome.png)

Now download a compatible version of [Chrome Driver](https://chromedriver.chromium.org/downloads)  
My chrome version is 84.0 so I downloaded Chrome Driver 84.0

## Installation

Once you have installed Selenium and downloaded Chrome Driver, clone the git repository on your machine
```bash
git clone https://github.com/p0i5on8/theTypingCat.git
```

Now copy the Chrome Driver in this repository
```bash
cp ~/Downloads/chromedriver.exe theTypingCat
```

## Usage

For 1 minute typing test
```bash
python3 theTypingCat.py -t 1
```

For 3 minutes test with user sign in
```bash
python3 theTypingCat.py -t 3 -u <username>
```
