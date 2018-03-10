"""mynewsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from myapp.views import about, listing, disp_detail, index, list_article, disp_article, post


article_patterns = [
    url(r'^$', list_article),
    url(r'^([a-zA-Z]+)/$', disp_article),
    ]

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', index),
    url('^about/', about),
    url('^list/$', listing),
    url('^list/([0-9a-zA-Z]+)/$', disp_detail),
    url('^list_article/', include(article_patterns)),
    url(r'post/(?P<post_date>\d{4}/\d{1,2}/\d{1,2})$', post)
]
