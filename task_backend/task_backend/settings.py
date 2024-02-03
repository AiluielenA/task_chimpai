
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task_backend',                          # Django App 
    'rest_framework_swagger',       # Swagger 
    'rest_framework',               # Django rest framework
    'drf_yasg'                      # Yet Another Swagger generator
]

STATIC_URL = '/static/'
ROOT_URLCONF = 'task_backend.urls'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',
    #     # Other authentication classes
    # ),
}

DEBUG = True  # or True if you are in development
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']  # Add other hostnames or IPs if needed

SWAGGER_API_BASE_URL = 'https://virtserver.swaggerhub.com/IULIAETEODORESCU/project_task/1.0.0'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # List your template directories here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # ... other context processors you might be using
            ],
        },
    },
]



MIDDLEWARE = [
    # ... other middleware classes
    'django.contrib.sessions.middleware.SessionMiddleware',  # This should come first
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 
    # ... other middleware classes
]

SECRET_KEY = 'ed8256e0-ac09-4744-a522-1dde5bac4181'



