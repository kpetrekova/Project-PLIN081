import re

def process_paragraphs(input_file, output_paragraphs, output_bin):
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_paragraphs, 'w', encoding='utf-8') as out_paragraphs, \
            open(output_bin, 'w', encoding='utf-8') as out_bin:

        full_paragraph_text = ""  # Stores the entire paragraph content
        char_id = None  # Identifier for CharID

        for line in infile:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # If we encounter a new structured paragraph with `#`, process the previous paragraph
            if "#" in line:
                # Process the previous paragraph, if any exists
                if full_paragraph_text:
                    # Replace '[p]' with a space
                    full_paragraph_text = re.sub(r'\[p\]', ' ', full_paragraph_text)

                    # Process paragraphs with CharID "xxx"
                    if char_id == "xxx":
                        # Write the paragraph to the bin file without modifying brackets
                        out_bin.write(f"{char_id}#{full_paragraph_text}\n")
                    else:
                        # If CharID is not "xxx", process bracketed texts
                        bracketed_texts = re.findall(r'\[.*?\]', full_paragraph_text)
                        for bracketed in bracketed_texts:
                            out_bin.write(f"---#{bracketed}\n")

                        # Remove texts within square brackets
                        full_paragraph_text = re.sub(r'\[.*?\]', '', full_paragraph_text).strip()
                        full_paragraph_text = re.sub(r'\s{2,}', ' ', full_paragraph_text)  # Adjust extra spaces

                        # Write the final paragraph to the output file
                        out_paragraphs.write(f"{full_paragraph_text}\n")

                    # Clear the variable for the next paragraph
                    full_paragraph_text = ""

                # Start a new paragraph and split the new line using `#`
                columns = line.split('#')
                if len(columns) >= 4:
                    char_id, plaintext = columns[2], columns[3]
                    full_paragraph_text = plaintext  # Set the initial paragraph content

            else:
                # Append additional parts of the paragraph that start with '[p]'
                full_paragraph_text += " " + re.sub(r'^\[p\]', ' ', line)


# Function call
process_paragraphs("OSS_database-paragraphs.txt", "Shakespeare-paragraphs.txt", "Shakespeare-bin.txt")
