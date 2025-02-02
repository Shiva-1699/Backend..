from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python framework.",
        )

    def test_get_translation(self):
        self.assertEqual(self.faq.get_translation('en'), self.faq.question)
