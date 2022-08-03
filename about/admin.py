from django.contrib import admin
from .models import AboutUs, TeamMember, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email')
    search_fields = ('subject', 'text')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'show_image')
    search_fields = ('user__username',)


admin.site.register(AboutUs)
