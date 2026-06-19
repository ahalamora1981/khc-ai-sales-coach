"""
AI Sales Coach Demo - Menu Analyzer
Kxxxx Hxxxx Foodservice Solution
"""

import streamlit as st
import json
import base64
import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Sales Coach - Menu Analyzer",
    page_icon="🍳",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: #f8f9fa;
        padding: 1.5rem 2rem;
        border-radius: 10px;
        border-left: 5px solid #e4002b;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: #262730;
        margin: 0;
        font-size: 1.8rem;
    }
    .main-header p {
        color: #666;
        margin: 0.5rem 0 0 0;
    }
    .product-card {
        background: #f8f9fa;
        border-left: 4px solid #e4002b;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .recommendation-header {
        background: #f8f9fa;
        color: #262730;
        padding: 0.75rem 1rem;
        border-radius: 5px;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #e4002b;
        font-weight: 600;
    }
    .innovation-box {
        background: #f5f7fa;
        color: #262730;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    .innovation-box h4 {
        color: #333;
        margin-top: 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #e4002b !important;
        border-bottom: 2px solid #e4002b !important;
    }
</style>
""", unsafe_allow_html=True)

# Load products
@st.cache_data
def load_products():
    with open("data/khc_products.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Initialize DashScope client
def get_client():
    return OpenAI(
        api_key=st.session_state.get("api_key", os.getenv("DASHSCOPE_API_KEY", "")),
        base_url=os.getenv("DASHSCOPE_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    )

# Get model name
def get_model():
    return os.getenv("LLM_MODEL", "qwen3.5-flash")

# System prompt for menu analysis
SYSTEM_PROMPT = """你是一位专业的餐饮销售顾问AI助手。

你的任务是分析餐厅菜单，并基于公司的产品组合提供专业的酱料推荐。

公司主要产品品牌和类别包括：
1. 味事达 (MasterFoods) - 中式酱料
   - 酱油系列：味极鲜、生抽、老抽、蒸鱼豉油、零添加系列
   - 蚝油系列：经典蚝油、素蚝油
   - 辣椒酱：豆豉辣椒酱

2. 亨氏 (Heinz) - 西式酱料
   - 番茄酱系列：经典番茄沙司、0蔗糖番茄沙司
   - 蛋黄酱/沙拉酱：蛋黄酱、焙煎芝麻酱、油醋汁
   - 复合调味酱：照烧酱、烧烤酱、辣椒酱

3. 广合 (Guanghe) - 传统调味品
   - 腐乳系列
   - 芝麻油

请分析菜单并提供：
1. 菜单分析（菜系类型、菜品数量、口味特征）
2. 推荐3-5款最适合的产品，说明推荐理由
3. 每款产品如何应用到具体菜品中
4. 1-2个创新建议（使用公司产品创造新菜品）

输出格式要求：
- 使用中文
- 结构清晰，使用标题和列表
- 提供具体的商业价值（如节省成本、提升口味等）
- 包含销售话术建议

请以JSON格式返回结果，包含以下字段：
{
    "menu_analysis": {
        "cuisine_type": "菜系类型",
        "dish_count": 菜品数量,
        "price_range": "价格范围",
        "taste_profile": {
            "spicy": 0-10,
            "umami": 0-10,
            "salty": 0-10,
            "sweet": 0-10,
            "savory": 0-10
        },
        "signature_dishes": ["招牌菜1", "招牌菜2"]
    },
    "recommendations": [
        {
            "product_id": "产品ID",
            "product_name_cn": "产品中文名",
            "brand": "品牌",
            "match_score": 85,
            "match_dishes": ["匹配菜品1", "匹配菜品2"],
            "reason": "推荐理由",
            "application": "具体应用方式",
            "value_proposition": "商业价值"
        }
    ],
    "innovation_suggestions": [
        {
            "dish_name": "创新菜品名",
            "description": "菜品描述",
            "products_used": ["使用的产品"],
            "target_audience": "目标客群",
            "pricing_suggestion": "建议售价"
        }
    ],
    "sales_talking_points": ["话术要点1", "话术要点2"]
}
"""

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_menu_image(image_path, client, products_json):
    """Analyze menu from image using Qwen with vision"""
    
    # Get file extension and determine media type
    ext = Path(image_path).suffix.lower()
    media_type_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    media_type = media_type_map.get(ext, "image/jpeg")
    
    # Encode image
    base64_image = encode_image(image_path)
    
    # Create product context
    product_summary = "\n".join([
        f"- {p['brand']} {p['name_cn']} ({p['id']}): {', '.join(p['applications'][:3])}"
        for p in products_json["products"]
    ])
    
    user_prompt = f"""请分析这张餐厅菜单图片，并提供产品推荐。

产品目录：
{product_summary}

