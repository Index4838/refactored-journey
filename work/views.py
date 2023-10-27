from django.shortcuts import render
import aspose.words as aw
import tempfile
from django.http import FileResponse
import os

def convert_to_pdf(request):
    if request.method == 'POST' and request.FILES.get('docx_file'):
        docx_file = request.FILES['docx_file']

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in docx_file.chunks():
                temp_file.write(chunk)

       
        try:
            doc = aw.Document(temp_file.name)

            saveOptions = aw.saving.PdfSaveOptions()
            saveOptions.compliance = aw.saving.PdfCompliance.PDF17 

            doc.save("PDF.pdf", saveOptions)
        finally:
            temp_file.close()  

    return render(request, 'index.html')

def download_file(request):
    file_path = os.path.join('PDF.pdf')  
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response





def index(request):
   
    
    return render(request, 'index.html')