#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    from django.contrib.auth.models import Group
    new_group, created = Group.objects.get_or_create(name='moderator')
    new_group, created = Group.objects.get_or_create(name='user')

    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_user('admin', password='1')
        user.is_superuser=True
        user.is_staff=True
        user.save()

    if not User.objects.filter(username='mod').exists():
        user = User.objects.create_user('mod', password='1')
        user.save()

        group = Group.objects.get(name='moderator')
        group.user_set.add(user)


if __name__ == '__main__':
    main()
