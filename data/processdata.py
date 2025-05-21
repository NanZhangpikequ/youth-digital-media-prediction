import pandas as pd
import os


file_path = r"C:\Users\Nanzh\PycharmProjects\pythonProject6\educationproject\raw_data_utf8.csv"
df = pd.read_csv(file_path)


df.fillna({
    '1、您的性别：': '未知',
    '3、当前所处教育阶段:': '未知',
    '5、主要使用场景': '未知',
}, inplace=True)
df.fillna(df.median(numeric_only=True), inplace=True)

age_mapping = {
    "6-8岁": 0.9,
    "16~18": 0.75,
    "19~21": 0.4,
    "22岁及以上": 0.2
}
gender_mapping = {"男": 0, "女": 1, "未知": -1}
education_mapping = {
    "高中阶段": 0.75,
    "高等教育阶段（大学-博士后）": 0.3,
    "已工作": 0.2,
    "未知": -1
}

df['年龄映射'] = df['2、您的年龄段：'].map(age_mapping)
df['性别映射'] = df['1、您的性别：'].map(gender_mapping)
df['学历映射'] = df['3、当前所处教育阶段:'].map(education_mapping)


scene_keywords = {
    '即时通讯': 'im',
    '短视频平台': 'short_video',
    '社交媒体': 'social',
    '网络游戏': 'game',
    '影视娱乐': 'video'
}
position_weights = [0.5, 0.3, 0.15, 0.05]


for scene_key in scene_keywords.values():
    df[f'scene_{scene_key}_weight'] = 0.0


for i, row in df.iterrows():
    scenes = str(row['5、主要使用场景']).split('→')
    for pos, s in enumerate(scenes[:4]):
        for keyword, scene_key in scene_keywords.items():
            if keyword in s:
                df.at[i, f'scene_{scene_key}_weight'] += position_weights[pos]


likert_1to5_mapping = {
    "从不": 1, "偶尔": 2, "有时": 3, "经常": 4, "总是": 5
}
likert_agreement_mapping = {
    "完全不符": 1, "不太符合": 2, "一般": 3, "比较符合": 4, "非常符合": 5
}

likert_columns = {
    "6、当我浏览社交媒体时，我常常将自己生活状态与他人进行比较": likert_1to5_mapping,
    "8、你是否会在遇到情绪低落时使用数字媒体（如刷视频、聊天、玩游戏等）？": likert_1to5_mapping,
    "9、数字媒体使用对你情绪状态的影响—使用后感到焦虑减轻": likert_agreement_mapping,
    "9、浏览内容后感到烦躁": likert_agreement_mapping,
    "9、线上互动中产生归属感": likert_agreement_mapping,
    "9、产生时间管理失控感": likert_agreement_mapping,
    "9、深夜使用时感到孤独感加剧": likert_agreement_mapping,
}

for col, mapping in likert_columns.items():
    if col in df.columns:
        df[col + '_打分'] = df[col].map(mapping)


print(df.head())


os.makedirs("outputs", exist_ok=True)


df.to_csv("outputs/cleaned_education_data.csv", index=False, encoding="utf-8-sig")
print("文件已保存为 outputs/cleaned_education_data.csv")
