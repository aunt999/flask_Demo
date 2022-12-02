#带有前后下划线的变量为python内置变量，如：__name__，其它为自定义变量
class User:
    table_name = 'zt_build'    #叫类属性
    def __init__(self):  #构造函数，初始化
        self.username = 'qiang'  #叫实例变量
        self.password = '123456'
        self.email = 'qiang@sina.com'

    def method(self, value):  #方法
        print("Hello %s" %value)


    def chain(self):
        print('通过返回当前类的实例进行连接的方法调用')
        return self

    def hello(self):
        print('Hello in china')
        return self

if __name__ == '__main__':
    user = User()   #实例化User类

    #链式操作的方法
    user.chain().chain().hello().chain()


    #将上面类定义的中的各种属性、方法（含内存地址）都以集合的形式显示出来
    print(User.__dict__)   #通过类名可以直接获取到类属性和方法
    print(user.__class__)  #通过实例可以获取到类的类名
    print(user.__class__.__dict__)   #通过实例也可以直接获取到类属性和方法
    print(user.__class__.__name__)   #通过实例获取到类的名称

    #以下三种为类的实例设置实例变量
    #第一种
    user.nickname = '张三'   #动态为实例设置变量
    print(user.__dict__)  #获取到类的定义的实例变量和值，包含新增的实例变量
    #第二种
    user.__setattr__('sex', '男')   #动态为实例设置变量,此方法以变量是字符串的方式定义
    print(user.__dict__)
    #第三种
    setattr(user, 'year-old', 24)  #动态为实例设置变量,此方法以变量是字符串的方式定义
    print(user.__dict__)

    #设置后获取实例变量的方式
    print(user.__getattribute__('sex'))   #这是get属性变量值的方式获取
    print(user.__getattribute__('method'))  #获取实例的方法
    user.__getattribute__('method')('福建')  #通过此方法，可以调用方法一
    print(user.__class__.__getattribute__(user, "table_name"))  #获取类中的属性变量的值
    getattr(user, 'method')('福州')   #通过此方法，可以调用方法二



    #通过双下划线来区分是否自定义的属性和方法
    for k, v in user.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, v)
