from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255, default="Object Detection with YOLOv5 & YOLOv8: Where’s Waldo?")
    objective = models.TextField()
    dataset_description = models.TextField(blank=True, null=True)
    model_training = models.TextField(blank=True, null=True)    
    sahi_description = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    key_learnings = models.TextField(blank=True, null=True)

    technologies_used = models.CharField(max_length=500)
    project_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    
    image1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image2 = models.ImageField(upload_to='projects/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies_used.split(',') if tech.strip()]

    def __str__(self):
        return self.title
