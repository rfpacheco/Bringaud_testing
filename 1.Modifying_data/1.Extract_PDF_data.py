import pdfplumber
import pandas as pd
from seaborn.external.docscrape import header


def extract_text_from_all_pages_with_layout(pdf_path):
    all_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text.append(page.extract_text())
    return "\n\n".join(all_text)  # Use double newlines to indicate a new page

def text_to_dataframe(text):
    lines = text.split('\n')
    # Customize this part based on the specific format of your table
    data = [line.split() for line in lines]
    columns = data[0]
    rows = data[1:]
    df = pd.DataFrame(data=rows, columns=columns)
    df.dropna(inplace=True)  # Remove the 'new page' marker, that is a residue of '\n\n'
    return df


def save_dataframe_to_csv(df, csv_path):
    df.to_csv(csv_path, index=False, header=True, sep=',')


def main():
    pdf_path = '../0.1.data/Bringaud_SIDERs.pdf'
    csv_path = '../0.1.data/bringaud_siders.csv'

    text = extract_text_from_all_pages_with_layout(pdf_path)
    df = text_to_dataframe(text)
    save_dataframe_to_csv(df, csv_path)


if __name__ == '__main__':
    main()
