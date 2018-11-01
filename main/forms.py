from django import forms
from .models import PDF,Doc

class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('pdfFile',)

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('docFile',)
