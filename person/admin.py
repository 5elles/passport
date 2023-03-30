from django.contrib import admin
from .models import Person, Passports, Residence, Cities, Streets, SubsFed, Districts, Countries, Localities, Regions
from transliterate import translit, get_available_language_codes

# Register your models here.



@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'person', 'city', 'locality', 'street', 'house', 'body', 'flat']
    ordering = ['id', 'person', 'date']
    prepopulated_fields = {'slug': ('city', 'locality', 'street', 'house', 'date')}

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cityName',)}


@admin.register(Streets)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('streetName',)}


@admin.register(SubsFed)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('sfName',)}


@admin.register(Districts)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('districtName',)}


@admin.register(Countries)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('countryName',)}


@admin.register(Localities)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('localityName',)}


@admin.register(Regions)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('regionName',)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'lastnameCyrillic',
        'firstnameCyrillic',
        'patronymicCyrillic',
        'birthDate',
        'slug',
        'time_create',
        'time_update',
    ]
    fields = [
        ('lastnameCyrillic', 'firstnameCyrillic', 'patronymicCyrillic'),
        ('lastnameLatin', 'firstnameLatin', 'patronymicLatin'),
        ('birthDate', 'gender'),
        ('countryOfBirth', 'sfOfBirth', 'regOfBirth', 'districtOfBirth', 'cityOfBirth', 'localityOfBirth'),
        'slug',
    ]
    prepopulated_fields = {
        "slug": ('lastnameCyrillic', 'birthDate', 'firstnameCyrillic'),
        'lastnameLatin': (translit('lastnameCyrillic', language_code='ru', reversed=True),),
        'firstnameLatin': (translit('firstnameCyrillic', language_code='ru', reversed=True),),
    }


@admin.register(Passports)
class PassportsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'passport_num',
        'person',
        'idType',
        'dateOfIssue',
        'authority',
        'slug',
        'time_create',
        'time_update',
    ]
    ordering = ['dateOfIssue', 'person']
    fields = [
        'photo',
        'person',
        ('passport_num', 'idType'),
        ('dateOfIssue', 'authority'),
        'slug',
    ]
    list_per_page = 10
    search_fields = [
        'passport_num',
        'idType',
        'dateOfIssue',
        'authority',
        'slug',
    ]
    prepopulated_fields = {"slug": ('passport_num', 'idType')}
