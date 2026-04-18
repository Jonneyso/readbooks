# 读名著 - 上海高考名著导读网站设计文档

## 1. 项目概述

本项目是一个基于Web的中国古典文学及外国文学名著导读平台，专门针对上海高考名著阅读要求设计。网站旨在为学生提供直观、全面的名著导读服务，包含作品简介、主要人物、主题思想和高考知识点等内容。

### 1.1 项目目标

- 展示名著的导读内容（作品简介、主要人物、主题思想、结构特点）
- 提供高考知识点整理和考试要点梳理
- 实现人物分类筛选功能
- 确保网站响应式，适配不同设备
- 提供统一的导航和页面层级结构

### 1.2 核心功能

- 名著导读（作品简介、主要人物、主题思想、结构特点）
- 人物分类展示（部分名著包含人物故事线）
- 高考知识点整理（按照高中月考、期中考、期末考、高考分类）
- 分类筛选功能
- 响应式设计

## 2. 技术栈

### 2.1 前端技术

- HTML5：页面结构
- CSS3：页面样式（Flexbox、Grid布局）
- JavaScript：交互逻辑、动态渲染

### 2.2 数据存储

- JSON：存储人物信息和故事线数据（部分名著）

## 3. 系统架构

### 3.1 页面层级结构

项目采用两层页面结构：

```
第一层：名著主页
    └── 名著卡片（读名著首页）

第二层：名著内容页
    ├── 名著导读
    └── 高考知识点（部分名著独有）
```

**层级导航规则：**
- 所有第二层页面都从主页名著卡片链接进入
- 返回按钮统一返回主页

### 3.2 页面结构

#### 3.2.1 第一层页面

| 页面 | 文件路径 | 说明 |
|------|----------|------|
| 读名著主页 | `index.html` | 名著卡片展示，网站入口 |

#### 3.2.2 第二层页面

**中国古典文学名著：**

