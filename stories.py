"""Data for the 22 November 2026 poster (round 3).

Seven biggest stories of the day. Each story carries a big headline,
a one-sentence tagline that explains it in plain words, a certainty
label, a source, and a key number. Text only; the poster script draws
everything else.
"""

MASTHEAD = "THE WORLD IN ONE DAY"
DATE_LINE = "SUNDAY, 22 NOVEMBER 2026"
SUBHEAD = "Seven stories from one Sunday — war, climate, trade, markets, quakes."

STATS = [
    ("2 RADARS", "Iran claims US hits in Bahrain"),
    ("KH-101", "Russian missile confirmed in Poland"),
    ("-3,7%", "S&P 500 into correction"),
    ("98,5%", "EU-Indonesia tariffs gone"),
]

# Each story: number, kicker, headline, tagline, certainty label, source, icon.
STORIES = [
    {
        "num": 1,
        "kicker": "GULF CRISIS · BAHRAIN",
        "headline": "IRAN STRIKES US BASES IN BAHRAIN",
        "tagline": "Tehran claims hits on two Patriot radars; Bahrain says a "
                   "civilian site burned and tankers were hit near Hormuz.",
        "label": "CLAIM",
        "source": "Reuters / Bahrain officials",
        "icon": "radar",
    },
    {
        "num": 2,
        "kicker": "SECURITY · POLAND",
        "headline": "NATO VOWS TO DEFEND EVERY INCH OF POLAND",
        "tagline": "A Russian Kh-101 missile is confirmed on Polish soil; "
                   "Rutte in Warsaw: the alliance stands with Poland.",
        "label": "CONFIRMED",
        "source": "Polish prosecutors / NATO",
        "icon": "missile",
    },
    {
        "num": 3,
        "kicker": "CLIMATE · ANTALYA",
        "headline": "COP31 IN OVERTIME — THE FIGHT IS OVER TWO WORDS",
        "tagline": "Talks run into a second day past deadline; the draft never "
                   "says \u201cfossil fuels\u201d — and 130 countries want the "
                   "words back.",
        "label": "CONFIRMED",
        "source": "Reuters / AP",
        "icon": "globe",
    },
    {
        "num": 4,
        "kicker": "MARKETS · NEW YORK",
        "headline": "STOCKS IN CORRECTION AS TECH ROUT DEEPENS",
        "tagline": "The S&P 500 sinks 3.7% and the Nasdaq wipes out its "
                   "2026 gains in an AI-led sell-off.",
        "label": "CONFIRMED",
        "source": "Market wires",
        "icon": "chart",
    },
    {
        "num": 5,
        "kicker": "TRADE · BRUSSELS",
        "headline": "EU AND INDONESIA SIGN LANDMARK TRADE DEAL",
        "tagline": "Ten years of talks end — duties gone on 98.5% of goods, "
                   "covering 730 million people.",
        "label": "CONFIRMED",
        "source": "European Commission / DW",
        "icon": "trade",
    },
    {
        "num": 6,
        "kicker": "CARTELS · SINALOA",
        "headline": "MEXICO CAPTURES FBI MOST-WANTED \u2018EL CHAPO ISIDRO\u2019",
        "tagline": "The $5m-reward fugitive is held in Sinaloa; 11 killed "
                   "as cartel gunmen fought back.",
        "label": "CONFIRMED",
        "source": "AP / FBI",
        "icon": "cuffs",
    },
    {
        "num": 7,
        "kicker": "QUAKE · PERU",
        "headline": "PERU QUAKE 6.7 SHAKES THE ANDES",
        "tagline": "Fifteen hurt and 127 homes damaged in Junín and Pasco; "
                   "the tremor is felt across Lima.",
        "label": "CONFIRMED",
        "source": "USGS",
        "icon": "quake",
    },
]

DATE_CHECK_TITLE = "DATE CHECK — SUNDAY 22 NOVEMBER 2026"
DATE_CHECK_BODY = (
    "Every story above happened or was first reported on this day. "
    "Deliberately left out: the Trump–Xi–Putin Shenzhen nuclear pledge "
    "(Thursday 19 Nov), the UN autonomous-weapons talks (Geneva, no "
    "binding deal), and the Hong Kong Election Committee vote (local "
    "election, not a world headline)."
)
PRESS_TIME = "Press time: Sunday 22 November 2026, evening (UTC)."

ALSO = (
    "Also Sunday: 186 Russian drones over Ukraine overnight as the "
    "Kryvyi Rih toll rises to 73 injured; a Russian ship burns in the "
    "Gulf of Finland; a 4.1 quake in Myanmar."
)

FOOTER_DATE = "SUNDAY 22 NOVEMBER 2026 — All seven stories happened or were first reported on this day."
FOOTER_SOURCES = "Sources: Reuters, AP, USGS, European Commission, DW, FBI — 22 November 2026."
