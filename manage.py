from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from info import creat_app, db

# from config import Config

#
# class Config():
#     DEBUG = True
#
#     SECRET_KEY = 'ZRqSDpV4b6wIoHKfgJqp5T2xiq7Jmryz2ms2XIsc3O8V5I8OTCKaMQOphf2RJVbk'
#
#
#     SQALCHEMY_DATABASES_URL = 'mysql:root@172.0.0.1:3306/infomation27'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#
#     # redis配置
#     REDIS_HOST = '127.0.0.1'
#     REDIS_PORT = 6379
#
#     # session
#     SESSION_TYPE = 'redis'
#     # 开启session签名
#     SESSION_USE_SIGNER = True
#     # 指定session保存到redis
#     SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
#     # 设置session会过期
#     SESSION_PERMANENT = False
#     # 设置过期时间
#     PERMANENT_SESSION_LIFETIME = 86400 * 2

# app = Flask(__name__)
#
# app.config.from_object(Config)
#
# db = SQLAlchemy(app)
#
# redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
#
# CSRFProtect(app)
#
# Session(app)


app = creat_app('developerment')

manager = Manager(app)
# app与db关联
Migrate(app, db)
# 迁移命令加入manager
manager.add_command('db',MigrateCommand)



# @app.route('/')
# def index():
#     session['name'] = 'ITcast'
#     logging.debug('测试db')
#     logging.warning('测试wa')
#     logging.info('测试if')
#     logging.fatal('测试ft')
#     current_app.logger.error('测试current_app')
#
#     return '00'

if __name__ == '__main__':
    manager.run()