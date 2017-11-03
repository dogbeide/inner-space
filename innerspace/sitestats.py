import math
# from posts.models import Post
# from comments.models import Comment
from django.contrib.auth import get_user_model
# User = get_user_model()

BASE_RATING_SHIFT = 0.1

def scale(rep):
    return 1 - math.fabs(rep-5)/5

def power(rep):
    if rep > 5:
        return (rep/5)**(rep/2.5)
    elif rep < 5:
        return rep/5
    else:
        return 1

# TODO: Implement user overall ranking leaderboard
def rank(user):
    pass
