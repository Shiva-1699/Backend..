from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

# Create a custom form for the admin panel to include CKEditor
class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),  # Apply CKEditor to the answer field
        }

# Register FAQ model with custom form
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm

admin.site.register(FAQ, FAQAdmin)
