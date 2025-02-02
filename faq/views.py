from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()  # Get all FAQs from the database
    return render(request, 'faq/faq_list.html', {'faqs': faqs})
