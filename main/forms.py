from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
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
                raise forms.ValidationError('В названии продукта присутствует запрещенное слово!')

        return cleaned_data