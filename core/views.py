from django.shortcuts import render
import os
import requests
from django.http import HttpResponse
from sources.sources import Sources
from classifier.prediction import Predict
from googletrans import Translator

# Create your views here.

def index(request):
    keyword = 'President kenyatta meets mike sonko'
    print(keyword)
    context={'item':'', 'result':'' }
    if request.method == 'POST':

        item = request.POST['news']
        if item:
            translator = Translator()
            translation = translator.translate(item,dest='en')
            print(type(translation))
            item = translation.text
            print(item)
            # Getting news sources related to the serached item
            news_source = Sources()
            author,title,description,url,source,date = news_source.extract(item)


            # prediction
            prediction = Predict()
            worded , prob =prediction.detecting_fake_news(item)
            prob = round(prob * 100 , 2)
            prob = str(prob)
            prob = prob+"%"

            worded = str(worded)
            worded = worded.upper()

            print(f"Probs is  {prob}   ,and  worded is  {worded}")
            print(type(item))

            context={
            'item':item, 'worded':worded , "probs":prob ,'title':title,'author':author,'description':description,
            'url':url,'source':source,'date':date
            }

            # return HttpResponse(result)
            return render(request,os.path.join('index.html'),context)
        else:
            return render(request,os.path.join('index.html'))
    else:
        return render(request,os.path.join('index.html'),context)



def getResult(request):
    pass