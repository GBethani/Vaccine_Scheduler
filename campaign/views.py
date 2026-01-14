from typing import Any
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from campaign.models import Campaign
from shot.models import Vaccination
from campaign.forms import CampaignForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class CampaignListView(LoginRequiredMixin, generic.ListView):
    model = Campaign
    template_name = "campaign/campaign-list.html"
    paginate_by = 1
    ordering = ["-id"]


class CampaignDetailView(LoginRequiredMixin, generic.DetailView):
    model = Campaign
    template_name = "campaign/campaign-detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["registration"] = Vaccination.objects.filter(campaign=self.kwargs["pk"]).count()
        return context


class CampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Campaign
    form_class = CampaignForm
    permission_required = ("campaign.add_campaign",)
    template_name = "campaign/campaign-create.html"
    success_message = "Campaign Created Successfully"
    success_url = reverse_lazy("campaign:campaign-list")

class CampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Campaign
    form_class = CampaignForm
    permission_required = ("campaign:change_campaign",)
    template_name = "campaign/campaign-update.html"
    success_message = "Campaign Updated Successfully"
    success_url = reverse_lazy("campaign:campaign-list")

class CampaignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Campaign
    template_name = "campaign/campaign-delete.html"
    permission_required = ("campaign.delete_campaign",)
    success_message = "Campaign Deleted Successfully"
    success_url = reverse_lazy("campaign:campaign-list")
    
