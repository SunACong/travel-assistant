import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import datetime
import random

# 设置页面配置
st.set_page_config(page_title="节假日出行推荐小助手", page_icon="✈️", layout="wide")

# 添加自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        background-color: #f8f9fa;
    }
    .highlight {
        color: #FF5722;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 应用标题
st.markdown('<h1 class="main-header">节假日出行推荐小助手</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">输入您的假期时间和偏好，我们将为您推荐最适合的旅游目的地和行程安排</p>', unsafe_allow_html=True)

# 侧边栏 - 用户输入
with st.sidebar:
    st.markdown('<h2 class="sub-header">旅行偏好设置</h2>', unsafe_allow_html=True)
    
    # 日期选择
    st.subheader("选择您的假期时间")
    start_date = st.date_input("开始日期", datetime.date.today())
    end_date = st.date_input("结束日期", datetime.date.today() + datetime.timedelta(days=3))
    
    # 计算旅行天数
    if start_date <= end_date:
        days = (end_date - start_date).days + 1
        st.success(f"您的假期共 {days} 天")
    else:
        st.error("结束日期必须在开始日期之后")
        days = 0
    
    # 旅行偏好
    st.subheader("您的旅行偏好")
    preferences = {
        "气候": st.selectbox("您偏好的气候类型", ["温暖", "凉爽", "不限"]),
        "环境": st.multiselect("您喜欢的环境类型", ["自然风光", "历史文化", "现代都市", "海滩海岸", "山川湖泊"]),
        "活动": st.multiselect("您感兴趣的活动", ["观光游览", "美食探索", "户外运动", "购物", "文化体验"]),
        "节奏": st.slider("旅行节奏 (1=悠闲放松, 5=紧凑充实)", 1, 5, 3),
        "预算": st.select_slider("预算范围", options=["经济", "适中", "高端"], value="适中")
    }
    
    # 生成推荐按钮
    generate_btn = st.button("生成旅行推荐", type="primary")

# 主界面
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

# 模拟数据 - 城市信息
def load_city_data():
    return {
        "北京": {
            "description": "中国首都，拥有丰富的历史文化遗产和现代都市风貌",
            "climate": "四季分明",
            "attractions": ["故宫", "长城", "颐和园", "天坛", "798艺术区"],
            "activities": ["历史探索", "文化体验", "美食品尝", "购物"],
            "coordinates": [39.9042, 116.4074],
            "tags": ["历史文化", "现代都市"],
            "budget_level": "适中"
        },
        "上海": {
            "description": "国际化大都市，融合了东西方文化的现代化城市",
            "climate": "温和湿润",
            "attractions": ["外滩", "豫园", "南京路", "迪士尼乐园", "田子坊"],
            "activities": ["都市观光", "购物", "美食", "夜景欣赏"],
            "coordinates": [31.2304, 121.4737],
            "tags": ["现代都市", "美食购物"],
            "budget_level": "高端"
        },
        "杭州": {
            "description": "风景秀丽的城市，以西湖闻名于世",
            "climate": "温和湿润",
            "attractions": ["西湖", "灵隐寺", "西溪湿地", "宋城", "龙井茶园"],
            "activities": ["自然观光", "品茶", "文化体验", "休闲放松"],
            "coordinates": [30.2741, 120.1551],
            "tags": ["自然风光", "历史文化"],
            "budget_level": "适中"
        },
        "三亚": {
            "description": "热带海滨城市，拥有美丽的海滩和丰富的热带风光",
            "climate": "热带季风",
            "attractions": ["亚龙湾", "天涯海角", "蜈支洲岛", "南山文化旅游区"],
            "activities": ["海滩度假", "水上运动", "自然观光", "美食品尝"],
            "coordinates": [18.2524, 109.5119],
            "tags": ["海滩海岸", "自然风光"],
            "budget_level": "高端"
        },
        "丽江": {
            "description": "风景如画的古城，纳西族文化的发源地",
            "climate": "温和干燥",
            "attractions": ["丽江古城", "玉龙雪山", "泸沽湖", "束河古镇"],
            "activities": ["古城漫步", "民族文化体验", "自然风光欣赏"],
            "coordinates": [26.8721, 100.2299],
            "tags": ["历史文化", "自然风光", "山川湖泊"],
            "budget_level": "适中"
        },
        "西安": {
            "description": "中国历史文化名城，古丝绸之路的起点",
            "climate": "温带季风",
            "attractions": ["兵马俑", "古城墙", "大雁塔", "华山", "回民街"],
            "activities": ["历史探索", "文化体验", "美食品尝"],
            "coordinates": [34.3416, 108.9398],
            "tags": ["历史文化"],
            "budget_level": "经济"
        },
        "成都": {
            "description": "休闲之都，以熊猫和美食闻名",
            "climate": "湿润亚热带",
            "attractions": ["大熊猫繁育研究基地", "锦里", "宽窄巷子", "都江堰", "青城山"],
            "activities": ["美食品尝", "熊猫观赏", "休闲娱乐", "自然观光"],
            "coordinates": [30.5723, 104.0665],
            "tags": ["美食", "自然风光", "休闲"],
            "budget_level": "经济"
        },
        "厦门": {
            "description": "美丽的海滨城市，以鼓浪屿闻名",
            "climate": "亚热带海洋性",
            "attractions": ["鼓浪屿", "厦门大学", "南普陀寺", "环岛路", "曾厝垵"],
            "activities": ["海岛游览", "骑行", "美食品尝", "文艺体验"],
            "coordinates": [24.4798, 118.0894],
            "tags": ["海滩海岸", "文艺小资"],
            "budget_level": "经济"
        },
        "桂林": {
            "description": "山水甲天下，喀斯特地貌的代表",
            "climate": "湿润亚热带",
            "attractions": ["漓江", "阳朔", "象鼻山", "龙脊梯田", "两江四湖"],
            "activities": ["漓江漂流", "山水观光", "摄影", "乡村体验"],
            "coordinates": [25.2736, 110.2907],
            "tags": ["自然风光", "山川湖泊"],
            "budget_level": "经济"
        },
        "青岛": {
            "description": "美丽的海滨城市，啤酒之都",
            "climate": "温带季风",
            "attractions": ["栈桥", "八大关", "崂山", "啤酒博物馆", "金沙滩"],
            "activities": ["海滨度假", "品尝啤酒和海鲜", "自然观光"],
            "coordinates": [36.0671, 120.3826],
            "tags": ["海滩海岸", "美食"],
            "budget_level": "适中"
        }
    }

# 推荐算法
def recommend_cities(preferences, days, city_data):
    # 根据用户偏好筛选城市
    scores = {}
    
    for city, info in city_data.items():
        score = 0
        
        # 气候匹配
        if preferences["气候"] == "不限" or (preferences["气候"] == "温暖" and "热带" in info["climate"] or "亚热带" in info["climate"]) or (preferences["气候"] == "凉爽" and "温带" in info["climate"]):
            score += 1
        
        # 环境匹配
        for env in preferences["环境"]:
            if env in info["tags"]:
                score += 2
        
        # 活动匹配
        activity_match = 0
        for act in preferences["活动"]:
            if act in info["activities"] or any(act.lower() in a.lower() for a in info["activities"]):
                activity_match += 1
        score += activity_match
        
        # 预算匹配
        if preferences["预算"] == info["budget_level"]:
            score += 2
        elif (preferences["预算"] == "适中" and info["budget_level"] == "经济") or (preferences["预算"] == "高端" and info["budget_level"] == "适中"):
            score += 1
        
        scores[city] = score
    
    # 根据分数排序并选择前N个城市
    recommended_cities = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # 根据旅行天数决定推荐城市数量
    if days <= 3:
        return recommended_cities[:1]  # 短途旅行只推荐1个城市
    elif days <= 7:
        return recommended_cities[:2]  # 中途旅行推荐2个城市
    else:
        return recommended_cities[:3]  # 长途旅行推荐3个城市

# 生成行程安排
def generate_itinerary(city, start_date, days, city_data, travel_pace):
    itinerary = []
    attractions = city_data[city]["attractions"]
    activities = city_data[city]["activities"]
    
    # 根据旅行节奏决定每天安排的景点数量
    attractions_per_day = max(2, min(5, travel_pace + 1))
    
    # 打乱景点顺序，使每次生成的行程有所不同
    random.shuffle(attractions)
    
    current_date = start_date
    remaining_attractions = attractions.copy()
    
    for day in range(1, days + 1):
        day_attractions = []
        
        # 为当天选择景点
        for _ in range(min(attractions_per_day, len(remaining_attractions))):
            if remaining_attractions:
                day_attractions.append(remaining_attractions.pop(0))
        
        # 如果景点用完了，重新开始
        if not remaining_attractions and day < days:
            remaining_attractions = attractions.copy()
            random.shuffle(remaining_attractions)
        
        # 随机选择一个活动
        day_activity = random.choice(activities)
        
        # 创建当天行程
        day_plan = {
            "date": current_date.strftime("%Y-%m-%d"),
            "day": day,
            "attractions": day_attractions,
            "activity": day_activity,
            "morning": f"游览 {' 和 '.join(day_attractions[:len(day_attractions)//2 + len(day_attractions)%2])}",
            "afternoon": f"游览 {' 和 '.join(day_attractions[len(day_attractions)//2 + len(day_attractions)%2:])}",
            "evening": f"体验{city}的{day_activity}"
        }
        
        itinerary.append(day_plan)
        current_date += datetime.timedelta(days=1)
    
    return itinerary



# 主程序逻辑
if generate_btn:
    with st.spinner("正在为您生成最佳旅行推荐..."):
        # 加载城市数据
        city_data = load_city_data()
        
        # 获取推荐城市
        recommended_cities = recommend_cities(preferences, days, city_data)
        
        # 生成行程安排
        all_itineraries = {}
        for city, score in recommended_cities:
            city_itinerary = generate_itinerary(city, start_date, days // len(recommended_cities) if len(recommended_cities) > 1 else days, city_data, preferences["节奏"])
            all_itineraries[city] = city_itinerary
        
        # 保存到session state
        st.session_state.recommendations = recommended_cities
        st.session_state.itineraries = all_itineraries

# 显示推荐结果
if st.session_state.recommendations:
    st.markdown('<h2 class="sub-header">为您推荐的目的地</h2>', unsafe_allow_html=True)
    
    # 创建地图
    m = folium.Map(location=[35.8617, 104.1954], zoom_start=4)
    
    # 加载城市数据
    city_data = load_city_data()
    
    # 为每个推荐的城市添加标记
    for city, score in st.session_state.recommendations:
        folium.Marker(
            location=city_data[city]["coordinates"],
            popup=f"<strong>{city}</strong><br>{city_data[city]['description']}",
            tooltip=city,
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
    
    # 显示地图
    st.markdown('<div class="card">', unsafe_allow_html=True)
    folium_static(m, width=800, height=500)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示每个推荐城市的详细信息和行程
    for city, score in st.session_state.recommendations:
        st.markdown(f'<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f'<h3>{city}</h3>', unsafe_allow_html=True)
            st.markdown(f"**推荐指数:** {'⭐' * (score // 2 + 1)}")
            st.markdown(f"**气候:** {city_data[city]['climate']}")
            st.markdown(f"**预算:** {city_data[city]['budget_level']}")
            st.markdown(f"**标签:** {', '.join(city_data[city]['tags'])}")
        
        with col2:
            st.markdown(f"**城市简介:** {city_data[city]['description']}")
            st.markdown("**热门景点:**")
            for attraction in city_data[city]['attractions']:
                st.markdown(f"- {attraction}")
        
        # 显示行程安排
        st.markdown("<h4>推荐行程安排</h4>", unsafe_allow_html=True)
        
        # 创建行程表格
        itinerary = st.session_state.itineraries[city]
        for day in itinerary:
            with st.expander(f"第{day['day']}天 ({day['date']})"):
                st.markdown(f"**上午:** {day['morning']}")
                st.markdown(f"**下午:** {day['afternoon']}")
                st.markdown(f"**晚上:** {day['evening']}")
        

        
        st.markdown('</div>', unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 节假日出行推荐小助手 | 让您的假期更精彩</p>", unsafe_allow_html=True)