# your_app/management/commands/cleanup_files.py
import os
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete files older than 13 minutes from the specified directory'

    def handle(self, *args, **kwargs):
        directory = '/path/to/your/mp3/files'
        now = datetime.now()

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                # Get the file's last modified time
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if now - file_mtime > timedelta(minutes=13):
                    os.remove(file_path)
                    self.stdout.write(self.style.SUCCESS(f'Deleted: {file_path}'))
