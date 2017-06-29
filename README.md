#BLL
# BLL运维管理系统
1. 基础环境部署
  - 选择git工具(coding.net)
      `git clone https://git.coding.net/benq1211/BLL.git`
      > 注意：.gitignore排除文件
  - 新建django项目
    `django-admin startproject BLL`
  - django初始化
   `cat settings.py
    ALLOWED_HOSTS = ["192.168.1.217","192.168.1.112","127.0.0.1"]
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/Shanghai'
    LOGOUT_REDIRECT_URL = '/'
    LOGIN_REDIRECT_URL = '/'
    admin.AdminSite.site_header = 'BLL运维系统管理后台'
    admin.AdminSite.site_title = '运维系统'
    `
    `cat BLL/urls.py
    from django.http import HttpResponse
    def index(request):
        return HttpResponse('123')
    url("^$", index),
    `
  - 前端模块选择
  
  - 
2. 资产管理(依赖django)
  - 新建app
  `python manage.py startapp asset`
  `python manage.py startapp user`
  > 
  - 建立model
  > 注意：使用user表，需要在settings设置AUTH_USER_MODEL = 'user.User'
   `python manage.py makemigrations`
   ` python manage.py migrate`

3. 模板初始化
 
