from rangefilter.filters import DateRangeFilter
from django.contrib import admin
from echo.models import Echo

@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_data', 'created')
    list_filter = ('user', ('created', DateRangeFilter))

    @admin.display(description='data', )
    def get_data(self, obj):
        cut = 30
        return obj.data if len(str(obj.data)) < cut else obj.data[:cut]