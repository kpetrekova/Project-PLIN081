"""Take files from one directory and adds them to csv to create a dataset. Intended for one-time use."""

from regex_sentence_segmentation import sentence_segmentation
import pandas as pd
import os
from sys import argv


def process_txt_to_df(filepath, is_shakespeare):
    """Split the text of the file into sentences, assigns a category, and stores them in a dataframe."""

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read()

    sentences = sentence_segmentation("".join(lines))

    dataframe = pd.DataFrame(sentences, columns=["sentence"])

    labels = []
    for _ in range(len(dataframe)):
        if is_shakespeare == "y":
            labels.append(1)
        else:
            labels.append(0)

    dataframe["label"] = labels
    return dataframe


def save_dataset_to_csv(df):
    """Save the dataset to csv, if the file does not exist, also adds header."""

    if os.path.isfile("sh_dataset.csv"):
        df.to_csv("sh_dataset.csv", mode="a", sep="#", encoding="utf-8", header=False, index=False)
    else:
        df.to_csv("sh_dataset.csv", mode="w", sep="#", encoding="utf-8", header=True, index=False)


if __name__ == "__main__":

    if len(argv) == 2:
        directory = "".join(argv[1:])

        data = input("Are there data of the same type (Shakespeare/not Shakespeare) in the directory? (y/n) ").lower()

        if data == "y":
            is_sh = input("Are there Shakespeare's texts? (y/n) ").lower()
            if is_sh not in "yn":
                print("Invalid input.")
                exit(1)

        elif data == "n":
            print("Choose directory only with one type of data.")
            exit(1)

        else:
            print("Invalid input.")
            exit(1)

        for filename in os.scandir(directory):
            if filename.is_file() and filename.path.endswith(".txt"):   # use only .txt files from the directory
                df = process_txt_to_df(filename.path, is_shakespeare=is_sh)
                save_dataset_to_csv(df)

    else:
        print("Invalid input. Needs one directory path.")
        print("Example: " + argv[0] + " path/to/dir")
        exit(1)
