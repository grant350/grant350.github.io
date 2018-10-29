from bs4 import BeautifulSoup
raw_html = open('./index.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for input in html.select('input'):
     if input['class'] == 'password':
        print(input.text)
