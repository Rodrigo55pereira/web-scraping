from bs4 import BeautifulSoup

# Execução padrão para ler arquivos
with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.table.contents)
print(type(soup.contents))
print(len(soup.contents))

print(soup.table.contents[1])
print(soup.table.contents[1].span)
