from django.utils.deprecation import MiddlewareMixin

from rul.forms import PaletteRequestForm


class PaletteRequestMid(MiddlewareMixin):
    def process_request(self, request):
        request.form = PaletteRequestForm
        return None
