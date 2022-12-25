from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from home.models import Settings, ContactFormu, ContactFormMessage
from Content.models import Content, Category


def index(request):
    settings = Settings.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Content.objects.all()[:6]
    contents = Content.objects.all()[:4]
    lastcontents = Content.objects.all().order_by('-id')[:4]
    randomcontents = Content.objects.all().order_by('?')[:4]
    context = {'settings':settings,
               'page': 'home',
               'sliderdata':sliderdata,
               'category': category,
               'contents':contents,
               'lastcontents':lastcontents,
               'randomcontents':randomcontents
               }
    return render(request, 'index.html', context)


def aktiviteler(request):
    settings = Settings.objects.get(pk=1)
    randomcontents = Content.objects.all().order_by('?')
    context = {'settings':settings,
               'randomcontents':randomcontents}
    return render(request, 'aktiviteler.html', context)


def content_detail(request):
    settings = Settings.objects.get(pk=1)
    content = Content.objects.all().order_by('?')[:1]
    context = {'settings':settings,
               'content':content}
    return render(request, 'content_detail.html', context)

def hakkimizda(request):
    settings = Settings.objects.get(pk=1)
    context = {'settings':settings}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    settings = Settings.objects.get(pk=1)
    context = {'settings':settings}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarıyla gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    settings = Settings.objects.get(pk=1)
    form = ContactFormu()
    context = {'settings':settings, 'form':form}
    return render(request, 'iletisim.html', context)


def category_contents(request, id, slug):
    category = Category.objects.all()
    contents = Content.objects.filter(category_id=id)
    context = {'contents':contents,
               'category':category}
    return render(request, 'aktivite.html', context)


def content_detail(request, id, slug):
    category = Category.objects.all()
    content = Content.objects.get(pk=id)
    context = {'category': category,
               'content':content}
    return render(request, 'content_detail.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş başarısız! Hatalı kullanıcı adı veya parola girişi.")
            return HttpResponseRedirect('/login')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        return HttpResponse("Sign up")
    return render(request), 'signup.html')



