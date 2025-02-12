from django.contrib import admin

from accounts.models.company_founder import CompanyFounder

@admin.register(CompanyFounder)
class CompanyFounderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "company_name",
        "is_active",
    ]
    search_fields = [
        "company_name",
    ]
    list_filter = [
        "is_active",
    ]