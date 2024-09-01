from django.shortcuts import render
from django.http import HttpResponse
import random
#views - файл, которые работает с запросами пользователя. По сути, здесь прописан бэк-энд.
# Create your views here.

#ф-я для прорисовки домашнего экрана
def home(request):
    return render(request, 'generator/home.html')

#ф-я для прорисовки странички "о сайте"
def about(request):
    return render(request, 'generator/about.html')

#ф-я для прорисовки странички "генерация пароля" и сама генерация
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))#если не указано, то будет 12

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})#загрузка html страницы с контекстом указанным и запросом пользователя
