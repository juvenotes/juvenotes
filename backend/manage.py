#!/usr/bin/env python

import os
import sys

from decouple import config


if __name__ == "__main__":
    settings_module = 'juvenotes.settings.production' if os.getenv('DJANGO_SETTINGS_MODULE') == 'juvenotes.settings.production' else config("DJANGO_SETTINGS_MODULE")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    # print(settings_module)

    if sys.argv[1] == "test":
        if settings_module:
            print(
                "Ignoring config('DJANGO_SETTINGS_MODULE') because it's test. "
                "Using 'juvenotes.settings.test'"
            )
        os.environ["DJANGO_SETTINGS_MODULE"] = "juvenotes.settings.test"
    else:
        if settings_module is None:
            print(
                "Error: no DJANGO_SETTINGS_MODULE found. Will NOT start devserver. "
                "Remember to create .env file at project root. "
                "Check README for more info."
            )
            sys.exit(1)
        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)