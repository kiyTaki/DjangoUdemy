from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import persons_list, persons_new, persons_update, persons_delete

urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>', persons_update, name="person_update"),
    path('delete/<int:id>', persons_delete, name="person_delete"),
]
