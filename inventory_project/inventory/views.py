from django.shortcuts import render
from django.http import JsonResponse
from .image_processing import process_image
import os

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        os.makedirs('media', exist_ok=True)
        image_path = os.path.join('media', image.name)
        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        extracted_text = process_image(image_path)
        return JsonResponse({'text': extracted_text})
    return render(request, 'upload.html')
