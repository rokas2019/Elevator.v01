from django.contrib import admin
from .models import Screen, Arrow, CurrentTime, Level
from django.utils.html import format_html

admin.site.register(Screen)
admin.site.register(Arrow)
admin.site.register(CurrentTime)


@admin.register(Level)
class Model1Admin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]
