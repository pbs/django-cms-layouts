from django.template.loaders.base import Loader as BaseLoader
from django.template.base import TemplateDoesNotExist


class MockLoader(BaseLoader):

    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        if template_name == 'cms/plugins/text.html':
            return ('{{body}}', 'cms/plugins/text.html')
        if template_name == 'page_template.html':
            return ('{% load cms_tags %}|'
                    '{% page_attribute "page_title" %}|'
                    '{% placeholder "header" %}|'
                    '{% placeholder "extra-page-content" %}|'
                    '{% placeholder "some-content" %}|'
                    '{% placeholder "footer" %}', 'page_template.html')
        if template_name == 'page_no_extra_content.html':
            return ('{% load cms_tags %}|'
                    '{% page_attribute "page_title" %}|'
                    '{% placeholder "header" %}|'
                    '{% placeholder "some-content" %}|'
                    '{% placeholder "footer" %}', 'page_template.html')
        if template_name == '404.html':
            return "404 Not Found", "404.html"
        else:
            raise TemplateDoesNotExist()
