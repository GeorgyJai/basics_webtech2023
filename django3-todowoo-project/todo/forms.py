from django.forms import ModelForm
from .models import Todo
#форма для создания задачи (нужна для пользовательского ввода)
#форма - это блок, который спрашивает у пользователя какие-то данные (необзятально те, которые запишет себе).
#но в данном случае да, она нужна чтобы создавать задачи, поэтому данные, введенные пользователем, эта форма вносит
# при создании модели, которая уже запишется в БД.


class TodoForm(ModelForm):
    class Meta:#Meta нужна чтобы автоматически из модели взять какие-то нужные поля.
        model = Todo# Чтобы не вручную прописывать их в форме.
        fields = ['title', 'memo', 'important']
#по сути, форма - это проводник между пользователем и объектами разных моделей, хранящихся в БД. (в данном случае)