# Sobre o projeto
Um simples site que permite a criação de listas de vídeos no youtube.
- [x] - Projeto Inicial
- [x] - Modal de vídeos
- [ ] - Lista de vídeos
- [ ] - Interface com VueJs
- [ ] - Login de acesso

##  Criando o Ambiente

```
$ python -m venv env
$ source env/bin/activate
$ pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/ca/ab/5e004afa025a6fb640c6e983d4983e6507421ff01be224da79ab7de7a21f/Django-3.0.8-py3-none-any.whl (7.5MB)
     |████████████████████████████████| 7.5MB 5.0MB/s 
Collecting pytz (from django)
  Using cached https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl
Collecting sqlparse>=0.2.2 (from django)
  Using cached https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl
    .
    .
    .
```

## Criando o projeto django
```
$ django-admin startproject coreapp .
```

Editando o ``coreapp/settings.py``
```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Campo_Grande'
```

### Executando o projeto
```
$ ./manage.py runserver
```

```
$ ./manage.py startapp youtubelist
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'youtubelist', # adição da app criada
]
```
Edite o arquivo ``youtubelist/models.py``
```
from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=250)
    url = models.URLField()
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
```


```
$ ./manage.py makemigrations
$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, youtubelist
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
```

Vamos criar um usuário administrador
```
$ ./manage.py createsuperuser
Usuário (leave blank to use 'william'): admin
Endereço de email: admin@admin.com
Password: 
Password (again): 
A senha é muito parecida com usuário
Esta senha é muito comum.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

Adicionando o modelo no admin
```
from django.contrib import admin
from .models import Video

admin.site.register(Video)
```