| 页面 | 文件路径 | 说明 |
|------|----------|------|
| 水浒传导读 | `shuihu/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 水浒传人物故事线 | `shuihu/characters.html` | 人物分类筛选、搜索、列表展示 |
| 水浒传人物详情 | `shuihu/character.html` | 人物肖像、信息卡片、故事时间轴 |
| 水浒传人物聚散全景 | `shuihu/mindmap_v3.html` | 人物聚散关系思维导图 |
| 红楼梦导读 | `hongloumeng/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 红楼梦人物故事线 | `hongloumeng/characters.html` | 人物分类筛选、搜索、列表展示 |
| 红楼梦人物详情 | `hongloumeng/character.html` | 人物肖像、信息卡片、故事时间轴 |
| 红楼梦人物关系图 | `hongloumeng/relationship.html` | 人物关系可视化 |
| 红楼梦高考知识点 | `hongloumeng/exams.html` | 高中考试、高考考点整理 |
| 西游记导读 | `xiyouji/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 西游记人物故事线 | `xiyouji/characters.html` | 人物分类筛选、搜索、列表展示 |
| 西游记人物详情 | `xiyouji/character.html` | 人物肖像、信息卡片、故事时间轴 |
| 三国演义导读 | `sanguo/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 三国演义人物故事线 | `sanguo/characters.html` | 人物分类筛选、搜索、列表展示 |
| 三国演义人物详情 | `sanguo/character.html` | 人物肖像、信息卡片、故事时间轴 |
| 论语导读 | `lunyu/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 论语高考知识点 | `lunyu/exams.html` | 高中考试、高考考点整理 |
| 儒林外史导读 | `rulinwaishi/index.html` | 作品简介、主要人物、主题思想、结构特点 |
| 儒林外史高考知识点 | `rulinwaishi/exams.html` | 高中考试、高考考点整理 |

**外国文学名著：**

| 页面 | 文件路径 | 说明 |
|------|----------|------|
| 巴黎圣母院导读 | `bali_shengmuyuan/index.html` | 作品简介、主要人物、主题思想 |
| 巴黎圣母院高考知识点 | `bali_shengmuyuan/exams.html` | 高中考试、高考考点整理 |
| 变形记导读 | `biancheng/index.html` | 作品简介、主要人物、主题思想 |
| 变形记高考知识点 | `biancheng/exams.html` | 高中考试、高考考点整理 |
| 茶馆导读 | `chaguan/index.html` | 作品简介、主要人物、主题思想 |
| 茶馆高考知识点 | `chaguan/exams.html` | 高中考试、高考考点整理 |
| 大卫·科波菲尔导读 | `dawen_kebofeiye/index.html` | 作品简介、主要人物、主题思想 |
| 大卫·科波菲尔高考知识点 | `dawen_kebofeiye/exams.html` | 高中考试、高考考点整理 |
| 复活导读 | `fuhuo/index.html` | 作品简介、主要人物、主题思想 |
| 复活高考知识点 | `fuhuo/exams.html` | 高中考试、高考考点整理 |
| 哈姆雷特导读 | `hanmosate/index.html` | 作品简介、主要人物、主题思想 |
| 哈姆雷特高考知识点 | `hanmosate/exams.html` | 高中考试、高考考点整理 |
| 红岩导读 | `hongyan/index.html` | 作品简介、主要人物、主题思想 |
| 红岩高考知识点 | `hongyan/exams.html` | 高中考试、高考考点整理 |
| 家导读 | `jia/index.html` | 作品简介、主要人物、主题思想 |
| 家高考知识点 | `jia/exams.html` | 高中考试、高考考点整理 |
| 老人与海导读 | `laoren_yu_hai/index.html` | 作品简介、主要人物、主题思想 |
| 老人与海高考知识点 | `laoren_yu_hai/exams.html` | 高中考试、高考考点整理 |
| 呐喊导读 | `nahan/index.html` | 作品简介、主要人物、主题思想 |
| 呐喊高考知识点 | `nahan/exams.html` | 高中考试、高考考点整理 |
| 欧也妮·葛朗台导读 | `ouyeini_gelangtai/index.html` | 作品简介、主要人物、主题思想 |
| 欧也妮·葛朗台高考知识点 | `ouyeini_gelangtai/exams.html` | 高中考试、高考考点整理 |
| 彷徨导读 | `panghuang/index.html` | 作品简介、主要人物、主题思想 |
| 彷徨高考知识点 | `panghuang/exams.html` | 高中考试、高考考点整理 |
| 平凡的世界导读 | `pingfan_de_shijie/index.html` | 作品简介、主要人物、主题思想 |
| 平凡的世界高考知识点 | `pingfan_de_shijie/exams.html` | 高中考试、高考考点整理 |
| 修养中国导读 | `xiuxiangzhongguo/index.html` | 作品简介、主要人物、主题思想 |
| 修养中国高考知识点 | `xiuxiangzhongguo/exams.html` | 高中考试、高考考点整理 |

## 4. 功能模块设计

### 4.1 导航菜单模块

- **功能**：提供统一的页面导航，包含内容筛选和页面切换
- **布局**：横向排列在页面顶端，白底圆角卡片样式
- **按钮样式**：
  - 默认状态：`background-color: #8B4513`
  - 悬停状态：`background-color: #654321`
  - 活动状态：`background-color: #654321` + `active`类
- **交互**：点击按钮筛选显示对应内容

### 4.2 人物列表模块（部分名著）

- **功能**：展示人物卡片列表，支持分类筛选和搜索
- **布局**：响应式网格布局
- **筛选**：按人物类别分类
- **交互**：点击人物卡片进入详情页面

### 4.3 人物详情模块（部分名著）

- **功能**：展示人物的详细信息
- **布局**：左右排版（3.5:6.5比例）
  - 左侧（35%）：人物肖像图片 + 图片说明
  - 右侧（65%）：信息卡片网格
- **信息卡片**：2列网格布局，全宽卡片占满整行
- **故事时间轴**：位于人物介绍下方

### 4.4 导读内容模块

- **功能**：展示名著的导读内容
- **内容**：作品简介、主要人物、主题思想、结构特点
- **布局**：内容区域可按导航筛选显示/隐藏

