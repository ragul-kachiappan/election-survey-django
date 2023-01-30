from django.urls import path
from survey_app.views import SurveyFormView, ResultsView

app_name = "survey_app"

urlpatterns = [
    path("survey/fill/", SurveyFormView.as_view(), name="survey_form"),
    path("survey/results/", ResultsView.as_view(), name="survey_results"),
]