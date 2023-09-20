from .models import Finch, Sponsor
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
   finch = Finch.objects.get(id=finch_id)
   id_list = finch.sponsors.all().values_list('id')
   sponsors_finch_doesnt_have = Sponsor.objects.exclude(id__in=id_list)
   feeding_form = FeedingForm()
   return render(request, 'finches/detail.html', {
      'finch': finch,
      'feeding_form': feeding_form,
      'sponsors': sponsors_finch_doesnt_have
    })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form) 
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['population', 'habitat', 'description', 'population_trend']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

class SponsorList(ListView):
  model = Sponsor

class SponsorDetail(DetailView):
  model = Sponsor

class SponsorCreate(CreateView):
  model = Sponsor
  fields = '__all__'

def assoc_sponsor(request, finch_id, sponsor_id):
  Finch.objects.get(id=finch_id).sponsors.add(sponsor_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_sponsor(request, finch_id, sponsor_id):
  Finch.objects.get(id=finch_id).sponsors.remove(sponsor_id)
  return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)