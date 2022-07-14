import datetime
import logging
import pytz
import os

from django.contrib.auth.models import Group
from django.core.files import File

from apiary import settings

logger = logging.getLogger(__name__)


class DefaultDataManager(object):
    def __init__(self):
        pass

