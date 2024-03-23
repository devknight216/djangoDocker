from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=100)
    address = models.GenericIPAddressField()
    STATUS_CHOICES = (
        (0, 'offline'),
        (1, 'error'),
        (2, 'online'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)

class Analyzer(models.Model):
    name = models.CharField(max_length=100)
    TYPE_CHOICES = (
        (0, 'pe'),
        (1, 'doc'),
        (2, 'script'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES)

class Task(models.Model):
    task_id = models.IntegerField()
    object = models.UUIDField()
    STATUS_CHOICES = (
        (0, 'waiting'),
        (1, 'processing'),
        (2, 'finished'),
        (3, 'error'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    creation_ts = models.DateTimeField(auto_now_add=True)
    completed_ts = models.DateTimeField(null=True, blank=True)
    VERDICT_CHOICES = (
        (0, 'malicious'),
        (1, 'suspicious'),
        (2, 'clean'),
    )
    verdict = models.IntegerField(choices=VERDICT_CHOICES)

    analyzers = models.ForeignKey(Analyzer, on_delete=models.CASCADE)  # One-to-many relationship
    nodes = models.ManyToManyField(Node)  # Many-to-many relationship
