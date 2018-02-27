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
        queryList = request.GET.get("image")
        searched_images = Image.search_by_category(queryList)
        message = f"{queryList}"

        return render(request, 'search.html',{"message":message,"imagey": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})
def location_results(request):

        location_images = Image.filter_by_location()

        return render(request, 'location.html',{"images": location_images})

# Create your views here.
def get_image(request,image_id):
    try:
        imager = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'my_image.html', {"imager":imager})
