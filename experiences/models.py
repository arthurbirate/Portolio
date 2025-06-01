from django.db import models

class Internship(models.Model):
    company_name = models.CharField(max_length=255)
    period = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    
    tasks = models.TextField(
        help_text="Comma-separated list of tasks (e.g., Built dashboards, Configured agents)"
    )
    tools_technologies = models.CharField(
        max_length=500,
        help_text="Comma-separated list of tools (e.g., Kibana, Grafana, Kafka)"
    )
    key_contributions = models.TextField(
        help_text="Comma-separated list of key contributions"
    )
    achievements = models.TextField(
        help_text="Comma-separated list of achievements"
    )
    
    technical_reflection = models.TextField()
    personal_reflection = models.TextField()

    def __str__(self):
        return f"{self.company_name} ({self.period})"

    def get_tasks_list(self):
        return [task.strip() for task in self.tasks.split(',') if task.strip()]

    def get_tools_list(self):
        return [tool.strip() for tool in self.tools_technologies.split(',') if tool.strip()]

    def get_achievements_list(self):
        return [ach.strip() for ach in self.achievements.split(',') if ach.strip()]

    def get_contributions_list(self):
        return [contrib.strip() for contrib in self.key_contributions.split(',') if contrib.strip()]
