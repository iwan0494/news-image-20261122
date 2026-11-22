"""Data for the 22 November 2026 world-news poster.

Twelve stories, all of which happened or were first reported on
Sunday 22 November 2026 (or late Saturday 21 November, reported
across the 22 November news cycle). Sources: international news
wires, 22 November 2026.
"""

DATE_LINE = "SUNDAY, 22 NOVEMBER 2026"
MASTHEAD = "THE WORLD IN ONE DAY"
SUBHEAD = "Twelve stories from one Sunday \u2014 climate, trade, war, quakes and markets."

STATS = [
    ("98.5%", "TARIFFS CUT", "EU\u2013Indonesia deal"),
    ("6.7", "PERU QUAKE", "15 hurt, 127 homes hit"),
    ("$5M", "REWARD", "\u2018El Chapo Isidro\u2019 caught"),
    ("2", "MISSILES", "land in Poland"),
]

FEATURES = [
    {
        "num": 1,
        "kicker": "CLIMATE \u00b7 ANTALYA",
        "headline": "COP31 nears deal after overtime talks",
        "body": (
            "A new package goes to a Sunday-morning vote after "
            "talks ran past Friday. The fight: a draft with no "
            "mention of fossil fuels."
        ),
        "fact": "35% electricity by 2035",
        "place": "Antalya, T\u00fcrkiye",
        "icon": "globe",
    },
    {
        "num": 2,
        "kicker": "TRADE \u00b7 BRUSSELS",
        "headline": "EU and Indonesia sign deal after 10 years",
        "body": (
            "Duties scrapped on up to 98.5% of tariff lines. The "
            "pact covers 730 million people; EU car duties go "
            "within five years."
        ),
        "fact": "98.5% of tariffs gone",
        "place": "Brussels",
        "icon": "trade",
    },
    {
        "num": 3,
        "kicker": "SECURITY \u00b7 POLAND",
        "headline": "Russian missiles land in Poland",
        "body": (
            "Two missiles and a drone came down in the south-east. "
            "NATO calls it a \u201cgrave violation\u201d; Trump says "
            "it was a mistake."
        ),
        "fact": "2 missiles + 1 drone",
        "place": "South-east Poland",
        "icon": "missile",
    },
]

TILES = [
    {
        "num": 4,
        "headline": "Peru quake 6.7 shakes the Andes",
        "body": "15 hurt, 127 homes damaged in Jun\u00edn and Pasco; felt in Lima.",
        "place": "Jun\u00edn, Peru",
        "icon": "quake",
    },
    {
        "num": 5,
        "headline": "Mexico captures \u2018El Chapo Isidro\u2019",
        "body": "FBI top-10 fugitive held in Sinaloa; 11 killed.",
        "place": "Sinaloa, Mexico",
        "icon": "cuffs",
    },
    {
        "num": 6,
        "headline": "Iran claims strikes on US radars",
        "body": "IRGC says it hit two Patriot radars; US says it intercepted.",
        "place": "Bahrain",
        "icon": "radar",
    },
    {
        "num": 7,
        "headline": "Strike hits Zelenskyy\u2019s hometown",
        "body": "Russian attack kills 2, wounds 60; Kyiv renews its NATO bid.",
        "place": "Kryvyi Rih, Ukraine",
        "icon": "blast",
    },
    {
        "num": 8,
        "headline": "Tech stocks crash, Asia plunges",
        "body": "Wall Street rout deepens and spreads across Europe and Asia.",
        "place": "New York / Asia",
        "icon": "chart",
    },
    {
        "num": 9,
        "headline": "Trump warns on AI centres abroad",
        "body": "US firms building AI data centres overseas face a \u201ctremendous tax\u201d.",
        "place": "Washington",
        "icon": "chip",
    },
    {
        "num": 10,
        "headline": "Myanmar quake 4.1 in early hours",
        "body": "Tremor strikes in the early hours of Sunday, seismologists report.",
        "place": "Myanmar",
        "icon": "quake",
    },
    {
        "num": 11,
        "headline": "Timor-Leste quake 6.8, no tsunami",
        "body": "Strong tremor off Lospalos; USGS sees low risk of casualties.",
        "place": "Timor-Leste",
        "icon": "quake",
    },
]

BRIEF = {
    "num": 12,
    "headline": "Drones set Russian ship ablaze in the Gulf of Finland",
    "body": (
        "Ukrainian drones hit a sanctioned Russian ship off Finland."
    ),
    "place": "Gulf of Finland",
}

ALSO_ON = [
    "Hong Kong: voting begins for the powerful Election Committee",
    "Ethiopia and Eritrea mass troops on their border",
    "UN talks on lethal autonomous weapons fall short",
    "Sudan: Tasis Alliance seizes Bau in the Blue Nile",
]

PLACES = [
    (1, "Antalya"),
    (2, "Brussels"),
    (3, "Poland"),
    (4, "Jun\u00edn"),
    (5, "Sinaloa"),
    (6, "Bahrain"),
    (7, "Kryvyi Rih"),
    (8, "New York"),
    (9, "Washington"),
    (10, "Myanmar"),
    (11, "Timor-Leste"),
    (12, "Gulf of Finland"),
]

FOOTER = (
    "SUNDAY 22 NOVEMBER 2026 \u2014 All twelve stories happened or "
    "were first reported on this day."
)
SOURCES = "Sources: international news wires, 22 November 2026."
