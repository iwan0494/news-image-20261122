"""Data for the ATLAS-35 poster: 35 verified stories from 22 November 2026.

Every headline and number here was verified against wire reporting
(Reuters, AP, AFP, CNN, WSJ, gov.uk, Ukrainian Air Force, USGS).
Nothing on the poster may add a number or a detail that is not in
this file.
"""

HEROES = [
    {
        "num": 1,
        "kicker": "CLIMATE \u00b7 ANTALYA",
        "headline": "COP31 talks set to collapse",
        "fact": "No new text \u2014 talks set to collapse",
    },
    {
        "num": 2,
        "kicker": "TRADE \u00b7 BRUSSELS",
        "headline": "EU and Indonesia sign trade deal",
        "fact": "98.5% of tariffs gone",
    },
    {
        "num": 3,
        "kicker": "SECURITY \u00b7 POLAND",
        "headline": "Russian missiles land in Poland",
        "fact": "2 missiles + 1 drone",
    },
]

# Each band: label, tab colour, and its one-line stories.
# A story line is "N. Headline \u2014 fact" rendered in two columns.
BANDS = [
    {
        "label": "EUROPE",
        "color": (30, 58, 95),
        "stories": [
            (4, "Denmark expels Russian defence attach\u00e9", "Kyivstoner plot"),
            (5, "Gen Z protests sweep 25 European countries", "25+ countries"),
            (6, "Ex-police chief De Gennaro found dead", "aged 78"),
            (7, "UK gives Ukraine 1,000 drones", "\u00a3260M package"),
            (8, "COP31 draft concedes 1.5\u00b0C overshoot", "limit to be passed"),
            (9, "UN: 128 states agree path on killer robots", "by 2028"),
            (10, "Italian transport workers strike", "trains disrupted"),
        ],
    },
    {
        "label": "WAR IN UKRAINE",
        "color": (185, 28, 28),
        "stories": [
            (11, "Kerch Bridge road arch dropped into sea", "227-m arch down"),
            (12, "Russia launches 186 drones overnight", "161 of 186 downed"),
            (13, "400-drone barrage kills 8 in Kyiv", "110 missiles"),
            (14, "Strike hits Kryvyi Rih", "2 killed, 60 wounded"),
            (15, "Dymer block hit, 14 missing", "14 missing"),
            (16, "Sparta II ablaze in Gulf of Finland", "crew evacuated"),
            (17, "Blasts reported over Kaliningrad", "first strikes on exclave"),
        ],
    },
    {
        "label": "MIDDLE EAST & AFRICA",
        "color": (120, 72, 20),
        "stories": [
            (18, "Iran claims strikes on US radars", "2 US radars targeted"),
            (19, "Gaza food vehicle strike kills 3", "3 killed"),
            (20, "Sudan: Tasis seizes Bau, Blue Nile", "Bau seized"),
            (21, "Ethiopia\u2013Eritrea troops massing", "border build-up"),
        ],
    },
    {
        "label": "ASIA\u2013PACIFIC",
        "color": (13, 92, 70),
        "stories": [
            (22, "Indonesia factory fire", "3 dead, 36 missing"),
            (23, "Trump, Xi & Putin meet in Shenzhen", "first-ever trilateral"),
            (24, "Myanmar quake 4.1", "magnitude 4.1"),
            (25, "Timor-Leste quake 6.8, no tsunami", "magnitude 6.8"),
            (26, "Hong Kong Election Committee voting begins", "voting begins"),
        ],
    },
    {
        "label": "AMERICAS",
        "color": (90, 40, 110),
        "stories": [
            (27, "Peru quake 6.7", "15 hurt, 127 homes hit"),
            (28, "\u2018El Chapo Isidro\u2019 captured", "$5M reward"),
            (29, "Trump warns AI data centres abroad", "\u201ctremendous tax\u201d"),
            (30, "Brazil Senate passes fiscal package", "45\u201331 vote"),
        ],
    },
    {
        "label": "MARKETS & SPORT",
        "color": (150, 90, 0),
        "stories": [
            (31, "Anthropic\u2019s record $81.3B IPO", "largest ever"),
            (32, "Tech crash: Nasdaq \u22125.3%", "S&P in correction"),
            (33, "Nvidia dives 14%", "\u221214%"),
            (34, "Verstappen wins Las Vegas GP", "wins by 0.639s"),
            (35, "Leeds stun Chelsea 4\u20131", "first win there since 1999"),
        ],
    },
]

# Numbered dots on the schematic world map: (story num, lon, lat, label).
MAP_DOTS = [
    (1, 30.7, 36.9, "Antalya"),
    (2, 6.0, 50.0, "Brussels"),
    (3, 22.0, 50.0, "Poland"),
    (7, -2.0, 52.5, "London"),
    (11, 38.5, 43.5, "Kerch"),
    (12, 30.5, 50.4, "Kyiv"),
    (16, 25.0, 61.0, "Gulf of Finland"),
    (18, 50.5, 26.0, "Bahrain"),
    (19, 34.5, 31.5, "Gaza"),
    (22, 106.0, -6.2, "Banten"),
    (23, 114.0, 22.5, "Shenzhen"),
    (26, 114.2, 22.3, ""),
    (27, -76.0, -11.0, "Jun\u00edn"),
    (28, -107.0, 25.0, "Sinaloa"),
    (34, -115.1, 36.2, "Las Vegas"),
]

FOOTER_LINE1 = (
    "SUNDAY 22 NOVEMBER 2026 \u2014 All 35 stories happened "
    "or were first reported on this day."
)
FOOTER_LINE2 = (
    "Sources: Reuters, AP, AFP, CNN, WSJ, gov.uk, Ukrainian Air Force, "
    "USGS \u2014 22 November 2026."
)

TOTAL_STORIES = 35
TOTAL_REGIONS = 7
