from django.conf.urls import url
from severity import views

urlpatterns = [
    url('predict', views.PredictionDetails.as_view()),
]
