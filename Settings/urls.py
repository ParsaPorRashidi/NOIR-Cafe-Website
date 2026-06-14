from django.urls import path
from .views import HomeAPIView , WaiterCallCreateView, ActiveWaiterCallsView, ResolveWaiterCallView

urlpatterns = [
    path('api/home/', HomeAPIView.as_view(), name='home-api'),
    path('api/waiter/call/', WaiterCallCreateView.as_view(), name='create_waiter_call'),
    path('api/waiter/active-calls/', ActiveWaiterCallsView.as_view(), name='get_active_calls'),
    path('api/waiter/resolve/<int:pk>/', ResolveWaiterCallView.as_view(), name='resolve_waiter_call'),
]