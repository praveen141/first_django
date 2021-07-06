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
    djtext = request.POST.get('content', 'default')
    # Check checkbox values
    removepun = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # print(removepun)
    # print(djtext)
    # GET the text
    if removepun == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        params = {'purpose': 'remove stops', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcap == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalize Letters', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n'  and char !='\r':
                analyzed= analyzed +char
        else:
            print('no')
        print("pre" , analyzed)
        params = {'purpose': 'New Line Removers', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if spaceremover == 'on':
        analyzed = djtext.replace('  ', '')
        params = {'purpose': 'Space Removers', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charcount == 'on':
        count = 0
        for char in djtext:
            count += 1
        analyzed = count
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
    if (removepun != 'on' and fullcap != 'on' and newlineremover != 'on' and spaceremover != 'on' and charcount != 'on'):
        return HttpResponse ('Please select any operation and try again')
    return render(request, 'analyze.html', params)