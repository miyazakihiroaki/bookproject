from django.urls import path

from . import views

urlpatterns = [
    path('fileupload/',views.uploadview),
    path('', views.index_view, name='index'),
    path('book/new', views.index_new_view, name="new"),
    path('book/price', views.index_price_view, name="price"),
    path('book/price_reverse', views.index_price_reverse_view, name="price-reverse"),
    path('book/', views.ListBookView.as_view(), name="list-book"),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name="detail-book"),
    path('book/create/', views.CreateBookView.as_view(), name="create-book"),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name="delete-book"), 
    path('book/<int:pk>/update', views.UpdateBookView.as_view(), name="update-book"), 
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),
    path('finish_delete', views.FinishDeleteView.as_view(), name="finish-delete"),
    path('finish_add', views.FinishAddView.as_view(), name="finish-add"),
    path('finish-update', views.FinishUpdateView.as_view(), name="finish-update") ,
]

# nameを忘れない
