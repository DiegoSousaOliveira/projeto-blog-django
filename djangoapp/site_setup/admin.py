from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup

#@admin.register(MenuLink)
#class MenuLinkAdmin(admin.ModelAdmin):
#    list_display = 'id', 'text', 'url_or_path', 'new_tab',
#    list_display_links = 'id', 'text', 'url_or_path', 'new_tab',
#    search_fields = 'id', 'text', 'url_or_path', 'new_tab',

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
