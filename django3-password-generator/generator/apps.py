from django.apps import AppConfig
#приложения это как отдельный блок сайта, вот был бы какой-нибудь еще генератор никнеймов, тогда да, здесь бы в приложениях ещё сделали.

class GeneratorConfig(AppConfig):
    name = 'generator'
