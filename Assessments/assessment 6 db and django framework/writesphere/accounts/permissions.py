def can_create_post(user):
    return user.is_authenticated and user.role in ['AUTHOR', 'ADMIN']


def can_edit_post(user, post):
    if not user.is_authenticated:
        return False

    if user.role == 'ADMIN':
        return True

    return post.author == user


def can_delete_post(user, post):
    if not user.is_authenticated:
        return False

    if user.role == 'ADMIN':
        return True

    return post.author == user

def can_edit_comment(user, comment):
    if not user.is_authenticated:
        return False

    if user.role == 'ADMIN':
        return True

    return comment.user == user