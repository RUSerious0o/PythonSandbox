from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def get_test_view_function(request):
    return render(request, 'function_template.html')


class ClassTestView(TemplateView):
    template_name = 'class_template.html'
