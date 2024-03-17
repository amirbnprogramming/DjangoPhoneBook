from abc import abstractmethod

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __(self):
        return self.name

    @abstractmethod
    def get_fields(self):
        pass

    @classmethod
    def get_list_fields(cls):
        pass

    @classmethod
    def get_active_objects(cls):
        return cls.objects.filter(is_active=True).all()

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def get_object_by_name(cls, name):
        return cls.objects.filter(name=name).first()

    @classmethod
    def get_object_by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def delete_all_objects(cls):
        cls.objects.all().delete()


class Country(BaseModel):
    phone_code = models.CharField(max_length=10, db_index=True, verbose_name="phone_code")
    iso_name = models.CharField(max_length=2, unique=True, verbose_name="iso_name")

    def get_fields(self):
        return f'{self.name} - {self.iso_name} - {self.phone_code} '

    @classmethod
    def get_list_fields(cls):
        return ['id', 'name', 'iso_name', 'phone_code']

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        ordering = ['-name']


class State(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="country", related_name="states")

    def get_fields(self):
        return f'{self.name} - {self.country.name}'

    @classmethod
    def get_list_fields(cls):
        return ['id', 'name', 'country']

    class Meta:
        verbose_name = 'state'
        verbose_name_plural = 'states'
        ordering = ['-name']


class City(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="state",related_name="cities")

    def get_fields(self):
        return f'{self.name} - {self.state.name} - {self.state.country.name}'

    @classmethod
    def get_list_fields(cls):
        return ['id', 'name', 'state']

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cties'
        ordering = ['-name']