请按照系统提示中的JSON格式返回分析结果。"""

    response = client.chat.completions.create(
        model=get_model(),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": user_prompt
                    }
                ]
            }
        ],
        temperature=0.7,
        max_tokens=4096
    )
    
    return response.choices[0].message.content

def analyze_menu_text(menu_text, client, products_json):
    """Analyze menu from text input using Qwen"""
    
    # Create product context
    product_summary = "\n".join([
        f"- {p['brand']} {p['name_cn']} ({p['id']}): {', '.join(p['applications'][:3])}"
        for p in products_json["products"]
    ])
    
    user_prompt = f"""请分析以下餐厅菜单，并提供产品推荐。

菜单内容：
{menu_text}

产品目录：
{product_summary}

请按照系统提示中的JSON格式返回分析结果。"""

    response = client.chat.completions.create(
        model=get_model(),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=4096
    )
    
    return response.choices[0].message.content

def parse_ai_response(response_text):
    """Parse AI response and extract JSON"""
    import re
    
    # Try to find JSON in the response
    # Look for JSON block
    json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except:
            pass
    
    # Try to find JSON object directly
    json_match = re.search(r'\{[\s\S]*\}', response_text)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except:
            pass
    
    # Return None if parsing fails
    return None

def display_results(analysis, full_response):
    """Display analysis results in a beautiful format"""
    
    if analysis is None:
        # If JSON parsing fails, display raw response
        st.markdown("### 📊 AI分析结果")
        st.markdown(full_response)
        return
    
    # Menu Analysis Section
    st.markdown('<div class="recommendation-header">📊 菜单分析</div>', unsafe_allow_html=True)
    
    menu = analysis.get("menu_analysis", {})
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("菜系类型", menu.get("cuisine_type", "N/A"))
    with col2:
        st.metric("菜品数量", menu.get("dish_count", "N/A"))
    with col3:
        st.metric("价格范围", menu.get("price_range", "N/A"))
    with col4:
        signature = menu.get("signature_dishes", [])
        st.metric("招牌菜", ", ".join(signature[:2]) if signature else "N/A")
    
    # Taste Profile
    taste = menu.get("taste_profile", {})
    if taste:
        st.markdown("**口味特征**")
        cols = st.columns(5)
        labels = {"spicy": "🌶️ 辣度", "umami": "鲜味", "salty": "咸度", "sweet": "甜度", "savory": "香味"}
        for i, (key, label) in enumerate(labels.items()):
            with cols[i]:
                value = taste.get(key, 0)
                st.progress(value / 10)
                st.caption(f"{label}: {value}/10")
    
    st.divider()
    
    # Recommendations Section
    st.markdown('<div class="recommendation-header">🎯 产品推荐</div>', unsafe_allow_html=True)
    
    recommendations = analysis.get("recommendations", [])
    for i, rec in enumerate(recommendations, 1):
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{i}. {rec.get('brand', '')} {rec.get('product_name_cn', '')}**")
                st.markdown(f"📌 **匹配度**: {rec.get('match_score', 'N/A')}%")
                st.markdown(f"🍽️ **推荐菜品**: {', '.join(rec.get('match_dishes', []))}")
                st.markdown(f"💡 **推荐理由**: {rec.get('reason', '')}")
                st.markdown(f"📋 **应用方式**: {rec.get('application', '')}")
                st.markdown(f"💰 **商业价值**: {rec.get('value_proposition', '')}")
            st.divider()
    
    # Innovation Suggestions
    innovations = analysis.get("innovation_suggestions", [])
    if innovations:
        st.markdown('<div class="recommendation-header">💡 创新建议</div>', unsafe_allow_html=True)
        
        for innovation in innovations:
            st.markdown(f"""
            <div class="innovation-box">
                <h4>🍳 {innovation.get('dish_name', '创新菜品')}</h4>
                <p><strong>描述:</strong> {innovation.get('description', '')}</p>
                <p><strong>使用产品:</strong> {', '.join(innovation.get('products_used', []))}</p>
                <p><strong>目标客群:</strong> {innovation.get('target_audience', '')}</p>
                <p><strong>建议售价:</strong> {innovation.get('pricing_suggestion', '')}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Sales Talking Points
    talking_points = analysis.get("sales_talking_points", [])
    if talking_points:
        st.markdown('<div class="recommendation-header">🗣️ 销售话术要点</div>', unsafe_allow_html=True)
        for point in talking_points:
            st.markdown(f"• {point}")

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🍳 AI Sales Coach - 菜单分析器</h1>
        <p>餐饮销售智能助手 | Powered by Qwen 3.7 Plus</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load products
    products = load_products()
    
    # Load API key from env
    env_api_key = os.getenv("DASHSCOPE_API_KEY", "")
    if env_api_key and "api_key" not in st.session_state:
        st.session_state["api_key"] = env_api_key
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ 配置")
        
        # API Key input
        api_key = st.text_input(
            "DashScope API Key",
            value=st.session_state.get("api_key", env_api_key),
            type="password",
            help="输入你的阿里云DashScope API Key"
        )
        if api_key:
            st.session_state["api_key"] = api_key
        
        if env_api_key:
            st.success("✅ 已从.env文件加载API Key")
        
        # Show current config
        st.markdown(f"""
        <div style="background: #f0f2f6; padding: 10px; border-radius: 5px; font-size: 12px;">
            <b>当前配置:</b><br>
            模型: {get_model()}<br>
            API: {os.getenv('DASHSCOPE_BASE_URL', 'N/A')[:30]}...
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        st.header("📦 产品目录")
        st.markdown(f"共 **{len(products['products'])}** 款产品")
        
        # Show product categories
        brands = {}
        for p in products["products"]:
            brand = p["brand"]
            if brand not in brands:
                brands[brand] = []
            brands[brand].append(p)
        
        for brand, prods in brands.items():
            with st.expander(f"{brand} ({len(prods)}款)"):
                for p in prods:
                    st.markdown(f"• {p['name_cn']}")
        
        st.divider()
        st.header("📋 示例菜单")
        st.markdown("sample-menus/ 文件夹中包含：")
        st.markdown("• 5张图片菜单")
        st.markdown("• 5个文本菜单")
    
    # Main content - tabs
    tab1, tab2 = st.tabs(["📷 图片菜单分析", "📝 文本菜单分析"])
    
    with tab1:
        st.markdown("### 上传菜单图片")
        st.markdown("支持 JPG、PNG 格式，AI将自动识别菜单内容并分析")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # File uploader
            uploaded_file = st.file_uploader(
                "选择菜单图片",
                type=["jpg", "jpeg", "png"],
                key="image_upload"
            )
            
            # Or select sample
            sample_files = list(Path("sample-menus").glob("*.jpg")) + list(Path("sample-menus").glob("*.png"))
            if sample_files:
                sample_names = [f.name for f in sample_files]
                selected_sample = st.selectbox(
                    "或选择示例菜单",
                    ["-- 选择示例 --"] + sample_names,
                    key="sample_select"
                )
                if selected_sample != "-- 选择示例 --":
                    uploaded_file = str(Path("sample-menus") / selected_sample)
        
        with col2:
            # Preview
            if uploaded_file:
                if isinstance(uploaded_file, str):
                    st.image(uploaded_file, caption="菜单预览", use_container_width=True)
                else:
                    st.image(uploaded_file, caption="菜单预览", use_container_width=True)
        
        # Analyze button
        if uploaded_file and st.session_state.get("api_key"):
            if st.button("🔍 开始分析", key="analyze_image", use_container_width=True):
                with st.spinner("AI正在分析菜单，请稍候..."):
                    try:
                        client = get_client()
                        
                        # Handle file path
                        if isinstance(uploaded_file, str):
                            image_path = uploaded_file
                        else:
                            # Save uploaded file temporarily
                            temp_path = Path("temp_upload.jpg")
                            temp_path.write_bytes(uploaded_file.getvalue())
                            image_path = str(temp_path)
                        
                        response = analyze_menu_image(image_path, client, products)
                        analysis = parse_ai_response(response)
                        display_results(analysis, response)
                        
                    except Exception as e:
                        st.error(f"分析出错: {str(e)}")
        elif not st.session_state.get("api_key"):
            st.warning("⚠️ 请先在左侧输入DashScope API Key")
    
    with tab2:
        st.markdown("### 输入菜单文本")
        st.markdown("可以直接粘贴菜单文本，AI将进行分析")
        
        # Text input options
        input_method = st.radio(
            "选择输入方式",
            ["直接输入", "选择示例菜单"],
            horizontal=True,
            key="text_input_method"
        )
        
        menu_text = ""
        
        if input_method == "直接输入":
            menu_text = st.text_area(
                "粘贴菜单文本",
                height=300,
                placeholder="例：\n川味坊\n麻婆豆腐......32元\n宫保鸡丁......42元\n...",
                key="menu_text_input"
            )
        else:
            # Sample text menus
            sample_text_files = list(Path("sample-menus").glob("*.txt"))
            if sample_text_files:
                sample_names = [f.stem for f in sample_text_files]
                selected_text_sample = st.selectbox(
                    "选择示例菜单",
                    ["-- 选择示例 --"] + sample_names,
                    key="text_sample_select"
                )
                if selected_text_sample != "-- 选择示例 --":
                    sample_path = Path("sample-menus") / f"{selected_text_sample}.txt"
                    menu_text = sample_path.read_text(encoding="utf-8")
                    st.text_area("菜单内容", value=menu_text, height=300, disabled=True)
        
        # Analyze button
        if menu_text and st.session_state.get("api_key"):
            if st.button("🔍 开始分析", key="analyze_text", use_container_width=True):
                with st.spinner("AI正在分析菜单，请稍候..."):
                    try:
                        client = get_client()
                        response = analyze_menu_text(menu_text, client, products)
                        analysis = parse_ai_response(response)
                        display_results(analysis, response)
                        
                    except Exception as e:
                        st.error(f"分析出错: {str(e)}")
        elif not st.session_state.get("api_key"):
            st.warning("⚠️ 请先在左侧输入DashScope API Key")
    
    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>AI Sales Coach Demo | Powered by Qwen 3.7 Plus | Built with ❤️ by Infoxxx</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
