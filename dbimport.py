from django.core.management.commands.inspectdb import Command
from django.conf import settings
from backend.settings import DATABASES
import sys

settings.DATABASES = DATABASES

orig_stdout = sys.stdout
a = open('models.txt', 'w')
sys.stdout = a

Command().execute(table_name_filter=lambda table_name: table_name in ('cotiza_oficinas',), database='default')

sys.stdout = orig_stdout
a.close()
