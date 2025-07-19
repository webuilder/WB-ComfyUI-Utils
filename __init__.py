# ComfyUI Audio Duration Node Package

# 直接定义节点类，避免导入问题
import os
import sys
import folder_paths

# 尝试导入torch，如果失败则使用备用方法
try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("警告: torch未安装，将使用备用方法处理音频数据")

class WB_AudioDurationNode:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.output_node = True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
        }

    RETURN_TYPES = ("FLOAT", "STRING",)
    RETURN_NAMES = ("duration_seconds", "duration_text",)
    FUNCTION = "get_duration"
    OUTPUT_NODE = True
    CATEGORY = "audio"

    def get_duration(self, audio):
        """
        简化的音频时长获取函数
        支持1D, 2D, 3D张量格式
        """
        try:
            print(f"=== 音频分析开始 ===")
            print(f"音频输入类型: {type(audio)}")
            
            # 处理字典格式
            if isinstance(audio, dict):
                print(f"音频字典键: {list(audio.keys())}")
                
                # 检查是否有必要的键 - 支持两种格式
                if ('waveform' in audio and 'sample_rate' in audio) or ('audio' in audio and 'sample_rate' in audio):
                    # 优先使用waveform，如果没有则使用audio
                    if 'waveform' in audio:
                        audio_data = audio['waveform']
                        print("使用waveform键")
                    else:
                        audio_data = audio['audio']
                        print("使用audio键")
                    
                    sample_rate = audio['sample_rate']
                    
                    print(f"音频数据类型: {type(audio_data)}")
                    print(f"采样率: {sample_rate}")
                    
                    # 尝试获取音频长度
                    if hasattr(audio_data, 'shape'):
                        print(f"音频数据形状: {audio_data.shape}")
                        
                        # 计算样本数 - 支持1D, 2D, 3D张量
                        if len(audio_data.shape) == 1:
                            # 1D: [samples]
                            num_samples = audio_data.shape[0]
                            print("处理1D张量")
                        elif len(audio_data.shape) == 2:
                            # 2D: [channels, samples] 或 [batch, samples]
                            num_samples = audio_data.shape[1]
                            print("处理2D张量")
                        elif len(audio_data.shape) == 3:
                            # 3D: [batch, channels, samples]
                            num_samples = audio_data.shape[2]
                            print("处理3D张量")
                        else:
                            return (0.0, f"不支持的形状: {audio_data.shape}")
                        
                        # 计算时长
                        duration_seconds = num_samples / sample_rate
                        duration_text = self.format_duration(duration_seconds)
                        
                        print(f"样本数: {num_samples}")
                        print(f"计算出的时长: {duration_seconds}秒")
                        print(f"格式化时长: {duration_text}")
                        
                        return (duration_seconds, duration_text)
                    
                    elif hasattr(audio_data, '__len__'):
                        # 如果数据有长度属性
                        num_samples = len(audio_data)
                        duration_seconds = num_samples / sample_rate
                        duration_text = self.format_duration(duration_seconds)
                        
                        print(f"使用长度属性，样本数: {num_samples}")
                        print(f"计算出的时长: {duration_seconds}秒")
                        
                        return (duration_seconds, duration_text)
                    
                    else:
                        return (0.0, f"无法获取音频数据长度，类型: {type(audio_data)}")
                
                else:
                    return (0.0, f"音频字典缺少必要键，当前键: {list(audio.keys())}")
            
            # 处理字符串（文件路径）
            elif isinstance(audio, str):
                print(f"音频文件路径: {audio}")
                if os.path.exists(audio):
                    # 简单估算
                    file_size = os.path.getsize(audio)
                    estimated_duration = (file_size * 8) / (128 * 1000)  # 假设128kbps
                    duration_text = self.format_duration(estimated_duration)
                    return (estimated_duration, f"估算时长: {duration_text}")
                else:
                    return (0.0, f"文件不存在: {audio}")
            
            else:
                return (0.0, f"不支持的音频输入类型: {type(audio)}")
                
        except Exception as e:
            import traceback
            print(f"=== 错误详情 ===")
            print(f"错误类型: {type(e)}")
            print(f"错误信息: {str(e)}")
            print(f"错误堆栈: {traceback.format_exc()}")
            return (0.0, f"处理错误: {str(e)}")

    def format_duration(self, seconds):
        """
        格式化时长显示
        """
        if seconds < 1:
            return f"{seconds:.3f}秒"
        elif seconds < 60:
            return f"{seconds:.2f}秒"
        elif seconds < 3600:
            minutes = int(seconds // 60)
            remaining_seconds = seconds % 60
            return f"{minutes}分{remaining_seconds:.2f}秒"
        else:
            hours = int(seconds // 3600)
            remaining_minutes = int((seconds % 3600) // 60)
            remaining_seconds = seconds % 60
            return f"{hours}小时{remaining_minutes}分{remaining_seconds:.2f}秒"

# 节点注册
NODE_CLASS_MAPPINGS = {
    "WB_AudioDuration": WB_AudioDurationNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WB_AudioDuration": "WB Audio Duration"
}

print("ComfyUI WB Audio Duration Node 已加载") 