def get_choice(user):
    if user.readable and user.writable:
        return 'Read/Write'
    elif not user.readable and user.writable:
        return 'Write'
    elif user.readable and not user.writable:
        return 'Read'
    elif not user.readable and not user.writable:
        return 'None'
    else:
        raise NotImplementedError