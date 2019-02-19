from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User(first_name='u1', last_name='u1')
    u1.save()
    u2 = User(first_name='u2', last_name='u2')
    u2.save()
    u3 = User(first_name='u3', last_name='u3')
    u3.save()
    blog1 = Blog(title='blog1', author=u1)
    blog1.save()
    blog2 = Blog(title='blog2', author=u2)
    blog2.save()
    blog1.subscribers.add(u1,u2)
    blog2.subscribers.add(u2)
    topic1 = Topic(title='topic1',blog=blog1, author=u1)
    topic2 = Topic(title='topic_content', blog=blog1,author=u3,created='2017-01-01')
    topic1.save()
    topic2.save()
    topic1.likes.add(u1,u2,u3)


def edit_all():
    User.objects.all().update(first_name='uu1')
    
	
def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    entry = User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    Blog.subscribers.through.objects.filter(user__first_name='u2').delete()


def get_topic_created_grated():
    topic = Topic.objects.filter(created__gt=datetime(year=2018, month=1, day=1,tzinfo=UTC))


def get_topic_title_ended():
    topic = Topic.objects.filter(name__endswith='content')
    return topic


def get_user_with_limit():
   users = User.objects.order_by('-id')[:2]
   return users


def get_topic_count():
    return Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')


def get_avg_topic_count():
  return Topic.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))
  return result


def get_blog_that_have_more_than_one_topic():
    blogs = Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1)
    return blogs


def get_topic_by_u1():
    entries = Blog.objects.filter(author__first_name='u1')
    return entries


def get_user_that_dont_have_blog():
	user = User.objects.filter(blog__isnull=True).order_by('pk')
	return user


def get_topic_that_like_all_users():
    entries = Topic.objects.annotate(like=Count('likes')).filter(likes=like)
    return entries


def get_topic_that_dont_have_like():
    entries = Topic.objects.filter(likes__isnull=True)
    return entries