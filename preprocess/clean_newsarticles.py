import re
import csv

#input_file = r'data\novinove_clanky\Fake News Detection\fake.csv'

#pattern pro webove stranky https a twitter musi jit out


def read_csv_to_dict(input_file):
    """Reads a CSV file and returns the data as a list."""
    content_list = [] 
    try: 
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f) 
            for raw in reader:  
                    content_list.append(raw)
        del content_list[-3:]
        return content_list
   
    
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
    # Try alternative encodings if UTF-8 fails
    try:
        with open(input_file, 'r', encoding='latin-1') as f:
            reader = csv.reader(f)
            for raw in reader:  
                    content_list.append(raw) 
        return content_list
    except Exception as alt_e:
        print(f"Alternative encoding failed: {alt_e}")


def remove_string(content_list, pattern_list):
    cleaned_list = []
    for raw in content_list:
        if isinstance(raw, list):
            cleaned_row = []
        for text in raw:
            text = str(text)
            for pattern in pattern_list:
                text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
            cleaned_row.append(text)
        cleaned_list.append(cleaned_row)
    return cleaned_list

#contentlist = remove_string(content_list, pattern_list)
# Example usage

"""def save_list (content_list, output_file):
    #output_file = r'data\cleaned_fakeclanky.txt'
    
    with open (output_file, 'w', encoding='utf-8') as f:
        f.writelines(f"{item}\n" for item in content_list)
#save_list(content_list)"""
def save_list(content_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        # Flatten the list and join elements with a space
        full_text = ' '.join(' '.join(str(item) for item in row) for row in content_list)
        f.write(full_text)
def main():
    myfile = r'data\novinove_clanky\Fake News Detection\fake.csv'
    output_file = 'cleaned_fake2.txt'
    pattern_list = [r'\b\d+\b',r'\[.*?\]',r'\(\): ', r'\*[a-z]+\b', r'https?:\/\/t\.co\/[a-zA-Z0-9]+', r'pic\.twitter\.com\/[a-zA-Z0-9]+',r'\(@[A-Za-z]+\d+\)', r'\(@[A-Za-z]+\)', r'\d+[a-zA-Z]+', r'#[A-Za-z]+']
        
    content_list = read_csv_to_dict (myfile)
    cleaned_list = remove_string(content_list, pattern_list) 
    save_list(cleaned_list,output_file)
    print(f"Successfully processed {len(content_list)} items and saved to {output_file}")
    
if __name__ == "__main__":
    main()
