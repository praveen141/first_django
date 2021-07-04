# Praveen created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = { 'dress' : 'skirt', 'brand' : 'Shagun'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Hello Praveen</h1> <a href="https://cleanblog.notes4python.xyz/" >PraveenSite
    # </a>''')


def about(request):
    return HttpResponse(" <h1>Hello Praveen</h1> \n <a href='/'>Back</a>")


def analyze(request):
    # GET the text
    djtext = request.GET.get('content', 'default')
    removepun = request.GET.get('removepunc', 'off')
    print(removepun)
    print(djtext)
    # GET the text
    if removepun != 'off':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed + i
        params = {'purpose': 'remove stops', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
    #return HttpResponse('''<h2> removepunc </h2>
    # <a href="http://127.0.0.1:8000/"> removepunc  </a>''')

#
# def capfirst(request):
#     return HttpResponse('''<h2> capfirst </h2>
#     <a href="http://127.0.0.1:8000/"> capfirst  </a>''')
#
#
# def newlineremove(request):
#     return HttpResponse('''<h2> newlineremover </h2>
#     <a href="http://127.0.0.1:8000/"> newlineremover  </a>''')
#
#
# def charcount(request):
#     return HttpResponse('''<h2> charcount </h2>
#     <a href="https://en.wikipedia.org/wiki/Chandigarh"> charcount  </a>''')
#
#
# def spaceremove(request):
#     return HttpResponse('''<h2> spaceremove </h2>
#     <a href="https://en.wikipedia.org/wiki/Chandigarh"> spaceremove  </a>''')
