
import io
from sumy.summarizers.lex_rank import LexRankSummarizer

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    parser=PlaintextParser(text,Tokenizer("english"))
    count=len(text.split("."))
    length=10
    while(length>count):
        length=count/2
    summary = summarizer(parser.document, length)
    for sentence in summary:
        print(sentence)
    # if text:
    #     return text
    return summary

if __name__ == '__main__':
    print(extract_text_from_pdf('Documentation.pdf'))
