from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from .forms import UserForm
from .models import Form, Skills, Category
from django.views.generic import(CreateView)
from django.http import HttpResponse, HttpResponseRedirect
from .pre import prediction_engine

"""class FirstPage(View):
    form_class = UserForm
    template_name = 'user_form/form.html'

    def get(self, request):
        form = self.form_class(None)
        user = request.user
        print(user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        form.save(self)

def load_skills(request):
    category_id = request.GET.get('category')
    skills = Skills.objects.filter(category_id = category_id).order_by('name')
    return render(request, 'user_form/skills.html', {'skills': skills})"""

#recent
"""class FirstPage(CreateView):
    model = Form
    fields = ['category','skills','income','edu_qualification']
    #success_url ='predict/'

    def get(self, request):
        category = Category.objects.all()
        skills = Skills.objects.all()
        return render(request, 'user_form/form_form.html', {'category': category, 'skills':skills})"""

class FirstPage(CreateView):
    model = Form
    fields = ['category','skills','income','edu_qualification']
    success_url ='predict/'

    def form_valid(self,form):
        article = form.save(commit=False)
        article.user = self.request.user
        return super(FirstPage, self).form_valid(form)


"""
    def post(self,form):
        form1= Form.objects.create()
        article = form1.save(form)
        article.user = self.request.user
        return HttpResponseRedirect("http://127.0.0.1:8000/form/predict")

    def load_form(request):
        category = Category.objects.all()
        return render(request, 'user_form/form_form.html', {'category': category})"""

def load_skills(request):
    category_id = request.GET.get('category')
    skills = Skills.objects.filter(category_id = category_id).order_by('name')
    return render(request, 'user_form/skills.html', {'skills': skills})

def predict_engine(request):
    current_user = request.user
    user_id = current_user.id
    data = Form.objects.filter(id = int(user_id))
    list_data= []
    for i in data:
        skill = i.skills.name
        category = i.category.name
        list_data =prediction_engine([str(skill)],str(category))
    print (list_data)
    return HttpResponseRedirect('done')