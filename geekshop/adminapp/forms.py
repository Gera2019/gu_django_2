from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from django.forms import ModelForm

from mainapp.models import Product, ProductsCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CategoryCreationForm(ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CategoryEditForm(ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''