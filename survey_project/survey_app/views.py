from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView
from .models import ElectionSurveyDetails
from .forms import SurveyForm
from django.db.models import Count


class SurveyFormView(FormView):
    template_name = "survey_form.html"
    form_class = SurveyForm
    success_url = reverse_lazy("survey_app:survey_results")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class ResultsView(TemplateView):
    template_name = "survey_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["results"] = ElectionSurveyDetails.objects.values("party_name").annotate(total=Count("party_name"))
        return context