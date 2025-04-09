# 城市数据模块

def load_city_data():
    """
    加载城市数据，包括城市描述、气候、景点、活动等信息
    """
    return {
        "北京": {
            "description": "中国首都，拥有丰富的历史文化遗产和现代都市风貌",
            "climate": "四季分明",
            "attractions": ["故宫", "长城", "颐和园", "天坛", "798艺术区"],
            "activities": ["历史探索", "文化体验", "美食品尝", "购物"],
            "coordinates": [39.9042, 116.4074],
            "tags": ["历史文化", "现代都市"],
            "budget_level": "适中",
            "image_url": "https://images.unsplash.com/photo-1584646098378-0874589d76b1",
            "best_season": "春秋季",
            "local_food": ["北京烤鸭", "炸酱面", "豆汁", "爆肚"],
            "travel_tips": "故宫和长城游客较多，建议提前预约；春秋季是最佳旅游季节；地铁是出行的最佳选择。"
        },
        "上海": {
            "description": "国际化大都市，融合了东西方文化的现代化城市",
            "climate": "温和湿润",
            "attractions": ["外滩", "豫园", "南京路", "迪士尼乐园", "田子坊"],
            "activities": ["都市观光", "购物", "美食", "夜景欣赏"],
            "coordinates": [31.2304, 121.4737],
            "tags": ["现代都市", "美食购物"],
            "budget_level": "高端",
            "image_url": "https://images.unsplash.com/photo-1538428494232-9c0d8a3ab403",
            "best_season": "春秋季",
            "local_food": ["小笼包", "生煎", "蟹粉狮子头", "红烧肉"],
            "travel_tips": "外滩夜景非常美丽；地铁交通便利；迪士尼乐园需提前预约；雨天较多，请携带雨具。"
        },
        "杭州": {
            "description": "风景秀丽的城市，以西湖闻名于世",
            "climate": "温和湿润",
            "attractions": ["西湖", "灵隐寺", "西溪湿地", "宋城", "龙井茶园"],
            "activities": ["自然观光", "品茶", "文化体验", "休闲放松"],
            "coordinates": [30.2741, 120.1551],
            "tags": ["自然风光", "历史文化"],
            "budget_level": "适中",
            "image_url": "https://images.unsplash.com/photo-1598887142487-2e7829cda8c0",
            "best_season": "春夏季",
            "local_food": ["西湖醋鱼", "东坡肉", "龙井虾仁", "叫花鸡"],
            "travel_tips": "西湖周边景点较多，建议安排2-3天；可以租自行车环湖；龙井茶是必买特产。"
        },
        "三亚": {
            "description": "热带海滨城市，拥有美丽的海滩和丰富的热带风光",
            "climate": "热带季风",
            "attractions": ["亚龙湾", "天涯海角", "蜈支洲岛", "南山文化旅游区"],
            "activities": ["海滩度假", "水上运动", "自然观光", "美食品尝"],
            "coordinates": [18.2524, 109.5119],
            "tags": ["海滩海岸", "自然风光"],
            "budget_level": "高端",
            "image_url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff",
            "best_season": "冬春季",
            "local_food": ["海南鸡饭", "清补凉", "海鲜", "椰子饭"],
            "travel_tips": "11月至次年4月是最佳旅游季节；防晒措施必不可少；蜈支洲岛需提前预约；淡季价格较为实惠。"
        },
        "丽江": {
            "description": "风景如画的古城，纳西族文化的发源地",
            "climate": "温和干燥",
            "attractions": ["丽江古城", "玉龙雪山", "泸沽湖", "束河古镇"],
            "activities": ["古城漫步", "民族文化体验", "自然风光欣赏"],
            "coordinates": [26.8721, 100.2299],
            "tags": ["历史文化", "自然风光", "山川湖泊"],
            "budget_level": "适中",
            "image_url": "https://images.unsplash.com/photo-1546436836-07a1beb01e8b",
            "best_season": "春秋季",
            "local_food": ["纳西烤肉", "丽江粑粑", "鸡豆凉粉", "酥油茶"],
            "travel_tips": "海拔较高，需注意高原反应；玉龙雪山需提前适应高原环境；古城夜景很美；消费水平较高。"
        },
        "西安": {
            "description": "中国历史文化名城，古丝绸之路的起点",
            "climate": "温带季风",
            "attractions": ["兵马俑", "古城墙", "大雁塔", "华山", "回民街"],
            "activities": ["历史探索", "文化体验", "美食品尝"],
            "coordinates": [34.3416, 108.9398],
            "tags": ["历史文化"],
            "budget_level": "经济",
            "image_url": "https://images.unsplash.com/photo-1567292301-593c5e0e932a",
            "best_season": "春秋季",
            "local_food": ["肉夹馍", "羊肉泡馍", "biangbiang面", "凉皮"],
            "travel_tips": "兵马俑和华山需要安排一整天时间；古城墙可以骑行；回民街是品尝美食的好去处。"
        },
        "成都": {
            "description": "休闲之都，以熊猫和美食闻名",
            "climate": "湿润亚热带",
            "attractions": ["大熊猫繁育研究基地", "锦里", "宽窄巷子", "都江堰", "青城山"],
            "activities": ["美食品尝", "熊猫观赏", "休闲娱乐", "自然观光"],
            "coordinates": [30.5723, 104.0665],
            "tags": ["美食", "自然风光", "休闲"],
            "budget_level": "经济",
            "image_url": "https://images.unsplash.com/photo-1545287072-2a8d6da81c3b",
            "best_season": "春秋季",
            "local_food": ["火锅", "担担面", "回锅肉", "麻婆豆腐"],
            "travel_tips": "熊猫基地建议早上去，熊猫较为活跃；成都交通便利；美食众多，可以尝试各种川菜。"
        },
        "厦门": {
            "description": "美丽的海滨城市，以鼓浪屿闻名",
            "climate": "亚热带海洋性",
            "attractions": ["鼓浪屿", "厦门大学", "南普陀寺", "环岛路", "曾厝垵"],
            "activities": ["海岛游览", "骑行", "美食品尝", "文艺体验"],
            "coordinates": [24.4798, 118.0894],
            "tags": ["海滩海岸", "文艺小资"],
            "budget_level": "经济",
            "image_url": "https://images.unsplash.com/photo-1590136000954-d0e2351304bc",
            "best_season": "春秋季",
            "local_food": ["沙茶面", "海蛎煎", "土笋冻", "叶氏麻糍"],
            "travel_tips": "鼓浪屿需要轮渡，建议提前购票；环岛路适合骑行；厦门大学需要提前预约；曾厝垵是文艺青年的天堂。"
        },
        "桂林": {
            "description": "山水甲天下，喀斯特地貌的代表",
            "climate": "湿润亚热带",
            "attractions": ["漓江", "阳朔", "象鼻山", "龙脊梯田", "两江四湖"],
            "activities": ["漓江漂流", "山水观光", "摄影", "乡村体验"],
            "coordinates": [25.2736, 110.2907],
            "tags": ["自然风光", "山川湖泊"],
            "budget_level": "经济",
            "image_url": "https://images.unsplash.com/photo-1537531383496-f4749b8032cf",
            "best_season": "春夏季",
            "local_food": ["桂林米粉", "啤酒鱼", "荔浦扣肉", "田螺酿"],
            "travel_tips": "漓江漂流是必体验项目；阳朔西街夜景很美；龙脊梯田需要包车前往；雨季景色更美但需注意安全。"
        },
        "青岛": {
            "description": "美丽的海滨城市，啤酒之都",
            "climate": "温带季风",
            "attractions": ["栈桥", "八大关", "崂山", "啤酒博物馆", "金沙滩"],
            "activities": ["海滨度假", "品尝啤酒和海鲜", "自然观光"],
            "coordinates": [36.0671, 120.3826],
            "tags": ["海滩海岸", "美食"],
            "budget_level": "适中",
            "image_url": "https://images.unsplash.com/photo-1567519836400-585d5a8364c0",
            "best_season": "夏秋季",
            "local_food": ["青岛啤酒", "海鲜", "鲅鱼水饺", "辣炒蛤蜊"],
            "travel_tips": "夏季是最佳旅游季节；啤酒节通常在7-8月举办；崂山需要一整天时间；海鲜市场价格可议。"
        },
        "大理": {
            "description": "风光秀丽的古城，白族文化的代表",
            "climate": "温和干燥",
            "attractions": ["大理古城", "洱海", "崇圣寺三塔", "蝴蝶泉", "喜洲古镇"],
            "activities": ["古城漫步", "环洱海骑行", "民族文化体验", "摄影"],
            "coordinates": [25.6065, 100.2679],
            "tags": ["历史文化", "自然风光", "山川湖泊"],
            "budget_level": "经济",
            "image_url": "https://images.unsplash.com/photo-1545243424-0ce743321e11",
            "best_season": "春秋季",
            "local_food": ["白族三道茶", "乳扇", "粑粑鸡", "洱海鱼"],
            "travel_tips": "环洱海骑行是必体验项目；古城夜景很美；可以和丽江行程结合；消费相对丽江较低。"
        },
        "张家界": {
            "description": "奇峰林立的自然景观，《阿凡达》取景地",
            "climate": "湿润亚热带",
            "attractions": ["武陵源", "天门山", "张家界国家森林公园", "黄龙洞", "玻璃桥"],
            "activities": ["自然观光", "徒步", "摄影", "极限运动"],
            "coordinates": [29.1168, 110.4788],
            "tags": ["自然风光", "山川湖泊"],
            "budget_level": "适中",
            "image_url": "https://images.unsplash.com/photo-1537531383496-f4749b8032cf",
            "best_season": "春秋季",
            "local_food": ["土家腊肉", "酸汤鱼", "血粑鸭", "蜂蜜柚子茶"],
            "travel_tips": "景区面积大，建议安排3-4天；旺季人多，提前预订酒店；山上气温较低，注意增减衣物；索道排队时间长。"
        }
    }

