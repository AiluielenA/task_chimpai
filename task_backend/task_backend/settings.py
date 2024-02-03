
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
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ... other middleware classes
]


