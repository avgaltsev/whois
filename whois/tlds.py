import re


_patterns = {
    
    "com": "No match for \"[^\"]+\"\.",
    "org": "NOT FOUND",
    "biz": "Not found: .+",
    "cat": "% Object \"[^\"]+\" NOT FOUND\.",
    "coop": "No domain records were found to match \"[^\"]+\"",
    "name": "No match\.",
    "ru": "No entries found for the selected source\(s\)\.",
    
}


_tokens = {
    
    #"br.com": "",
    #"cn.com": "",
    #"de.com": "",
    #"eu.com": "",
    #"gb.com": "",
    #"gb.net": "",
    #"gr.com": "",
    #"hu.com": "",
    #"no.com": "",
    #"qc.com": "",
    #"ru.com": "",
    #"sa.com": "",
    #"se.com": "",
    #"se.net": "",
    #"uk.com": "",
    #"uk.net": "",
    #"us.com": "",
    #"uy.com": "",
    #"za.com": "",
    #"jpn.com": "",
    #"web.com": "",

    "com": _patterns["com"],

    #"za.net": "",
    "net": _patterns["com"],

    #"eu.org": "",
    #"za.org": "",
    "org": _patterns["org"],

    #"edu": "",
    #"gov": "",
    #"int": "",
    #"mil": "",

    #"e164.arpa": "",
    #"in-addr.arpa": "",
    #"arpa": "",

    "aero": _patterns["org"],
    "asia": _patterns["org"],
    "biz": _patterns["biz"],
    "cat": _patterns["cat"],
    "coop": _patterns["coop"],
    "info": _patterns["org"],
    "jobs": _patterns["com"],
    "mobi": _patterns["org"],
    "museum": _patterns["cat"],
    "name": _patterns["name"],
    "post": _patterns["org"],
    "pro": _patterns["org"],
    "tel": _patterns["biz"],
    "travel": _patterns["biz"],
    "xxx": _patterns["org"],

    #"ac": "",
    #"ad": "",
    #"ae": "",
    #"af": "",
    #"ag": "",
    #"ai": "",
    #"al": "",
    #"am": "",
    #"an": "",
    #"ao": "",
    #"aq": "",
    #"ar": "",
    #"as": "",
    #"priv.at": "",
    #"at": "",
    #"au": "",
    #"aw": "",
    #"ax": "",
    #"az": "",
    #"ba": "",
    #"bb": "",
    #"bd": "",
    #"be": "",
    #"bf": "",
    #"bg": "",
    #"bh": "",
    #"bi": "",
    #"bj": "",
    #"bl": "",
    #"bm": "",
    #"bn": "",
    #"bo": "",
    #"bq": "",
    #"br": "",
    #"bs": "",
    #"bt": "",
    #"bv": "",
    #"by": "",
    #"bw": "",
    #"bz": "",
    #"co.ca": "",
    #"ca": "",
    "cc": _patterns["com"],
    #"cd": "",
    #"cf": "",
    #"cg": "",
    #"ch": "",
    #"ci": "",
    #"ck": "",
    #"cl": "",
    #"cm": "",
    #"edu.cn": "",
    #"cn": "",
    #"uk.co": "",
    #"co": "",
    #"cr": "",
    #"cu": "",
    #"cv": "",
    #"cw": "",
    #"cx": "",
    #"cy": "",
    #"cz": "",
    #"de": "",
    #"dj": "",
    #"dk": "",
    #"dm": "",
    #"do": "",
    #"dz": "",
    #"ec": "",
    #"ee": "",
    #"eg": "",
    #"eh": "",
    #"er": "",
    #"es": "",
    #"et": "",
    #"eu": "",
    #"fi": "",
    #"fj": "",
    #"fk": "",
    #"fm": "",
    #"fo": "",
    #"fr": "",
    #"ga": "",
    #"gb": "",
    #"gd": "",
    #"ge": "",
    #"gf": "",
    #"gg": "",
    #"gh": "",
    #"gi": "",
    #"gl": "",
    #"gm": "",
    #"gn": "",
    #"gp": "",
    #"gq": "",
    #"gr": "",
    #"gs": "",
    #"gt": "",
    #"gu": "",
    #"gw": "",
    #"gy": "",
    #"hk": "",
    #"hm": "",
    #"hn": "",
    #"hr": "",
    #"ht": "",
    #"hu": "",
    #"id": "",
    #"ie": "",
    #"il": "",
    #"im": "",
    #"in": "",
    #"io": "",
    #"iq": "",
    #"ir": "",
    #"is": "",
    #"it": "",
    #"je": "",
    #"jm": "",
    #"jo": "",
    #"jp": "",
    #"ke": "",
    #"kg": "",
    #"kh": "",
    #"ki": "",
    #"km": "",
    #"kn": "",
    #"kp": "",
    #"kr": "",
    #"kw": "",
    #"ky": "",
    #"kz": "",
    #"la": "",
    #"lb": "",
    #"lc": "",
    #"li": "",
    #"lk": "",
    #"lr": "",
    #"ls": "",
    #"lt": "",
    #"lu": "",
    #"lv": "",
    #"ly": "",
    #"ma": "",
    #"mc": "",
    #"md": "",
    #"me": "",
    #"mf": "",
    #"mg": "",
    #"mh": "",
    #"mk": "",
    #"ml": "",
    #"mm": "",
    #"mn": "",
    #"mo": "",
    #"mp": "",
    #"mq": "",
    #"mr": "",
    #"ms": "",
    #"mt": "",
    #"mu": "",
    #"mv": "",
    #"mw": "",
    #"mx": "",
    #"my": "",
    #"mz": "",
    #"na": "",
    #"nc": "",
    #"ne": "",
    #"nf": "",
    #"ng": "",
    #"ni": "",
    #"nl": "",
    #"no": "",
    #"np": "",
    #"nr": "",
    #"nu": "",
    #"nz": "",
    #"om": "",
    #"pa": "",
    #"pe": "",
    #"pf": "",
    #"pg": "",
    #"ph": "",
    #"pk": "",
    #"co.pl": "",
    #"pl": "",
    #"pm": "",
    #"pn": "",
    #"pr": "",
    #"ps": "",
    #"pt": "",
    #"pw": "",
    #"py": "",
    #"qa": "",
    #"re": "",
    #"ro": "",
    #"rs": "",
    #"edu.ru": "",
    "ru": _patterns["ru"],
    #"rw": "",
    #"sa": "",
    #"sb": "",
    #"sc": "",
    #"sd": "",
    #"se": "",
    #"sg": "",
    #"sh": "",
    #"si": "",
    #"sj": "",
    #"sk": "",
    #"sl": "",
    #"sm": "",
    #"sn": "",
    #"so": "",
    #"sr": "",
    #"ss": "",
    #"st": "",
    "su": _patterns["ru"],
    #"sv": "",
    #"sx": "",
    #"sy": "",
    #"sz": "",
    #"tc": "",
    #"td": "",
    #"tf": "",
    #"tg": "",
    #"th": "",
    #"tj": "",
    #"tk": "",
    #"tl": "",
    #"tm": "",
    #"tn": "",
    #"to": "",
    #"tp": "",
    #"tr": "",
    #"tt": "",
    #"tv": "",
    #"tw": "",
    #"tz": "",
    #"biz.ua": "",
    #"co.ua": "",
    #"pp.ua": "",
    #"ua": "",
    #"ug": "",
    #"ac.uk": "",
    #"bl.uk": "",
    #"british-library.uk": "",
    #"gov.uk": "",
    #"icnet.uk": "",
    #"jet.uk": "",
    #"mod.uk": "",
    #"nhs.uk": "",
    #"nls.uk": "",
    #"parliament.uk": "",
    #"police.uk": "",
    #"uk": "",
    #"um": "",
    #"fed.us": "",
    #"us": "",
    #"com.uy": "",
    #"uy": "",
    #"uz": "",
    #"va": "",
    #"vc": "",
    #"ve": "",
    #"vg": "",
    #"vi": "",
    #"vn": "",
    #"vu": "",
    #"wf": "",
    #"ws": "",
    #"ye": "",
    #"yt": "",
    #"ac.za": "",
    #"alt.za": "",
    #"co.za": "",
    #"gov.za": "",
    #"net.za": "",
    #"org.za": "",
    #"web.za": "",
    #"za": "",
    #"zm": "",
    #"zw": "",
    
}


def recognize(domain, whois):
    
    tld = ".".join(domain.split(".")[1:])
    
    if tld in _tokens:
        return "free" if re.search(_tokens[tld], whois) else "occupied"
    
    return "unrecognized"
