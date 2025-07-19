# 发布指南

## 发布到Node Manager的步骤

### 1. 准备GitHub仓库

1. 在GitHub上创建新仓库 ✅ 已完成
2. 仓库名: `WB-ComfyUI-Utils` ✅ 已完成
3. 设置为公开仓库 ✅ 已完成

### 2. 上传代码

```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: WB ComfyUI Utils - Audio Duration Node"

# 添加远程仓库
git remote add origin https://github.com/webuilder/WB-ComfyUI-Utils.git

# 推送到GitHub
git push -u origin main
```

### 3. 更新package.json

编辑 `package.json` 文件，更新以下信息：

```json
{
  "name": "wb-comfyui-utils",
  "version": "1.0.0",
  "description": "A collection of useful ComfyUI utility nodes including audio duration, text processing, and more",
  "author": "webuilder",
  "repository": {
    "type": "git",
    "url": "https://github.com/webuilder/WB-ComfyUI-Utils"
  },
  "keywords": [
    "comfyui",
    "utils",
    "audio",
    "duration",
    "text",
    "processing",
    "nodes"
  ],
  "license": "MIT",
  "dependencies": [],
  "comfyui": {
    "nodes": [
      "WB_AudioDuration"
    ]
  }
}
```

### 4. 更新README.md

编辑 `README.md` 文件，更新：
- 作者信息 ✅ 已完成
- GitHub仓库链接 ✅ 已完成
- 问题反馈链接 ✅ 已完成

### 5. 更新LICENSE

编辑 `LICENSE` 文件，更新版权信息：
```
Copyright (c) 2024 webuilder
```
✅ 已完成

### 6. 测试节点

在发布前，确保节点在ComfyUI中正常工作：
1. 将代码复制到ComfyUI的custom_nodes目录
2. 重启ComfyUI
3. 测试节点功能

### 7. 创建Release

1. 在GitHub仓库页面点击 "Releases"
2. 点击 "Create a new release"
3. 填写版本信息：
   - Tag: v1.0.0
   - Title: WB ComfyUI Utils v1.0.0
   - Description: 描述工具集功能
4. 发布Release

### 8. 等待Node Manager收录

Node Manager会自动扫描GitHub上的ComfyUI节点仓库。通常需要几天时间才会出现在搜索结果中。

### 9. 验证发布

1. 在ComfyUI中打开Node Manager
2. 搜索 "WB Utils" 或 "WB Audio Duration"
3. 确认节点可以正常安装

## 注意事项

1. **仓库必须是公开的** ✅ 已完成
2. **必须包含package.json文件** ✅ 已完成
3. **package.json中的comfyui.nodes字段必须正确** ✅ 已完成
4. **README.md应该包含详细的安装和使用说明** ✅ 已完成
5. **代码应该经过充分测试**

## 常见问题

### Q: 节点没有出现在Node Manager中？
A: 检查以下几点：
- 仓库是否为公开 ✅ 已完成
- package.json格式是否正确 ✅ 已完成
- 是否创建了Release

### Q: 安装后节点不工作？
A: 检查以下几点：
- __init__.py文件是否正确 ✅ 已完成
- 节点注册是否正确 ✅ 已完成
- 依赖是否满足 ✅ 已完成

### Q: 如何更新节点？
A: 创建新的Release，更新版本号。

### Q: 如何添加新节点到工具集？
A: 
1. 在__init__.py中添加新节点类
2. 在NODE_CLASS_MAPPINGS中注册新节点
3. 在package.json的comfyui.nodes数组中添加新节点名
4. 更新README.md文档
5. 创建新的Release 