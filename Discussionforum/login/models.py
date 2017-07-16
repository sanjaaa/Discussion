from django.db import models


from django.utils import timezone

# class user_account(models.Model):
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     created_date = models.DateTimeField(
#             default=timezone.now)
# 
#     def __str__(self):
#         return self.name

class discussion(models.Model):
#     usser_account_id = models.ForeignKey('user_account',
#         on_delete=models.CASCADE,)
    subject = models.TextField()
    created_date_discussion = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.subject
    
class comment(models.Model):
    discussion_id = models.ForeignKey('discussion',
        on_delete=models.CASCADE,)
#     user_account_id = models.ForeignKey('user_account',
#         on_delete=models.CASCADE,)
    content = models.TextField()
    created_date_discussion = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.content