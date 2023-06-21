from bs4 import BeautifulSoup
import requests

'''
# Lear html

with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html.parser')

print(soup_string)
'''

'''
# lxml

r = requests.get('https://www.the-numbers.com')
soup = BeautifulSoup(r.text, 'lxml')

print(soup)
'''

'''
# html5

with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')

print(soup_string)

'''
'''

# capturando tags

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.title

print(tag)
print(tag.name)

tag = soup.p
print(tag.name)

'''

# Acessando atributos do html
'''

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.p['class'])
print(soup.p.attrs)
print(soup.a['href']) 
print(soup.a.get('href'))

'''

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

# Formata todas as tags
print(soup.prettify())

# Pega todos os textos das tags
print(soup.get_text())

# pega o texto dos filhos
print(soup.p.get_text())

# pega o texto da tag atual
print(soup.p.string)

# imprime o texto pegando o caminho
print(soup.p.b.string)