### 4.5 高考知识点模块

- **功能**：整理名著相关考试知识点
- **分类**：高中月考、期中考、期末考、高考
- **布局**：可折叠的详情列表

## 5. 文件结构

```
readbooks/
├── index.html                      # 主页（名著卡片）
├── start_server.py                # 本地服务器启动脚本
│
├── shuihu/                         # 水浒传
│   ├── index.html                  # 水浒传导读
│   ├── characters.html             # 水浒传人物故事线
│   ├── character.html              # 水浒传人物详情
│   ├── mindmap_v3.html              # 水浒传人物聚散全景
│   ├── shuihu_120_data.json         # 水浒传人物数据
│   ├── heroes_ranking.json          # 水浒传人物座次
│   └── images/                      # 水浒传人物肖像
│
├── hongloumeng/                    # 红楼梦
│   ├── index.html                  # 红楼梦导读
│   ├── characters.html             # 红楼梦人物故事线
│   ├── character.html              # 红楼梦人物详情
│   ├── relationship.html           # 红楼梦人物关系图
│   ├── exams.html                  # 红楼梦高考知识点
│   └── hongloumeng_data.json        # 红楼梦人物数据
│
├── xiyouji/                        # 西游记
│   ├── index.html                  # 西游记导读
│   ├── characters.html             # 西游记人物故事线
│   ├── character.html              # 西游记人物详情
│   └── xiyouji_data.json           # 西游记人物数据
│
├── sanguo/                         # 三国演义
│   ├── index.html                  # 三国演义导读
│   ├── characters.html             # 三国演义人物故事线
│   ├── character.html              # 三国演义人物详情
│   └── sanguo_data.json            # 三国演义人物数据
│
├── lunyu/                          # 论语
│   ├── index.html                  # 论语导读
│   └── exams.html                  # 论语高考知识点
│
├── rulinwaishi/                    # 儒林外史
│   ├── index.html                  # 儒林外史导读
│   └── exams.html                  # 儒林外史高考知识点
│
├── bali_shengmuyuan/               # 巴黎圣母院
│   ├── index.html                  # 巴黎圣母院导读
│   └── exams.html                  # 巴黎圣母院高考知识点
│
├── biancheng/                      # 变形记
│   ├── index.html                  # 变形记导读
│   └── exams.html                  # 变形记高考知识点
│
├── chaguan/                        # 茶馆
│   ├── index.html                  # 茶馆导读
│   └── exams.html                  # 茶馆高考知识点
│
├── dawen_kebofeiye/                # 大卫·科波菲尔
│   ├── index.html                  # 大卫·科波菲尔导读
│   └── exams.html                  # 大卫·科波菲尔高考知识点
│
├── fuhuo/                          # 复活
│   ├── index.html                  # 复活导读
│   └── exams.html                  # 复活高考知识点
│
├── hanmosate/                      # 哈姆雷特
│   ├── index.html                  # 哈姆雷特导读
│   └── exams.html                  # 哈姆雷特高考知识点
│
├── hongyan/                        # 红岩
│   ├── index.html                  # 红岩导读
│   └── exams.html                  # 红岩高考知识点
│
├── jia/                            # 家
│   ├── index.html                  # 家导读
│   └── exams.html                  # 家高考知识点
│
├── laoren_yu_hai/                  # 老人与海
│   ├── index.html                  # 老人与海导读
│   └── exams.html                  # 老人与海高考知识点
│
├── nahan/                          # 呐喊
│   ├── index.html                  # 呐喊导读
│   └── exams.html                  # 呐喊高考知识点
│
├── ouyeini_gelangtai/              # 欧也妮·葛朗台
│   ├── index.html                  # 欧也妮·葛朗台导读
│   └── exams.html                  # 欧也妮·葛朗台高考知识点
│
├── panghuang/                      # 彷徨
│   ├── index.html                  # 彷徨导读
│   └── exams.html                  # 彷徨高考知识点
│
├── pingfan_de_shijie/              # 平凡的世界
│   ├── index.html                  # 平凡的世界导读
│   └── exams.html                  # 平凡的世界高考知识点
│
├── xiuxiangzhongguo/               # 修养中国
│   ├── index.html                  # 修养中国导读
│   └── exams.html                  # 修养中国高考知识点
│
├── images/                         # 共享图片资源
│   └── default.jpg                 # 默认头像
│
├── README.md                       # 项目说明文件
├── DESIGN.md                       # 项目设计文档
│
└── .trae/                          # Trae IDE配置
    └── specs/                      # 规格说明
```

