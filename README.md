# 社保政策查询与缴费规划助手

<div align="center">

![版本](https://img.shields.io/badge/版本-v2.1-blue)
![更新时间](https://img.shields.io/badge/更新-2026--03-orange)
![覆盖城市](https://img.shields.io/badge/覆盖城市-20%2B-green)
![开源协议](https://img.shields.io/badge/开源协议-MIT-yellow)

**全国通用 | 细化到省市 | 2026年最新政策**

[📦 下载 Skill](social-security-advisor-v2.1.zip) • [🖼️ 查看海报](poster/) • [📞 联系作者](#作者联系方式)

</div>

---

## ✨ 功能特性

### 📊 智能缴费计算
- 支持职工社保、灵活就业、居民社保
- 覆盖全国20+城市（北京、上海、广州、深圳、杭州、成都等）
- 自动计算个人和单位缴费明细
- 实时对比不同缴费档位

### 💰 养老金精准测算
- 根据缴费年限、档位预估退休待遇
- 基础养老金 + 个人账户养老金详细计算
- 不同缴费年限收益对比
- 延迟退休政策影响分析

### 🎯 2026补贴政策查询
- 4050就业困难人员补贴
- 高校毕业生灵活就业补贴
- 困难人员专项补贴
- 国办25号文25%补贴（至2026.12.31）
- 各省市补贴标准一键查询

### 📋 业务办理指引
- 参保登记流程
- 社保转移接续
- 异地就医备案
- 退休申请指南
- 重要时间节点提醒

---

## 🎉 2026年重大新规

| 新规内容 | 变化 | 影响 |
|---------|------|------|
| 缴费基数下限 | 60% → **50%** | 年省数千元 |
| 灵活就业参保 | 限制户籍 → **全国取消** | 凭居住证即可参保 |
| 4050补贴 | 多次申领 → **终身一次** | 申请时机关键 |
| 失业金与补贴 | 可同时领 → **互斥** | 需合理规划 |
| 小程序码支持 | - | **新增**扫码使用 |

---

## 📦 安装方式

### 方式一：下载安装包

1. 下载 [`social-security-advisor-v2.1.zip`](social-security-advisor-v2.1.zip)
2. 解压到 WorkBuddy skills 目录
3. 重启 WorkBuddy 即可使用

### 方式二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/XHJ2AIDEVS/social-security-advisor.git

# 复制 skill 目录到 WorkBuddy skills-marketplace
cp -r social-security-advisor/skill ~/.workbuddy/skills-marketplace/skills/
```

---

## 🚀 使用方法

### 快速开始

在 WorkBuddy 中，直接询问社保相关问题即可：

```
# 查询政策
"北京社保缴费基数是多少？"

# 计算缴费
"在上海，月薪15000元，每月要缴多少社保？"

# 测算养老金
"我今年35岁，在北京缴了10年社保，60岁退休能领多少养老金？"

# 查询补贴
"4050补贴怎么申请？"

# 办理指引
"社保转移怎么办理？"
```

### 运行计算器脚本

```bash
# 查看支持的城市
python scripts/social_security_calculator.py --list-cities

# 计算职工社保
python scripts/social_security_calculator.py --city 北京 --salary 15000

# 计算灵活就业
python scripts/social_security_calculator.py --city 上海 --type flex --base-rate 80

# 测算养老金
python scripts/social_security_calculator.py --retirement --city 北京 --years 30 --avg-index 0.8
```

---

## 📚 文档结构

```
social-security-advisor/
├── skill/                          # Skill 核心文件
│   ├── SKILL.md                    # Skill 定义和工作流程
│   ├── references/                 # 参考文档
│   │   ├── national-policy.md      # 全国基准政策
│   │   ├── province-policy.md      # 各省市详细政策
│   │   ├── calculation-guide.md    # 计算公式与测算
│   │   ├── service-guide.md        # 业务办理指南
│   │   └── subsidy-policy-2026.md  # 2026年补贴政策
│   └── scripts/                    # 工具脚本
│       └── social_security_calculator.py
├── poster/                         # 推广海报
│   └── index.html
├── social-security-advisor-v2.1.zip # 打包文件
└── README.md
```

---

## 🌟 数据覆盖

### 已支持城市（20+）

直辖市：北京、上海、天津、重庆

省会城市：广州、深圳、杭州、南京、成都、武汉、西安、长沙、郑州、济南、合肥、南宁、呼和浩特、乌鲁木齐、拉萨、海口、福州、南昌、哈尔滨、长春、贵阳、昆明

> 持续更新中，如需添加其他城市，欢迎提交 Issue 或 Pull Request

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🔗 相关链接

- [WorkBuddy 官网](https://www.codebuddy.cn)
- [Skills Marketplace](https://github.com/workbuddy/skills-marketplace)
- [国家社会保险公共服务平台](https://www.12333.gov.cn)

---

## 📊 更新日志

### v2.1 (2026-03-17)
- ✨ 新增作者联系方式展示
- ✨ 新增小程序码支持
- 🎨 优化推广海报设计
- 🐛 修复若干显示问题

### v2.0.0 (2026-03-17)
- 🎉 重大更新：新增 2026年补贴政策模块
- 📊 更新各省市最新补贴标准
- 📝 新增 `subsidy-policy-2026.md` 文档
- 🚀 更新缴费基数下限至50%
- 📱 新增灵活就业无户籍限制政策
- 🔧 升级计算器脚本

### v1.0.0 (2025-12-01)
- 🎉 首次发布
- ✨ 基础社保查询功能
- 📊 缴费计算器
- 💰 养老金测算

---

## 📞 作者联系方式

<div align="center">

### QQ
**1817694478**

### 微信扫码留言
<div style="margin: 20px 0;">
  <img src="https://gpt.cntaxs.com/smart-admin-api/upload/public/notice/5eb569d40189404aa3a1a3fd0f0141fa_20260317215606.png" alt="微信二维码" style="width: 200px; max-width: 100%; height: auto;">
</div>

**微信扫码互动交流**

---

> 如有问题反馈或合作咨询，欢迎通过以上方式联系作者

</div>

---

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star 支持一下！

[![Star History Chart](https://api.star-history.com/svg?repos=XHJ2AIDEVS/social-security-advisor&type=Date)](https://star-history.com/#XHJ2AIDEVS/social-security-advisor&Date)

---

<div align="center">

**Made with ❤️ by WorkBuddy Community**

**Copyright © 2026. All rights reserved.**

</div>
