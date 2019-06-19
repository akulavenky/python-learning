from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.

#Creating custom email validator else you can use default
#you can create a custome validation in a different file and import here as well
#We can validate not only email, you can use wherever you want
def validate_author_email(value):
    if not "@" in value:
        raise ValidationError("Not a valid email")
    return value

def validate_user_email(value):
    if not "user" in value:
        raise ValidationError("Not a valid email")
    return value


PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]

class PostModel(models.Model):
    id			= models.BigAutoField(primary_key=True)
    active		= models.BooleanField(default=True)
    title		= models.CharField(
				max_length=240, 
				verbose_name='Post Title', #it will shows title as Post Title instead of title
				unique=True,
				error_messages={
					"unique": "This title is not unique, please try again.",
					"blank": "This field is not full, please try again.",
				},
				help_text='Must be a unique title.')
    slug		= models.SlugField(null=True, blank=True)
    content		= models.TextField(null=True, blank=True)
    publish     	= models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count  	= models.IntegerField(default=0)
    publish_date	= models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    #author_email	= models.CharField(max_length=240, validators=[validate_author_email, validate_user_email], null=True, blank=True) #custom email validator
    author_email	= models.EmailField(max_length=240, null=True, blank=True) # Default 
    #id			= models.IntegerField(primaty_key=True  #auto increments 1, 2, 3, 4


    #To know more about *args, **kwargs
    #def random_method(self, abc, edb, title, keyword1=None, keyword2=None):
    #   print(title)
    #   print(keyword)

    #To override the default save method
    #def save(self, *args, **kwargs):
    #    self.title = 'A new title'
    #    super(PostModel, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    # If you want to give uni/title name to the PostModel objects instead of showing postmodel object 1, postmodel object 2 and etc
    def __unicode__(self): #python 2
        return smart_text(self.title)

    def __str__(self):    #python 3
        return smart_text(self.title) #smart_text will convert the string to encoding='utf-8'

'''
python manage.py makemigrations #every time you change models.py, it will set the parameters for db
python manage.py migrate  # It will update in the db
'''
