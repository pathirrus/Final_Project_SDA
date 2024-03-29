from django.contrib import admin
from website.models import Service, Reservation
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["service_name", "price", "time_of_service"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user_id", "service_id", 'visit_date']
