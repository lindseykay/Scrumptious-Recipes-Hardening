from django.contrib import admin
from .models import MealPlan

# Register your models here.


class MealPlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(MealPlan, MealPlanAdmin)
