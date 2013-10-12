from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .forms import AddForm
from .models import Quote


class AddQuote(CreateView):
    template_name = 'new.html'
    form_class = AddForm
    success_url = '/'


class ViewQuote(DetailView):
    model = Quote
    template_name = 'quote.html'


class QuoteList(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quotes'


class DeleteQuote(DeleteView):
    model = Quote
    template_name = 'delete.html'
    success_url = '/'
