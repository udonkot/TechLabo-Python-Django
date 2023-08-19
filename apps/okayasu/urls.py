from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Add your urls here.
app_name = 'okayasu'

urlpatterns = [
    # ユーザページ表示
    path('', views.okayasu_page),

    # data取得
    path('data/', views.data_request, name='data_request'),
    # query実行
    path('select/data/', views.query_select_data),
    path('insert/data/', views.query_insert_data),
]
