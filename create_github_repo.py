#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub API 仓库创建脚本
用于通过GitHub API创建新的GitHub仓库并推送代码
"""

import requests
import json
import subprocess
import os
import sys

# 配置信息
GITHUB_TOKEN = ""  # 请在这里填写您的GitHub Personal Access Token
GITHUB_USERNAME = "XHJ2AIDEVS"
REPO_NAME = "social-security-advisor"
REPO_DESCRIPTION = "社保顾问WorkBuddy Skill - 2026年最新社保政策和缴费计算工具"
IS_PRIVATE = False  # 是否为私有仓库

# 仓库创建API
CREATE_REPO_API = "https://api.github.com/user/repos"

def create_repository():
    """通过GitHub API创建仓库"""
    
    # 检查token是否配置
    if not GITHUB_TOKEN:
        print("❌ 错误: 请先在脚本中配置 GITHUB_TOKEN")
        print("\n📝 获取GitHub Personal Access Token的步骤:")
        print("1. 访问: https://github.com/settings/tokens")
        print("2. 点击 'Generate new token (classic)'")
        print("3. 勾选 'repo' 权限(包括 repo:status, repo_deployment, public_repo)")
        print("4. 设置过期时间并生成token")
        print("5. 复制生成的token,粘贴到本脚本的 GITHUB_TOKEN 变量中")
        return False
    
    # 准备请求数据
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "name": REPO_NAME,
        "description": REPO_DESCRIPTION,
        "private": IS_PRIVATE,
        "auto_init": False,  # 不自动初始化(使用本地git仓库)
        "has_issues": True,
        "has_wiki": True,
        "has_downloads": True
    }
    
    print(f"🚀 正在创建GitHub仓库: {REPO_NAME}")
    print(f"📝 描述: {REPO_DESCRIPTION}")
    print(f"🔒 私有: {'是' if IS_PRIVATE else '否'}")
    print("-" * 50)
    
    try:
        # 发送创建仓库请求
        response = requests.post(CREATE_REPO_API, headers=headers, json=data, timeout=30)
        
        # 检查响应状态
        if response.status_code == 201:
            repo_data = response.json()
            print("✅ 仓库创建成功!")
            print(f"📍 仓库地址: {repo_data['html_url']}")
            print(f"🔗 克隆地址: {repo_data['clone_url']}")
            return True, repo_data
        elif response.status_code == 422:
            error_data = response.json()
            if "errors" in error_data:
                for error in error_data["errors"]:
                    if error.get("field") == "name" and "already exists" in error.get("message", ""):
                        print("⚠️  警告: 仓库已存在")
                        print(f"📍 仓库地址: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
                        return True, {"clone_url": f"git@github.com:{GITHUB_USERNAME}/{REPO_NAME}.git"}
            print(f"❌ 创建失败: {error_data}")
            return False
        else:
            print(f"❌ 创建失败 (HTTP {response.status_code})")
            print(f"错误信息: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求错误: {e}")
        return False

def push_to_github():
    """推送本地代码到GitHub"""
    
    # 获取当前工作目录
    current_dir = os.getcwd()
    
    print(f"📂 当前工作目录: {current_dir}")
    print("-" * 50)
    
    try:
        # 检查是否在git仓库中
        result = subprocess.run(
            ["git", "status"],
            capture_output=True,
            text=True,
            cwd=current_dir,
            timeout=10
        )
        
        if result.returncode != 0:
            print("❌ 错误: 当前目录不是Git仓库")
            return False
        
        # 添加远程仓库
        remote_url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
        print(f"🔗 配置远程仓库: {remote_url}")
        
        # 检查远程仓库是否已存在
        result = subprocess.run(
            ["git", "remote", "-v"],
            capture_output=True,
            text=True,
            cwd=current_dir,
            timeout=10
        )
        
        if "origin" in result.stdout:
            print("📝 更新远程仓库地址...")
            subprocess.run(
                ["git", "remote", "set-url", "origin", remote_url],
                cwd=current_dir,
                timeout=10
            )
        else:
            print("📝 添加远程仓库...")
            subprocess.run(
                ["git", "remote", "add", "origin", remote_url],
                cwd=current_dir,
                timeout=10
            )
        
        # 推送代码
        print("-" * 50)
        print("📤 正在推送代码到GitHub...")
        print("⏳ 这可能需要一些时间,请耐心等待...")
        
        result = subprocess.run(
            ["git", "push", "-u", "origin", "master"],
            cwd=current_dir,
            timeout=300
        )
        
        if result.returncode == 0:
            print("\n" + "=" * 50)
            print("🎉 代码推送成功!")
            print("=" * 50)
            print(f"📍 仓库地址: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
            print("=" * 50)
            return True
        else:
            print(f"\n❌ 推送失败")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ 操作超时")
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("  GitHub 仓库创建工具")
    print("=" * 60)
    print()
    
    # 步骤1: 创建仓库
    print("步骤 1/2: 创建GitHub仓库")
    print("-" * 60)
    success, repo_data = create_repository()
    
    if not success:
        print("\n❌ 仓库创建失败,请检查配置和网络连接")
        return False
    
    print()
    
    # 步骤2: 推送代码
    print("步骤 2/2: 推送代码到GitHub")
    print("-" * 60)
    push_success = push_to_github()
    
    if push_success:
        print("\n🎊 全部完成!")
        print(f"🔗 访问您的仓库: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        return True
    else:
        print("\n⚠️  代码推送失败,但仓库已创建")
        print(f"📍 仓库地址: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        print("💡 您可以手动执行以下命令推送:")
        print(f"   cd {os.getcwd()}")
        print(f"   git push -u origin master")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)
