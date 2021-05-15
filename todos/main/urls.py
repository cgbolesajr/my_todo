from django.urls import path
from main import views


urlpatterns=[
        # path('', views.homePageView,name='home'),
        path('', views.HomePageListView.as_view(),name='home'),
        path('contact/', views.contactPageView, name='contact'),
        # path('detail/<todo_id>/', views.todo_detailPageView, name='detail'),
        path('detail/<pk>', views.TodoDetailView.as_view(), name='detail'),
        # path('todo/',views.todo_createPageView,name='todo' ),
        # path('update/<todo_id>', views.todo_updatePageView,name='update'),
        path('update/<pk>', views.TodoUpdateView.as_view(),name='update'),
        path('todo/', views.TodoCreateView.as_view(), name='todo')
    ]
