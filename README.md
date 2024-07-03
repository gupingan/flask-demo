## Flask 速通案例

系统地学习并快速掌握 Flask 框架，从快速启动到高级功能的实现，涵盖了 Flask 开发的各个方面。通过一系列有条理的示例和练习，帮助开发者深入理解 Flask 的核心概念和最佳实践。

### 依赖解决

```bash
pip install poetry  # 国内下载缓慢请自行使用镜像源下载

# 接下来安装环境所依赖的包
poetry lock
poetry install
```

### 大纲目录

#### Day 01: Flask 基础

1. **快速启动 Flask 项目**：介绍如何快速启动一个 Flask 项目。
2. **Flask 项目加载配置**：讲解如何在 Flask 项目中加载配置文件。
3. **路由的基本参数**：介绍 Flask 路由的基本参数设置。
4. **路由转换器以及路由参数**：深入讲解路由转换器的使用以及如何传递路由参数。
5. **自定义路由转换器**：学习如何自定义路由转换器以满足特定需求。
6. **Flask 命令行运行**：介绍如何通过命令行运行 Flask 项目。

#### Day 02: 请求与响应

1. **获取请求中的查询参数**：学习如何获取请求中的查询参数。
2. **HTTP 获取请求体**：讲解如何获取 HTTP 请求体中的数据。
3. **HTTP 获取请求头**：介绍如何获取 HTTP 请求头信息。
4. **响应数据**：学习如何构建和返回响应数据。
5. **HTTP 跳转页面**：介绍如何实现页面跳转。
6. **跳转页面并携带路由参数**：深入讲解如何在页面跳转时携带路由参数。
7. **自定义状态码和响应头**：学习如何自定义 HTTP 状态码和响应头。
8. **Cookie 的使用和基于 Cookie 的登录验证**：介绍 Cookie 的使用以及如何基于 Cookie 实现登录验证。
9. **Session 的使用和基于 Session 的登录验证**：学习 Session 的使用以及如何基于 Session 实现登录验证。

#### Day 03: 请求钩子与模板引擎

1. **请求全局钩子及其生命周期**：介绍请求全局钩子的概念及其生命周期。
2. **主动抛出异常和捕获异常**：学习如何主动抛出和捕获异常。
3. **上下文全局变量**：讲解 Flask 中的上下文全局变量。
4. **Flask 部分子命令**：介绍 Flask 的部分子命令及其使用。
5. **练习生成项目**：通过练习生成一个简单的 Flask 项目。
6. **Flask 中视图引入模板**：学习如何在视图中引入模板。
7. **render_template 与 render_template_string**：对比 `render_template` 和 `render_template_string` 的使用。

#### Day 04: 模板与静态文件

1. **模板输出变量**：学习如何在模板中输出变量。
2. **模板中的 IF 流程控制**：介绍模板中的 IF 流程控制语句。
3. **模板中的 FOR 流程控制**：讲解模板中的 FOR 流程控制语句。
4. **过滤器的基本使用**：学习如何在模板中使用过滤器。
5. **常见的内置过滤器**：介绍一些常见的内置过滤器。
6. **列表过滤器与块过滤器**：深入讲解列表过滤器与块过滤器的使用。
7. **自定义过滤器**：学习如何自定义过滤器。
8. **模板继承**：介绍模板继承的概念及其实现。
9. **CSRF 攻击防范**：学习如何防范 CSRF 攻击。

#### Day 05: SQLAlchemy 基础

1. **SQLAlchemy 基本使用**：介绍 SQLAlchemy 的基本使用方法。
2. **Flask-SQLAlchemy 连接**：讲解如何在 Flask 中连接 SQLAlchemy。
3. **Flask-SQLAlchemy 基本操作 [REST]**：学习 SQLAlchemy 的基本 CRUD 操作。
4. **Flask-SQLAlchemy 查询数据**：介绍如何使用 SQLAlchemy 查询数据。
5. **Flask-SQLAlchemy 过滤查询**：学习如何使用 SQLAlchemy 进行过滤查询。
6. **Flask-SQLAlchemy 逻辑查询和限制查询**：深入讲解逻辑查询和限制查询。
7. **Flask-SQLAlchemy 分页查询**：学习如何实现分页查询。
8. **Flask-SQLAlchemy 聚合分组**：介绍聚合查询和分组查询的使用。
9. **Flask-SQLAlchemy 关联查询一对一**：学习一对一关联查询的实现。
10. **Flask-SQLAlchemy 关联查询一对多**：介绍一对多关联查询的实现。

#### Day 06: SQLAlchemy 进阶

1. **创建连接、会话及模型**：学习如何创建连接、会话及定义模型。
2. **添加一条数据**：介绍如何添加一条数据。
3. **添加多条数据**：学习如何添加多条数据。
4. **查询一条数据**：介绍查询一条数据的方法。
5. **条件过滤数据**：深入讲解条件过滤数据的实现。
6. **逻辑查询数据**：学习逻辑查询数据的方法。
7. **成员查询数据**：介绍成员查询数据的实现。
8. **更新数据**：学习如何更新数据。
9. **删除数据**：介绍如何删除数据。
10. **其他操作**：学习一些其他常见的操作。
11. **原生 SQL 执行**：介绍如何执行原生 SQL 语句。
12. **异步操作**：学习如何在 SQLAlchemy 中实现异步操作。

#### Day 07: 进阶功能

1. **Flask-SQLAlchemy 关系表关联查询多对多**：学习多对多关联查询的实现。
2. **Flask-SQLAlchemy 关系模型关联查询多对多**：深入讲解多对多关联模型的查询。
3. **FlaskAlchemy 自关联表示行政区划**：学习自关联模型的实现。
4. **Flask-SQLAlchemy 临时逻辑外键关联查询**：介绍临时逻辑外键关联查询的实现。
5. **Flask-SQLAlchemy 模型内虚拟外键关联查询**：学习虚拟外键关联查询的实现。
6. **Flask-Migrate 数据迁移**：学习如何使用 Flask-Migrate 进行数据迁移。
7. **Faker 生成测试数据**：介绍如何使用 Faker 生成测试数据。
8. **蓝图的实现以及使用**：学习如何实现和使用蓝图。
9. **Flask-session 的使用**：介绍 Flask-session 的使用。
10. **Flask-Session 结合 SqlAlchemy**：学习如何结合 SqlAlchemy 使用 Flask-Session。
11. **Flask-Session 结合 Redis**：介绍如何结合 Redis 使用 Flask-Session。