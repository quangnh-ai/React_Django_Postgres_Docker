from django.urls import path
import prediction.views as views


# Create url patterns for predict app
urlpatterns = [
    path('predict/', views.IRIS_Model_Predict.as_view(), name='api_predict'),
]