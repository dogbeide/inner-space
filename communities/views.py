from django.shortcuts import render
from django.contrib import messages
# COMMUNITIES views
# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from communities.models import Community,CommunityMember

from . import models

class CreateCommunity(generic.CreateView,LoginRequiredMixin):
    fields = ('name','description')
    model = Community

class SingleCommunity(generic.DetailView):
    model = Community

class ListCommunities(generic.ListView):
    model = Community

class JoinCommunity(generic.RedirectView,LoginRequiredMixin):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('communities:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        community = get_object_or_404(Community,slug=self.kwargs.get('slug'))

        try:
            CommunityMember.objects.create(user=self.request.user,community=community)
        except IntegrityError:
            messages.warning(self.request,"Oops, you're already a member.")
        else:
            messages.success(self.request,"Welcome to the {} community!".format(community.name))

        return super().get(request,*args,**kwargs)

class LeaveCommunity(generic.RedirectView, LoginRequiredMixin):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('communities:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            member = models.CommunityMember.objects.filter(
                user=self.request.user,
                community__slug=self.kwargs.get('slug')
            ).get()
        except models.CommunityMember.DoesNotExist:
            messages.warning(self.request,"Oops, you're not a member yet.")
        else:
            member.delete()
            messages.success(self.request,"You have left this community.")

        return super().get(request,*args,**kwargs)

#
