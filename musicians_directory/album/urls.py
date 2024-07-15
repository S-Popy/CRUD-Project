from django.urls import path
from . import views

urlpatterns = [
    path('add_album/', views.add_album, name = 'add_album'),
    path('edit/<int:id>', views.edit_data, name = 'edit_data'),
    path('delete/<int:id>', views.delete_data, name = 'delete_data'),
]