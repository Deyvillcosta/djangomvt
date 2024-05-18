from django.contrib import admin
from django.urls import path

import estoque.views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', estoque.views.home, name="home")

]
