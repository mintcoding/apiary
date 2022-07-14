from django.conf import settings
from collections import OrderedDict
from copy import deepcopy
import sys


def are_migrations_running():
    """
    Checks whether the app was launched with the migration-specific params
    """
    # return sys.argv and ('migrate' in sys.argv or 'makemigrations' in sys.argv)
    return sys.argv and (
        "migrate" in sys.argv
        or "makemigrations" in sys.argv
        or "showmigrations" in sys.argv
        or "sqlmigrate" in sys.argv
    )
