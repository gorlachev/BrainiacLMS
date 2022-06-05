from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    help = (
        "This command for call makemessages and use flags --locale, --ignore and --no-loction"
    )

    def handle(self, *args, **options):
        call_command('makemessages', '--locale=ru', '--ignore=env', '--no-location')