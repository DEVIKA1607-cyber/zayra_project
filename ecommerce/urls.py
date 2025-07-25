from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import role_redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('products/', include('products.urls')),
    path('content/', include('prod_content.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('delivery/', include('delivery.urls')),
    path('analytics/', include('analytics.urls')),
    path('redirect/', role_redirect_view, name='role_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)