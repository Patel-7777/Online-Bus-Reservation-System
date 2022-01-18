from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    # path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    # path("service", views.service, name='service'),
    path("sign-up", views.sign_up, name='sign-up'),
    path("book", views.book, name='book'),
    path("admin", views.admin, name='admin'),
    path("deleteBus/<int:pk>", views.deleteBus, name='deleteBus'),
    path("deletehistory/<int:pk>", views.deletehistory, name='deletehistory'),
    path("bookBus/<str:name>/<str:pick>/<str:dest>/<str:ptime>/<str:dtime>/<int:fare>/<str:bustype>/<str:date>", views.book_Bus, name='book_Bus'),
    path("login", views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path("trackBus", views.trackBus, name='trackBus'),
    path("PassInfo", views.PassInfo, name='PassInfo'),
    path("history", views.history, name='history')
   
]