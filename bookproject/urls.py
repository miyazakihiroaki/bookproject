from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # urls.pyファイルは上から順にURLの照合が行われる
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    # ↓どんな文字列でrequestが送られてきたとしても「include('book.urls')」を呼び出す。
    path('', include('book.urls')),
]

# Djangoがブラウザからリクエストを受け取ると、まずはプロジェクトのurls.pyがそのrequestを受け取り、requestに記載されたURLとurls.pyファイルに記載されている文字列が一致した場合に、アプリのurls.pyファイルを呼び出すイメージ

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)