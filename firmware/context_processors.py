def is_moderator(request):
    return request.user.groups.filter(name='moderator').exists()


def user(request):
    return {
        'user': request.user,
        'moderator': is_moderator(request)
    }