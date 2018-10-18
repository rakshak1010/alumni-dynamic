from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
DEGREE = (
    (1, 'Undergraduate'),
    (2, 'Postgradute'),
    (3, 'Doctrate'),
    (4, 'Scientist')   
)

CURRENCY = (
    (1, 'Rupees'),
    (2, 'Dollars'),
    (3, 'Yens'),
    (4, 'Other')
)
 


class Giving_back(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    amount = models.FloatField(choices=CURRENCY, blank=True, null=True)
    additional_remarks = models.TextField(blank=True)
    donation_date = models.DateTimeField(auto_now_add=True)



class Post(models.Model):
    content = models.TextField(primary_key=True)
    post_made = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True, blank=True)
    media_upload = models.FileField(upload_to='uploads/', blank=True, null=True)



class Faculty(models.Model):
    user_faculty = models.OneToOneField( User, primary_key=True, on_delete=models.CASCADE)
    past_positions = models.TextField(blank=False)
    profile_picture_faculty = models.FileField( upload_to='uploads/')
    education = models.TextField(choices=DEGREE, blank=True)
    current_position = models.TextField(blank=False)
    fields_of_interest = models.TextField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?\d{1,2}?\d{9,15}$')
    phone_number_faculty = models.CharField(validators=[phone_regex], max_length=18, blank=False)
    content = models.ForeignKey('Post', on_delete=models.CASCADE)
    transaction_id = models.ForeignKey('Giving_back', on_delete=models.CASCADE)
    status = models.OneToOneField('self', on_delete=models.CASCADE, blank=False)
    
    class Meta:
        unique_together = (('user_faculty','phone_number_faculty'))


class Alumnus(models.Model):
    user_alumnus = models.OneToOneField( User, primary_key=True, on_delete=models.CASCADE)
    profile_picture = models.FileField( upload_to='uploads/')
    batch = models.IntegerField( blank=False, null=False)
    current_post = models.TextField(blank=False)
    birthday = models.DateField(blank=True)
    institute_rollno = models.IntegerField( blank=False)
    testimonial = models.TextField(blank=True)
    areas_of_interest = models.TextField(blank=True)
    CV_pdf_upload = models.FileField(upload_to='uploads/')
    links_for_CV = models.URLField(unique=True, blank=True)
    transaction_id = models.ForeignKey('Giving_back', on_delete=models.CASCADE)
    content = models.ForeignKey('Post', on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?\d{1,2}?\d{9,15}$')
    phone_number_alumnus = models.CharField(validators=[phone_regex], max_length=18, blank=False)
    status = models.OneToOneField('self', on_delete=models.CASCADE, blank=False)

    
    class Meta:
        unique_together = (('user_alumnus','phone_number_alumnus'),)



class Replies(models.Model):
    time_of_reply = models.DateTimeField(blank=False, null=False)
    content_of_reply = models.TextField(null=False)
    content = models.ForeignKey('Post', on_delete=models.CASCADE)
    

    class Meta:
        order_with_respect_to = 'content'