from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Person, Passports, Residence
from django.db.models import Q
# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person/person_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'person'


class DocumentDetailView(DetailView):
    model = Passports
    template_name = 'person/doc_detail.html'
    slug_field = 'slug'
    context_object_name = 'document'


class ResidenceDetailView(DetailView):
    model = Residence
    template_name = 'person/residence_detail.html'
    slug_field = 'slug'
    context_object_name = 'residence'


class SearchResults(ListView):
    model = Person
    template_name = 'person/search_results.html'

    def get_queryset(self):
        lastname_c = self.request.GET.get('lastname_c')
        firstname_c = self.request.GET.get('firstname_c')
        patronymic_c = self.request.GET.get('patronymic_c')
        lastname_l = self.request.GET.get('lastname_l')
        firstname_l = self.request.GET.get('firstname_l')
        patronymic_l = self.request.GET.get('patronymic_l')
        id_num = self.request.GET.get('id_num')
        day = self.request.GET.get('day')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')
        gender = self.request.GET.get('gender')
        id_type = self.request.GET.get('id_type')
        pass_num = self.request.GET.get('pass_num')
        pass_day = self.request.GET.get('pass_day')
        pass_month = self.request.GET.get('pass_month')
        pass_year = self.request.GET.get('pass_year')
        sf = self.request.GET.get('sf')
        region = self.request.GET.get('region')
        # district = self.request.GET.get('district')
        city = self.request.GET.get('city')
        # locality = self.request.GET.get('locality')
        street = self.request.GET.get('street')
        house = self.request.GET.get('house')
        body = self.request.GET.get('body')
        flat = self.request.GET.get('flat')

        object_list = Person.objects.filter(
            Q(lastnameCyrillic__iregex=lastname_c) & Q(firstnameCyrillic__iregex=firstname_c) & Q(
                patronymicCyrillic__iregex=patronymic_c) &
            Q(lastnameLatin__iregex=lastname_l) & Q(firstnameLatin__iregex=firstname_l) & (Q(
                patronymicLatin__iregex=patronymic_l) | Q(patronymicLatin__isnull=True)) & Q(birthDate__day__iregex=day)
            & Q(birthDate__month__iregex=month) & Q(birthDate__year__iregex=year) & Q(id__iregex=id_num)
            & Q(gender__iregex=gender) & Q(passports__idType__iregex=id_type) & Q(
                passports__passport_num__iregex=pass_num) & Q(passports__dateOfIssue__day__iregex=pass_day) &
            Q(passports__dateOfIssue__month__iregex=pass_month) & Q(passports__dateOfIssue__year__iregex=pass_year)
            & (Q(residence__sf__sfName__iregex=sf) | Q(residence__sf__sfName__isnull=True))
            # & (Q(residence__region__regionName__iregex=region) | Q(residence__region__regionName__isnull=True))
            # & (Q(residence__district__districtName__contains=district) | Q(residence__district__districtName__isnull=True))
            & (Q(residence__city__cityName__contains=city) | Q(residence__city__cityName__isnull=True))
            # & (Q(residence__locality__localityName__iregex=locality) | Q(residence__locality__localityName__isnull=True))
            & (Q(residence__street__streetName__iregex=street) | Q(residence__street__streetName__isnull=True))
            & ((Q(residence__house__iregex=house)) | Q(residence__house__isnull=True))
            # & (Q(residence__body=body) | Q(residence__body__isnull=True))
            & (Q(residence__flat__iregex=flat) | Q(residence__flat__isnull=True))

        ).order_by('lastnameCyrillic', 'firstnameCyrillic', 'patronymicCyrillic', 'id')

        return set(object_list)


class SearchPersons(TemplateView):
    template_name = 'person/search_persons.html'
