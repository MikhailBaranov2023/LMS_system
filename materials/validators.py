from rest_framework.validators import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_link = value.get('video_link')
        if video_link is not None and 'www.youtube' not in video_link:
            raise ValidationError('Вы можете прикреплять материалы только с YouTube')