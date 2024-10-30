import re


def sent_segmentation(text):
    """Return a list of sentences from the text."""
    
    text = text.replace("\n", " ")
    while "  " in text:
        text = text.replace("  ", " ")

    sentences = []
    sent = ""

    for i in range(len(text)-2):

        # sentence can't start with end quotations marks
        if len(sent) == 0 and text[i] == "\"“":
            break

        # check if not end of text
        # check if char is interpunction
        # check if previous char is not capital (no segmentation on abreviations)
        # check if char after space is capital
        # check beginning of next sentence
        elif (i == len(text)-1 or i != len(text)-3 or i != len(text)-2 or i != 0) \
            and (re.search(r"[.!?;:]", text[i]) \
            and re.search(r"[^A-Z]", text[i-1]) \
            and (re.search(r"[A-Z'“\"]", text[i+2])) \
            or (re.search(r"[\"”]", text[i+1]) and re.search(r"[A-Z'“\"]", text[i+3]))):

            # if next char end of quotation, append both
            if re.search(r"[\"”]", text[i+1]):
                sentences.append(sent + text[i] + text[i+1])
                sent = ""
            else:
                sentences.append(sent + text[i])
                sent = ""
        else:
            sent += text[i]

    # append last sentence of the text + its interpunction
    sentences.append(sent + text[len(text)-2:])

    clean_sentences = []

    for sent in sentences:

        if sent[0] == " " or sent[0] == "\n":
            sent = sent[1:]
            clean_sentences.append(sent + "\n")

        elif (sent[0] == "”" or sent[0] == "\"") and sent[1] == " ":
            sent = sent[2:]
            clean_sentences.append(sent + "\n")
        else:
            clean_sentences.append(sent + "\n")

    return clean_sentences


def preprocess_from_file(filename):
    """Create a new file with segmented text extracted from the txt file. Can be used for preprocessing dataset."""

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    segmented_text = sent_segmentation(text)

    new_file_name = filename[:len(filename)-4] + "_sentences.txt"

    with open(new_file_name, "w", encoding="utf-8") as f:
        for sent in segmented_text:
            f.write(sent)

    print("done")
