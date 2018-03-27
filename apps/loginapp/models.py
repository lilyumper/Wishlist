# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.




class Checker(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 1:
            errors.append("First Name must be more than 1 character")
        if len(postData['last_name']) < 1:
            errors.append("Last Name Must be more than 1 character")
        if re.search('[0-9]', postData['first_name']) > 0:
            errors.append("First Name Cannot Contain Numbers")
        if re.search('[0-9]', postData['last_name']) > 0:
            errors.append("Last Name Cannot Contain Numbers")
        if len(postData['email']) < 1:
            errors.append("Email field must be filled")
        if postData['email'] and not re.match(EMAIL_REGEX, postData['email']):
            errors.append("Invalid email formatting")
        if len(postData['password']) < 8:
            errors.append("Password Must Be At least 8 Characters")
        if postData['password'] != postData['confirm']:
            errors.append("Passwords do not match")
        if len(self.filter(email=postData['email'])) > 0:
            errors.append("Email in use")
        if not postData['birthday']:
                errors.append('birthday cannot be blank')
        if postData['birthday']:
            if datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.datetime.now() - datetime.timedelta(days=365*18):
                errors.append("You must be at least 18 years old to enter this site!")
        return errors
        
     

    def login_validator(self, postData):
        errors = []
        emails = postData['lemail']
        print len(emails)
        password = postData['lpassword']
        user = Users.objects.filter(email=emails)
        if len(Users.objects.filter(email=emails)) < 1:
            errors.append('email does not exist')
        if len(emails) <= 0:
            errors.append('both email and password must be filled in')
        if len(password) <= 0:
            errors.append('both email and password must be filled in')
            return errors
        if len(user) > 0:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return errors
            else:
                errors.append("Invalid Password")
                return errors
    
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length = 255)
    birthday = models.DateField()
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255) 

    objects=Checker()
    
    
    
