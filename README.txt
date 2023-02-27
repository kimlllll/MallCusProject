一、 环境准备
1. 创建虚拟环境，下载Django
    https://blog.csdn.net/weixin_45980989/article/details/125947157
    也可以在ide终端创建虚拟环境

在terminal 报错：mallEnv\Scripts\activate : 无法加载文件 D:\pythonenve\mallEnv\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。
解决办法：https://blog.csdn.net/qq_40891747/article/details/127664492

2.使用git管理

3.配置开发环境
  3.1 新建配置文件
   manage.py 启动的是测试服务器 settings.py 是开发环境的配置文件 创建一个settings文件夹 用来管理所有的配置文件
   在其中创建 dev.py  也就是开发环境的配置文件
 3.2 在manage.py文件中 加入dev文件的注册
    main方法中：
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MallCusProject.settings.dev")
 3.3 添加生产环境的配置文件
     在wsgi.py中配置  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MallCusProject.settings.prod")
4. 配置模板
    配置jinja2
    在配置文件dev.py 中配置TEMPLATES
    4.1 在虚拟环境中安装jinja2
    4.2 在配置文件中配置
       {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [
            os.path.join(BASE_DIR,"templates") #指定了模板文件的加载路径
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    4.3 指定了模板文件的加载路径 （见4.2 代码）

    4.4 添加模板引擎 static url
    from jinja2 import Environment
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.urls import reverse

    def jinja2_environment(**options):
         env = Environment(**options)
         # 自定义语法 {{ static("静态文件的相对路径")}}  {{url("路由的命名空间")}}
         env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,  #reverse 函数
        })
    return env
    4.5 配置jinja2模板引擎
        TEMPLATES->OPTIONS:
            #补充jinja2模板引擎环境
            'environment':'MallCusProject.utils.jinja2_env.jinja2_environment'



    5. 配置MySQL数据库 ： 使用MySQL数据库存储用户、商品、订单数据
    5.1 步骤：
        1. 新建MySQL数据库
        可以使用工具创建 ，再进行连接
        2. 连接数据库
           DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",

        "ENGINE": "django.db.backends.mysql",
        "HOST":"127.0.0.1",
        "PORT":3306,
        "USER":"root",
        "PASSWORD":"woaini1989",
        "NAME": "mallproject",

    }
}
      3. 安装pymysql
         进入虚拟环境，在虚拟环境中安装pymysql  pip install pymysql
         在MallCusProject的_init_.py中，配置pymysql
         from pymysql import install_as_MySQLdb
         install_as_MySQLdb

   6.配置Redis数据库，存储缓存数据或者是状态保持的数据
     步骤：1. 安装django-redis扩展包
          2.配置redis数据库


  7.配置工程日志
  8.配置静态文件







