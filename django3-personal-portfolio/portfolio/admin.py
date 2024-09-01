from django.contrib import admin
from .models import Project
#прописываем чтобы отображалась табличка на странице сайта (та табличка, которая в models прописана)
admin.site.register(Project)
