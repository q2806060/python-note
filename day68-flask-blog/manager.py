#启动和管理项目的相关操作代码
from app import create_app, db
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

#导入所有的实体类方便使用db指令做迁移
from app.models import *

#调用create_app得到app实例
app = create_app()

#通过Manager()管理项目，并增加数据迁移指令
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()