# 天气数据模拟
def get_weather_forecast(city, date):
    """
    模拟获取城市天气预报
    """
    import random
    from datetime import datetime, timedelta
    
    # 根据城市和季节模拟天气情况
    weather_types = {
        "北京": {"春": ["晴朗", "多云", "小雨"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["晴朗", "多云", "小雪"]},
        "上海": {"春": ["多云", "小雨", "阴天"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雨"]},
        "杭州": {"春": ["多云", "小雨", "阴天"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雨"]},
        "三亚": {"春": ["晴朗", "多云"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云", "阵雨"], "冬": ["晴朗", "多云"]},
        "丽江": {"春": ["晴朗", "多云"], "夏": ["晴朗", "多云", "阵雨"], "秋": ["晴朗", "多云"], "冬": ["晴朗", "多云", "小雪"]},
        "西安": {"春": ["晴朗", "多云", "沙尘"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雪"]},
        "成都": {"春": ["多云", "小雨", "阴天"], "夏": ["多云", "阵雨", "雷阵雨"], "秋": ["多云", "小雨"], "冬": ["多云", "小雨"]},
        "厦门": {"春": ["晴朗", "多云", "小雨"], "夏": ["晴朗", "多云", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雨"]},
        "桂林": {"春": ["多云", "小雨", "阴天"], "夏": ["多云", "阵雨", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雨"]},
        "青岛": {"春": ["晴朗", "多云", "小雨"], "夏": ["晴朗", "多云", "阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雪"]},
        "大理": {"春": ["晴朗", "多云"], "夏": ["晴朗", "多云", "阵雨"], "秋": ["晴朗", "多云"], "冬": ["晴朗", "多云"]},
        "张家界": {"春": ["多云", "小雨", "阴天"], "夏": ["多云", "阵雨", "雷阵雨"], "秋": ["晴朗", "多云"], "冬": ["多云", "小雨"]}
    }
    
    # 根据日期判断季节
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    month = date_obj.month
    
    if 3 <= month <= 5:
        season = "春"
    elif 6 <= month <= 8:
        season = "夏"
    elif 9 <= month <= 11:
        season = "秋"
    else:
        season = "冬"
    
    # 获取城市当季可能的天气类型
    possible_weather = weather_types.get(city, {}).get(season, ["晴朗", "多云"])
    
    # 生成温度范围
    temp_ranges = {
        "春": {"min": 10, "max": 25},
        "夏": {"min": 22, "max": 35},
        "秋": {"min": 15, "max": 28},
        "冬": {"min": -5, "max": 15}
    }
    
    # 根据城市调整温度
    city_temp_adjust = {
        "北京": {"min": 0, "max": 0},
        "上海": {"min": 2, "max": 2},
        "杭州": {"min": 2, "max": 2},
        "三亚": {"min": 10, "max": 8},
        "丽江": {"min": -2, "max": -5},
        "西安": {"min": 0, "max": 0},
        "成都": {"min": 2, "max": -2},
        "厦门": {"min": 5, "max": 3},
        "桂林": {"min": 3, "max": 2},
        "青岛": {"min": -2, "max": -3},
        "大理": {"min": 0, "max": -2},
        "张家界": {"min": 0, "max": -1}
    }
    
    adjust = city_temp_adjust.get(city, {"min": 0, "max": 0})
    temp_range = temp_ranges.get(season, {"min": 15, "max": 25})
    
    min_temp = temp_range["min"] + adjust["min"]
    max_temp = temp_range["max"] + adjust["max"]
    
    # 生成7天天气预报
    forecast = []
    current_date = date_obj
    
    for i in range(7):
        weather = random.choice(possible_weather)
        min_t = random.randint(min_temp - 2, min_temp + 2)
        max_t = random.randint(max_temp - 2, max_temp + 2)
        
        # 确保最高温度大于最低温度
        if max_t <= min_t:
            max_t = min_t + random.randint(1, 5)
        
        forecast.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "day": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][current_date.weekday()],
            "weather": weather,
            "min_temp": min_t,
            "max_temp": max_t,
            "wind": random.choice(["微风", "东风", "西风", "南风", "北风"]) + random.choice(["3级", "4级", "5级"])
        })
        
        current_date += timedelta(days=1)
    
    return forecast

# 交通信息模拟
def get_transportation_info(from_city, to_city):
    """
    模拟获取城市间交通信息
    """
    import random
    
    # 模拟交通方式和时间
    transportation_modes = ["飞机", "高铁", "火车", "汽车"]
    
    # 根据城市距离调整可用交通方式
    city_distances = {
        ("北京", "上海"): {"distance": 1318, "modes": ["飞机", "高铁"]},
        ("北京", "杭州"): {"distance": 1279, "modes": ["飞机", "高铁"]},
        ("北京", "三亚"): {"distance": 2788, "modes": ["飞机"]},
        ("北京", "丽江"): {"distance": 2342, "modes": ["飞机"]},
        ("北京", "西安"): {"distance": 912, "modes": ["飞机", "高铁"]},
        ("北京", "成都"): {"distance": 1671, "modes": ["飞机", "高铁"]},
        ("北京", "厦门"): {"distance": 1753, "modes": ["飞机", "高铁"]},
        ("北京", "桂林"): {"distance": 1897, "modes": ["飞机", "高铁"]},
        ("北京", "青岛"): {"distance": 550, "modes": ["飞机", "高铁", "火车"]},
        ("上海", "杭州"): {"distance": 169, "modes": ["高铁", "火车", "汽车"]},
        ("上海", "三亚"): {"distance": 1892, "modes": ["飞机"]},
        ("上海", "丽江"): {"distance": 2224, "modes": ["飞机"]},
        ("上海", "西安"): {"distance": 1229, "modes": ["飞机", "高铁"]},
        ("上海", "成都"): {"distance": 1666, "modes": ["飞机", "高铁"]},
        ("上海", "厦门"): {"distance": 679, "modes": ["飞机", "高铁"]},
        ("上海", "桂林"): {"distance": 1172, "modes": ["飞机", "高铁"]},
        ("上海", "青岛"): {"distance": 766, "modes": ["飞机", "高铁", "火车"]},
    }
    
    # 获取城市间距离和交通方式
    city_pair = (from_city, to_city)
    if city_pair not in city_distances:
        city_pair = (to_city, from_city)  # 尝试反向查找
    
    info = city_distances.get(city_pair, {"distance": random.randint(500, 2000), "modes": transportation_modes})
    
    # 根据距离和交通方式生成时间和价格
    result = []
    for mode in info["modes"]:
        if mode == "飞机":
            duration = f"{int(info['distance']/700)}小时{random.randint(0, 59)}分钟"
            price = int(info['distance'] * (0.7 + random.random() * 0.6))
        elif mode == "高铁":
            duration = f"{int(info['distance']/250)}小时{random.randint(0, 59)}分钟"
            price = int(info['distance'] * (0.4 + random.random() * 0.3))
        elif mode == "火车":
            duration = f"{int(info['distance']/120)}小时{random.randint(0, 59)}分钟"
            price = int(info['distance'] * (0.2 + random.random() * 0.2))
        else:  # 汽车
            duration = f"{int(info['distance']/80)}小时{random.randint(0, 59)}分钟"
            price = int(info['distance'] * (0.15 + random.random() * 0.15))
        
        result.append({
            "mode": mode,
            "duration": duration,
            "price": price,
            "distance": info['distance']
        })
    
    return result

# 特色活动数据
def get_special_activities(city, season):
    """
    获取城市特色活动
    """
    activities =