from django.shortcuts import render
from django.http import HttpResponse
from application.models import SearchForm
from app import search_word
# Create your views here.

def home(request):
    word='computer'
    if request.method=='POST':
        word=request.POST['word']
    result=search_word(word)
    context={'word':word.capitalize(),'syn':result['synonyms'],'definition':result['definition'],'examples':result['examples'],'pos':result['pos'][0][1]}
    return render(request,'index.html',context)

