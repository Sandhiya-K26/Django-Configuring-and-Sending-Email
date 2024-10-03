
# urls.py
from django.urls import path
from ex4app import views  # This is importing views from your app, ex4app


urlpatterns = [
    path('send_email/', views.send_email, name='send_email'),  # Map the email function to the URL
]
