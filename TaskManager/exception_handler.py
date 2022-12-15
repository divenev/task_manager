from django.shortcuts import render


def handler_error500(request, *args, **kwargs):
    return render(request, 'webtask/error_template.html')

def handler_error404(request, *args, **kwargs):
    return render(request, 'webtask/error_template.html')
