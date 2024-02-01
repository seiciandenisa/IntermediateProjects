import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    # it will take a pdf file of type string, and it will return a list  of string
    # each page of the pdf will have the text extracted and inserted as an element of the list
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf,
                           strict=False)  # strict will raise an exception if there are any issues with reading or extraction of the pdf

        print('Pages: ', len(reader.pages))
        print('-' * 20)  # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        # variable that equals a list of string; list comprehension to extract the text from each page
        return pdf_text


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:  # extracting the text from the list
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        # print(split_text)

        all_words += [word for word in split_text if word]
        # if check removes empty spaces because an empty string evaluates to false

    return Counter(all_words)


def main():
    extract_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = count_words(text_list=extract_text)

    for word, mentions in counter.most_common(5):
        print(f'{word:10}:{mentions} times')


if __name__ == '__main__':
    main()

# try to count how many characters are in the pdf of how many word there are
