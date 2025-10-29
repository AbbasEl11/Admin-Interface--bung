from django.contrib import admin
from .models import  EventCategory , Location , Event


# Register your models here.

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass




@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]
    search_fields = ["title", "date"]
    list_filter = ["category"]
    date_hierarchy = 'date'

    fieldsets = (
        (
            "Allgemein",
            {
                "fields": ("title", "category", "date"),
            },
        ),
        (
            "Organisation",
            {
                "fields": ("location", "capacity"),
            },
        ),
)


    

    
    
    
