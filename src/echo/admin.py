from rangefilter.filters import DateRangeFilter
from django.contrib import admin
from echo.models import Echo


@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = ("user", "get_data", "created")
    list_filter = ("user", ("created", DateRangeFilter))

    @admin.display(
        description="data",
    )
    def get_data(self, obj):
        data = str(obj.data)
        cut = 30
        return data if len(data) < cut else f"{data[:cut]}..."
