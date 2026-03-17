# GitHub 推送操作指南

## 当前状态
✅ Git本地仓库已初始化并提交(位于 `social-security-advisor-github/`)
✅ 远程仓库地址已配置: `https://github.com/XHJ2AIDEVS/social-security-advisor.git`
⏳ 等待推送到远程仓库

## 推送步骤

### 前提条件
1. **确保您已在GitHub上创建了仓库**: `social-security-advisor`
   - 如果未创建,请先访问 https://github.com/new 创建空仓库
   - 仓库名称必须为: `social-security-advisor`

2. **配置Git凭据**(首次推送需要):
   ```powershell
   git config --global user.name "XHJ2AIDEVS"
   git config --global user.email "your-email@example.com"  # 替换为您的邮箱
   ```

   **或者使用Personal Access Token**(推荐):
   - 访问 https://github.com/settings/tokens 生成token
   - 选择 `repo` 权限
   - 复制token,推送时会作为密码使用

### 推送命令

在PowerShell中执行以下命令:

```powershell
# 进入项目目录
cd c:/Users/Administrator/WorkBuddy/20260317174751/social-security-advisor-github

# 推送到GitHub(首次推送需要输入用户名和密码/token)
git push -u origin master
```

**如果遇到认证问题,使用token方式:**
```powershell
# 推送时用户名输入: XHJ2AIDEVS
# 密码输入: your-personal-access-token
git push -u origin master
```

### 验证推送成功

推送成功后,访问以下地址查看仓库:
📦 **https://github.com/XHJ2AIDEVS/social-security-advisor**

## 常见问题解决

### 问题1: "Failed to connect to github.com"
- **原因**: 网络连接问题或防火墙拦截
- **解决**:
  1. 检查网络连接
  2. 尝试使用VPN或代理
  3. 配置Git使用代理:
     ```powershell
     git config --global http.proxy http://proxy-server:port
     git config --global https.proxy https://proxy-server:port
     ```

### 问题2: "Authentication failed"
- **原因**: 用户名、密码或token错误
- **解决**:
  1. 使用GitHub用户名和密码(密码已弃用,建议使用token)
  2. 或使用Personal Access Token
  3. 清除凭据缓存:
     ```powershell
     git credential-manager erase
     ```

### 问题3: "src refspec master does not match any"
- **原因**: 本地分支名称不匹配
- **解决**: 检查当前分支名称并推送:
  ```powershell
  git branch
  git push -u origin <当前分支名称>
  ```

### 问题4: 远程仓库已存在文件
- **原因**: GitHub仓库非空
- **解决**: 强制推送(谨慎使用):
  ```powershell
  git push -u origin master --force
  ```
  或先拉取再推送:
  ```powershell
  git pull origin master --allow-unrelated-histories
  git push -u origin master
  ```

## 推送后的仓库结构

成功推送后,您的GitHub仓库应包含以下文件:

```
social-security-advisor/
├── .gitignore
├── LICENSE
├── README.md
├── SKILL.md
├── GITHUB_SETUP_GUIDE.md
├── references/
│   ├── calculation-guide.md
│   ├── national-policy.md
│   ├── province-policy.md
│   ├── service-guide.md
│   └── subsidy-policy-2026.md
├── scripts/
│   └── social_security_calculator.py
├── assets/
│   └── qr-wechat.png (需手动添加)
└── social-security-advisor-poster.html
```

## 下一步操作

推送成功后,您可以:

1. **设置仓库为公开**: 在GitHub仓库设置中选择"Public"
2. **添加描述**: 在仓库About区域添加项目描述
3. **添加Topics**: 添加 `social-security`, `calculator`, `workbuddy-skill` 等标签
4. **发布Release**: 在GitHub Releases中发布v1.0.0版本

## 联系支持

如果推送过程中遇到问题,请联系:
- **QQ**: 1817694478
- **微信**: 扫描二维码留言

---

**生成时间**: 2026-03-17
**项目**: Social Security Advisor Skill
**GitHub用户**: XHJ2AIDEVS
