# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from payement_app import views
#
# router = DefaultRouter()
# router.register('razorpay', views.PaymentViewSet)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('payment/', include(router.urls())),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payement_app.views import PaymentViewSet

router = DefaultRouter()
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('razorpay/', include(router.urls)),
]