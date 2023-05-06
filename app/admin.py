from django.contrib import admin

from app.models import HomePage, Map, Muraciet, New, Product
# Register your models here.
@admin.register(Muraciet)
class MuracietAdmin(admin.ModelAdmin):
    class Meta():
        model = Muraciet
    list_display = ["ad","soyad","telefon","email"]
    search_fields =  ["ad","soyad","telefon","email"]
    
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    class Meta():
        model = New
    list_display = ["title","photo","tarix","metn"]
    search_fields = ["title","photo","tarix","metn"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta():
        model = Product
    list_display = ["name","title","origin","alcohol","manifacture_year"]
    search_fields =["name","title","origin","alcohol","manifacture_year","composition","temperature","keeping_form"]
admin.site.register(Map)


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    class Meta():
        model = HomePage
    def has_add_permission(self, request):
        base_add_permission = super(HomePageAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = HomePage.objects.all().count()
            if count == 0:
                return True
        return False