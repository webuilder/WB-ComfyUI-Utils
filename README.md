# ComfyUI WB Audio Duration Node

一个简单的ComfyUI自定义节点，用于获取音频文件的时长。

## 功能

- 支持1D, 2D, 3D音频张量格式
- 支持 `waveform` 和 `audio` 键格式
- 提供详细的调试信息
- 格式化时长显示（秒、分、小时）

## 安装

1. 将此文件夹复制到ComfyUI的 `custom_nodes` 目录
2. 重启ComfyUI
3. 在节点列表中找到 "WB Audio Duration"

## 使用方法

1. 添加 "Load Audio" 节点加载音频文件
2. 添加 "WB Audio Duration" 节点
3. 连接音频输出到时长节点
4. 运行工作流查看结果

## 输出

- `duration_seconds`: 时长（秒，浮点数）
- `duration_text`: 格式化的时长文本

## 支持格式

- 1D张量: `[samples]`
- 2D张量: `[channels, samples]` 或 `[batch, samples]`
- 3D张量: `[batch, channels, samples]`

## 调试信息

节点会在控制台输出详细的调试信息，包括：
- 音频输入类型
- 音频字典键
- 音频数据形状
- 计算过程 