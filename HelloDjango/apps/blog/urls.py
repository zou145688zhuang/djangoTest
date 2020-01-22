from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('tag/<int:pk>/',views.CloudTag,name = 'tag'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('category/<int:pk>/',views.CategoryInfo,name='category'),
    path('upload_image/',views.upload_image,name = 'upload_image')

]