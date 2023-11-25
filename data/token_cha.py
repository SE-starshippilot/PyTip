from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
# read the extracted file
with open('extracted_chap.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# use NLTK to tokenize
tokens = word_tokenize(text)
#write in the tokens
for token in tokens:
    with open('token_chap.txt', 'a', encoding='utf-8') as file:
        file.write(token)
        file.write("\n")
# indicated done
print("done")
