from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import pdf2image

def convert_pdf_to_images(request):
    global context
    try:
        with open(settings.LOCAL_PDF_PATH, 'rb') as f:
            pdf_bytes = f.read()
        pages = pdf2image.convert_from_bytes(pdf_bytes)
        image_paths = []
        for i, page in enumerate(pages):
            if i > 30 :
                break;
            image_path = f'converted_page_{i+1}.jpg'  # Customize filename
             # page.save(MEDIA_ROOT / image_path , 'JPEG')
             # page.save(f'static/{image_path}', 'JPEG')  # Save to static directory
            image_paths.append(image_path)
    
        
        
    except Exception as e:
        print(f"Error converting PDF: {e}")
    context = {'image_paths': image_paths}
    return render(request,'index.html', context)
    # return HttpResponse(f"{context}Hello, world. You're at the polls index.")
        # return render(request, 'index.html', {'error': 'Error processing PDF'})

    