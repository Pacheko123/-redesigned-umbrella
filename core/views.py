from django.shortcuts import render
import os

from detector.sources import Sources

# Create your views here.

def index(request):
	keyword = 'President kenyatta meets mike sonko'
	source = Sources(keyword)
	source.extract(keyword)

	context={'name':'Relatively Fake'}
	return render(request,os.path.join('index.html'),context)


def getResult(request):
   # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)