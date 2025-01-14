from django.template import Library
from apps.home.models import SiteSetting

register = Library()


@register.inclusion_tag("includes/header.html")
def header_view(request):
    branding = SiteSetting.objects.first()
    color = branding.color if branding else None
    logo = branding.logo if branding else None
    return {
        "request": request,
        "color": color,
        "logo": logo,
    }
