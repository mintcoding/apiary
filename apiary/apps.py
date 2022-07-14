from __future__ import unicode_literals
from django.conf import settings

from django.apps import AppConfig


class LicensingTemplateConfig(AppConfig):
    name = "apiary"
    verbose_name = settings.SYSTEM_NAME

    run_once = False

    def ready(self):
        if not self.run_once:
            pass
            #from apiary.components.organisations import signals
            #from apiary.components.proposals import signals

        self.run_once = True
