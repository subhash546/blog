from .models import Category,Sociallinks


def categories_processor(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def social_links(request):
    social_links=Sociallinks.objects.all()
    return dict(social_links=social_links)

