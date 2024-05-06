from django import forms

from main.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'active_version':
                field.widget.attrs['class'] = ' form-check-input'

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('product_name', 'product_description', 'product_image', 'product_price', 'product_category',)
        # exclude = ('is_active')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        banned_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                        'бесплатно', 'обман', 'полиция', 'радар')

        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'В названии продукта присутствует запрещенное слово {word}!')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        banned_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                        'бесплатно', 'обман', 'полиция', 'радар')

        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'В описании продукта присутствует запрещенное слово {word}!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

