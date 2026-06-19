# AI Sales Coach Demo

餐饮销售智能助手演示应用

## 功能特性

- 📷 **图片菜单分析** - 上传菜单图片，AI自动识别并分析
- 📝 **文本菜单分析** - 输入菜单文本，AI进行智能分析
- 🎯 **产品推荐** - 基于菜单特点推荐最适合的产品
- 💡 **创新建议** - 提供使用公司产品的创新菜品建议
- 🗣️ **销售话术** - 生成针对该餐厅的销售话术要点

## 技术栈

- **前端**: Streamlit
- **AI模型**: Qwen 3.7 Plus (通过DashScope API)
- **语言**: Python 3.12

## 快速开始

### 1. 安装依赖

```bash
uv sync
```

### 2. 获取API Key

前往 [阿里云DashScope](https://dashscope.console.aliyun.com/) 获取API Key

### 3. 运行应用

```bash
uv run streamlit run app.py
```

### 4. 使用应用

1. 在左侧边栏输入DashScope API Key
2. 选择图片上传或文本输入方式
3. 上传菜单图片或输入/选择菜单文本
4. 点击"开始分析"按钮
5. 查看AI生成的分析报告

## 示例菜单

`sample-menus/` 文件夹包含：

### 图片菜单 (5张)
- 001.jpg - 江南忆 (高端中式餐厅)
- 002.jpg - 小熊猫大排档 (海鲜大排档)
- 003.jpg - Western Restaurant (西餐厅)
- 004.jpg - Chinese Restaurant (中式餐厅)
- 005.jpg - Fast Food (快餐店)

### 文本菜单 (5个)
- 006_sichuan_hotpot.txt - 蜀香阁火锅
- 007_cantonese_dimsum.txt - 点都德茶楼
- 008_western_restaurant.txt - The Garden Bistro
- 009_sichuan_restaurant.txt - 川味坊
- 010_japanese_restaurant.txt - 樱花屋日本料理

## 产品目录

本Demo包含以下产品：

### 味事达 (MasterFoods)
- 味极鲜特级酿造酱油
- 蒸鱼豉油
- 零添加初榨生抽
- 老抽
- 蚝油
- 素蚝油
- 豆豉辣椒酱

### 亨氏 (Heinz)
- 番茄沙司
- 0蔗糖番茄沙司
- 蛋黄酱
- 焙煎芝麻沙拉酱
- 油醋汁
- 辣椒酱
- 照烧酱
- 烧烤酱

### 广合 (Guanghe)
- 腐乳
- 芝麻油

## 项目结构

```
ai-sales-coach-demo/
├── app.py                  # 主应用文件
├── data/
│   └── khc_products.json   # 产品目录
├── sample-menus/           # 示例菜单
│   ├── *.jpg               # 图片菜单
│   └── *.txt               # 文本菜单
├── pyproject.toml          # 项目配置
└── README.md               # 说明文档
```

## 注意事项

- 请确保网络可以访问DashScope API
- 图片菜单建议使用清晰的照片以获得最佳识别效果
- API调用会产生费用，请注意控制使用量

## 开发团队

AI Sales Coach Project  
Powered by Infoxxx
