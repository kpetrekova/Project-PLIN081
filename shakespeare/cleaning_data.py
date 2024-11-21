"""change documents to UTF-8"""


"""tohle má ostatní texty uložit do UTF-8 formátu
Taky by to mělo vymazat všechno, kromě textu knihy ze zdrojů gutenberg"""
"""CHANGE documents to UTF-8 and save as a new files and convert to one dictionary"""
import os
import glob
import re

def read_text_files_from_subfolders(main_folder_path):
# Find all .txt files in the specified main folder and its subfolders
    text_files = glob.glob(os.path.join(main_folder_path, '**', '*.txt'), recursive=True)
    
    # Dictionary to store the contents of each file
    file_contents = {}
    
    # Loop through the text files, read their content, and store in dictionary
    for i, file in enumerate(text_files):
        with open(file, 'r',encoding='utf-8-sig') as f:
            # Create dynamic names like 'file_1', 'file_2', etc.
            file_contents[f'file_{i+1}'] = f.read()
    
    return file_contents

main_folder_path = 'data'
file_contents = read_text_files_from_subfolders(main_folder_path)


file_contents = {}
for file_name, content in file_contents.items():
        file_path = os.path.join('UTF-8data', f'{file_name}.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
for i, file in enumerate(os.listdir('UTF-8data')):
    file_path = os.path.join('UTF-8data', file)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents[f'file_{i+1}'] = f.read()
    


"""function remove everuthinng before and after pattern from Guthenberge source. Only a text of book should stay"""
#pattern 1 delete ewerything before the "start of the project" and second one delete everything after the end of the book
def delete_guthenberg_info (contentdict):

    start_pattern = r'\*\*\* START OF (THE|THIS) PROJECT GUTENBERG EBOOK.*?\*\*\*'
    end_pattern = r'\*\*\* END OF (THE|THIS) PROJECT GUTENBERG EBOOK'
   
    for file_name, file_content in contentdict.items():
         # Check if file_content is in bytes and decode it
        if isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')  # Decode bytes to string

        modified_text = re.sub(f'^.*?{start_pattern}', '', file_content, flags=re.DOTALL)
        modified_text = re.sub(f'{end_pattern}.*$', '', modified_text, flags=re.DOTALL)

        contentdict[file_name] = modified_text
        
    return contentdict


  
file_contents_noguthenberg = delete_guthenberg_info(file_contents)
#print(file_contents_noguthenberg)


"""save as file"""
#pro kontrolu stahuji soubory do jednoho souboru, od ktereho si slibuji, ze uvidim jestli jsem odstranila to co jsem chtela
"""#Combine the contents into a single string with a separator
combined_content = "\n\n---\n\n".join(file_contents.values())
# Save the combined content to a single .txt file
output_file_path = 'combined_texts4.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(combined_content)"""
 
combined_content = ""
for filename, content in file_contents.items():
    combined_content += f"\n\n--- Start of {filename} ---\n\n"
    combined_content += content
    combined_content += f"\n\n--- End of {filename} ---\n\n"

# Save the combined content to a single .txt file
output_file_path = 'combined_texts2.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(combined_content)

print(f"Combined content with filename separators has been written to {output_file_path}")   
    


"open folder"
with open('combined_texts2.txt', 'r', encoding='utf-8') as f:
    # Read the entire file
    content = f.read()


def remove_paragraph_starting_with(text, start_sentence):
    # Create a regular expression pattern to match the start sentence and everything until the next paragraph
    pattern = re.escape(start_sentence) + r'.*?(?:\n\n|\Z)'  # Match until two newlines or end of text

    # Replace the matched paragraph with an empty string
    cleaned_text = re.sub(pattern, '', text, count=1, flags=re.DOTALL)  # count=1 ensures only one paragraph is removed
    
    return cleaned_text

"""removiing paragraph with specific pattern"""
# Remove article starting with the specific sentence
start_sentence = "Copyright pages exist to tell you"
content = remove_paragraph_starting_with(content, start_sentence)

start_sentence = "This ebook is"
content = remove_paragraph_starting_with(content, start_sentence)
#print(content)
output_file_path = 'combinedtexts2_withoutebooks'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(content)

###



import re

def remove_paragraph_starting_with(text, start_sentence_pattern):
    # Create a regular expression pattern to match the start sentence and everything until the next paragraph
    pattern = r'{}.*?(?:\n{{2,}}|\Z)'.format(start_sentence_pattern)  # Match until two or more newlines or end of text

    # Replace the matched paragraph with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)  # count=1 ensures only one paragraph is removed

    return cleaned_text

# Read the content from the file
with open('combinedtexts_handclean.txt', 'r', encoding='utf-8') as f: 
    newcontent = f.read()

# Define the start sentence regular expression
start_sentence_pattern = r'\[(F|f)ootnote \d+:.*?\]'

# Remove the paragraph that starts with the specified sentence
content = remove_paragraph_starting_with(newcontent, start_sentence_pattern)

# Print the cleaned content
print(content)

def remove_paragraph_including(text, keyword):
    # Create a regular expression pattern to match any paragraph containing the keyword
    pattern = r'([^\n]*{}[^\n]*?(?:\n(?!\n)[^\n]*)*)(?:\n{{2,}}|\Z)'.format(keyword)

    # Replace all matched paragraphs with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)  # IGNORECASE to match 'footprint' case-insensitively
    
    return cleaned_text
keyword = "footnote"

# Remove all paragraphs that contain the specified keyword
cleaned_content = remove_paragraph_including(content, keyword)

# Print the cleaned content or save to a new file if it's large
print(cleaned_content)

output_file_path = 'combinedtexts2_handclean_removedfootnotes'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

 
    
    
import re

"""tohle jenom zmeni dokument "the complete works...." na UTF-8 formát a uloží zpátky"""

#ShakespeR
# Read the UTF-8 with BOM file and write it as normal UTF-8
input_file_path = 'data\The Complete Works of William Shakespeare.txt'
output_file_path = 'Shakespear_utf8.txt'
def convert_to_UTF8 (input_file_path,output_file_path):
    with open(input_file_path, 'r', encoding='utf-8-sig') as infile:
        content = infile.read()  # Read the file, automatically strips BOM

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(content)  # Write it as normal UTF-8

    print(f"Converted '{input_file_path}' to '{output_file_path}' without BOM.")
  
    convert_to_UTF8 (input_file_path,output_file_path)
####
"""function in progress"""
def remove_string(text, pattern):
    
    # Replace all matched paragraphs with an empty string
    text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL) 
    return text

roman_numeral_pattern = r'\b[MDCLXVI]+\b'    # Roman numerals
arabic_numeral_pattern = r'\b\d+\b'          # Arabic numerals
name_character_pattern = r'\b[A-Z]{1,}\b'  # Names that start with an uppercase letter and are followed by lowercase letters (fix typo in variable name)
square_bracket_pattern = r'\[.*?\]'         # Text inside square brackets
