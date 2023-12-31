from bs4 import BeautifulSoup
import os
for i in range(1,21):
    #read html 
    with open('chap%d'%i, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    #extract paragraph
    paragraphs = soup.find_all('p')

    # creat output file
    with open('./extracted_chap%d.txt'%i, 'w', encoding='utf-8') as file:
        # write in
        for paragraph in paragraphs:
            file.write(paragraph.get_text() + '\n')


print("done")

