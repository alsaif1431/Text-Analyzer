from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    dict = {"name": "saif", "place": "Mars"}
    return render(request, "index.html", dict)
    # return HttpResponse("This is Index page! and we can also provide Links using Anchor Tags!",dict)


def links(request):
    return HttpResponse('''<a href="https://saifpasha.devfolio.io">MySite</a>''')


def about(request):
    return HttpResponse("<h2><i>This is an about page! </i></h2> <a href='/'>Back</a>")


# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse("This is a normal function!<a href='/'>Back</a>")

def analyzer(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    char_count = request.POST.get('char_count', 'off')
    swap_case = request.POST.get('swap_case', 'off')
    space_remover = request.POST.get('space_remover', 'off')
    punctuations = '''!@#$%^&*" " ,[;'];'[:><?]'''
    analyzed = ""

    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuations : ',
                  'Analyzed_texts': analyzed}
        return render(request, 'analyze.html', params)
    elif capitalize == 'on':
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized String : ',
                  'Analyzed_texts': analyzed}
        return render(request, 'analyze.html', params)
    elif char_count == 'on':
        count = 0
        for char in djtext:
            count += 1
        analyzed += str(count)
        params = {'purpose': 'Count', 'Analyzed_texts': analyzed}
        return render(request, 'analyze.html', params)
    elif swap_case == 'on':
        analyzed += djtext.swapcase()
        params = {'purpose': 'SwapCase', 'Analyzed_texts': analyzed}
        return render(request, 'analyze.html', params)
    elif space_remover == 'on':
        for char in djtext:
            if char != " ":
                analyzed += char
        params = {'purpose': 'SpaceRemoved : ', 'Analyzed_texts': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse(f"No Operations Performed :{djtext}")
