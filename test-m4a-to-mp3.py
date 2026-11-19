# 代码为AI生成
from pydub import AudioSegment

# 1. 这里改成你自己的m4a文件路径，比如"我的音频.m4a"
m4a_file = "/Users/luojingfeng/Desktop/中奖概率倍高.m4a"
# 2. 输出的mp3文件名
mp3_file = "/Users/luojingfeng/Desktop/test.mp3"

# 读取m4a文件，转成AudioSegment对象
audio = AudioSegment.from_file(m4a_file, format="m4a")
# 导出为mp3，比特率设为192k（音质足够，体积也不大）
audio.export(mp3_file, format="mp3", bitrate="192k")

print("转换完成啦！")