from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    # Add other language-specific fields as necessary

    def get_translation(self, lang='en'):
        # Default to English if translation not available
        return getattr(self, f"question_{lang}", self.question)
    
    def __str__(self):
        return self.question
