from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Message(models.Model):
    message_content = models.CharField(max_length=5000)
    subject = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - from: {self.sender} - {self.creation_date}"

    class Meta:
        ordering = ['creation_date']

