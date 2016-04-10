from django.db import models
from messageboard.utils import Error

class MessageManager(models.Manager):
    def add_message(self, user, content):
        if not user:
            err = Error()
            err.set_message('A new message much have a user')
            return False, err
        
        if not content:
            err = Error()
            err.set_message('Invalid content')
            return False, err
                
        try:
            _message = self.create(user=user, content=content)
            _message.save()
        except Exception as e:
            err = Error()
            err.set_message(e.strerror)
            return False, err
        return True, _message

class Message(models.Model):
    objects = MessageManager()
    user = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)
    is_palindrome = models.BooleanField()

    def save(self, *args, **kwargs):
        self.is_palindrome = self.check_palindrome()
    	super(Message, self).save(*args, **kwargs)

    def check_palindrome(self):
        org_msg = [char.lower() for char in self.content if char not in " ?,\"!.'()[]{}:;-"]
        rev_msg = [char.lower() for char in reversed(self.content) if char not in " ?,\"!.'()[]{}:;-"]
        return  org_msg == rev_msg
    	

