from django.shortcuts import render


# Create your views here.
def about(request):
    '''
    renders the about page of the website using the dictionary function
    '''
    return render(request, 'about/about_page.html')
