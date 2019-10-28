from django.urls import path
from .views import ListMessageView, ListSettingView, ListPaySystemView


urlpatterns = [

    path('messages/', ListMessageView.as_view(), name="messages-all"),
    path('settings/', ListSettingView.as_view(), name="settings-all"),
    path('paysystems/', ListPaySystemView.as_view(), name="paysystems-all"),
    
]