from django.db import models
from abc import abstractmethod
from Locations.models import Country, State, City


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated_at')

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
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


class Person(BaseModel):
    first_name = models.CharField(max_length=100, verbose_name='first_name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    user_name = models.CharField(max_length=100, verbose_name='user_name', unique=True, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="State")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")
    street = models.CharField(max_length=50, verbose_name='Street')
    postal_code = models.CharField(max_length=15, verbose_name='Postal_Code')
    phone_number = models.CharField(max_length=24, verbose_name='Phone_number', )

    def __str__(self):
        return self.user_name

    @classmethod
    def get_list_fields(cls):
        return ['id', 'first_name', 'last_name', 'user_name', 'country', 'state', 'city', 'street', 'postal_code',
                'phone_number', 'is_active', 'created_at', 'updated_at']

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        ordering = ['-id']
