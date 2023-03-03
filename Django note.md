# Django project

系统配置：

* Intel(R) Core(TM) i7-10700 CPU @ 2.90GHz   2.90 GHz
* Windows 10 
* Python 3.10
* PyCharm 2022.2.2
* Django 3.1.1
* mysql 5.7.38 winx64


## 配置虚拟环境

利用 PyCharm 直接配置虚拟环境，新建虚拟环境储存或者使用原有虚拟环境

## 创建项目

直接在 PyCharm 中新建 Django 项目，命名 `djangoProject_test` 得到的项目文件如下：
```angular2html
djangoProject_test/             # 项目名称
    manage.py                   # 一个命令行实用程序，使用命令行与 Django 进行交互
    djangoProject_test/         # 实际 Python 包名称，注意保持和项目名称一致
        __init__.py
        settings.py             # 这个 Django 项目的设置
        urls.py                 # 这个 Django 项目的 URL 声明；由 Django 驱动的站点的“目录”。
        asgi.py                 # 为项目提供服务的兼容 ASGI 的 Web 服务器的入口点。
        wsgi.py                 # 为项目提供服务的 WSGI 兼容 Web 服务器的入口点
```
在 mysite 目录下运行以下命令验证 Django 项目是否有效：
```
...\> py manage.py runserver
```
在项目中新建 app （实际上就是一个新的Python类），使用如下命令行语句创建，这样做的好处是可以直接生成所需要的基本文件（特别是`migrations`）。
```
···\> py manage.py startapp app_test
```
可以获得如下的 app 文件结构：
```angular2html
app_test/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
注意：这时我们需要将新建的 app 注册进与项目同名的包 `djangoProject_test` 里的设置文件 `settings.py` 中：
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'app_test',   可以直接写app名称，推荐写为下面这种方式避免迁移项目环境后出错
    'app_test.apps.AppConfig',
]
```

## 创建 MySQL 数据库并使用 Django 操作

### 创建 MySQL 数据库并连接到 Django 项目

我们在命令程序中使用命令如下登录 MySQL 
```angular2html
···\> mysql -h 主机ip地址 -P 端口号 -u 用户名 -p密码
···\> mysql -h 主机ip地址 -P 端口号 -u 用户名 -p密码            
# 本机登录省略主机IP与端口号，默认密码为空省略密码
```
使用命令查看已经创建的数据库并创建新的数据库
```angular2html
mysql> show databases;
create database djangoProject_test;
show create database djangoProject_test;    
# 注意数据库的字符编码设置是否为 utf8 ，避免日后出现错误        
```
在 PyCharm 点击`Database -> + -> Data Source -> MySQL`输入刚刚创建的数据库用户名与数据库名称，这样我们将数据库与 Django 项目连接起来。最后，我们需要在设置文件 `settings.py` 中将我们的数据库进行设置：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎，我们在这里使用的是MySQL
        'OPTIONS': {'charset': 'utf8mb4'},      
        'HOST': '127.0.0.1',                    # 设置为本机IP地址
        'PORT': '3306',
        'NAME': 'djangoProject_test',           # 设置为我们刚刚创建的数据库
        'USER': 'root',                         
        'PASSWORD': ''
    }
}
```
为了对 MySQL 数据库进行操作我们还需要安装几个包如下：
* PyMySQL 1.0.2
* mysqlclient 2.1.1

### 使用 Django 处理数据库

以下是几个常用的与迁移交互的命令，即 Django 处理数据库架构的方式：
* **migrate**，负责应用和撤销迁移。 
* **makemigrations**，基于模型的修改创建迁移。 
* **sqlmigrate**，展示迁移使用的 SQL 语句。 
* **showmigrations**，列出项目的迁移和迁移的状态。

**makemigrations** 负责将`models.py`中的类变量打包进独立的迁移文件中，而 **migrate** 负责将其应用至数据库。通过这样的交互式命令，我们可以直接在 Django 框架中对数据库进行操作。

#### 数据库连接报错
Python3 与 Django 连接数据库，出现了报错：`Error loading MySQLdb module: No module named 'MySQLdb'`。原因如下：

在 python2 中，使用 `pip install mysql-python` 进行安装连接 MySQL 的库，使用时 `import MySQLdb` 进行使用；
在 python3 中，改变了连接库，改为了 pymysql 库，使用 `pip install pymysql` 进行安装，直接导入即可使用；
但是在 Django 中， 连接数据库时使用的是 MySQLdb 库，这在与 python3 的合作中就会报以下错误了：
```python
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
```
或者是：
```python
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
```
我们需要在项目的在 `__init__.py` 文件中添加以下代码即可：
```python
import pymysql
pymysql.install_as_MySQLdb()
```


我们运行命令如下：
```
···\> py manage.py makemigrations app_test
```
得到输出：
```
Migrations for 'app_test':
  app_test\migrations\0001_initial.py
    - Create model Person
```
此时我们在`migrations`文件夹下得到了一个新的`0001_initial.py`文件，其中代码如下：
```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='name')),
                ('age', models.CharField(default='', max_length=200, verbose_name='age')),
            ],
        ),
    ]

```
我们可以看到，在指定了`···\> py manage.py makemigrations app_test`的对象为`app_test`后，操作 **makemigrations** 制作了一个和名为`app_test`的 app 中`models.py`文件里定义的类变量有关的新文件。

我们再使用命令：
```
···\> py manage.py migrate
```
就可以在连接到的数据库里创建 app 中`models.py`文件中的类变量对应的表。

















### settings.py 文件中的设置

INSTALLED_APPS
```
django.contrib.admin                # 管理站点。您很快就会使用它。
django.contrib.auth                 # 认证系统。
django.contrib.contenttypes         # 内容类型的框架。
django.contrib.sessions             # 会话框架。
django.contrib.messages             # 消息传递框架。
django.contrib.staticfiles          # 管理静态文件的框架。
```



