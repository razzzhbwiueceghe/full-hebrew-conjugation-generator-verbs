# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify,
import re

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)






root =

def match_hebrew_root(text):
    pattern = r'\b[\u0590-\u05FF]{3,5}\b'
    # Explanation of the pattern:
    # \b               - Word boundary
    # [\u0590-\u05FF]  - Match any Hebrew letter
    # {3,5}            - Match between 3 and 5 of the previous pattern
    # \b               - Word boundary
    match = re.match(pattern, text)
    if match:
        return match.group()
    else:
        return None

# Test the function
text = "שלום עליכם"
hebrew_root = match_hebrew_root(word)
if hebrew_root:
    print(f"The text contains the Hebrew root '{hebrew_root}'.")
else:
    print("No Hebrew root found.")



#gizrot below with each binyan
#consider to use regex instead of a bunch of dictionaries in consideration of efal and efol
pealim = {
    "paal": {
        "paal_shlemim":{
            "hoveh":{
            ("כותב",): {
            "ani": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
            "ata": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
            "hu": f"{root1}{xolammalei}{root2}{tzerei}{root3}",},

            ("כותבת",): {
            "ani": f"{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
            "at": f"{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
            "hi": f"{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",},

            ("כותבים",): {
            "anaxnu": f"{root1}{xolammalei}{root2}{shva}{root3}{chirik}{yod}{memsofit}",
            "atem": f"{root1}{xolammalei}{root2}{shva}{root3}{chirik}{yod}{memsofit}",
            "hem": f"{root1}{xolammalei}{root2}{shva}{root3}{chirik}{yod}{memsofit}",},

            ("כותבות",): {
            "anaxnu":f"{root1}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
            "aten":f"{root1}{xolammalei}{root2}{shva}{root3}{chirik}{tav}",
            "hen":f"{root1}{xolammalei}{root2}{shva}{root3}{chirik}{tav}",}
            }

            },

            "avar":{
            ("כתבתי",):{
            "ani":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{chirik}{yod}"
            }
            ,
            ("כתבת",):{
            "ata":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}"
            },
            ("כתבת"):{
            "at":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}"
            },
            ("כתב"):{
            "hu":f"{root1}{qametz}{root2}{patax}{root3}"

            },
            ("כתבה"):{
            "hi":f"{root1}{qametz}{root2}{shva}{root3}{qametz}{hey}"
            },
            ("כתבנו"):{
            "anaxnu":f"{root1}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}"
            },
            ("כתבתם"):{
            "atem":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
            },
            ("כתבתן"):{
            "aten":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
            },
            ("כתבו"):{
            "hem":f"{root1}{qametz}{root2}{shva}{root3}{shureq}"
            },
            ("כתבו"):{
            "hen":f"{root1}{qametz}{root2}{shva}{root3}{shureq}"
            },



            "atid":{
            "efal":{
            ("אבלע"):{{
            "ani":f"{alef}{segol}{root1}{shva}{root2}{patax}{root3}",

            ("תבלע"):{
            "ata":f"{tav_with_mapik}{xireq}{root1}{shva}{patax}{root3}",

            ("תבלעי"):{
            "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",

            ("תבלוע"):{
            "hu":f"{yod}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

            ("יבלוע"):{
            "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod},"

            ("נבלע"):{
            "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

            ("תבלעו"):{
            "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("תבלעו"):{
            "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("יבלעו"):{
            "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("יבלעו"):{
            "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",




            "efol":,
            ("אכתוב"):{
            "ani":f"{alef}{sehol}{root1}{shva}{root2}{xolammalei}{root3}",

            ("תכתוב"):{
            "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolam}{root3}",

            ("תכתבי"):{
            "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",

            ("יכתוב"):{
            "hu":f"{yod}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

            ("תכתוב"):{
            "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolam}{root3},"

            ("נכתוב"):{
            "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

            ("תכתבו"):{
            "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("תכתבו"):{
            "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("יכתבו"):{
            "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",

            ("יכתבו"):{
            "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shuruq}",





        "paal_lamed_hey_yod":{
        "hoveh":{
        ("קונה",): {
        "ani": f"{root1}{xolammalei}{root2}{hey}",
        "ata": f"{root1}{xolammalei}{root2}{hey}",
        "hu": f"{root1}{xolammalei}{root2}{hey}",},

        ("קונה",): {
        "ani": f"{root1}{xolammalei}{root2}{hey}",
        "at": f"{root1}{xolammalei}{root2}{hey}",
        "hi": f"{root1}{xolammalei}{root2}{hey}",},

        ("קונים",): {
        "anaxnu": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
        "atem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
        "hem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",},

        ("קונות",): {
        "anaxnu":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
        "aten":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
        "hen":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",}
        }

        },

        "avar":{
        ("קניתי",):{
        "ani":f""
        }
        ,
        ("קנית",):{
        "ata":f""
        },
        ("קנית"):{
        "at":f""
        },
        ("קנה"):{
        "hu":f""

        },
        ("קנתה"):{
        "hi":f""
        },
        ("קנינו"):{
        "anaxnu":f""
        },
        ("קניתם"):{
        "atem":f""
        },
        ("קניתן"):{
        "aten":f""
        },
        ("קנו"):{
        "hem":f""
        },
        ("קנו"):{
        "hen":f""
        },



        "atid":{

        ("אקנה"):{
        "ani":f"",

        ("תקנה"):{
        "ata":f"",

        ("תקני"):{
        "at":f"",

        ("יקנה"):{
        "hu":f"",

        ("תקנה"):{
        "hi":f","

        ("נקנה"):{
        "anaxnu":f"",

        ("תקנו"):{
        "atem":f"",

        ("תקנו"):{
        "aten":f"",

        ("יקנו"):{
        "hem":f"",

        ("יקנו"):{
        "hen":f"",









        "paal_pey_yod":{
        "hoveh":{
        ("יורד",): {
        "ani": f"",
        "ata": f"",
        "hu": f"",},

        ("יורדת",): {
        "ani": f"",
        "at": f"",
        "hi": f"",},

        ("יורדים",): {
        "anaxnu": f"",
        "atem": f"",
        "hem": f"",},

        ("יורדות",): {
        "anaxnu":f"",
        "aten":f"",
        "hen":f"",}
        }

        },

        "avar":{
        ("ירדתי",):{
        "ani":f""
        }
        ,
        ("ירדת",):{
        "ata":f""
        },
        ("ירדת"):{
        "at":f"
        },
        ("ירד"):{
        "hu":f""

        },
        ("ירדה"):{
        "hi":f""
        },
        ("ירדנו"):{
        "anaxnu":f""
        },
        ("ירדתם"):{
        "atem":f""
        },
        ("ירדתן"):{
        "aten":f""
        },
        ("ירדו"):{
        "hem":f""
        },
        ("ירדו"):{
        "hen":f""
        },



        "atid":{

        ("ארד"):{
        "ani":f"",

        ("תרד"):{
        "ata":f"",

        ("תרדי"):{
        "at":f"",

        ("ירד"):{
        "hu":f"",

        ("תרד"):{
        "hi":f","

        ("נרד"):{
        "anaxnu":f"",

        ("תרדו"):{
        "atem":f"",

        ("תרדו"):{
        "aten":f"",

        ("ירדו"):{
        "hem":f"",

        ("ירדו"):{
        "hen":f"",







    "paal_lamed_alef":{
    "hoveh":{
    ("קורא",): {
    "ani": f"",
    "ata": f"",
    "hu": f"",},

    ("קוראת",): {
    "ani": f"",
    "at": f"",
    "hi": f"",},

    ("קוראים",): {
    "anaxnu": f"",
    "atem": f"",
    "hem": f"",},

    ("קוראות",): {
    "anaxnu":f"",
    "aten":f"",
    "hen":f"",}
    }

    },

    "avar":{
    ("קראתי",):{
    "ani":f""
    }
    ,
    ("קראת",):{
    "ata":f""
    },
    ("קראת"):{
    "at":f""
    },
    ("קרא"):{
    "hu":f""

    },
    ("קראה"):{
    "hi":f""
    },
    ("קראנו"):{
    "anaxnu":f""
    },
    ("קראתם"):{
    "atem":f""
    },
    ("קראתן"):{
    "aten":f""
    },
    ("קראו"):{
    "hem":f""
    },
    ("קראו"):{
    "hen":f""
    },



    "atid":{

    ("אקרא"):{
    "ani":f"",

    ("תקרא"):{
    "ata":f"",

    ("תקראי"):{
    "at":f"",

    ("יקרא"):{
    "hu":f"",

    ("תקרא"):{
    "hi":f","

    ("נקרא"):{
    "anaxnu":f"",

    ("תקראו"):{
    "atem":f"",

    ("תקראו"):{
    "aten":f"",

    ("יקראו"):{
    "hem":f"",

    ("יקראו"):{
    "hen":f"",









paal pey_nun:
"hoveh":{
("נותן",): {
"ani": f"",
"ata": f"",
"hu": f"",},

("נותנת",): {
"ani": f"",
"at": f"",
"hi": f"",},

("נותנים",): {
"anaxnu": f"",
"atem": f"",
"hem": f"",},

("נותנות",): {
"anaxnu":f"",
"aten":f"",
"hen":f"",}
}

},

"avar":{
("נתנתי",):{
"ani":f""
}
,
("נתנת",):{
"ata":f""
},
("נתנת"):{
"at":f""
},
("נתן"):{
"hu":f""

},
("נתנה"):{
"hi":f""
},
(""):{
"anaxnu":f""
},
("נתנתם"):{
"atem":f""
},
("נתנתן"):{
"aten":f""
},
("נתנו"):{
"hem":f""
},
("נתנו"):{
"hen":f""
},
}


"atid":{

("אתן"):{
"ani":f"",

("תתן"):{
"ata":f"",

("תתני"):{
"at":f"",

("יתן"):{
"hu":f"",

("תתן"):{
"hi":f","

("נתן"):{
"anaxnu":f"",

("תתנו"):{
"atem":f"",

("תתנו"):{
"aten":f"",

("יתנו"):{
"hem":f"",

("יתנו"):{
"hen":f"",





paal pey_aleph:
"hoveh":{
("אוכל",): {
"ani": f"",
"ata": f"",
"hu": f"",},

("אוכלת",): {
"ani": f"",
"at": f"",
"hi": f"",},

("אוכלים",): {
"anaxnu": f"",
"atem": f"",
"hem": f"",},

("אוכלות",): {
"anaxnu":f"",
"aten":f"",
"hen":f"",}
}

},

"avar":{
("אכלתי",):{
"ani":f""
}
,
("אכלת",):{
"ata":f""
},
("אכלת"):{
"at":f""
},
("אכל"):{
"hu":f""

},
("אכלה"):{
"hi":f""
},
("אכלנו"):{
"anaxnu":f""
},
("אכלתם"):{
"atem":f""
},
("אכלתן"):{
"aten":f""
},
("אכלו"):{
"hem":f""
},
("אכלו"):{
"hen":f""
},
}


"atid":{

("אוכל"):{
"ani":f"",

("תואכל"):{
"ata":f"",

("תואכלי"):{
"at":f"",

("יואכל"):{
"hu":f"",

("תואכל"):{
"hi":f","

("נואכל"):{
"anaxnu":f"",

("תואכלו"):{
"atem":f"",

("תואכלו"):{
"aten":f"",

("יואכלו"):{
"hem":f"",

("יואכלו"):{
"hen":f"",}










paal_ayin_vav
("גר",): {
"ani": f"{root1}{mapik}{qametz}{root3}",
"ata": f"{root1}{mapik}{qametz}{root3}",
"hu": f"{root1}{mapik}{qametz}{root3}",},

("גרה",): {
"ani": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
"at": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
"hi": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",},

("גרים",): {
"anaxnu": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",},

("גרות",): {
"anaxnu":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
"aten":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
"hen":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("גרתי",):{
"ani":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
}
,
("גרת",):{
"ata":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{qametz}"
},
("גרת"):{
"at":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{shva}"
},
("גר"):{
"hu":f"{root1}{mapik}{qametz}{root3}"

},
("גרה"):{
"hi":f"{root1}{mapik}{qametz}{root3}{qametz}{hey}"
},
("גרנו"):{
"anaxnu":f"{root1}{mapik}{patax}{root3}{shva}{nun}{shureq}"
},
("גרתם"):{
"atem":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
},
("גרתן"):{
"aten":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}"
},
("גרו"):{
"hem":f"{root1}{mapik}{qametz}{root3}{shureq}"
,
("גרו"):{
"hen":f"{root1}{mapik}{qametz}{root3}{shureq}"
},
}


"atid":{

("אגור"):{
"ani":f"{alef}{qametz}{root1}{root2}{root3}",

("תגור"):{
"ata":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}",

("תגורי"):{
"at":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{xiriq}{yod}",

("יגור"):{
"hu":f"{yod}{qametz}{root1}{root2}{root3}",

("תגור"):{
"hi":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}"

("נגור"):{
"anaxnu":f"{nun}{qametz}{root1}{root2}{root3}",

("תגורו"):{
"atem":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",

("תגורו"):{
"aten":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",

("יגורו"):{
"hem":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",

("יגורו"):{
"hen":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",}









        }}
    }
}

        atid(paal_efal) = {(0,"למד"):(1,"efal"),
                    (0, "שכב"):(1, "efal"),
                    (0, "לבש"):(1, "efal"),
                    ()}











piel_shlemim:
("מכתב",): {
"ani": f"{mem}{dagesh}{nikkud changes}{root1}{root2}{root3}",
"ata": f"{mem}{nikkud changes}{root1}{root2}{root3}",
"hu": f"{mem}{nikkud changes}{root1}{root2}{root3}",},

("מכתבת",): {
"ani": f"{mem}{dagesh}{nikkud changes}{root1}{root2}{root3}{tav}",
"at": f"{mem}{nikkud changes}{root1}{root2}{root3}{tav}",
"hi": f"{mem}{nikkud changes}{root1}{root2}{root3}{tav}",},

("מכתבים",): {
"anaxnu": f"{mem}{dagesh}{nikkud changes}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{nikkud changes}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{nikkud changes}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

("מכתבות",): {
"anaxnu":f"{mem}{dagesh}{nikkud changes}{root1}{root2}{root3}{xolam}{tav}",
"aten":f"{mem}{nikkud changes}{root1}{root2}{root3}{xolam}{tav}",
"hen":f"{mem}{nikkud changes}{root1}{root2}{root3}{xolam}{tav}",}
}


#gerate transfucer state here with nekkudot changes
},

"avar":{
("כיתבתי",):{
"ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("כיתבת",):{
"ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{qametz}"
},
("כיתבת"):{
"at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{shva}"
},
("כיתב"):{
"hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

},
("כיתבה"):{
"hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
},
("כיתבנו"):{
"anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{sh}"
},
("כיתבתם"):{
"atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
},
("כיתבתן"):{
"aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}"
},
("כיתבו"):{
"hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
("כיתבו"):{
"hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
}


"atid":{

("אכתב"):{
"ani":f"{alef}{segol}{root1}{root2}{root3}",

("תכתב"):{
"ata":f"{tav_with_mapik}{root1}{root2}{root3}",

("תכתבי"):{
"at":f"{tav_with_mapik}{root1}{root2}{root3}{xiriq}{yod}",

("יכתב"):{
"hu":f"{yod}{root1}{root2}{root3}",

("תכתב"):{
"hi":f"{tav_with_mapik}{root1}{root2}{root3}",

("נכתב"):{
"anaxnu":f"{nun}{root1}{root2}{root3}",

("תכתבו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

("תכתבו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

("יכתבו"):{
"hem":f"{yod}{root1}{root2}{root3}{shureq}",

("יכתבו"):{
"hen":f"{yod}{root1}{root2}{root3}{shureq}",}




piel_merubayim:
("משכתב",): {
"ani": f"{mem}{root1}{root2}{root3}{root4}",
"ata": f"{mem}{root1}{root2}{root3}{root4}",
"hu": f"{mem}{root1}{root2}{root3}{root4}",},

("משכתבת",): {
"ani": f"{mem}{root1}{root2}{root3}{root4}{tav}",,
"at": f"{mem}{root1}{root2}{root3}{root4}{tav}",
"hi": f"{mem}{root1}{root2}{root3}{root4}{tav}",},

("משכתבים",): {
"anaxnu": f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
"atem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
"hem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",},

("משכתבות",): {
"anaxnu": f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
"aten":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
"hen":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",}
}

},

"avar":{
("שיכתבתי",):{
"ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("שיכתבת",):{
"ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}"
},
("שיכתבת"):{
"at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}"
},
("שיכתב"):{
"hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

},
("שיכתבה"):{
"hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
},
("שיכתבנו"):{
"anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}"
},
("שיכתבתם"):{
"atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("שיכתבתן"):{
"aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("שיכתבו"):{
"hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
("שיכתבו"):{
"hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
}


"atid":{

("אשכתב"):{
"ani":f"{aleph}{root1}{root2}{root3}{root4}",

("תשכתב"):{
"ata":f"{tav_with_mapik}{root1}{root2}{root3}{root4}",

("תשכתבי"):{
"at":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{xiriq}{yod}",

("ישכתב"):{
"hu":f"{yod}{root1}{root2}{root3}{root4}",

("תשכתב"):{
"hi":f"{tav_with_mapik}{root1}{root2}{root3}{root4}"

("נשכתב"):{
"anaxnu":f"{nun}{root1}{root2}{root3}{root4}",

("תשכתבו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",

("תשכתבו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",

("ישכתבו"):{
"hem":f"{yod}{root1}{root2}{root3}{root4}{shureq}",

("ישכתבו"):{
"hen":f"{yod}{root1}{root2}{root3}{root4}{shureq}",}





piel_lamed_alef
("ממלא",): {
"ani": f"{mem}{root1}{root2}{root3}",
"ata": f"{mem}{root1}{root2}{root3}",
"hu": f"{mem}{root1}{root2}{root3}",},

("ממלאה",): {
"ani": f"{mem}{root1}{root2}{root3}{hey}",
"at": f"{mem}{root1}{root2}{root3}{hey}",
"hi": f"{mem}{root1}{root2}{root3}{hey}",},

("ממלאים",): {
"anaxnu": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

("ממלאות",): {
"anaxnu":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("מילאתי",):{
"ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("מילאת",):{
"ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}"
},
("מילאת"):{
"at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}"
},
("מילא"):{
"hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

},
("מילאה"):{
"hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
},
("מילאנו"):{
"anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}"
},
("מילאתם"):{
"atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("מילאתן"):{
"aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("מילאו"):{
"hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
("מילאו"):{
"hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
},
}


"atid":{

("אמלא"):{
"ani":f"{alef}{root1}{root2}{root3}",

("תמלא"):{
"ata":f"{tav_with_mapik}{root1}{root2}{root3}",

("תמלאי"):{
"at":f"{tav_with_mapik}{root1}{root2}{root3}{yod}",

("ימלא"):{
"hu":f"{yod}{root1}{root2}{root3}",

("תמלא"):{
"hi":f"{tav_with_mapik}{root1}{root2}{root3}"

("נמלא"):{
"anaxnu":f"{nun}{root1}{root2}{root3}",

("תמלאו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

("תמלאו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

("ימלאו"):{
"hem":f"{yod}{root1}{root2}{root3}{shureq}",

("ימלאו"):{
"hen":f"{yod}{root1}{root2}{root3}{shureq}",}



piel_lamed_hey_yod
("משנה",): {
"ani": f"{mem}{root1}{root2}{hey}",
"ata": f"{mem}{root1}{root2}{hey}",
"hu": f"{mem}{root1}{root2}{hey}",},

("משנה",): {
"ani": f"{mem}{root1}{root2}{hey}",
"at": f"{mem}{root1}{root2}{hey}",
"hi": f"{mem}{root1}{root2}{hey}",},

("משנים",): {
"anaxnu": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",},

("משנות",): {
"anaxnu":f"{mem}{root1}{root2}{xolammalei}{tav}",
"aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
"hen":f"{mem}{root1}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("שיניתי",):{
"ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}"
}
,
("שינית",):{
"ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}"
},
("שינית"):{
"at":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{shva}"
},
("שינה"):{
"hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{hey}"

},
("שינתה"):{
"hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{tav}{hey}"
},
("שינינו"):{
"anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}"
},
("שיניתם"):{
"atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
},
("שיניתן"):{
"aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
},
("שינו"):{
"hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}"
},
("שינו"):{
"hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}"
},
}


"atid":{

("אשנה"):{
"ani":f"{alef}{root1}{root2}{hey}",

("תשנה"):{
"ata":f"{tav_with_mapik}{root1}{root2}{hey}",

("תשני"):{
"at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

("ישנה"):{
"hu":f"{yod}{root1}{root2}{hey}",

("תשנה"):{
"hi":f"{tav_with_mapik}{root1}{root2}{hey}",

("נשנה"):{
"anaxnu":f"{nun}{root1}{root2}{hey}",

("תשנו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

("תשנו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

("ישנו"):{
"hem":f"{yod}{root1}{root2}{shureq}",

("ישנו"):{
"hen":f"{yod}{root1}{root2}{shureq}",}




hifil_shlemim
("מרגיש",): {
"ani": f"",
"ata": f"",
"hu": f"",},

("מרגישה",): {
"ani": f"",
"at": f"",
"hi": f"",},

("מרגישים",): {
"anaxnu": f"",
"atem": f"",
"hem": f"",},

("מרגישות",): {
"anaxnu":f"",
"aten":f"",
"hen":f"",}
}

},

"avar":{
("הרגשתי",):{
"ani":f""
}
,
("הרגשת",):{
"ata":f""
},
("הרגשת"):{
"at":f""
},
("הרגיש"):{
"hu":f""

},
("הרגישה"):{
"hi":f""
},
("הרגשנו"):{
"anaxnu":f""
},
("הרגשתם"):{
"atem":f""
},
("הרגשתן"):{
"aten":f""
},
("הרגישו"):{
"hem":f""
},
("הרגישו"):{
"hen":f""
},
}


"atid":{

("ארגיש"):{
"ani":f"{alef}{}{root1}{root2}{xiriq}{yod}{root3}",

("תרגיש"):{
"ata":f"{tav_with_mapik}{}{root1}{root2}{xiriq}{yod}{root3}",

("תרגישי"):{
"at":f"{tav_with_mapik}{}{root1}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

("ירגיש"):{
"hu":f"{yod}{root1}{root2}{xiriq}{yod}{root3}",

("תרגיש"):{
"hi":f"{tav_with_mapik}{}{root1}{root2}{xiriq}{yod}{root3}",

("נרגיש"):{
"anaxnu":f"{nun}{root1}{root2}{xiriq}{yod}{root3}",

("תרגישו"):{
"atem":f"{tav_with_mapik}{}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

("תרגישו"):{
"aten":f"{tav_with_mapik}{}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

("ירגישו"):{
"hem":f"{yod}{}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

("ירגישו"):{
"hen":f"{yod}{}{root1}{root2}{xiriq}{yod}{root3}{shureq}",}





hifil_pey_yod
("מוריד",): {
"ani": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
"ata": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
"hu": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",},

("מורידה",): {
"ani": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
"at": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
"hi": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",},

("מורידים",): {
"anaxnu": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",},

("מורידות",): {
"anaxnu":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("הורדתי",):{
"ani":f"{hey}{xolammalei}{root2}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
}
,
("הורדת",):{
"ata":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}"
},
("הורדת"):{
"at":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}"
},
("הוריד"):{
"hu":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}"

},
("הורידה"):{
"hi":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}"
},
("הורדנו"):{
"anaxnu":f"{hey}{xolammalei}{root2}{root3}{nun}{shureq}"
},
("הורדתם"):{
"atem":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הורדתן"):{
"aten":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הורידו"):{
"hem":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
},
("הורידו"):{
"hen":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
},
}


"atid":{

("אוריד"):{
"ani":f"{alef}{xolammalei}{root2}{xiriq}{yod}{root3}",

("תוריד"):{
"ata":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",

("תורידי"):{
"at":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

("יוריד"):{
"hu":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}",

("תוריד"):{
"hi":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",

("נוריד"):{
"anaxnu":f"{nun}{xolammalei}{root2}{xiriq}{yod}{root3}",

("תורידו"):{
"atem":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

("תורידו"):{
"aten":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

("יורידו"):{
"hem":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

("יורידו"):{
"hen":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",




hifil_pey_nun
("מנהיג",): {
"ani": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
"ata": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
"hu": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",

("מנהיגה",): {
"ani": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
"at": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
"hi": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",

("מנהיגים",): {
"anaxnu": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",

("מנהיגות",): {
"anaxnu":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
"aten":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
"hen":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
}

},

"avar":{
("הנהגתי",):{
"ani":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("הנהגת",):{
"ata":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{qametz}"
},
("הנהגת"):{
"at":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{shva}"
},
("הנהיג"):{
"hu":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}"

},
("הנהיגה"):{
"hi":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{hey}"
},
("הנהגנו"):{
"anaxnu":f"{hey}{xiriq}{nun}{root2}{root3}{nun}{shureq}"
},
("הנהגתם"):{
"atem":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הנהגתן"):{
"aten":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הנהיגו"):{
"hem":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
},
("הנהיגו"):{
"hen":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
},
}


"atid":{

("אנהיג"):{
"ani":f"{alef}{nun}{root2}{xiriq}{yod}{root3}",

("תנהיג"):{
"ata":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",

("תנהיגי"):{
"at":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

("ינהיג"):{
"hu":f"{yod}{nun}{root2}{xiriq}{yod}{root3}",

("תנהיג"):{
"hi":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",

("ננהיג"):{
"anaxnu":f"{nun}{nun}{root2}{xiriq}{yod}{root3}",

("תנהיגו"):{
"atem":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

("תנהיגו"):{
"aten":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

("ינהיגו"):{
"hem":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

("ינהיגו"):{
"hen":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",}





hifil_ayin_vav_yod
("מבין",): {
"ani": f"{mem}{root1}{xiriq}{yod}{root3}",
"ata": f"{mem}{root1}{xiriq}{yod}{root3}",
"hu": f"{mem}{root1}{xiriq}{yod}{root3}",},

("מבינה",): {
"ani": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
"at": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
"hi": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",},

("מבינים",): {
"anaxnu": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",},

("מבינות",): {
"anaxnu":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
"aten":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
"hen":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("הבנתי",):{
"ani":f"{hey}{root1}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("הבנת",):{
"ata":f"{hey}{root1}{root3}{tav_with_mapik}{qametz}"
},
("הבנת"):{
"at":f"{hey}{root1}{root3}{tav_with_mapik}{shva}"
},
("הבין"):{
"hu":f"{hey}{root1}{xiriq}{yod}{root3}"

},
("הבינה"):{
"hi":f"{hey}{root1}{xiriq}{yod}{root3}{hey}"
},
("הבנו"):{
"anaxnu":f"{hey}{root1}{root3}{shureq}"
},
("הבנתם"):{
"atem":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הבנתן"):{
"aten":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הבינו"):{
"hem":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
},
("הבינו"):{
"hen":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
},
}


"atid":{

("אבין"):{
"ani":f"{alef}{root2}{xiriq}{yod}{root3}",

("תבין"):{
"ata":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",

("תביני"):{
"at":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

("יבין"):{
"hu":f"{yod}{root2}{xiriq}{yod}{root3}",

("תבין"):{
"hi":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",

("נבין"):{
"anaxnu":f"{nun}{root2}{xiriq}{yod}{root3}",

("תבינו"):{
"atem":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{shureq}",

("תבינו"):{
"aten":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{shureq}",

("יבינו"):{
"hem":f"{yod}{root2}{xiriq}{yod}{root3}{shureq}",

("יבינו"):{
"hen":f"{yod}{root2}{xiriq}{yod}{root3}{shureq}",}






hifil_lamed_hey_yod
("מרצה",): {
"ani": f"{mem}{root1}{root2}{hey}",
"ata": f"{mem}{root1}{root2}{hey}",
"hu": f"{mem}{root1}{root2}{hey}",},

("מרצה",): {
"ani": f"{mem}{root1}{root2}{hey}",
"at": f"{mem}{root1}{root2}{hey}",
"hi": f"{mem}{root1}{root2}{hey}",},

("מרצים",): {
"anaxnu": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",},

("מרצות",): {
"anaxnu":f"{mem}{root1}{root2}{xolammalei}{tav}",
"aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
"hen":f"{mem}{root1}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("הרציתי",):{
"ani":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}"
}
,
("הרצית",):{
"ata":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{qametz}"
},
("הרצית"):{
"at":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{shva}"
},
("הרצה"):{
"hu":f"{hey}{root1}{root2}{hey}"

},
("הרצתה"):{
"hi":f"{hey}{root1}{root2}{tav}{hey}"
},
("הרצינו"):{
"anaxnu":f"{hey}{root1}{root2}{xiriq}{yod}{nun}{shureq}"
},
("הרציתם"):{
"atem":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
},
("הרציתן"):{
"aten":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
},
("הרצו"):{
"hem":f"{hey}{root1}{root2}{shureq}"
},
("הרצו"):{
"hen":f"{hey}{root1}{root2}{shureq}"
},
}


"atid":{

("ארצה"):{
"ani":f"{alef}{root1}{root2}{hey}",

("תרצה"):{
"ata":f"{tav_with_mapik}{root1}{root2}{hey}",

("תרצי"):{
"at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

("ירצה"):{
"hu":f"{yod}{root1}{root2}{hey}",

("תרצה"):{
"hi":f"{tav_with_mapik}{root1}{root2}{hey}",

("נרצה"):{
"anaxnu":f"{nun}{root1}{root2}{hey}",

("תרצו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

("תרצו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

("ירצו"):{
"hem":f"{yod}{root1}{root2}{shureq}",

("ירצו"):{
"hen":f"{yod}{root1}{root2}{shureq}",}




#hifil_kapolim-- ע״ע where the last letter of shoresh is same as second to last letter
("מסב",): {
"ani": f"{mem}{root1}{root2}",
"ata": f"{mem}{root1}{root2}",
"hu": f"{mem}{root1}{root2}",},

("מסיבה",): {
"ani": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
"at": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
"hi": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",},

("מסיבים",): {
"anaxnu": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",},

("מסיבות",): {
"anaxnu":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
"aten":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
"hen":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("הסבתי/הסבותי",):{
"ani":f"{hey}{root1}{root2}{tav_with_mapik}{xiriq}{yod}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{xiriq}{yod}"
}
,
("הסבות/הסבת",):{
"ata":f"{hey}{root1}{root2}{tav_with_mapik}{qametz}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{qametz}"
},
("הסבות/הסבת"):{
"at":f"{hey}{root1}{root2}{tav_with_mapik}{shva}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{shva}"
},
("הסב"):{
"hu":f"{hey}{root1}{root2}"

},
("הסבה"):{
"hi":f"{hey}{root1}{root2}{hey}"
},
("הסבנו/הסבונו"):{
"anaxnu":f"{hey}{root1}{root2}{nun}{shureq}/{hey}{root1}{root2}{xolammalei}{nun}{shureq}"
},
("הסבותם/הסבתם"):{
"atem":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{memsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{memsofit}"
},
("הסבותן/הסבתן"):{
"aten":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{nunsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{nunsofit}"
},
("הסבו"):{
"hem":f"{hey}{root1}{root2}{shureq}"
},
("הסבו"):{
"hen":f"{hey}{root1}{root2}{shureq}"
},
}


"atid":{

("אסב"):{
"ani":f"{alef}{root1}{root2}",

("תסב"):{
"ata":f"{tav_with_mapik}{root1}{root2}",

("תסבי"):{
"at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

("יסב"):{
"hu":f"{yod}{root1}{root2}",

("תסב"):{
"hi":f"{tav_with_mapik}{root1}{root2}",

("נסב"):{
"anaxnu":f"{nun}{root1}{root2}",

("תסבו"):{
"atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

("תסבו"):{
"aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

("יסבו"):{
"hem":f"{yod}{root1}{root2}{shureq}",

("יסבו"):{
"hen":f"{yod}{root1}{root2}{shureq}",}


hitpael_regil
("מתרגש",): {
"ani": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
"ata": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
"hu": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",},

("מתרגשת",): {
"ani":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
"at": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
"hi": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",},

("מתרגשים",): {
"anaxnu": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

("מתרגשות",): {
"anaxnu":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("התרגשתי",):{
"ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("התרגשת",):{
"ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{qametz}"
},
("התרגשת"):{
"at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{shva}"
},
("התרגש"):{
"hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}"

},
("התרגשה"):{
"hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{hey}"
},
("התרגשנו"):{
"anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{nun}{shureq}"
},
("התרגשתם"):{
"atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("התרגשתן"):{
"aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("התרגשו"):{
"hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{shureq}"
},
("התרגשו"):{
"hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}"
},
}


"atid":{

("אתרגש"):{
"ani":f"{alef}{tav}{root1}{root2}{root3}",

("תתרגש"):{
"ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

("תתרגשי"):{
"at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",

("יתרגש"):{
"hu":f"{yod}{tav}{root1}{root2}{root3}",

("תתרגש"):{
"hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

("נתרגש"):{
"anaxnu":f"{nun}{tav}{root1}{root2}{root3}",

("תתרגשו"):{
"atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

("תתרגשו"):{
"aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

("יתרגשו"):{
"hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",

("יתרגשו"):{
"hen":f"{yod}{tav}{root1}{root2}{root3}{shureq}",}





hitpael_samech_tav
("מסתלק",): {
"ani": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
"ata": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
"hu": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",},

("מסתלקת",): {
"ani": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
"at": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
"hi": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",},

("מסתלקים",): {
"anaxnu": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",},

("מסתלקות",): {
"anaxnu":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("הסתלקתי",):{
"ani":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("הסתלקת",):{
"ata":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{qametz}"
},
("הסתלקת"):{
"at":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{shva}"
},
("הסתלק"):{
"hu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}"

},
("הסתלקה"):{
"hi":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{hey}"
},
("הסתלקנו"):{
"anaxnu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{nun}{shureq}"
},
("הסתלקתם"):{
"atem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הסתלקתן"):{
"aten":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הסתלקו"):{
"hem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
},
("הסתלקו"):{
"hen":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
},
}


"atid":{

("אסתלק"):{
"ani":f"{alef}{samech}{tav}{root2}{root3}",

("תסתלק"):{
"ata":f"{tav_with_mapik}{samech}{tav}{root2}{root3}",

("תסתלקי"):{
"at":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{xiriq}{yod}",

("יסתלק"):{
"hu":f"{yod}{samech}{tav}{root2}{root3}",

("תסתלק"):{
"hi":f"{tav_with_mapik}{samech}{tav}{root2}{root3}"

("נסתלק"):{
"anaxnu":f"{nun}{samech}{tav}{root2}{root3}",

("תסתלקו"):{
"atem":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",

("תסתלקו"):{
"aten":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",

("יסתלקו"):{
"hem":f"{yod}{samech}{tav}{root2}{root3}{shureq}",

("יסתלקו"):{
"hen":f"{yod}{samech}{tav}{root2}{root3}{shureq}",}




hitpael_ayin_yod_vav
("מתעורר",): {
"ani": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
"ata": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
"hu": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",},

("מתעוררת",): {
"ani": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
"at": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
"hi": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",},

("מתעוררים",): {
"anaxnu": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",},

("מתעוררות",): {
"anaxnu":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("התעוררתי",):{
"ani":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("התעוררת",):{
"ata":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{qametz}"
},
("התעוררת"):{
"at":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{shva}"
},
("התעורר"):{
"hu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}"

},
("התעוררה"):{
"hi":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{hey}"
},
("התעוררנו"):{
"anaxnu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{nun}{shureq}"
},
("התעוררתם"):{
"atem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("התעוררתן"):{
"aten":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("התעוררו"):{
"hem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
},
("התעוררו"):{
"hen":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
},
}


"atid":{

("אתעורר"):{
"ani":f"{alef}{tav}{root1}{vav}{root3}{root3}",

("תתעורר"):{
"ata":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",

("תתעוררי"):{
"at":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}",

("יתעורר"):{
"hu":f"{yod}{tav}{root1}{vav}{root3}{root3}",

("תתעורר"):{
"hi":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",

("נתעורר"):{
"anaxnu":f"{nun}{tav}{root1}{vav}{root3}{root3}",

("תתעוררו"):{
"atem":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",

("תתעוררו"):{
"aten":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",

("יתעוררו"):{
"hem":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",

("יתעוררו"):{
"hen":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",}





hitpael_lamed_alef
("מתמצא",): {
"ani": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
"ata": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
"hu": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",},

("מתמצאת",): {
"ani": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
"at": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
"hi": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",},

("מתמצאים",): {
"anaxnu": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",},

("מתמצאות",): {
"anaxnu":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",}
}

},

"avar":{
("התמצאתי",):{
"ani":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}"
}
,
("התמצאת",):{
"ata":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{qametz}"
},
("התמצאת"):{
"at":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{shva}"
},
("התמצא"):{
"hu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}"

},
("התמצאה"):{
"hi":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{hey}"
},
("התמצאנו"):{
"anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{nun}{shureq}"
},
("התמצאתם"):{
"atem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}"
},
("התמצאתן"):{
"aten":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}"
},
("התמצאו"):{
"hem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
},
("התמצאו"):{
"hen":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
},
}


"atid":{

("אתמצא"):{
"ani":f"{alef}{tav}{root1}{root2}{root3}",

("תתמצא"):{
"ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

("תתמצאי"):{
"at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",

("יתמצא"):{
"hu":f"{yod}{tav}{root1}{root2}{root3}",

("תתמצא"):{
"hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

("נתמצא"):{
"anaxnu":f"{nun}{tav}{root1}{root2}{root3}",

("תתמצאו"):{
"atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

("תתמצאו"):{
"aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

("יתמצאו"):{
"hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",

("יתמצאו"):{
"hen":f{yod}{tav}{root1}{root2}{root3}{shureq}",}





hitpael_tzadi_tet
("מצטער",): {
"ani": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
"ata": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
"hu": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",},

("מצטערת",): {
"ani":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
"at": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
"hi": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",},

("מצטערים",): {
"anaxnu": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",},

("מצטערות",): {
"anaxnu":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("הצטערתי",):{
"ani":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("הצטערת",):{
"ata":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{qametz}"
},
("הצטערת"):{
"at":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{shva}"
},
("הצטער"):{
"hu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}"

},
("הצטערה"):{
"hi":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{hey}"
},
("הצטערנו"):{
"anaxnu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{nun}{shureq}"
},
("הצטערתם"):{
"atem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הצטערתן"):{
"aten":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הצטערו"):{
"hem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
},
("הצטערו"):{
"hen":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
},
}


"atid":{

("אצטער"):{
"ani":f"{alef}{tzadi}{tet}{root2}{root3}",

("תצטער"):{
"ata":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",

("תצטערי"):{
"at":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}",

("יצטער"):{
"hu":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}",

("תצטער"):{
"hi":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",

("נצטער"):{
"anaxnu":f"{nun}{xiriq}{tzadi}{tet}{root2}{root3}",

("תצטערו"):{
"atem":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

("תצטערו"):{
"aten":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

("יצטערו"):{
"hem":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

("יצטערו"):{
"hen":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",}





hitpael_zayin_dalet
("מזדקן",): {
"ani": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
"ata": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
"hu": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",},

("מזדקנת",): {
"ani": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
"at": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
"hi": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",},

("מזדקנים",): {
"anaxnu": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",},

("מזדקנות",): {
"anaxnu":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("הזדקנתי",):{
"ani":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("הזדקנת",):{
"ata":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{qametz}"
},
("הזדקנת"):{
"at":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{shva}"
},
("הזדקן"):{
"hu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}"

},
("הזדקנה"):{
"hi":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{hey}"
},
("הזדקנו"):{
"anaxnu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{nun}{shureq}"
},
("הזדקנתם"):{
"atem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("הזדקנתן"):{
"aten":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("הזדקנו"):{
"hem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
},
("הזדקנו"):{
"hen":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
},
}


"atid":{

("אזדקן"):{
"ani":f"{alef}{zayin}{dalet}{root2}{root3}",

("תזדקן"):{
"ata":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",

("תזדקני"):{
"at":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}",

("יזדקן"):{
"hu":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}",

("תזדקן"):{
"hi":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",

("נזדקן"):{
"anaxnu":f"{nun}{xiriq}{zayin}{dalet}{root2}{root3}",

("תזדקנו"):{
"atem":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

("תזדקנו"):{
"aten":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

("יזדקנו"):{
"hem":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

("יזדקנו"):{
"hen":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",}





hitpael_shin_sin_tav
("משתפר",): {
"ani": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
"ata": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
"hu": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",},

("משתפרת",): {
"ani": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
"at": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
"hi": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",},

("משתפרים",): {
"anaxnu": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",},

("משתפרות",): {
"anaxnu":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}}{tav}{root2}{root3}{xolammalei}{tav}",
"aten":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
"hen":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("השתפרתי",):{
"ani":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("השתפרת",):{
"ata":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{qametz}"
},
("השתפרת"):{
"at":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{shva}"
},
("השתפר"):{
"hu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}"

},
("השתפרה"):{
"hi":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{hey}"
},
("השתפרנו"):{
"anaxnu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{nun}{shva}"
},
("השתפרתם"):{
"atem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("השתפרתן"):{
"aten":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("השתפרו"):{
"hem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
},
("השתפרו"):{
"hen":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
},
}


"atid":{

("אשתפר"):{
"ani":f"{alef}{shin_sin}{tav}{root2}{root3}",

("תשתפר"):{
"ata":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",

("תשתפרי"):{
"at":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}",

("ישתפר"):{
"hu":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}",

("תשתפר"):{
"hi":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",

("נשתפר"):{
"anaxnu":f"{nun}{xiriq}{shin_sin}{tav}{root2}{root3}",

("תשתפרו"):{
"atem":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

("תשתפרו"):{
"aten":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

("ישתפרו"):{
"hem":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

("ישתפרו"):{
"hen":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",}


#make finite state transducer that considers if first root is shin_sin, tzadi, etc.

hitpael_lamed_hey_yod
("מתגלה",): {
"ani": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
"ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
"hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",},

("מתגלה",): {
"ani": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
"at": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
"hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",},

("מתגלים",): {
"anaxnu": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",},

("מתגלות",): {
"anaxnu":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
"aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
"hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("התגליתי",):{
"ani":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}"
}
,
("התגלית",):{
"ata":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}"
},
("התגלית"):{
"at":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{shva}"
},
("התגלה"):{
"hu":f"{hey}{xiriq}{tav}{root1}{root2}{hey}"

},
("התגלתה"):{
"hi":f"{hey}{xiriq}{tav}{root1}{root2}{tav}{hey}"
},
("התגלינו"):{
"anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{nun}{shureq}"
},
("התגליתם"):{
"atem":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
},
("התגליתן"):{
"aten":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
},
("התגלו"):{
"hem":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
},
("התגלו"):{
"hen":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
},
}


"atid":{

("אתגלה"):{
"ani":f"{alef}{tav}{root1}{root2}{hey}",

("תתגלה"):{
"ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",

("תתגלי"):{
"at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{xiriq}{yod}",

("יתגלה"):{
"hu":f"{yod}{xiriq}{tav}{root1}{root2}{hey}",

("תתגלה"):{
"hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",

("נתגלה"):{
"anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{hey}",

("תתגלו"):{
"atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",

("תתגלו"):{
"aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",

("יתגלו"):{
"hem":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}",

("יתגלו"):{
"hen":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}",}



hitpael_merubayim
("מתבלבל",): {
"ani": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
"ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
"hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",},

("מתבלבלת",): {
"ani": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
"at": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
"hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",},

("מתבלבלים",): {
"anaxnu": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
"atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
"hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",},

("מתבלבלות",): {
"anaxnu":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
"aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
"hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",}
}

},

"avar":{
("התבלבלתי",):{
"ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{xiriq}{yod}"
}
,
("התבלבלת",):{
"ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{qametz}"
},
("התבלבלת"):{
"at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{shva}"
},
("התבלבל"):{
"hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}"

},
("התבלבלה"):{
"hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{hey}"
},
("התבלבלנו"):{
"anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{nun}{shureq}"
},
("התבלבלתם"):{
"atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{memsofit}"
},
("התבלבלתן"):{
"aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{nunsofit}"
},
("התבלבלו"):{
"hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
},
("התבלבלו"):{
"hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
},
}


"atid":{

("אתבלבל"):{
"ani":f"{alef}{tav}{root1}{root2}{root3}{root4}",

("תתבלבל"):{
"ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",

("תתבלבלי"):{
"at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}",

("יתבלבל"):{
"hu":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}",

("תתבלבל"):{
"hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",

("נתבלבל"):{
"anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{root3}{root4}",

("תתבלבלו"):{
"atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

("תתבלבלו"):{
"aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

("יתבלבלו"):{
"hem":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

("יתבלבלו"):{
"hen":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",}



##maybe write a regex for basic vowel patterns for hoveh avar and atid told in regards to root configuration

nifal_shlemim
("נכנס",): {
"ani": f"{nun}{xiriq}{root1}{root2}{root3}",
"ata": f"{nun}{xiriq}{root1}{root2}{root3}",
"hu": f"{nun}{xiriq}{root1}{root2}{root3}",},

("נכנסת",): {
"ani": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
"at": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
"hi": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",},

("נכנסים",): {
"anaxnu": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"atem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
"hem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

("נכנסות",): {
"anaxnu":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
"aten":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
"hen":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",}
}

},

"avar":{
("ניכנסתי",):{
"ani":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("ניכנסת",):{
"ata":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{qametz}"
},
("ניכנסת"):{
"at":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{shva}"
},
("ניכנס"):{
"hu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}"

},
("ניכנסה"):{
"hi":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{hey}"
},
("ניכנסנו"):{
"anaxnu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{nun}{shureq}"
},
("ניכנסתם"):{
"atem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("ניכנסתן"):{
"aten":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("ניכנסו"):{
"hem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
},
("ניכנסו"):{
"hen":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
},
}


"atid":{

("אכנס"):{
"ani":f"{alef}{root1}{root2}{root3}",

("תיכנס"):{
"ata":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",

("תיכנסי"):{
"at":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{xiriq}{yod}",

("ייכנס"):{
"hu":f"{yod}{yod}{root1}{root2}{root3}",

("תיכנס"):{
"hi":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",

("ניכנס"):{
"anaxnu":f"{nun}{yod}{root1}{root2}{root3}",

("תיכנסו"):{
"atem":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",

("תיכנסו"):{
"aten":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",

("ייכנסו"):{
"hem":f"{yod}{yod}{root1}{root2}{root3}{shureq}",

("ייכנסו"):{
"hen":f"{yod}{yod}{root1}{root2}{root3}{shureq}",}



nifal_pey_yod
("נולד",): {
"ani": f"{nun}{xolammalei}{root1}{root2}",
"ata": f"{nun}{xolammalei}{root1}{root2}",
"hu": f"{nun}{xolammalei}{root1}{root2}",},

("נולדת",): {
"ani": f"{nun}{xolammalei}{root1}{root2}{tav}",
"at": f"{nun}{xolammalei}{root1}{root2}{tav}",
"hi": f"{nun}{xolammalei}{root1}{root2}{tav}",},

("נולדים",): {
"anaxnu": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",},

("נולדות",): {
"anaxnu":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
"aten":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
"hen":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("נולדתי",):{
"ani":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
}
,
("נולדת",):{
"ata":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}"
},
("נולדת"):{
"at":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}"
},
("נולד"):{
"hu":f"{nun}{xolammalei}{root2}{root3}"

},
("נולדה"):{
"hi":f"{nun}{xolammalei}{root2}{root3}{hey}"
},
("נולדנו"):{
"anaxnu":f"{nun}{xolammalei}{root2}{root3}{nun}{shureq}"
},
("נולדתם"):{
"atem":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
},
("נולדתן"):{
"aten":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
},
("נולדו"):{
"hem":f"{nun}{xolammalei}{root2}{root3}{shureq}"
},
("נולדו"):{
"hen":f"{nun}{xolammalei}{root2}{root3}{shureq}"
},
}


"atid":{

("אוולד"):{
"ani":f"",

("תיוולד"):{
"ata":f"",

("תיוולדי"):{
"at":f"",

("ייוולד"):{
"hu":f"",

("תיוולד"):{
"hi":f","

("ניוולד"):{
"anaxnu":f"",

("תיוולדו"):{
"atem":f"",

("תיוולדו"):{
"aten":f"",

("ייוולדו"):{
"hem":f"",

("ייוולדו "):{
"hen":f"",}



nifal_lamed_hey_yod
("נראה",): {
"ani": f"{nun}{xiriq}{root1}{root2}{hey}",
"ata": f"{nun}{xiriq}{root1}{root2}{hey}",
"hu": f"{nun}{xiriq}{root1}{root2}{hey}",},

("נראית",): {
"ani": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
"at": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
"hi":f"{nun}{xiriq}{root1}{root2}{yod}{tav}",},

("נראים",): {
"anaxnu": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
"atem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
"hem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",},

("נראות",): {
"anaxnu":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
"aten":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
"hen":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",}
}

},

"avar":{
("נראיתי",):{
"ani":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}"
}
,
("נראית",):{
"ata":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{qametz}"
},
("נראית"):{
"at":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{shva}"
},
("נראה"):{
"hu":f"{nun}{xiriq}{root1}{root2}{hey}"

},
("נראתה"):{
"hi":f"{nun}{xiriq}{root1}{root2}{tav}{hey}"
},
("נראינו"):{
"anaxnu":f"{nun}{xiriq}{root1}{root2}{yod}{nun}{shureq}"
},
("נראיתם"):{
"atem":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{memsofit}"
},
("נראיתן"):{
"aten":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{nunsofit}"
},
("נראו"):{
"hem":f"{nun}{xiriq}{root1}{root2}{shureq}"
},
("נראו"):{
"hen":f"{nun}{xiriq}{root1}{root2}{shureq}"
},
}


"atid":{

("איראה"):{
"ani":f"",

("תיראה"):{
"ata":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",

("תיראי"):{
"at":f"{tav_with_mapik}{yod}{root1}{root2}{xiriq}{yod}",

("ייראה"):{
"hu":f"{yod}{yod}{root1}{root2}{hey}",

("תיראה"):{
"hi":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",

("ניראה"):{
"anaxnu":f"{nun}{yod}{root1}{root2}{hey}",

("תיראו"):{
"atem":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",

("תיראו"):{
"aten":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",

("ייראו"):{
"hem":f"{yod}{yod}{root1}{root2}{shureq}",

("ייראו"):{
"hen":f"{yod}{yod}{root1}{root2}{shureq}",}


nifal_lamed_alef
("נמצא",): {
"ani": f"{nun}{xiriq}{root1}{root2}{alef}",
"ata": f"{nun}{xiriq}{root1}{root2}{alef}",
"hu": f"{nun}{xiriq}{root1}{root2}{alef}",},

("נמצאת",): {
"ani": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
"at": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
"hi": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",},

("נמצאים",): {
"anaxnu": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"atem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"hem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",},

("נמצאות",): {
"anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
"aten":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
"hen":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",}
}

},

"avar":{
("נמצאתי",):{
"ani":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}"
}
,
("נמצאצת",):{
"ata":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{qametz}"
},
("נמצאת"):{
"at":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{shva}"
},
("נמצא"):{
"hu":f"{nun}{xiriq}{root1}{root2}{alef}"

},
("נמצאה"):{
"hi":f"{nun}{xiriq}{root1}{root2}{alef}{hey}"
},
("נמצאנו"):{
"anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{nun}{shureq}"
},
("נמצאתם"):{
"atem":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}"
},
("נמצאתן"):{
"aten":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}"
},
("נמצאו"):{
"hem":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
},
("נמצאו"):{
"hen":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
},
}


"atid":{

("אימצא"):{
"ani":f"",

("תימצא"):{
"ata":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

("תימצאי"):{
"at":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{xiriq}{yod}",

("יימצא"):{
"hu":f"{yod}{yod}{root1}{root2}{alef}",

("תימצא"):{
"hi":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

("נימצא"):{
"anaxnu":f"{nun}{yod}{root1}{root2}{alef}",

("תימצאו"):{
"atem":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

("תימצאו"):{
"aten":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

("יימצאו"):{
"hem":f"{yod}{yod}{root1}{root2}{alef}{shureq}",

("יימצאו"):{
"hen":f"{yod}{yod}{root1}{root2}{alef}{shureq}",

alef = "U+05D0"
nunsofit = "U+05DF"
memsofit = "U+05DD"
yod = "U+05D9"
nun = "U+05E0"
hey = "U+05D4"
tav_with_mapik = "U+05EA U+05BC"
vav = "U+05D5"
tav = "U+05EA"



shin_sin = "U+05E9"
tzadi = "U+05E6"
dalet = "U+05D3"
tet = "U+05D8"
samech = "U+05E1"
zayin = "U+05D6"


dagesh = "U+05BC"
mapik = ""
xiriq = "U+05B4"
qametz = "U+05B8"
segol = "U+05B6"
shureq = "U+05D5, U+05BC"
xolammalei = "U+05D5, U+05B9"
xolam = ""
patax = "U+05B7"
shva = "U+05B0"
tzerei = "U+05B5"


pual
("מכותב",): {
"ani": f"{nun}{xiriq}{root1}{root2}{alef}",
"ata": f"{nun}{xiriq}{root1}{root2}{alef}",
"hu": f"{nun}{xiriq}{root1}{root2}{alef}",},

("מכותבת",): {
"ani": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
"at": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
"hi": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",},

("מכותבים",): {
"anaxnu": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"atem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
"hem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",},

("מכותבות",): {
"anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
"aten":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
"hen":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",}
}

},

"avar":{
("כיו",):{
"ani":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}"
}
,
("נמצאצת",):{
"ata":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{qametz}"
},
("נמצאת"):{
"at":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{shva}"
},
("נמצא"):{
"hu":f"{nun}{xiriq}{root1}{root2}{alef}"

},
("נמצאה"):{
"hi":f"{nun}{xiriq}{root1}{root2}{alef}{hey}"
},
("נמצאנו"):{
"anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{nun}{shureq}"
},
("נמצאתם"):{
"atem":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}"
},
("נמצאתן"):{
"aten":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}"
},
("נמצאו"):{
"hem":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
},
("נמצאו"):{
"hen":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
},
}


"atid":{

("אימצא"):{
"ani":f"",

("תימצא"):{
"ata":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

("תימצאי"):{
"at":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{xiriq}{yod}",

("יימצא"):{
"hu":f"{yod}{yod}{root1}{root2}{alef}",

("תימצא"):{
"hi":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

("נימצא"):{
"anaxnu":f"{nun}{yod}{root1}{root2}{alef}",

("תימצאו"):{
"atem":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

("תימצאו"):{
"aten":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

("יימצאו"):{
"hem":f"{yod}{yod}{root1}{root2}{alef}{shureq}",

("יימצאו"):{
"hen":f"{yod}{yod}{root1}{root2}{alef}{shureq}",

hufal


#look up regex with hebrew letters, also use checker for input for shoresh to make sure its correct and if not then send back an error
#this is the place to put the business logic for all of the conjugations (can be functions or state machines, which would be used in the route handlers)
#do everything in hebrew for the conjugation part- variable names should be english and variables should be hebrew-- string should not be mixed value
#first write conjugations without nekudot and then go back later -- conjugate first

@app.route('/conjugate', methods = ['POST']) #can use state machines in the route handlers
def conjugate():
    shoresh = request.json['shoresh']
    binyan = request.json['binyan']
    zman = request.json['zman']

    #this is where call functions that you define above

    return jsonify({"shoresh":shoresh, "binyan":binyan, "zman":zman})

@app.route('/parse', methods = ['POST'])
def parse():
    return 'think about what variables i want to create below def'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
