from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm

from .mixins import FormUserNeededMixin, UserOwnerMixin


#from django import forms
#from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class=TweetModelForm
    template_name='tweets/create_view.html'
    #success_url = '/tweet/create'
    #success_url = reverse_lazy('tweet:detail)
    

#class TweetCreateView(FormUserNeededMixin,LoginRequiredMixin,CreateView):
 #   form_class=TweetModelForm
  #  template_name='tweets/create_view.html'
   # success_url = '/tweet/create'
    #login_url = '/admin/'




#class TweetCreateView(CreateView):
    #form_class = TweetModelForm
   # template_name='tweet/create_view'
    #success_url = '/tweet/create'

    #def form_valid(self, form):
     #   if request.iser.is_authenticated():
      #      form.instance.user = self.request.user
       #     return super(TweetCreateView, self).form_valid(form)
#
 #       else:
  #          form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList('User must be logged in')
   #         return self.form_invalid(form)

#def tweet_create_view(request):
 #   form = TweetModelForm(request.POST or None)
#
 #   if form.is_valid():
  #      instance = form.save(commit=False)
   #     instance.user = request.user
    #    instance.save()
#
 #   context = {
  #      'form':form,
   #     
    #}
#
 #   return render(request, 'tweets/create_view', context)

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/tweet_confirm_delete.html'
    success_url = reverse_lazy('tweet:list')


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name='tweets/detail_view.html'


#class TweetDetailView(DetailView):
    #queryset = Tweet.objects.all()
    #template_name='tweets/detail_view.html'

   # def get_object(self):
    #    return Tweet.objects.get()

class TweetListView(ListView):
    template_name = 'tweets/list_view.html'
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()

        query = self.request.GET.get('q', None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains=query) 
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm
        context['create_url'] = reverse_lazy('tweet:create')
        return context


#class TweetListView(ListView):
 #   queryset = Tweet.objects.all()
  #  template_name = 'tweets/list_view.html'
##
  #  def get_context_data(self, *args, **kwargs):
   #     context = super(TweetListView, self).get_context_data(*args, **kwargs)
    #    return context



#def tweet_detail_view(request, pk=None):
   # obj =  get_object_or_404(Tweet, pk=pk)

  #  template_name='tweets/detail_view.html'
 #   context = {'object':obj}
#    return render(request, template_name, context)
#

#def tweet_list_view(request):
 #   queryset = Tweet.objects.all()
  #  template_name = 'tweets/list_view.html'
   # context = {'object_list':queryset}
    #return render(request, template_name, context)