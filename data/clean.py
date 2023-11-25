import string
import re
#read the file

with open('matplotlib_questions.txt', 'r', encoding='utf-8') as file:
    text = file.read()


    # remove punctuactions
clean_text = text.translate(str.maketrans("", "", string.punctuation))  
#remove numbers
clean_text = re.sub(r'\d+', '', clean_text) 
#remove space
# clean_text = ' '.join(clean_text.split())  # 去除多余的空格和换行符



with open('extracted.txt', 'a', encoding='utf-8') as file:
    file.write(clean_text)

input_file_path = 'extracted.txt'
output_file_path = 'extracted.txt'
word_to_remove = 'not answers'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

modified_lines = [line.replace(word_to_remove, '') for line in lines]
with open(output_file_path, 'w') as file:
    file.write('\n'.join(modified_lines))

with open(input_file_path, 'r') as file:
    lines = file.readlines()
non_empty_lines = [line.strip() for line in lines if line.strip()]

# 移除空行

with open(output_file_path, 'w') as file:
    file.write('\n'.join(non_empty_lines))

print(f"File with empty lines removed saved to: {output_file_path}")

print("done!")