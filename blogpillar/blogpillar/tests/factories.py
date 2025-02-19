import factory
from django.contrib.auth.models import User 

from blogpillar.blog.models import Post 

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    password = 'test'
    username = 'test'
    is_superuser = True
    is_staff = True 

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        
    title = "x"
    sub_title = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"