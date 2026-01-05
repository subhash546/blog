from django.contrib import admin
from .models import Category,Blog,About,Sociallinks

# Register your models here.

class BlogModel(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('title',)
    }
    
    list_display=('title','category','author','is_featured','created_at')
    search_fields=('id','title')
    list_editable=('is_featured',)
    
    
    

admin.site.register(Category)
admin.site.register(Blog,BlogModel)

class AboutModel(admin.ModelAdmin):
    def has_add_permission(self, request):
        about =About.objects.count()
        if about >=1:
            return False
        return True
    




admin.site.register(About,AboutModel)
admin.site.register(Sociallinks)