## 6. 设计规范

### 6.1 颜色系统

| 用途 | 颜色值 | 说明 |
|------|--------|------|
| 主色调 | `#8B4513` | 棕色，用于按钮、标题等 |
| 深色调 | `#654321` | 深棕色，用于悬停、活动状态 |
| 背景色 | `#f5f5dc` | 米色，页面背景 |
| 卡片背景 | `rgba(255,255,255,0.9)` | 半透明白色 |
| 边框色 | `#8B4513` | 棕色边框 |

### 6.2 字体规范

- 标题字体：系统默认字体
- 正文字体：系统默认字体
- 字号层级：
  - 页面标题：2rem
  - 副标题：1.2rem
  - 正文：1rem
  - 小字：0.8rem

### 6.3 按钮样式

```css
.nav-link {
    display: block;
    padding: 10px 20px;
    background-color: #8B4513;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.nav-link:hover {
    background-color: #654321;
}

.nav-link.active {
    background-color: #654321;
}
```

### 6.4 导航菜单容器样式

```css
.nav-menu {
    display: flex;
    justify-content: center;
    margin-bottom: 40px;
    background-color: rgba(255,255,255,0.9);
    border-radius: 8px;
    padding: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
```

### 6.5 响应式断点

| 屏幕尺寸 | 断点 | 说明 |
|----------|------|------|
| 大屏幕 | ≥1200px | 4列网格 |
| 中屏幕 | 992px-1199px | 3列网格 |
| 小屏幕 | 768px-991px | 2列网格 |
| 超小屏幕 | <768px | 1列网格，导航菜单垂直排列 |

## 7. 性能优化

### 7.1 图片加载优化（部分名著）

- 优先从本地加载图片
- 本地图片加载失败时，从网络加载
- 最终回退机制：使用默认图片

### 7.2 数据加载优化

- 使用Fetch API加载JSON数据
- 按需加载人物详情数据

## 8. 未来扩展

### 8.1 功能扩展

- 为更多名著添加人物关系图
- 增强内容筛选功能
- 添加更多人物的详细故事线

### 8.2 技术升级

- 考虑使用现代前端框架（React、Vue）重构
- 添加后端服务，实现数据的动态管理

## 9. 项目状态

项目已完成，包含以下名著：

**中国古典文学名著：**
- 《水浒传》：导读、人物故事线、人物详情、人物聚散全景
- 《红楼梦》：导读、人物故事线、人物详情、人物关系图、高考知识点
- 《西游记》：导读、人物故事线、人物详情
- 《三国演义》：导读、人物故事线、人物详情
- 《论语》：导读、高考知识点
- 《儒林外史》：导读、高考知识点

**外国文学名著：**
- 《巴黎圣母院》：导读、高考知识点
- 《变形记》：导读、高考知识点
- 《茶馆》：导读、高考知识点
- 《大卫·科波菲尔》：导读、高考知识点
- 《复活》：导读、高考知识点
- 《哈姆雷特》：导读、高考知识点
- 《红岩》：导读、高考知识点
- 《家》：导读、高考知识点
- 《老人与海》：导读、高考知识点
- 《呐喊》：导读、高考知识点
- 《欧也妮·葛朗台》：导读、高考知识点
- 《彷徨》：导读、高考知识点
- 《平凡的世界》：导读、高考知识点
- 《修养中国》：导读、高考知识点

网站功能完整，布局统一美观，响应式设计适配不同屏幕尺寸。页面层级清晰，导航逻辑明确。
