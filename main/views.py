from django.shortcuts import render,redirect
from .models import PDF,Doc
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import PDFForm,DocForm
from django.conf import settings
from .summarizer import extract_text_from_pdf
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from docx import Document
# Create your views here.
def main(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        # print(form)
        pdfURL='.'+str(settings.MEDIA_URL)+'documents/'+str(request.FILES['pdfFile'])
        print(pdfURL)
        if form.is_valid():
            instance=form.save()
            # print(videoURL)
            # instance.save()
            # print(instance.pdfFile.url)
            summary=extract_text_from_pdf("."+instance.pdfFile.url)

            # summary=""
            return render(request,'display.html',{ 'summary' : summary,'type':'pda' })
    else:
        form = PDFForm()
        form2 = DocForm()
        return render(request, 'main.html', {
            'form': form,
            'form2': form2
        })

def docsum(request):
    if request.method == 'POST':
        # print(form)
        form = DocForm(request.POST, request.FILES)
        # print(form)
        docURL='.'+str(settings.MEDIA_URL)+'documents/'+str(request.FILES['docFile'])
        print(docURL)
        if form.is_valid():
            instance=form.save()
            # print(videoURL)
            # instance.save()
            print(instance.docFile.url)

            document = Document("."+instance.docFile.url)
            docText = b"\n\n".join([paragraph.text.encode('utf-8') for paragraph in document.paragraphs])
            # summary=""
            print(docText.decode('utf-8'))
            d=docText.decode('utf-8')
            return render(request,'display.html',{ 'summary' : d,'type':'doc' })

def textsum(request):
    if request.method == 'POST':
        text=request.POST.get('text')
        # print(form)
        print(text)
        summarizer = LexRankSummarizer()
        #Summarize the document with 2 sentences
        parser=PlaintextParser(text,Tokenizer("english"))
        count=len(text.split("."))
        length=10
        while(length>count):
            length=count/2
        summary = summarizer(parser.document, length)
        return render(request,'display.html',{ 'summary' : summary, 'type':'pdf' })
