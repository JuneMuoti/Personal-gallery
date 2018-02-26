from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
def index(request):
    images=Image.my_image()
    return render(request,'index.html',{"images":images})



def about(request):



    return render(request,'about.html')
def contact(request):

    return render(request,'contact.html')


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(query)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})
# Create your views here.
def get_image(request,image_id):
    try:
        imager = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'my_image.html', {"imager":imager})
