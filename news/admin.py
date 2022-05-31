from django.contrib import admin
from .models import Rent
from .models import Kommet
from .models import Articles

admin.site.register(Rent)
admin.site.register(Kommet)
admin.site.register(Articles)

