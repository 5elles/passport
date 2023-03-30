import datetime

from django.db import models


# Create your models here.

class Countries(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    countryName = models.CharField(
        max_length=40,
        unique=True,
        blank=True,
        null=True,
        verbose_name='страна'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.countryName}'


class SubsFed(models.Model):
    class Meta:
        verbose_name = 'Субъект РФ'
        verbose_name_plural = 'Субъекты РФ'

    sfName = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name='СФ'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.sfName}'


class Regions(models.Model):
    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    regionName = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        verbose_name='область'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.regionName}'


class Districts(models.Model):
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    districtName = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        verbose_name='район'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.districtName}'


class Cities(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    cityName = models.CharField(
        max_length=40,
        unique=True,
        blank=True,
        null=True,
        verbose_name='город'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.cityName}'


class Localities(models.Model):
    class Meta:
        verbose_name = 'Малый нп'
        verbose_name_plural = 'Малые нп'

    localityName = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        verbose_name='н.п.'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.localityName}'


class Streets(models.Model):
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    streetName = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name='улица'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.streetName}'


class Person(models.Model):
    class Meta:
        verbose_name = 'Физлицо'
        verbose_name_plural = 'Физлица'

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'М'),
        (FEMALE, 'Ж')
    ]
    lastnameCyrillic = models.CharField(
        max_length=40,
        verbose_name='фамилия'
    )
    firstnameCyrillic = models.CharField(
        max_length=40,
        verbose_name='имя'
    )
    patronymicCyrillic = models.CharField(
        max_length=40,
        verbose_name='отчество',
        blank=True,
        null=True,
        default=None
    )
    lastnameLatin = models.CharField(
        max_length=40,
        verbose_name='фамилия (латин.)'
    )
    firstnameLatin = models.CharField(
        max_length=40,
        verbose_name='имя (англ.)'
    )
    patronymicLatin = models.CharField(
        max_length=40,
        verbose_name='отчество (англ.)',
        blank=True,
        null=True,
        default=None
    )
    birthDate = models.DateField(
        verbose_name='дата рождения'
    )

    countryOfBirth = models.ForeignKey(
        Countries,
        on_delete=models.CASCADE,
        verbose_name='страна рождения',
        blank=True,
        null=True,
    )
    sfOfBirth = models.ForeignKey(
        SubsFed,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name='субъект РФ'
    )
    regOfBirth = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name='область'
    )
    districtOfBirth = models.ForeignKey(
        Districts,
        on_delete=models.CASCADE,
        verbose_name='район рождения',
        blank=True,
        null=True,
        default=None
    )

    cityOfBirth = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        verbose_name='город рождения',
        blank=True,
        null=True,
        default=None
    )

    localityOfBirth = models.ForeignKey(
        Localities,
        on_delete=models.CASCADE,
        verbose_name='н.п. рождения',
        blank=True,
        null=True,
        default=None
    )

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        verbose_name='пол'
    )

    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.lastnameCyrillic} {self.firstnameCyrillic} {self.patronymicCyrillic} | id - {self.id}'


class Passports(models.Model):
    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    PASSPORT = 'P'
    RESIDENTCARD = 'R'
    IDTYPE = [
        (PASSPORT, 'Паспорт'),
        (RESIDENTCARD, 'Вид на жительство')
    ]
    AUTHORITY = [
        ('MIA', 'МВД'),
        ('MFA', 'МИД')
    ]
    photo = models.ImageField(
        unique=True,
        upload_to='IDphotos',
        verbose_name='фото'
    )

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='владелец ID'
    )

    passport_num = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='номер ID',
    )
    idType = models.CharField(
        max_length=1,
        choices=IDTYPE,
        default='P',
        verbose_name='тип ID'
    )
    dateOfIssue = models.DateField(
        verbose_name='дата выдачи',
        default=datetime.date.today,
    )
    authority = models.CharField(
        max_length=3,
        choices=AUTHORITY,
        verbose_name='кем выдан'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.passport_num} - {self.person}'



class Residence(models.Model):
    class Meta:
        verbose_name = 'Место регистрации'
        verbose_name_plural = 'Места регистрации'

    date = models.DateField(
        default=datetime.date.today,
        verbose_name='дата регистрации',
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='лицо'
    )
    sf = models.ForeignKey(
        SubsFed,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name='субъект РФ'
    )
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name='область'
    )
    district = models.ForeignKey(
        Districts,
        on_delete=models.CASCADE,
        verbose_name='район',
        blank=True,
        null=True,
        default=None,
    )

    city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        verbose_name='город',
        blank=True,
        null=True,
        default=None,
    )

    locality = models.ForeignKey(
        Localities,
        on_delete=models.CASCADE,
        verbose_name='н.п.',
        blank=True,
        null=True,
        default=None
    )
    street = models.ForeignKey(
        Streets,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name='улица'
    )
    house = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        default=None,
        verbose_name='дом'
    )
    body = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        default=None,
        verbose_name='корпус'
    )
    flat = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        default=None,
        verbose_name='квартира'
    )
    slug = models.SlugField(
        null=False,
        db_index=True,
        unique=True,
        verbose_name='URL'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='время изменения',
    )

    def __str__(self):
        return f'{self.city} {self.locality} {self.street} {self.house} {self.body}, {self.flat} | id - {self.id}'
