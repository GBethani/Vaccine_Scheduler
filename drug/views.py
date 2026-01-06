from django.shortcuts import render
from django.views import View
from .models import Drug
from django.http import Http404, HttpResponseRedirect
from .forms import VaccineForm
from django.urls import reverse
from django.shortcuts import get_object_or_404


class VaccineList(View):
    def get(self, request):
        vaccine_list = Drug.objects.all()
        context = {
            "object_list": vaccine_list
        }
        return render(request, "drug/drug-list.html", context)


class VaccineDetail(View):
    def get(self, request, id):
        try:
            vaccine = Drug.objects.get(id=id)
        except Drug.DoesNotExist:
            raise Http404("Vaccine instance not found")
        
        context = {
            "object": vaccine,
        }
        return render(request, "drug/drug-detail.html", context)
    
class CreateVaccine(View):
    form_class = VaccineForm
    template_name = "drug/create-drug.html"

    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vaccine:list"))
        return render(request, self.template_name, {"form": form})


class UpdateVaccine(View):
    form_class = VaccineForm
    template_name = "drug/update-drug.html"

    def get(self, request, id):
        vaccine = get_object_or_404(Drug, id=id)
        context = {
            "form": self.form_class(instance=vaccine),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        vaccine = get_object_or_404(Drug, id=id)
        form = self.form_class(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vaccine:detail", kwargs={"id": vaccine.id}))
        return render(request, self.template_name, {"form": form})


class DeleteVaccine(View):
    template_name = "drug/delete-drug.html"

    def get(self, request, id):
        vaccine = get_object_or_404(Drug, id=id)
        context = {
            "object": vaccine
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        Drug.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse("vaccine:list"))
