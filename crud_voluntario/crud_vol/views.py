from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Voluntario

class VoluntarioList(ListView): 
    model = Voluntario

class VoluntarioDetail(DetailView): 
    model = Voluntario

class VoluntarioCreate(CreateView): 
    model = Voluntario

class VoluntarioUpdate(UpdateView): 
    model = Contact

class VoluntarioDelete(DeleteView): 
    model = Voluntario

class UserCreate(CreateView):
    form_class = SignUpForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()