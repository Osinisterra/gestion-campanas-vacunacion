import os

from django.core.management import ManagementUtility

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    ManagementUtility().execute()
