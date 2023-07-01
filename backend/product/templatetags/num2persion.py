from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def num2persian(value):
    persian_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    persian_number = ''.join(persian_digits.get(char, char) for char in str(value))
    return mark_safe(persian_number)

register.filter('num2persian', num2persian)
