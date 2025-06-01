from django.db import models

class AboutMe(models.Model):
    full_name = models.CharField(max_length=100, default="Birate Kabanza Arthur")
    title = models.CharField(max_length=150, default="Data-Driven Explorer with a Global Journey")

    biography = models.TextField(help_text="Your main story, academic shift, and motivations.")
    passions = models.TextField(help_text="Reading, travel, non-fiction books, etc.")

    # Academic journey fields
    studied_in_china = models.BooleanField(default=True)
    chinese_degree = models.CharField(max_length=100, default="Petroleum Engineering")
    studied_in_belgium = models.BooleanField(default=True)
    belgian_degree = models.CharField(max_length=100, default="Applied Computer Science (AI Track)")
    belgian_institution = models.CharField(max_length=150, default="Thomas More University of Applied Sciences")

    # Languages
    native_language = models.CharField(max_length=50, default="French")
    fluent_languages = models.CharField(max_length=100, default="English")

    strengths = models.TextField(help_text="Comma-separated list of strengths like discipline, reading, global mindset, etc.")

    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_strengths_list(self):
        return [item.strip() for item in self.strengths.split(',') if item.strip()]

    def __str__(self):
        return f"About Me - {self.full_name}"
