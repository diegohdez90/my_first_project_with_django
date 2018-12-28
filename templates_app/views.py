from django.shortcuts import render

# Create your views here.
def index(request):
  context = { 'text': 'This is a demo text to cut "hello" from this string', 'number': 100 }
  return render(request, 'templates_app/index.html',context)

def other(request):
  return render(request, 'templates_app/other.html')

def relative(request):
  return render(request, 'templates_app/relative_url_template.html')

