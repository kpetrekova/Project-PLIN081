import re
from sys import argv

def analyse_text(input_text):
    """Calculate the percentage of the letter a in the text and compare with Czech.""" 
    text = re.sub(r'[^a-zá-ž]', '', input_text.lower())
    a_count = text.count("a")/len(text)
    # Subtract the relative frequency of occurrences of the letter a in the received text
    # from the result of the frequency analysis of graphemes in the factual style (1983).
    # See http://sas.ujc.cas.cz/archiv.php?art=2913
    result = 0.062193 - a_count 
    return result * 100

if len(argv) > 1:
    input_text = " ".join(argv[1:])
    result = analyse_text(input_text)
    symbol = "more" if result < 0 else "less"
    print(f"There are {abs(result)}% {symbol} \"a\" characters in this text than in the regular Czech text.")
else:
    print("Please enter some text to analyse.")