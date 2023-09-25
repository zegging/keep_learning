# Django单元测试启动失败，数据库报错

* Django==3.1.1

* Python==3.6.5 

## Got an error creating the test database: (1044, "Access denied for user 'dbuser'@'%' to database 'test_project'")

### 报错详情

这是当我在给我的 Django 项目编写单元测试的时候遇到的第一个错误（项目已经有很多功能了但是还没有单元测试，这个要问前辈……）。原因很简单，这是因为我配置的`default`数据库是由中间件部门维护的DBV，`user：dbuser`并没有在服务端创建数据库的权限。

Django 的单元测试如果使用`django.test.TestCase`类的话会在基类`django.test.TransactionTestCase`中指明使用默认数据库`default`的配置链接服务端。

```python
class TransactionTestCase(SimpleTestCase):

    # Subclasses can ask for resetting of auto increment sequence before each
    # test case
    reset_sequences = False

    # Subclasses can enable only a subset of apps for faster tests
    available_apps = None

    # Subclasses can define fixtures which will be automatically installed.
    fixtures = None

    databases = {DEFAULT_DB_ALIAS} # DEFAULT_DB_ALIAS = 'default'
```

Django 框架会在同一个服务端（default）新建一个空白数据库用于测试，所以需要配置中的用户 USER 有权限在服务端创建和删除数据库。我的单元测试产生报错的原因就在这里——我缺少权限。

详情查看官方文档：[Django-测试数据库](https://docs.djangoproject.com/zh-hans/4.2/topics/testing/overview/#the-test-database)

### 解决方案

因此我需要使用一个本地的 MySQL 数据库来作为单元测试的数据库：

```python
DATABASES = {
	# ...
    'test': {
        'ENGINE': 'django.db.backends.mysql',  # 测试数据库使用 mysql 引擎
        'OPTIONS': {'charset': 'utf8mb4'},
        'HOST': '',
        'PORT': ,
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
```

这个`test`数据库会在稍微修改后的单元测试中替换原来的`default`库使用。Django 单元测试工具会根据`test`新建一个新的数据库作为测试用库。

我们需要在单元测试代码中指明要使用的数据库：

```python
class SmokeTestCase(TestCase):
    # databases = {'test'}
    def test_addition(self):
        def addition(x,y):
            return x+y
        self.assertEqual(addition(1,2),2,'ass is failed') #断言函数加和运算
```

到这里其实还没有解决问题，我立马遇到了另一个报错：

## django.core.exceptions.ImproperlyConfigured: Circular dependency in TEST[DEPENDENCIES]

### 报错详情

```
Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/commands/test.py", line 23, in run_from_argv
    super().run_from_argv(argv)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/core/management/commands/test.py", line 53, in handle
    failures = test_runner.run_tests(test_labels)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/test/runner.py", line 695, in run_tests
    old_config = self.setup_databases(aliases=databases)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/test/runner.py", line 616, in setup_databases
    self.parallel, **kwargs
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/test/utils.py", line 157, in setup_databases
    test_databases, mirrored_aliases = get_unique_databases_and_mirrors(aliases)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/test/utils.py", line 283, in get_unique_databases_and_mirrors
    test_databases = dict(dependency_ordered(test_databases.items(), dependencies))
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/django/test/utils.py", line 236, in dependency_ordered
    raise ImproperlyConfigured("Circular dependency in TEST[DEPENDENCIES]")
django.core.exceptions.ImproperlyConfigured: Circular dependency in TEST[DEPENDENCIES]

```

我们可以看到这是因为在进行数据库创建的时候存在一个循环依赖，直接进入`/django/test/utils.py`中查看代码。

```python
def get_unique_databases_and_mirrors(aliases=None):
    """
    Figure out which databases actually need to be created.

    Deduplicate entries in DATABASES that correspond the same database or are
    configured as test mirrors.

    Return two values:
    - test_databases: ordered mapping of signatures to (name, list of aliases)
                      where all aliases share the same underlying database.
    - mirrored_aliases: mapping of mirror aliases to original aliases.
    """
    if aliases is None:
        aliases = connections
    mirrored_aliases = {}
    test_databases = {}
    dependencies = {}
    default_sig = connections[DEFAULT_DB_ALIAS].creation.test_db_signature()

    for alias in connections:
        connection = connections[alias]
        test_settings = connection.settings_dict['TEST']

        if test_settings['MIRROR']:
            # If the database is marked as a test mirror, save the alias.
            mirrored_aliases[alias] = test_settings['MIRROR']
        elif alias in aliases:
            # Store a tuple with DB parameters that uniquely identify it.
            # If we have two aliases with the same values for that tuple,
            # we only need to create the test database once.
            item = test_databases.setdefault(
                connection.creation.test_db_signature(),
                (connection.settings_dict['NAME'], set())
            )
            item[1].add(alias)

            if 'DEPENDENCIES' in test_settings:
                dependencies[alias] = test_settings['DEPENDENCIES']
            else:
                if alias != DEFAULT_DB_ALIAS and connection.creation.test_db_signature() != default_sig:
                    dependencies[alias] = test_settings.get('DEPENDENCIES', [DEFAULT_DB_ALIAS])

    test_databases = dict(dependency_ordered(test_databases.items(), dependencies))
    return test_databases, mirrored_aliases
```

这是因为在数据库配置中有一个循环依赖，Django假设所有的数据库都依赖与默认数据库`default`，然而在我们的单元测试中`test`显然是不依赖于`default`的，导致了报错。官方文档中有详细的解释：[Django-数据库的创建顺序](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#controlling-creation-order-for-test-databases)

### 解决方案

所以我们需要显示地指明数据库的依赖关系：

```python
DATABASES = {
	# ...
    'test': {
        'ENGINE': 'django.db.backends.mysql',  # 测试数据库使用 mysql 引擎
        'OPTIONS': {'charset': 'utf8mb4'},
        'HOST': '',
        'PORT': ,
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        "TEST": {
            "DEPENDENCIES": [],
        },
    }
}
```

但到这里还没有结束……

## django.db.utils.ProgrammingError: (1146, "Table 'test_smp_test.ask_kujialeaskhref' doesn't exist")

### 报错详情

```
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/MySQLdb/cursors.py", line 319, in _query
    db.query(q)
  File "/root/miniconda3/envs/smp/lib/python3.6/site-packages/MySQLdb/connections.py", line 254, in query
    _mysql.connection.query(self, query)
django.db.utils.ProgrammingError: (1146, "Table 'test_smp_test.ask_kujialeaskhref' doesn't exist")
```

显然这是因为没有这张表导致的，原因很简单，我再dev环境并没有同步`migrations`中的迁移文件，所以创建测试数据库中的表的时候就会报错。

### 解决方法

很简单，生成数据库迁移文件就可以了。