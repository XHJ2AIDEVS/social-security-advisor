# GitHub 仓库发布指南

## 步骤一：在 GitHub 上创建新仓库

1. 访问 [GitHub 新建仓库页面](https://github.com/new)

2. 填写仓库信息：
   - **Repository name**: `social-security-advisor`
   - **Description**: 全国通用、细化到省市的社保政策查询与缴费规划助手（2026版）
   - **Public**: ☑️ 公开仓库
   - **Add a README file**: ☐ 不勾选（我们已经有了）
   - **Add .gitignore**: ☐ 不勾选（我们已经有了）
   - **Choose a license**: ☐ 不勾选（我们已经有了 MIT License）

3. 点击 "Create repository" 按钮

4. 记下仓库的 URL，例如：`https://github.com/yourusername/social-security-advisor.git`

## 步骤二：推送代码到 GitHub

在命令行中执行以下命令（请替换 `yourusername` 为您的 GitHub 用户名）：

```bash
cd C:\Users\Administrator\WorkBuddy\20260317174751\social-security-advisor-github

# 添加远程仓库
git remote add origin https://github.com/yourusername/social-security-advisor.git

# 推送到 GitHub
git push -u origin master
```

如果需要认证，GitHub 会提示您输入用户名和密码（或 Personal Access Token）。

## 步骤三：配置 GitHub Pages（可选）

如果您想在线展示海报：

1. 进入仓库页面，点击 "Settings"
2. 在左侧菜单中找到 "Pages"
3. 在 "Build and deployment" 下：
   - Source: 选择 "Deploy from a branch"
   - Branch: 选择 `main` (或 `master`) 和 `/(root)`
4. 点击 "Save"

等待几分钟后，您的海报将在以下 URL 可访问：
`https://yourusername.github.io/social-security-advisor/`

## 步骤四：创建 GitHub Release（推荐）

1. 进入仓库页面，点击 "Releases" → "Create a new release"
2. 填写信息：
   - **Tag**: `v2.1`
   - **Release title**: `v2.1 - 2026年社保补贴政策更新`
   - **Description**:
     ```
     ## 新增功能
     - 2026年社保补贴政策模块
     - 各省市最新补贴标准
     - 缴费基数下限降至50%
     - 灵活就业无户籍限制
     - 推广海报

     ## 优化改进
     - 更新文档结构
     - 添加作者联系方式
     - 新增小程序码支持

     ## 数据更新
     - 20+城市社保数据
     - 2026年最新政策
     ```
3. 点击 "Publish release"

## 步骤五：完善仓库信息

在 GitHub 仓库页面：

1. **添加话题标签**（Topics）：
   - `social-security`
   - `insurance`
   - `python`
   - `workbuddy`
   - `china`
   - `pension`
   - `government-services`

2. **设置仓库徽章**（可选）：
   访问 [shields.io](https://shields.io) 创建自定义徽章

3. **添加贡献者指南**（可选）：
   创建 `CONTRIBUTING.md` 文件

## 常见问题

### Q: 推送时提示认证失败怎么办？

A: GitHub 已不再支持密码认证，请使用 Personal Access Token：
1. 访问 GitHub Settings → Developer settings → Personal access tokens
2. 生成新 token，勾选 `repo` 权限
3. 使用 token 代替密码进行认证

### Q: 如何删除已有的远程仓库？

A:
```bash
git remote remove origin
git remote add origin https://github.com/yourusername/social-security-advisor.git
```

### Q: 如何修改仓库的 README.md？

A: 直接在 GitHub 仓库页面在线编辑，或本地修改后执行：
```bash
git add README.md
git commit -m "Update README"
git push
```

## 下一步建议

1. **添加小程序码图片**：
   将小程序码图片命名为 `miniprogram-code.png`，放到 `poster/` 目录

2. **创建 Issues 模板**：
   在 `.github/ISSUE_TEMPLATE/` 目录下创建问题模板

3. **添加 CI/CD 配置**（可选）：
   在 `.github/workflows/` 目录下添加自动化工作流

4. **发布到 WorkBuddy Skills Marketplace**：
   将仓库链接提交到官方 marketplace

---

## 仓库信息汇总

- **仓库名称**: social-security-advisor
- **版本**: v2.1
- **开源协议**: MIT License
- **本地路径**: `C:\Users\Administrator\WorkBuddy\20260317174751\social-security-advisor-github`
- **文件数量**: 12 个文件
- **提交次数**: 1 次提交

---

**完成后，请将您的 GitHub 仓库 URL 告诉我，我可以帮您进一步优化！**
