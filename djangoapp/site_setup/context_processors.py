from site_setup.models import SiteSetup

def context_processors_example(request):
    return {
        'name': 'Veio do context_processors_example'
    }

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup
    }