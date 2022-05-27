# Checkout Views
# The following function and class have been adapted from
# GitHub. 2019. django-ecommerce/ at master · justdjango/django-ecommerce. [online]
#  Available at: <https://github.com/justdjango/django-ecommerce/blob/master/core/>
#  [Accessed 25 March 2022]

from django import template
from ..models import Order

register = template.Library()


@register.filter
def cart_product_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].products.count()
    return 0



