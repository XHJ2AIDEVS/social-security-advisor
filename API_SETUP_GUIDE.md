# GitHub API 创建仓库使用指南

## 📋 准备工作

### 1. 获取 GitHub Personal Access Token

#### 步骤:
1. 访问 GitHub Token 设置页面:
   ```
   https://github.com/settings/tokens
   ```

2. 点击 "Generate new token" → "Generate new token (classic)"

3. 配置 Token:
   - **Note**: 输入描述,例如 "Social Security Advisor"
   - **Expiration**: 选择过期时间(建议选择 "30 days" 或 "No expiration")
   - **Select scopes**: 勾选以下权限:
     - ✅ `repo` (完整仓库访问权限)
     - ✅ `repo:status`
     - ✅ `repo_deployment`
     - ✅ `public_repo` (如果是公开仓库)

4. 点击 "Generate token" 生成token

5. **重要**: 立即复制token(只显示一次!)
   ```
   ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

### 2. 配置脚本

编辑 `create_github_repo.py` 文件:

```python
# 在第11行附近填写您的token
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # 粘贴您的token
```

**其他配置**(已预设,如需修改):
```python
GITHUB_USERNAME = "XHJ2AIDEVS"  # GitHub用户名
REPO_NAME = "social-security-advisor"  # 仓库名称
REPO_DESCRIPTION = "社保顾问WorkBuddy Skill"  # 仓库描述
IS_PRIVATE = False  # 是否为私有仓库(True/False)
```

## 🚀 使用方法

### 方法1: 直接运行(推荐)

1. **打开PowerShell或命令提示符**

2. **进入项目目录**:
   ```powershell
   cd c:/Users/Administrator/WorkBuddy/20260317174751/social-security-advisor-github
   ```

3. **运行脚本**:
   ```powershell
   python create_github_repo.py
   ```

4. **等待执行完成**
   - 脚本会自动创建仓库
   - 自动推送所有代码
   - 完成后显示仓库地址

### 方法2: 分步执行

如果自动推送失败,可以分步执行:

#### 步骤1: 创建仓库
```powershell
python create_github_repo.py
```

如果创建成功但推送失败,继续步骤2。

#### 步骤2: 手动推送
```powershell
git push -u origin master
```

## 📝 执行过程说明

### 预期输出:

```
============================================================
  GitHub 仓库创建工具
============================================================

步骤 1/2: 创建GitHub仓库
------------------------------------------------------------
🚀 正在创建GitHub仓库: social-security-advisor
📝 描述: 社保顾问WorkBuddy Skill - 2026年最新社保政策和缴费计算工具
🔒 私有: 否
--------------------------------------------------
✅ 仓库创建成功!
📍 仓库地址: https://github.com/XHJ2AIDEVS/social-security-advisor
🔗 克隆地址: https://github.com/XHJ2AIDEVS/social-security-advisor.git

步骤 2/2: 推送代码到GitHub
------------------------------------------------------------
📂 当前工作目录: c:\Users\Administrator\WorkBuddy\20260317174751\social-security-advisor-github
🔗 配置远程仓库: https://github.com/XHJ2AIDEVS/social-security-advisor.git
📝 添加远程仓库...
--------------------------------------------------
📤 正在推送代码到GitHub...
⏳ 这可能需要一些时间,请耐心等待...

==================================================
🎉 代码推送成功!
==================================================
📍 仓库地址: https://github.com/XHJ2AIDEVS/social-security-advisor
==================================================

🎊 全部完成!
🔗 访问您的仓库: https://github.com/XHJ2AIDEVS/social-security-advisor
```

## ⚠️ 常见问题

### 问题1: "请先在脚本中配置 GITHUB_TOKEN"

**原因**: 未配置GitHub Token

**解决**:
1. 编辑 `create_github_repo.py`
2. 找到第11行 `GITHUB_TOKEN = ""`
3. 粘贴您的token

### 问题2: "创建失败 (HTTP 401)"

**原因**: Token无效或已过期

**解决**:
1. 重新生成token
2. 更新脚本中的token

### 问题3: "创建失败 (HTTP 422) - 仓库已存在"

**原因**: 仓库已被创建

**解决**:
- 这是正常的,脚本会继续推送代码

### 问题4: "网络请求错误"

**原因**: 网络连接问题

**解决**:
1. 检查网络连接
2. 尝试使用VPN或代理
3. 配置Python requests使用代理:
   ```python
   proxies = {
       'http': 'http://proxy-server:port',
       'https': 'https://proxy-server:port',
   }
   # 在 requests.post() 中添加 proxies=proxies
   ```

### 问题5: "推送失败"

**原因**: Git推送失败

**解决**:
1. 手动执行: `git push -u origin master`
2. 检查是否需要认证
3. 查看详细错误信息

## 🔒 安全建议

1. **不要泄露Token**:
   - 不要将token提交到Git仓库
   - 不要在公开平台分享token
   - 脚本执行完成后可以删除token

2. **使用环境变量**(更安全):

   ```powershell
   # PowerShell
   $env:GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   python create_github_repo.py
   ```

   然后修改脚本:
   ```python
   import os
   GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
   ```

3. **定期更新Token**:
   - 建议设置过期时间
   - 定期更换token

## ✅ 验证创建成功

1. 访问仓库地址: https://github.com/XHJ2AIDEVS/social-security-advisor

2. 检查文件列表:
   - ✅ SKILL.md
   - ✅ references/ (5个文档)
   - ✅ scripts/social_security_calculator.py
   - ✅ poster/index.html
   - ✅ README.md
   - ✅ LICENSE
   - ✅ .gitignore

3. 检查提交记录:
   - 应该有3次提交(v1, v2, v3)

## 📞 获取帮助

如果遇到问题:
- **QQ**: 1817694478
- **微信**: 扫描二维码留言

---

**生成时间**: 2026-03-17
**项目**: Social Security Advisor Skill
