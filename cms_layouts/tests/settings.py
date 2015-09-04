SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'cms.plugins.text',
    'cms_layouts',
    'cms_layouts.tests',
]

CMS_TEMPLATES = [('page_template.html', 'page_template.html'),
                 ('page_no_extra_content.html', 'page_no_extra_content.html')]
CMS_MODERATOR = False
CMS_PERMISSION = True
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
ROOT_URLCONF = 'cms_layouts.tests.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
CACHE_BACKEND = 'locmem:///'

SOUTH_TESTS_MIGRATE = False
SECRET_KEY = 'secret'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': (
                "django.contrib.auth.context_processors.auth",
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                'django.template.context_processors.csrf',
                "cms.context_processors.media",
                "sekizai.context_processors.sekizai",
                "django.template.context_processors.static",
            ),
            'loaders': (
                'cms_layouts.tests.utils.MockLoader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
        },
    },
]
