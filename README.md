vtlab_django_orm
================

**veritabanı lab dersi için hazırlamış olduğum django ile orm örneği**

uygulamayı denemek için [django](https://www.djangoproject.com/) kurulu bir sistemde;

`git clone git@github.com:sayz/vtlab_django_orm.git` komutu ile uygulamayı sisteminize klonlayın.

uygulamanızın olduğu dizine geçin

`settings.py` dosyasında veritabanı ile ilgili bilgilerinizi ( *user, password vb.* ) girdikten sonra


```
  python manage.py syncdb
  python manage.py runserver
```

komutlarını verin. 

daha sonra tarayıcınızdan [localhost:8080](http://localhost:8000/) adresine girerek uygulamaya erişebilirsiniz.
