from django.contrib import admin

from .models import Display, Badge




class DisplayAdmin(admin.ModelAdmin):
    model = Display
    list_display = ['get_badge_name', 'type', 'uploadedResource', 'linkedResource' ]
    list_filter = ['type', 'badge']
    search_fields = ('badge', 'uploadedResource', 'linkedResource')

    def get_badge_name(self, obj):
        return ", ".join([k.title for k in obj.badge_set.all()])

    get_badge_name.admin_order_field  = 'badge'  #Allows column order sorting
    get_badge_name.short_description = 'Badge Name'  #Renames column head


admin.site.register(Display, DisplayAdmin)