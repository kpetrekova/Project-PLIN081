import re

def process_paragraphs(input_file, output_paragraphs, output_bin):
    """
    Processes structured paragraphs from an input file, extracts and formats content,
    and saves results to separate output files.

    The input file is an extracted table from a Microsoft Access database on the Open Source Shakespeare website
    (https://www.opensourceshakespeare.org). The data is organized into four columns in the format:

        `WorkID#ParagraphID#CharID#PlainText`

    - `WorkID`: Identifier of the work (e.g., the title of the play or sonnet).
    - `ParagraphID`: Unique identifier for each paragraph within the given work.
    - `CharID`: Character identifier, which may contain the character's name or `"xxx"` for stage directions.
    - `PlainText`: The main text content of the paragraph, which may contain special markers such as `[p]`
      (indicating a line break) or other text in square brackets.

    Function behavior:
    - If `CharID` is `"xxx"`, indicating a stage direction, the entire paragraph is written to `shakespeare_bin.txt`
      as is, prefixed with `xxx`.
    - If `CharID` is not `"xxx"`, the function replaces all `[p]` markers with spaces to remove line breaks
      and extracts any text within square brackets. These extracted texts are saved to `shakespeare_bin.txt` prefixed with `---`,
      while the cleaned paragraph is saved as a single line to `shakespeare_paragraphs.txt`.

    Example input line in `oss_database_paragraphs.txt`:
        12night#631279#belch#Here comes the little villain.
        [p][Enter MARIA]
        [p]How now, my metal of India!

    Example output:
        - In `shakespeare_paragraphs.txt` file:
            Here comes the little villain. How now, my metal of India!

        - In `shakespeare_bin.txt` file:
            ---#[Enter MARIA]
            xxx#[Exit]
    """

    with open(input_file, 'r', encoding='utf-8') as input_file_handler, \
            open(output_paragraphs, 'w', encoding='utf-8') as output_paragraphs_handler, \
            open(output_bin, 'w', encoding='utf-8') as output_bin_handler:

        full_paragraph_text = ""  # Holds combined content of a paragraph across multiple lines
        char_id = None

        for line in input_file_handler:
            line = line.strip()

            if not line:
                continue

            # If we encounter a new structured paragraph with `#`, process the previous paragraph
            if "#" in line:
                # Process the previous paragraph, if any exists
                if full_paragraph_text:
                    # Replace '[p]' with a space
                    full_paragraph_text = full_paragraph_text.replace("[p]", " ")

                    # Process paragraphs with CharID "xxx"
                    if char_id == "xxx":
                        # Write the paragraph to the bin file without modifying brackets
                        output_bin_handler.write(f"{char_id}#{full_paragraph_text}\n")
                    else:
                        # If CharID is not "xxx", process bracketed texts
                        bracketed_texts = re.findall(r'\[.*?\]', full_paragraph_text)
                        for bracketed in bracketed_texts:
                            output_bin_handler.write(f"---#{bracketed}\n")

                        # Remove texts within square brackets
                        full_paragraph_text = re.sub(r'\[.*?\]', '', full_paragraph_text).strip()
                        full_paragraph_text = re.sub(r'\s{2,}', ' ', full_paragraph_text)  # Adjust extra spaces

                        # Write the final paragraph to the output file
                        output_paragraphs_handler.write(f"{full_paragraph_text}\n")

                    # Clear the variable for the next paragraph
                    full_paragraph_text = ""

                # Start a new paragraph and split the new line using `#`
                columns = line.split('#')
                if len(columns) >= 4:
                    char_id, plaintext = columns[2], columns[3]
                    full_paragraph_text = plaintext  # Initialize new paragraph content

            else:
                # Append additional parts of the paragraph that start with '[p]'
                full_paragraph_text += " " + line.replace("[p]", " ")


# Function call
process_paragraphs("data/shakespeare_data_cleaning/oss_database_paragraphs.txt", "data/shakespeare_data_cleaning/shakespeare_paragraphs.txt", "data/shakespeare_data_cleaning/shakespeare_bin.txt")
