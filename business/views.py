from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .crn import call
from .models import Business

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'business/index.html'
    #context_object_name = 'latest_question_list'

    model = Business
    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]

class EditView(generic.FormView):
    template_name = 'business/form.html'
    model = Business

def result(request):
    crn = request.GET['crn']

    result = call(crn)

    return render(request, 'business/results.html', {
        'result': result
    })

