from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from .forms import UserForm
from .models import Form, Skills
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

class FirstPage(CreateView):
    model = Form
    fields = ['category','skills','income','edu_qualification']
    success_url ='predict/'

    def form_valid(self,form):
        article = form.save(commit=False)
        article.user = self.request.user
        return super(FirstPage, self).form_valid(form)


def load_skills(request):
    category_id = request.GET.get('category')
    skills = Skills.objects.filter(category_id = category_id).order_by('name')
    return render(request, 'user_form/skills.html', {'skills': skills})

def predict_engine(request):
    print ('running')
    current_user = request.user
    user_id = current_user.id
    data = Form.objects.filter(id = int(user_id-1))
    list_data = []
    print (user_id,'user id',data)
    for i in data:
        skill = i.skills.name
        category = i.category.name
        print (category)
        list_data = prediction_engine([str(skill).split()],str(category))
    #print (skill,category)
    print  (list_data)
    context_dict = dict()
    for i in list_data:
        context_dict['%s' % (i)]:i
    return render(request,'user_form/dashboard.html',context_dict)
