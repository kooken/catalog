from django import template

register = template.Library()


@register.filter
def blog_media_tag(data):
    if data:
        return f'/media/{data}'
    return 'Картиночка не загрузилась...'
