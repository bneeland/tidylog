from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class Product(TemplateView):
    template_name = "product.html"

class Pricing(TemplateView):
    template_name = "pricing.html"

class Contact(TemplateView):
    template_name = "contact.html"
