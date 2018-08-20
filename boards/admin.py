from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LogicBlock)
admin.site.register(TriggerAction)
admin.site.register(Trigger)
admin.site.register(Rating)
admin.site.register(Risk)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Evidence)
admin.site.register(WeightConfig)
admin.site.register(Board)