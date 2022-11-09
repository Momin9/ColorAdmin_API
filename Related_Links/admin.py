from django.contrib import admin

from Related_Links.models import Privacy_and_Policy, Contact_Us, Terms_of_Use, Shopping_Help

# Register your models here.

admin.site.register(Privacy_and_Policy)
admin.site.register(Contact_Us)
admin.site.register(Terms_of_Use)
admin.site.register(Shopping_Help)
