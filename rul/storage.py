from django.core.files import File
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    def _open(self, name, mode='rb'):
        return File(open(self.path(name), mode))

    def _save(self, name, content):
        full_path = self.path(name)
        try:
            with open(full_path, 'wb') as fd:
                for chunk in content.chunks():
                    fd.write(chunk)
        except FileExistsError:
            # A new name is needed if the file exists.
            pass
        # Store filenames with forward slashes, even on Windows.
        return name

    def get_available_name(self, name, **kwargs):
        return name
