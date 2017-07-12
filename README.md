# BLL运维管理系统
1. 基础环境部署
  - 选择git工具(coding.net)
      `git clone https://git.coding.net/benq1211/BLL.git`
      > 注意：.gitignore排除文件
  - 新建django项目
    `django-admin startproject BLL`
    `pip install django-bootstrap-form`
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
   > 注意：模板文件路径放在根目录下
   > settings配置：
    `'DIRS': [os.path.join(BASE_DIR, 'templates')],`

   提取模板到base.html
4. 资产功能实现
   1. 列出所有的资产
      ip,hostanme,group,env,cpu,memory,disk
   2. 详细列表(未做)
   3. 删除(未实行)
   4. 添加(未实行)
5. 项目组添加
   1. 列出所有的项目
   2. 删除 (改进弹框确认)
   3. 添加





 # 问题总结
   1. 多对多数据库怎么传递参数字段显示
    asset 和 assetgroup 是多对多的关系

      models.py
group = models.ManyToManyField(AssetGroup, blank=True, verbose_name=u"所属主机组")

views.py
def index(request):
    asset_list = Asset.objects.all()

    return render(request,'asset/index.html',{'asset_list':asset_list})



template.html


td>{{  asset.group.name }}</td>


这个asset.group.name怎么通过view.py传递到template.html




2  多传递参数进行保存
class GroupCreateView(CreateView):
    def form_valid(self):
        """form is valid"""
        group = form.save(commit=False) # create group instanse but don't save in database
        group.user = request.user
        group.save() # save group to database


