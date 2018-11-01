from django.shortcuts import render,redirect
from .models import PDF
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import PDFForm
from django.conf import settings
from .summarizer import extract_text_from_pdf
# Create your views here.
def main(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        # print(form)
        pdfURL='.'+str(settings.MEDIA_URL)+'documents/'+str(request.FILES['pdfFile'])
        print(pdfURL)
        if form.is_valid():
            instance=form.save(commit=False)
            # print(videoURL)
            instance.save()
            print(instance.pdfFile.url)
            summary=extract_text_from_pdf("."+instance.pdfFile.url)

            # summary=""
            return render(request,'display.html',{ 'summary' : summary })
    else:
        form = PDFForm()
        return render(request, 'main.html', {
            'form': form
        })
