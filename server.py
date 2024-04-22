# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import re

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/conjugations', methods=['GET'])
def get_conjugations():
    verb = request.args.get('verb')
    conjugations = conjugate_verb(verb)
    return jsonify(conjugations)

if __name__ == '__main__':
    app.run(debug=True)



#try to get to import all of the files into one dictionary




#anin= ani nekeva
#ani = both zachar or nekeva
#aniz = ani zachar

#mishkalim below with each binyan
#consider to use regex instead of a bunch of dictionaries in consideration of efal and efol

pealim = {

"paal": {
    "shlemim":{
        "hoveh":{

            "aniz": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
            "ata": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
            "hu": f"{root1}{xolammalei}{root2}{tzerei}{root3}",

            "anin": f"{root1}{olammalei}{root2}{segol}{root3}{segol}{tav}",
            "at": f"{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
            "hi": f"{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",

            "anaxnuz": f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",

            "anaxnun":f"{root1}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
            "aten":f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{tav}",
            "hen":f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{tav}",
        },

        "avar":{
            "כתבתי":{
            "ani":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "כתבת":{
            "ata":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}"
            },
            "כתבת":{
            "at":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}"
            },
            "כתב":{
            "hu":f"{root1}{qametz}{root2}{patax}{root3}"

            },
            "כתבה":{
            "hi":f"{root1}{qametz}{root2}{shva}{root3}{qametz}{hey}"
            },
            "כתבנו":{
            "anaxnu":f"{root1}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}"
            },
            "כתבתם":{
            "atem":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
            },
            "כתבתן":{
            "aten":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
            },
            "כתבו":{
            "hem":f"{root1}{qametz}{root2}{shva}{root3}{shureq}"
            },
            "כתבו":{
            "hen":f"{root1}{qametz}{root2}{shva}{root3}{shureq}"
            },



        "atid":{

            "efal":{
                "אבלע":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{patax}{root3}",

                "תבלע":{
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{patax}{root3}",

                "תבלעי":{
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",

                "יבלע":{
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{patax}{root3}",

                "תבלע":{
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",

                "נבלע":{
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{patax}{root3}",

                "תבלעו":{
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "תבלעו":{
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "יבלעו":{
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "יבלעו":{
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",




            "efol":{
                "אכתוב":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{xolammalei}{root3}",

                "תכתוב":{
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

                "תכתבי":{
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",

                "יכתוב":{
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

                "תכתוב":{
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

                "נכתוב":{
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",

                "תכתבו":{
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "תכתבו":{
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "יכתבו":{
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",

                "יכתבו":{
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",


    "lamed_hey_yod":{
        "hoveh":{
             "קונה":{
              "aniz": f"{root1}{xolammalei}{root2}{segol}{hey}",
              "ata": f"{root1}{xolammalei}{root2}{segol}{hey}",
              "hu": f"{root1}{xolammalei}{root2}{segol}{hey}",},

              "קונה":{
              "anin": f"{root1}{xolammalei}{root2}{qametz}{hey}",
              "at": f"{root1}{xolammalei}{root2}{qametz}{hey}",
              "hi": f"{root1}{xolammalei}{root2}{qametz}{hey}",},

              "קונים":{
              "anaxnuz": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
              "atem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
              "hem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",},

              "קונות":{
              "anaxnun":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
              "aten":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
              "hen":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",}
              }

              },

        "avar":{
          "קניתי":{
          "ani":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}"
          }
          ,
          "קנית":{
          "ata":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}"
          },
          "קנית":{
          "at":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{shva}"
          },
          "קנה":{
          "hu":f"{root1}{qametz}{root2}{qametz}{hey}"

          },
          "קנתה":{
          "hi":f"{root1}{qametz}{root2}{shva}{tav}{qametz}{hey}"
          },
          "קנינו":{
          "anaxnu":f"{root1}{qametz}{root2}{xiriq}{yod}{nun}{shureq}"
          },
          "קניתם":{
          "atem":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
          },
          "קניתן":{
          "aten":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
          },
          "קנו":{
          "hem":f"{root1}{qametz}{root2}{shureq}"
          },
          "קנו":{
          "hen":f"{root1}{qametz}{root2}{shureq}"
          },



      "atid":{

          "אקנה":{
          "ani":f"{alef}{segol}{root1}{shva}{root2}{segol}{hey}",

          "תקנה":{
          "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",

          "תקני":{
          "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xiriq}{yod}",

          "יקנה":{
          "hu":f"{yod}{xiriq}{root1}{shva}{root2}{segol}{hey}",

          "תקנה":{
          "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",

          "נקנה":{
          "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{segol}{hey}",

          "תקנו":{
          "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",

          "תקנו":{
          "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",

          "יקנו":{
          "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shureq}",

          "יקנו":{
          "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shureq}",






    "pey_yod":{

        "hoveh":{
          "יורד":{
          "aniz": f"{yod}{xolammalei}{root2}{tzerei}{root3}",
          "ata": f"{yod}{xolammalei}{root2}{tzerei}{root3}",
          "hu": f"{yod}{xolammalei}{root2}{tzerei}{root3}",},

          "יורדת":{
          "anin": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
          "at": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
          "hi": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",},

          "יורדים":{
          "anaxnuz": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
          "atem": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
          "hem": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",},

          "יורדות":{
          "anaxnun":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
          "aten":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
          "hen":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",}
          }

          },

        "avar":{
          "ירדתי":{
          "ani":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
          }
          ,
          "ירדת":{
          "ata":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}"
          },
          "ירדת":{
          "at":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}",
          },
          "ירד":{
          "hu":f"{yod}{qametz}{root2}{patax}{root3}"

          },
          "ירדה":{
          "hi":f"{yod}{qametz}{root2}{shva}{root3}{qametz}{hey}"
          },
          "ירדנו":{
          "anaxnu":f"{yod}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}"
          },
          "ירדתם":{
          "atem":f"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{memsofit}"
          },
          "ירדתן":{
          "aten":f"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{nunsofit}"
          },
          "ירדו":{
          "hem":f"{yod}{qametz}{root2}{shva}{root3}{shureq}"
          },
          "ירדו":{
          "hen":f"{yod}{qametz}{root2}{shva}{root3}{shureq}"
          },



        "atid":{

          "ארד":{
          "ani":f"{alef}{tzerei}{root2}{tzerei}{root3}",

          "תרד":{
          "ata":f"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",

          "תרדי":{
          "at":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{xiriq}{yod}",

          "ירד":{
          "hu":f"{yod}{tzerei}{root2}{tzerei}{root3}",

          "תרד":{
          "hi":f"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",

          "נרד":{
          "anaxnu":f"{nun}{tzerei}{root2}{tzerei}{root3}",

          "תרדו":{
          "atem":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",

          "תרדו":{
          "aten":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",

          "ירדו":{
          "hem":f"{yod}{tzerei}{root2}{shva}{root3}{shureq}",

          "ירדו":{
          "hen":f"{yod}{tzerei}{root2}{shva}{root3}{shureq}",





    "lamed_alef":{
        "hoveh":{
          "קורא":{
          "aniz": f"{root1}{xolammalei}{root2}{tzerei}{alef}",
          "ata": f"{root1}{xolammalei}{root2}{tzerei}{alef}",
          "hu": f"{root1}{xolammalei}{root2}{tzerei}{alef}",},

          "קוראת":{
          "anin": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
          "at": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
          "hi": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",},

          "קוראים":{
          "anaxnuz": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
          "atem": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
          "hem": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",},

          "קוראות":{
          "anaxnun":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
          "aten":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
          "hen":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",}
          }

          },

        "avar":{
          "קראתי":{
          "ani":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{xiriq}{yod}"
          }
          ,
          "קראת":{
          "ata":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{qametz}"
          },
          "קראת":{
          "at":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{shva}"
          },
          "קרא":{
          "hu":f"{root1}{qametz}{root2}{qametz}{alef}"

          },
          "קראה":{
          "hi":f"{root1}{qametz}{root2}{shva}{alef}{qametz}{hey}"
          },
          "קראנו":{
          "anaxnu":f"{root1}{qametz}{root2}{qametz}{alef}{nun}{shureq}"
          },
          "קראתם":{
          "atem":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{memsofit}"
          },
          "קראתן":{
          "aten":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{nunsofit}"
          },
          "קראו":{
          "hem":f"{root1}{qametz}{root2}{shva}{alef}{shureq}"
          },
          "קראו":{
          "hen":f"{root1}{qametz}{root2}{shva}{alef}{shureq}"
          },



        "atid":{

          "אקרא":{
          "ani":f"{alef}{segol}{root1}{shva}{root2}{qametz}{alef}",

          "תקרא":{
          "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",

          "תקראי":{
          "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{xiriq}{yod}",

          "יקרא":{
          "hu":f"{yod}{xiriq}{root1}{shva}{root2}{qametz}{alef}",

          "תקרא":{
          "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",

          "נקרא":{
          "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{qametz}{alef}",

          "תקראו":{
          "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",

          "תקראו":{
          "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",

          "יקראו":{
          "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",

          "יקראו":{
          "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",









    "pey_nun":{
        "hoveh":{
          "נותן":{
          "aniz": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
          "ata": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
          "hu": f"{root1}{xolammalei}{root2}{tzerei}{root3}",},

          "נותנת":{
          "anin": f"",
          "at": f"",
          "hi": f"",},

          "נותנים":{
          "anaxnuz": f"",
          "atem": f"",
          "hem": f"",},

          "נותנות":{
          "anaxnun":f"",
          "aten":f"",
          "hen":f"",}
          }

          },

        "avar":{
          "נתנתי":{
          "ani":f""
          }
          ,
          "נתנת":{
          "ata":f""
          },
          "נתנת":{
          "at":f""
          },
          "נתן":{
          "hu":f""

          },
          "נתנה":{
          "hi":f""
          },
          "":{
          "anaxnu":f""
          },
          "נתנתם":{
          "atem":f""
          },
          "נתנתן":{
          "aten":f""
          },
          "נתנו":{
          "hem":f""
          },
          "נתנו":{
          "hen":f""
          },



        "atid":{

          "אתן":{
          "ani":f"{alef}{root2}{root3}",

          "תתן":{
          "ata":f"{tav_with_mapik}{root2}{root3}",

          "תתני":{
          "at":f"{tav_with_mapik}{root2}{root3}{xiriq}{yod}",

          "יתן":{
          "hu":f"{yod}{root2}{root3}",

          "תתן":{
          "hi":f"{tav_with_mapik}{root2}{root3}",

          "נתן":{
          "anaxnu":f"{nun}{root2}{root3}",

          "תתנו":{
          "atem":f"{tav_with_mapik}{root2}{root3}{shureq}",

          "תתנו":{
          "aten":f"{tav_with_mapik}{root2}{root3}{shureq}",

          "יתנו":{
          "hem":f"{yod}{root2}{root3}{shureq}",

          "יתנו":{
          "hen":f"{yod}{root2}{root3}{shureq}",




    "pey_aleph":{
        "hoveh":{
          "אוכל":{
          "aniz": f"{alef}{xolammalei}{root2}{root3}",
          "ata": f"",
          "hu": f"",

          "אוכלת":{
          "anin": f"{alef}{xolammalei}{root2}{root3}{tav}",
          "at": f"{alef}{xolammalei}{root2}{root3}{tav}",
          "hi": f"{alef}{xolammalei}{root2}{root3}{tav}",},

          "אוכלים":{
          "anaxnuz": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
          "atem": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
          "hem": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",},

          "אוכלות":{
          "anaxnun":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
          "aten":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
          "hen":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",}
          }

          },

        "avar":{
          "אכלתי":{
          "ani":f"{alef}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
          }
          ,
          "אכלת":{
          "ata":f"{alef}{root2}{root3}{tav_with_mapik}{qametz}"
          },
          "אכלת":{
          "at":f"{alef}{root2}{root3}{tav_with_mapik}{shva}"
          },
          "אכל":{
          "hu":f"{alef}{root2}{root3}"

          },
          "אכלה":{
          "hi":f"{alef}{root2}{root3}{hey}"
          },
          "אכלנו":{
          "anaxnu":f"{alef}{root2}{root3}{nun}{shureq}"
          },
          "אכלתם":{
          "atem":f"{alef}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
          },
          "אכלתן":{
          "aten":f"{alef}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
          },
          "אכלו":{
          "hem":f"{alef}{root2}{root3}{shureq}"
          },
          "אכלו":{
          "hen":f"{alef}{root2}{root3}{shureq}"
          },


        "atid":{

          "אוכל":{
          "ani":f"{alef}{xolammalei}{alef}{root2}{root3}",

          "תואכל":{
          "ata":f"{tav}{xolammalei}{alef}{root2}{root3}",

          "תואכלי":{
          "at":f"{tav}{xolammalei}{alef}{root2}{root3}{xiriq}{yod}",

          "יואכל":{
          "hu":f"{yod}{xolammalei}{alef}{root2}{root3}",

          "תואכל":{
          "hi":f"{tav}{xolammalei}{alef}{root2}{root3}",

          "נואכל":{
          "anaxnu":f"{nun}{xolammalei}{alef}{root2}{root3}",

          "תואכלו":{
          "atem":f"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",

          "תואכלו":{
          "aten":f"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",

          "יואכלו":{
          "hem":f"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",

          "יואכלו":{
          "hen":f"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",










    "ayin_vav":{
        "hoveh":{
          "גר":{
          "aniz": f"{root1}{mapik}{qametz}{root3}",
          "ata": f"{root1}{mapik}{qametz}{root3}",
          "hu": f"{root1}{mapik}{qametz}{root3}",},

          "גרה":{
          "anin": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
          "at": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
          "hi": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",},

          "גרים":{
          "anaxnuz": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
          "atem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
          "hem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",},

          "גרות":{
          "anaxnun":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
          "aten":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
          "hen":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",}
          }

          },

        "avar":{
          "גרתי":{
          "ani":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
          }
          ,
          "גרת":{
          "ata":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{qametz}"
          },
          "גרת":{
          "at":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{shva}"
          },
          "גר":{
          "hu":f"{root1}{mapik}{qametz}{root3}"

          },
          "גרה":{
          "hi":f"{root1}{mapik}{qametz}{root3}{qametz}{hey}"
          },
          "גרנו":{
          "anaxnu":f"{root1}{mapik}{patax}{root3}{shva}{nun}{shureq}"
          },
          "גרתם":{
          "atem":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
          },
          "גרתן":{
          "aten":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}"
          },
          "גרו":{
          "hem":f"{root1}{mapik}{qametz}{root3}{shureq}"
          ,
          "גרו":{
          "hen":f"{root1}{mapik}{qametz}{root3}{shureq}"
          },



        "atid":{

          "אגור":{
          "ani":f"{alef}{qametz}{root1}{root2}{root3}",

          "תגור":{
          "ata":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}",

          "תגורי":{
          "at":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{xiriq}{yod}",

          "יגור":{
          "hu":f"{yod}{qametz}{root1}{root2}{root3}",

          "תגור":{
          "hi":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}",

          "נגור":{
          "anaxnu":f"{nun}{qametz}{root1}{root2}{root3}"},

          "תגורו":{
          "atem":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",

          "תגורו":{
          "aten":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",

          "יגורו":{
          "hem":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",

          "יגורו":{
          "hen":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",



"piel":{
    "shlemim":{
        "hoveh":{
            "מכתב":{
            "aniz": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}",
            "ata": f"{mem}{nikkudchanges}{root1}{root2}{root3}",
            "hu": f"{mem}{nikkudchanges}{root1}{root2}{root3}",},

            "מכתבת":{
            "anin": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{tav}",
            "at": f"{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",
            "hi": f"{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",},

            "מכתבים":{
            "anaxnuz": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "מכתבות":{
            "anaxnun":f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
            "aten":f"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
            "hen":f"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",}
            }


#gerate transfucer state here with nekkudot changes
},

        "avar":{
            "כיתבתי":{
            "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "כיתבת":{
            "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{qametz}"
            },
            "כיתבת":{
            "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{shva}"
            },
            "כיתב":{
            "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

            },
            "כיתבה":{
            "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
            },
            "כיתבנו":{
            "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{sh}"
            },
            "כיתבתם":{
            "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{memsofit}"
            },
            "כיתבתן":{
            "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}"
            },
            "כיתבו":{
            "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },
            "כיתבו":{
            "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },



        "atid":{

            "אכתב":{
            "ani":f"{alef}{segol}{root1}{root2}{root3}",

            "תכתב":{
            "ata":f"{tav_with_mapik}{root1}{root2}{root3}",

            "תכתבי":{
            "at":f"{tav_with_mapik}{root1}{root2}{root3}{xiriq}{yod}",

            "יכתב":{
            "hu":f"{yod}{root1}{root2}{root3}",

            "תכתב":{
            "hi":f"{tav_with_mapik}{root1}{root2}{root3}",

            "נכתב":{
            "anaxnu":f"{nun}{root1}{root2}{root3}",

            "תכתבו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

            "תכתבו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

            "יכתבו":{
            "hem":f"{yod}{root1}{root2}{root3}{shureq}",

            "יכתבו":{
            "hen":f"{yod}{root1}{root2}{root3}{shureq}",




    "merubayim":{
        "hoveh":{
            "משכתב":{
            "aniz": f"{mem}{root1}{root2}{root3}{root4}",
            "ata": f"{mem}{root1}{root2}{root3}{root4}",
            "hu": f"{mem}{root1}{root2}{root3}{root4}",},

            "משכתבת":{
            "anin": f"{mem}{root1}{root2}{root3}{root4}{tav}",
            "at": f"{mem}{root1}{root2}{root3}{root4}{tav}",
            "hi": f"{mem}{root1}{root2}{root3}{root4}{tav}",},

            "משכתבים":{
            "anaxnuz": f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
            "atem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
            "hem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",},

            "משכתבות":{
            "anaxnun": f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            "aten":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            "hen":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "שיכתבתי":{
            "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "שיכתבת":{
            "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "שיכתבת":{
            "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "שיכתב":{
            "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

            },
            "שיכתבה":{
            "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
            },
            "שיכתבנו":{
            "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}"
            },
            "שיכתבתם":{
            "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "שיכתבתן":{
            "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "שיכתבו":{
            "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },
            "שיכתבו":{
            "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },



        "atid":{

            "אשכתב":{
            "ani":f"{aleph}{root1}{root2}{root3}{root4}",

            "תשכתב":{
            "ata":f"{tav_with_mapik}{root1}{root2}{root3}{root4}",

            "תשכתבי":{
            "at":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{xiriq}{yod}",

            "ישכתב":{
            "hu":f"{yod}{root1}{root2}{root3}{root4}",

            "תשכתב":{
            "hi":f"{tav_with_mapik}{root1}{root2}{root3}{root4}",

            "נשכתב":{
            "anaxnu":f"{nun}{root1}{root2}{root3}{root4}",

            "תשכתבו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",

            "תשכתבו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",

            "ישכתבו":{
            "hem":f"{yod}{root1}{root2}{root3}{root4}{shureq}",

            "ישכתבו":{
            "hen":f"{yod}{root1}{root2}{root3}{root4}{shureq}",





    "lamed_alef":{
        "hoveh":{
            "ממלא": {
            "aniz": f"{mem}{root1}{root2}{root3}",
            "ata": f"{mem}{root1}{root2}{root3}",
            "hu": f"{mem}{root1}{root2}{root3}",},

            "ממלאה": {
            "anin": f"{mem}{root1}{root2}{root3}{hey}",
            "at": f"{mem}{root1}{root2}{root3}{hey}",
            "hi": f"{mem}{root1}{root2}{root3}{hey}",},

            "ממלאים": {
            "anaxnuz": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "ממלאות": {
            "anaxnun":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "מילאתי":{
            "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "מילאת":{
            "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "מילאת":{
            "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "מילא":{
            "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}"

            },
            "מילאה":{
            "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}"
            },
            "מילאנו":{
            "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}"
            },
            "מילאתם":{
            "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "מילאתן":{
            "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "מילאו":{
            "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },
            "מילאו":{
            "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },



        "atid":{

            "אמלא":{
            "ani":f"{alef}{root1}{root2}{root3}",

            "תמלא":{
            "ata":f"{tav_with_mapik}{root1}{root2}{root3}",

            "תמלאי":{
            "at":f"{tav_with_mapik}{root1}{root2}{root3}{yod}",

            "ימלא":{
            "hu":f"{yod}{root1}{root2}{root3}",

            "תמלא":{
            "hi":f"{tav_with_mapik}{root1}{root2}{root3}",

            "נמלא":{
            "anaxnu":f"{nun}{root1}{root2}{root3}",

            "תמלאו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

            "תמלאו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",

            "ימלאו":{
            "hem":f"{yod}{root1}{root2}{root3}{shureq}",

            "ימלאו":{
            "hen":f"{yod}{root1}{root2}{root3}{shureq}",



    "lamed_hey_yod":{
        "hoveh":{
            "משנה": {
            "aniz": f"{mem}{root1}{root2}{hey}",
            "ata": f"{mem}{root1}{root2}{hey}",
            "hu": f"{mem}{root1}{root2}{hey}",},

            "משנה": {
            "anin": f"{mem}{root1}{root2}{hey}",
            "at": f"{mem}{root1}{root2}{hey}",
            "hi": f"{mem}{root1}{root2}{hey}",},

            "משנים": {
            "anaxnuz": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",},

            "משנות": {
            "anaxnun":f"{mem}{root1}{root2}{xolammalei}{tav}",
            "aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
            "hen":f"{mem}{root1}{root2}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "שיניתי":{
            "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "שינית":{
            "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}"
            },
            "שינית":{
            "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{shva}"
            },
            "שינה":{
            "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{hey}"

            },
            "שינתה":{
            "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{tav}{hey}"
            },
            "שינינו":{
            "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}"
            },
            "שיניתם":{
            "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
            },
            "שיניתן":{
            "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
            },
            "שינו":{
            "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}"
            },
            "שינו":{
            "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}"
            },



        "atid":{

            "אשנה":{
            "ani":f"{alef}{root1}{root2}{hey}",

            "תשנה":{
            "ata":f"{tav_with_mapik}{root1}{root2}{hey}",

            "תשני":{
            "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

            "ישנה":{
            "hu":f"{yod}{root1}{root2}{hey}",

            "תשנה":{
            "hi":f"{tav_with_mapik}{root1}{root2}{hey}",

            "נשנה":{
            "anaxnu":f"{nun}{root1}{root2}{hey}",

            "תשנו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

            "תשנו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

            "ישנו":{
            "hem":f"{yod}{root1}{root2}{shureq}",

            "ישנו":{
            "hen":f"{yod}{root1}{root2}{shureq}",



"hifil":{
    "shlemim":{
        "hoveh":{
            "מרגיש": {
            "aniz": f"",
            "ata": f"",
            "hu": f"",},

            "מרגישה": {
            "anin": f"",
            "at": f"",
            "hi": f"",},

            "מרגישים": {
            "anaxnuz": f"",
            "atem": f"",
            "hem": f"",},

            "מרגישות": {
            "anaxnun":f"",
            "aten":f"",
            "hen":f"",}
            }

            },

        "avar":{
            "הרגשתי":{
            "ani":f""
            }
            ,
            "הרגשת":{
            "ata":f""
            },
            "הרגשת":{
            "at":f""
            },
            "הרגיש":{
            "hu":f""

            },
            "הרגישה":{
            "hi":f""
            },
            "הרגשנו":{
            "anaxnu":f""
            },
            "הרגשתם":{
            "atem":f""
            },
            "הרגשתן":{
            "aten":f""
            },
            "הרגישו":{
            "hem":f""
            },
            "הרגישו":{
            "hen":f""
            },



        "atid":{

            "ארגיש":{
            "ani":f"{alef}{root1}{root2}{xiriq}{yod}{root3}",

            "תרגיש":{
            "ata":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",

            "תרגישי":{
            "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

            "ירגיש":{
            "hu":f"{yod}{root1}{root2}{xiriq}{yod}{root3}",

            "תרגיש":{
            "hi":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",

            "נרגיש":{
            "anaxnu":f"{nun}{root1}{root2}{xiriq}{yod}{root3}",

            "תרגישו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

            "תרגישו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

            "ירגישו":{
            "hem":f"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",

            "ירגישו":{
            "hen":f"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",





    "pey_yod":{
        "hoveh":{
            "מוריד": {
            "aniz": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
            "ata": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
            "hu": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",},

            "מורידה": {
            "anin": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
            "at": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
            "hi": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",},

            "מורידים": {
            "anaxnuz": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",},

            "מורידות": {
            "anaxnun":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "הורדתי":{
            "ani":f"{hey}{xolammalei}{root2}{root3}{shva}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הורדת":{
            "ata":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "הורדת":{
            "at":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "הוריד":{
            "hu":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}"

            },
            "הורידה":{
            "hi":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}"
            },
            "הורדנו":{
            "anaxnu":f"{hey}{xolammalei}{root2}{root3}{nun}{shureq}"
            },
            "הורדתם":{
            "atem":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "הורדתן":{
            "aten":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הורידו":{
            "hem":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            },
            "הורידו":{
            "hen":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            },



        "atid":{

            "אוריד":{
            "ani":f"{alef}{xolammalei}{root2}{xiriq}{yod}{root3}",

            "תוריד":{
            "ata":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",

            "תורידי":{
            "at":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

            "יוריד":{
            "hu":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}",

            "תוריד":{
            "hi":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",

            "נוריד":{
            "anaxnu":f"{nun}{xolammalei}{root2}{xiriq}{yod}{root3}",

            "תורידו":{
            "atem":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

            "תורידו":{
            "aten":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

            "יורידו":{
            "hem":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",

            "יורידו":{
            "hen":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",




    "pey_nun":{
        "hoveh":{
            "מנהיג": {
            "aniz": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
            "ata": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
            "hu": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",

            "מנהיגה": {
            "anin": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
            "at": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
            "hi": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",

            "מנהיגים": {
            "anaxnuz": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",

            "מנהיגות": {
            "anaxnun":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            }

            },

        "avar":{
            "הנהגתי":{
            "ani":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הנהגת":{
            "ata":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "הנהגת":{
            "at":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "הנהיג":{
            "hu":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}"

            },
            "הנהיגה":{
            "hi":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{hey}"
            },
            "הנהגנו":{
            "anaxnu":f"{hey}{xiriq}{nun}{root2}{root3}{nun}{shureq}"
            },
            "הנהגתם":{
            "atem":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "הנהגתן":{
            "aten":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הנהיגו":{
            "hem":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            },
            "הנהיגו":{
            "hen":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            },



        "atid":{

            "אנהיג":{
            "ani":f"{alef}{nun}{root2}{xiriq}{yod}{root3}",

            "תנהיג":{
            "ata":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",

            "תנהיגי":{
            "at":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",

            "ינהיג":{
            "hu":f"{yod}{nun}{root2}{xiriq}{yod}{root3}",

            "תנהיג":{
            "hi":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",

            "ננהיג":{
            "anaxnu":f"{nun}{nun}{root2}{xiriq}{yod}{root3}",

            "תנהיגו":{
            "atem":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

            "תנהיגו":{
            "aten":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

            "ינהיגו":{
            "hem":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",

            "ינהיגו":{
            "hen":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",





    "ayin_vav_yod":{
        "hoveh":{
            "מבין": {
            "aniz": f"{mem}{root1}{xiriq}{yod}{root3}",
            "ata": f"{mem}{root1}{xiriq}{yod}{root3}",
            "hu": f"{mem}{root1}{xiriq}{yod}{root3}",},

            "מבינה": {
            "anin": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
            "at": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
            "hi": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",},

            "מבינים": {
            "anaxnuz": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",},

            "מבינות": {
            "anaxnun":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",}
            }

            },

    "avar":{
        "הבנתי":{
        "ani":f"{hey}{root1}{root3}{tav_with_mapik}{xiriq}{yod}"
        }
        ,
        "הבנת":{
        "ata":f"{hey}{root1}{root3}{tav_with_mapik}{qametz}"
        },
        "הבנת":{
        "at":f"{hey}{root1}{root3}{tav_with_mapik}{shva}"
        },
        "הבין":{
        "hu":f"{hey}{root1}{xiriq}{yod}{root3}"

        },
        "הבינה":{
        "hi":f"{hey}{root1}{xiriq}{yod}{root3}{hey}"
        },
        "הבנו":{
        "anaxnu":f"{hey}{root1}{root3}{shureq}"
        },
        "הבנתם":{
        "atem":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
        },
        "הבנתן":{
        "aten":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
        },
        "הבינו":{
        "hem":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
        },
        "הבינו":{
        "hen":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
        },



    "atid":{

        "אבין":{
        "ani":f"{alef}{root2}{xiriq}{yod}{root3}"
        },
        "תבין":{
        "ata":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}"
        },
        "תביני":{
        "at":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{xiriq}{yod}"
        },
        "יבין":{
        "hu":f"{yod}{root2}{xiriq}{yod}{root3}"
        },
        "תבין":{
        "hi":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}"
        },
        "נבין":{
        "anaxnu":f"{nun}{root2}{xiriq}{yod}{root3}"
        },
        "תבינו":{
        "atem":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{shureq}"
        },
        "תבינו":{
        "aten":f"{tav}{root2}{xiriq}{root3}{shureq}"
        },
        "יבינו":{
        "hem":f"{yod}{root2}{xiriq}{root3}{shureq}"
        },
        "יבינו":{
        "hen":f"{yod}{root2}{xiriq}{yod}{root3}{shureq}"
        }





    "lamed_hey_yod":
        "hoveh":
            "מרצה": {
            "aniz": f"{mem}{root1}{root2}{hey}",
            "ata": f"{mem}{root1}{root2}{hey}",
            "hu": f"{mem}{root1}{root2}{hey}",},

            "מרצה": {
            "anin": f"{mem}{root1}{root2}{hey}",
            "at": f"{mem}{root1}{root2}{hey}",
            "hi": f"{mem}{root1}{root2}{hey}",},

            "מרצים": {
            "anaxnuz": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",},

            "מרצות": {
            "anaxnun":f"{mem}{root1}{root2}{xolammalei}{tav}",
            "aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
            "hen":f"{mem}{root1}{root2}{xolammalei}{tav}",}
            }

            },

    "avar":{
        "הרציתי":{
        "ani":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}"
        }
        ,
        "הרצית":{
        "ata":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{qametz}"
        },
        "הרצית":{
        "at":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{shva}"
        },
        "הרצה":{
        "hu":f"{hey}{root1}{root2}{hey}"

        },
        "הרצתה":{
        "hi":f"{hey}{root1}{root2}{tav}{hey}"
        },
        "הרצינו":{
        "anaxnu":f"{hey}{root1}{root2}{xiriq}{yod}{nun}{shureq}"
        },
        "הרציתם":{
        "atem":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
        },
        "הרציתן":{
        "aten":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
        },
        "הרצו":{
        "hem":f"{hey}{root1}{root2}{shureq}"
        },
        "הרצו":{
        "hen":f"{hey}{root1}{root2}{shureq}"
        },



    "atid":{

        "ארצה":{
        "ani":f"{alef}{root1}{root2}{hey}",

        "תרצה":{
        "ata":f"{tav_with_mapik}{root1}{root2}{hey}",

        "תרצי":{
        "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

        "ירצה":{
        "hu":f"{yod}{root1}{root2}{hey}",

        "תרצה":{
        "hi":f"{tav_with_mapik}{root1}{root2}{hey}",

        "נרצה":{
        "anaxnu":f"{nun}{root1}{root2}{hey}",

        "תרצו":{
        "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

        "תרצו":{
        "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

        "ירצו":{
        "hem":f"{yod}{root1}{root2}{shureq}",

        "ירצו":{
        "hen":f"{yod}{root1}{root2}{shureq}",




#hifil_kapolim-- ע״ע where the last letter of shoresh is same as second to last letter
    "kapolim":
        "hoveh":
            "מסב": {
            "aniz": f"{mem}{root1}{root2}",
            "ata": f"{mem}{root1}{root2}",
            "hu": f"{mem}{root1}{root2}",},

            "מסיבה": {
            "anin": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
            "at": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
            "hi": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",},

            "מסיבים": {
            "anaxnuz": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",},

            "מסיבות": {
            "anaxnun":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
            "aten":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
            "hen":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "הסבתי/הסבותי":{
            "ani":f"{hey}{root1}{root2}{tav_with_mapik}{xiriq}{yod}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הסבות/הסבת":{
            "ata":f"{hey}{root1}{root2}{tav_with_mapik}{qametz}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{qametz}"
            },
            "הסבות/הסבת":{
            "at":f"{hey}{root1}{root2}{tav_with_mapik}{shva}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{shva}"
            },
            "הסב":{
            "hu":f"{hey}{root1}{root2}"

            },
            "הסבה":{
            "hi":f"{hey}{root1}{root2}{hey}"
            },
            "הסבנו/הסבונו":{
            "anaxnu":f"{hey}{root1}{root2}{nun}{shureq}/{hey}{root1}{root2}{xolammalei}{nun}{shureq}"
            },
            "הסבותם/הסבתם":{
            "atem":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{memsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{memsofit}"
            },
            "הסבותן/הסבתן":{
            "aten":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{nunsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הסבו":{
            "hem":f"{hey}{root1}{root2}{shureq}"
            },
            "הסבו":{
            "hen":f"{hey}{root1}{root2}{shureq}"
            },



        "atid":{

            "אסב":{
            "ani":f"{alef}{root1}{root2}",

            "תסב":{
            "ata":f"{tav_with_mapik}{root1}{root2}",

            "תסבי":{
            "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",

            "יסב":{
            "hu":f"{yod}{root1}{root2}",

            "תסב":{
            "hi":f"{tav_with_mapik}{root1}{root2}",

            "נסב":{
            "anaxnu":f"{nun}{root1}{root2}",

            "תסבו":{
            "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",

            "תסבו":{
            "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",

            "יסבו":{
            "hem":f"{yod}{root1}{root2}{shureq}",

            "יסבו":{
            "hen":f"{yod}{root1}{root2}{shureq}",


"hitpael":
    "shlemim":
        "hoveh":
            "מתרגש": {
            "aniz": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
            "ata": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
            "hu": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",},

            "מתרגשת": {
            "anin":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
            "at": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
            "hi": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",},

            "מתרגשים": {
            "anaxnuz": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "מתרגשות": {
            "anaxnun":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "התרגשתי":{
            "ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "התרגשת":{
            "ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "התרגשת":{
            "at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "התרגש":{
            "hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}"

            },
            "התרגשה":{
            "hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{hey}"
            },
            "התרגשנו":{
            "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{nun}{shureq}"
            },
            "התרגשתם":{
            "atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "התרגשתן":{
            "aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "התרגשו":{
            "hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{shureq}"
            },
            "התרגשו":{
            "hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}"
            },



        "atid":{

            "אתרגש":{
            "ani":f"{alef}{tav}{root1}{root2}{root3}",

            "תתרגש":{
            "ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

            "תתרגשי":{
            "at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",

            "יתרגש":{
            "hu":f"{yod}{tav}{root1}{root2}{root3}",

            "תתרגש":{
            "hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

            "נתרגש":{
            "anaxnu":f"{nun}{tav}{root1}{root2}{root3}",

            "תתרגשו":{
            "atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

            "תתרגשו":{
            "aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

            "יתרגשו":{
            "hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",

            "יתרגשו":{
            "hen":f"{yod}{tav}{root1}{root2}{root3}{shureq}",




    "samech_tav":
        "hoveh":
            "מסתלק": {
            "aniz": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
            "ata": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
            "hu": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",},

            "מסתלקת": {
            "anin": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
            "at": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
            "hi": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",},

            "מסתלקים": {
            "anaxnuz": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "מסתלקות": {
            "anaxnun":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "הסתלקתי":{
            "ani":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הסתלקת":{
            "ata":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "הסתלקת":{
            "at":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "הסתלק":{
            "hu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}"

            },
            "הסתלקה":{
            "hi":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{hey}"
            },
            "הסתלקנו":{
            "anaxnu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{nun}{shureq}"
            },
            "הסתלקתם":{
            "atem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "הסתלקתן":{
            "aten":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הסתלקו":{
            "hem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
            },
            "הסתלקו":{
            "hen":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
            },


        "atid":{

            "אסתלק":{
            "ani":f"{alef}{samech}{tav}{root2}{root3}",

            "תסתלק":{
            "ata":f"{tav_with_mapik}{samech}{tav}{root2}{root3}",

            "תסתלקי":{
            "at":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{xiriq}{yod}",

            "יסתלק":{
            "hu":f"{yod}{samech}{tav}{root2}{root3}",

            "תסתלק":{
            "hi":f"{tav_with_mapik}{samech}{tav}{root2}{root3}"

            "נסתלק":{
            "anaxnu":f"{nun}{samech}{tav}{root2}{root3}",

            "תסתלקו":{
            "atem":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",

            "תסתלקו":{
            "aten":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",

            "יסתלקו":{
            "hem":f"{yod}{samech}{tav}{root2}{root3}{shureq}",

            "יסתלקו":{
            "hen":f"{yod}{samech}{tav}{root2}{root3}{shureq}",




    "ayin_yod_vav":
        "hoveh":
            "מתעורר": {
            "aniz": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
            "ata": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
            "hu": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",},

            "מתעוררת": {
            "anin": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
            "at": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
            "hi": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",},

            "מתעוררים": {
            "anaxnuz": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",},

            "מתעוררות": {
            "anaxnun":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "התעוררתי":{
            "ani":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "התעוררת":{
            "ata":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{qametz}"
            },
            "התעוררת":{
            "at":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{shva}"
            },
            "התעורר":{
            "hu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}"

            },
            "התעוררה":{
            "hi":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{hey}"
            },
            "התעוררנו":{
            "anaxnu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{nun}{shureq}"
            },
            "התעוררתם":{
            "atem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "התעוררתן":{
            "aten":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "התעוררו":{
            "hem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
            },
            "התעוררו":{
            "hen":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
            },



        "atid":{

            "אתעורר":{
            "ani":f"{alef}{tav}{root1}{vav}{root3}{root3}",

            "תתעורר":{
            "ata":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",

            "תתעוררי":{
            "at":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}",

            "יתעורר":{
            "hu":f"{yod}{tav}{root1}{vav}{root3}{root3}",

            "תתעורר":{
            "hi":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",

            "נתעורר":{
            "anaxnu":f"{nun}{tav}{root1}{vav}{root3}{root3}",

            "תתעוררו":{
            "atem":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",

            "תתעוררו":{
            "aten":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",

            "יתעוררו":{
            "hem":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",

            "יתעוררו":{
            "hen":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",





    "lamed_alef":
        "hoveh":
            "מתמצא": {
            "aniz": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
            "ata": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
            "hu": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",},

            "מתמצאת": {
            "anin": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
            "at": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
            "hi": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",},

            "מתמצאים": {
            "anaxnuz": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",},

            "מתמצאות": {
            "anaxnun":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "התמצאתי":{
            "ani":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "התמצאת":{
            "ata":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{qametz}"
            },
            "התמצאת":{
            "at":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{shva}"
            },
            "התמצא":{
            "hu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}"

            },
            "התמצאה":{
            "hi":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{hey}"
            },
            "התמצאנו":{
            "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{nun}{shureq}"
            },
            "התמצאתם":{
            "atem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}"
            },
            "התמצאתן":{
            "aten":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}"
            },
            "התמצאו":{
            "hem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
            },
            "התמצאו":{
            "hen":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
            },


        "atid":{

            "אתמצא":{
            "ani":f"{alef}{tav}{root1}{root2}{root3}",

            "תתמצא":{
            "ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

            "תתמצאי":{
            "at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",

            "יתמצא":{
            "hu":f"{yod}{tav}{root1}{root2}{root3}",

            "תתמצא":{
            "hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",

            "נתמצא":{
            "anaxnu":f"{nun}{tav}{root1}{root2}{root3}",

            "תתמצאו":{
            "atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

            "תתמצאו":{
            "aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",

            "יתמצאו":{
            "hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",

            "יתמצאו":{
            "hen":f"{yod}{tav}{root1}{root2}{root3}{shureq}",





    "tzadi_tet":
        "hoveh":
            "מצטער": {
            "aniz": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
            "ata": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
            "hu": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",},

            "מצטערת": {
            "anin":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
            "at": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
            "hi": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",},

            "מצטערים": {
            "anaxnuz": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "מצטערות": {
            "anaxnun":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "הצטערתי":{
            "ani":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הצטערת":{
            "ata":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "הצטערת":{
            "at":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "הצטער":{
            "hu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}"

            },
            "הצטערה":{
            "hi":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{hey}"
            },
            "הצטערנו":{
            "anaxnu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{nun}{shureq}"
            },
            "הצטערתם":{
            "atem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "הצטערתן":{
            "aten":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הצטערו":{
            "hem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            },
            "הצטערו":{
            "hen":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            },



        "atid":{

            "אצטער":{
            "ani":f"{alef}{tzadi}{tet}{root2}{root3}",

            "תצטער":{
            "ata":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",

            "תצטערי":{
            "at":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}",

            "יצטער":{
            "hu":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}",

            "תצטער":{
            "hi":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",

            "נצטער":{
            "anaxnu":f"{nun}{xiriq}{tzadi}{tet}{root2}{root3}",

            "תצטערו":{
            "atem":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

            "תצטערו":{
            "aten":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

            "יצטערו":{
            "hem":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",

            "יצטערו":{
            "hen":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",





    "zayin_dalet":
        "hoveh":
            "מזדקן": {
            "aniz": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
            "ata": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
            "hu": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",},

            "מזדקנת": {
            "anin": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
            "at": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
            "hi": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",},

            "מזדקנים": {
            "anaxnuz": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "מזדקנות": {
            "anaxnun":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "הזדקנתי":{
            "ani":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "הזדקנת":{
            "ata":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "הזדקנת":{
            "at":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "הזדקן":{
            "hu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}"

            },
            "הזדקנה":{
            "hi":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{hey}"
            },
            "הזדקנו":{
            "anaxnu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{nun}{shureq}"
            },
            "הזדקנתם":{
            "atem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "הזדקנתן":{
            "aten":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "הזדקנו":{
            "hem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            },
            "הזדקנו":{
            "hen":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            },



        "atid":{

            "אזדקן":{
            "ani":f"{alef}{zayin}{dalet}{root2}{root3}",

            "תזדקן":{
            "ata":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",

            "תזדקני":{
            "at":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}",

            "יזדקן":{
            "hu":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}",

            "תזדקן":{
            "hi":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",

            "נזדקן":{
            "anaxnu":f"{nun}{xiriq}{zayin}{dalet}{root2}{root3}",

            "תזדקנו":{
            "atem":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

            "תזדקנו":{
            "aten":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

            "יזדקנו":{
            "hem":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",

            "יזדקנו":{
            "hen":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",





    "shin_sin_tav":
        "hoveh":
            "משתפר": {
            "aniz": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
            "ata": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
            "hu": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",},

            "משתפרת": {
            "anin": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
            "at": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
            "hi": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",},

            "משתפרים": {
            "anaxnuz": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "משתפרות": {
            "anaxnun":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}}{tav}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "השתפרתי":{
            "ani":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "השתפרת":{
            "ata":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "השתפרת":{
            "at":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "השתפר":{
            "hu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}"

            },
            "השתפרה":{
            "hi":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{hey}"
            },
            "השתפרנו":{
            "anaxnu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{nun}{shva}"
            },
            "השתפרתם":{
            "atem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "השתפרתן":{
            "aten":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "השתפרו":{
            "hem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            },
            "השתפרו":{
            "hen":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            },


        "atid":{

            "אשתפר":{
            "ani":f"{alef}{shin_sin}{tav}{root2}{root3}",

            "תשתפר":{
            "ata":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",

            "תשתפרי":{
            "at":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}",

            "ישתפר":{
            "hu":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}",

            "תשתפר":{
            "hi":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",

            "נשתפר":{
            "anaxnu":f"{nun}{xiriq}{shin_sin}{tav}{root2}{root3}",

            "תשתפרו":{
            "atem":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

            "תשתפרו":{
            "aten":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

            "ישתפרו":{
            "hem":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",

            "ישתפרו":{
            "hen":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",


#make finite state transducer that considers if first root is shin_sin, tzadi, etc.

    "lamed_hey_yod":
        "hoveh":
            "מתגלה": {
            "aniz": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
            "ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
            "hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",},

            "מתגלה": {
            "anin": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
            "at": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
            "hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",},

            "מתגלים": {
            "anaxnuz": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",},

            "מתגלות": {
            "anaxnun":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
            "aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
            "hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "התגליתי":{
            "ani":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "התגלית":{
            "ata":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}"
            },
            "התגלית":{
            "at":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{shva}"
            },
            "התגלה":{
            "hu":f"{hey}{xiriq}{tav}{root1}{root2}{hey}"

            },
            "התגלתה":{
            "hi":f"{hey}{xiriq}{tav}{root1}{root2}{tav}{hey}"
            },
            "התגלינו":{
            "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{nun}{shureq}"
            },
            "התגליתם":{
            "atem":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}"
            },
            "התגליתן":{
            "aten":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}"
            },
            "התגלו":{
            "hem":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
            },
            "התגלו":{
            "hen":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
            },



        "atid":{

            "אתגלה":{
            "ani":f"{alef}{tav}{root1}{root2}{hey}",

            "תתגלה":{
            "ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",

            "תתגלי":{
            "at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{xiriq}{yod}",

            "יתגלה":{
            "hu":f"{yod}{xiriq}{tav}{root1}{root2}{hey}",

            "תתגלה":{
            "hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",

            "נתגלה":{
            "anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{hey}",

            "תתגלו":{
            "atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",

            "תתגלו":{
            "aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",

            "יתגלו":{
            "hem":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}",

            "יתגלו":{
            "hen":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}",



    "merubayim":
        "hoveh":
            "מתבלבל": {
            "aniz": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
            "ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
            "hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",},

            "מתבלבלת": {
            "anin": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
            "at": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
            "hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",},

            "מתבלבלים": {
            "anaxnuz": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
            "atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
            "hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",},

            "מתבלבלות": {
            "anaxnun":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            "aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            "hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "התבלבלתי":{
            "ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "התבלבלת":{
            "ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{qametz}"
            },
            "התבלבלת":{
            "at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{shva}"
            },
            "התבלבל":{
            "hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}"

            },
            "התבלבלה":{
            "hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{hey}"
            },
            "התבלבלנו":{
            "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{nun}{shureq}"
            },
            "התבלבלתם":{
            "atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{memsofit}"
            },
            "התבלבלתן":{
            "aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{nunsofit}"
            },
            "התבלבלו":{
            "hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            },
            "התבלבלו":{
            "hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            },



        "atid":{

            "אתבלבל":{
            "ani":f"{alef}{tav}{root1}{root2}{root3}{root4}",

            "תתבלבל":{
            "ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",

            "תתבלבלי":{
            "at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}",

            "יתבלבל":{
            "hu":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}",

            "תתבלבל":{
            "hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",

            "נתבלבל":{
            "anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{root3}{root4}",

            "תתבלבלו":{
            "atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

            "תתבלבלו":{
            "aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

            "יתבלבלו":{
            "hem":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",

            "יתבלבלו":{
            "hen":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",



##maybe write a regex for basic vowel patterns for hoveh avar and atid told in regards to root configuration

"nifal":
    "shlemim":
        "hoveh":
            "נכנס": {
            "aniz": f"{nun}{xiriq}{root1}{root2}{root3}",
            "ata": f"{nun}{xiriq}{root1}{root2}{root3}",
            "hu": f"{nun}{xiriq}{root1}{root2}{root3}",},

            "נכנסת": {
            "anin": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
            "at": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
            "hi": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",},

            "נכנסים": {
            "anaxnuz": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "atem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
            "hem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",},

            "נכנסות": {
            "anaxnun":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
            "aten":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
            "hen":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "ניכנסתי":{
            "ani":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "ניכנסת":{
            "ata":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "ניכנסת":{
            "at":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "ניכנס":{
            "hu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}"

            },
            "ניכנסה":{
            "hi":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{hey}"
            },
            "ניכנסנו":{
            "anaxnu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{nun}{shureq}"
            },
            "ניכנסתם":{
            "atem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "ניכנסתן":{
            "aten":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "ניכנסו":{
            "hem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
            },
            "ניכנסו":{
            "hen":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
            },



        "atid":{

            "אכנס":{
            "ani":f"{alef}{root1}{root2}{root3}",

            "תיכנס":{
            "ata":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",

            "תיכנסי":{
            "at":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{xiriq}{yod}",

            "ייכנס":{
            "hu":f"{yod}{yod}{root1}{root2}{root3}",

            "תיכנס":{
            "hi":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",

            "ניכנס":{
            "anaxnu":f"{nun}{yod}{root1}{root2}{root3}",

            "תיכנסו":{
            "atem":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",

            "תיכנסו":{
            "aten":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",

            "ייכנסו":{
            "hem":f"{yod}{yod}{root1}{root2}{root3}{shureq}",

            "ייכנסו":{
            "hen":f"{yod}{yod}{root1}{root2}{root3}{shureq}",



    "pey_yod":
        "hoveh"
            "נולד": {
            "aniz": f"{nun}{xolammalei}{root1}{root2}",
            "ata": f"{nun}{xolammalei}{root1}{root2}",
            "hu": f"{nun}{xolammalei}{root1}{root2}",},

            "נולדת": {
            "anin": f"{nun}{xolammalei}{root1}{root2}{tav}",
            "at": f"{nun}{xolammalei}{root1}{root2}{tav}",
            "hi": f"{nun}{xolammalei}{root1}{root2}{tav}",},

            "נולדים": {
            "anaxnuz": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",},

            "נולדות": {
            "anaxnun":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
            "aten":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
            "hen":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "נולדתי":{
            "ani":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "נולדת":{
            "ata":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}"
            },
            "נולדת":{
            "at":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}"
            },
            "נולד":{
            "hu":f"{nun}{xolammalei}{root2}{root3}"

            },
            "נולדה":{
            "hi":f"{nun}{xolammalei}{root2}{root3}{hey}"
            },
            "נולדנו":{
            "anaxnu":f"{nun}{xolammalei}{root2}{root3}{nun}{shureq}"
            },
            "נולדתם":{
            "atem":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}"
            },
            "נולדתן":{
            "aten":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}"
            },
            "נולדו":{
            "hem":f"{nun}{xolammalei}{root2}{root3}{shureq}"
            },
            "נולדו":{
            "hen":f"{nun}{xolammalei}{root2}{root3}{shureq}"
            },



        "atid":{

            "אוולד":{
            "ani":f"{alef}",

            "תיוולד":{
            "ata":f"",

            "תיוולדי":{
            "at":f"",

            "ייוולד":{
            "hu":f"",

            "תיוולד":{
            "hi":f","

            "ניוולד":{
            "anaxnu":f"",

            "תיוולדו":{
            "atem":f"",

            "תיוולדו":{
            "aten":f"",

            "ייוולדו":{
            "hem":f"",

            "ייוולדו ":{
            "hen":f"",



    "lamed_hey_yod":
        "hoveh":
            "נראה": {
            "aniz": f"{nun}{xiriq}{root1}{root2}{hey}",
            "ata": f"{nun}{xiriq}{root1}{root2}{hey}",
            "hu": f"{nun}{xiriq}{root1}{root2}{hey}",},

            "נראית": {
            "anin": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
            "at": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
            "hi":f"{nun}{xiriq}{root1}{root2}{yod}{tav}",},

            "נראים": {
            "anaxnuz": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
            "atem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
            "hem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",},

            "נראות": {
            "anaxnun":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
            "aten":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
            "hen":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "נראיתי":{
            "ani":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "נראית":{
            "ata":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{qametz}"
            },
            "נראית":{
            "at":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{shva}"
            },
            "נראה":{
            "hu":f"{nun}{xiriq}{root1}{root2}{hey}"

            },
            "נראתה":{
            "hi":f"{nun}{xiriq}{root1}{root2}{tav}{hey}"
            },
            "נראינו":{
            "anaxnu":f"{nun}{xiriq}{root1}{root2}{yod}{nun}{shureq}"
            },
            "נראיתם":{
            "atem":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{memsofit}"
            },
            "נראיתן":{
            "aten":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{nunsofit}"
            },
            "נראו":{
            "hem":f"{nun}{xiriq}{root1}{root2}{shureq}"
            },
            "נראו":{
            "hen":f"{nun}{xiriq}{root1}{root2}{shureq}"
            },


        "atid":{

            "איראה":{
            "ani":f"",

            "תיראה":{
            "ata":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",

            "תיראי":{
            "at":f"{tav_with_mapik}{yod}{root1}{root2}{xiriq}{yod}",

            "ייראה":{
            "hu":f"{yod}{yod}{root1}{root2}{hey}",

            "תיראה":{
            "hi":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",

            "ניראה":{
            "anaxnu":f"{nun}{yod}{root1}{root2}{hey}",

            "תיראו":{
            "atem":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",

            "תיראו":{
            "aten":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",

            "ייראו":{
            "hem":f"{yod}{yod}{root1}{root2}{shureq}",

            "ייראו":{
            "hen":f"{yod}{yod}{root1}{root2}{shureq}",


    "lamed_alef":
        "hoveh":
            "נמצא": {
            "aniz": f"{nun}{xiriq}{root1}{root2}{alef}",
            "ata": f"{nun}{xiriq}{root1}{root2}{alef}",
            "hu": f"{nun}{xiriq}{root1}{root2}{alef}",},

            "נמצאת": {
            "anin": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
            "at": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
            "hi": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",},

            "נמצאים": {
            "anaxnuz": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
            "atem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
            "hem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",},

            "נמצאות": {
            "anaxnun":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
            "aten":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
            "hen":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",}
            }

            },

        "avar":{
            "נמצאתי":{
            "ani":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}"
            }
            ,
            "נמצאצת":{
            "ata":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{qametz}"
            },
            "נמצאת":{
            "at":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{shva}"
            },
            "נמצא":{
            "hu":f"{nun}{xiriq}{root1}{root2}{alef}"

            },
            "נמצאה":{
            "hi":f"{nun}{xiriq}{root1}{root2}{alef}{hey}"
            },
            "נמצאנו":{
            "anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{nun}{shureq}"
            },
            "נמצאתם":{
            "atem":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}"
            },
            "נמצאתן":{
            "aten":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}"
            },
            "נמצאו":{
            "hem":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
            },
            "נמצאו":{
            "hen":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
            },



        "atid":{

            "אימצא":{
            "ani":f"",

            "תימצא":{
            "ata":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

            "תימצאי":{
            "at":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{xiriq}{yod}",

            "יימצא":{
            "hu":f"{yod}{yod}{root1}{root2}{alef}",

            "תימצא":{
            "hi":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",

            "נימצא":{
            "anaxnu":f"{nun}{yod}{root1}{root2}{alef}",

            "תימצאו":{
            "atem":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

            "תימצאו":{
            "aten":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",

            "יימצאו":{
            "hem":f"{yod}{yod}{root1}{root2}{alef}{shureq}",

            "יימצאו":{
            "hen":f"{yod}{yod}{root1}{root2}{alef}{shureq}",






#maybe make regex for pual and hufal




#hufal

#hoveh
#מוכתב
#מוכתבת
#מוכתבים
#מוכתבות

#avar
#הוכתבתי
#הוכתבת
#הוכבת
#הוכתב
#הוכתבה
#הוכתבנו
#הוכתבתם
#הוכתבתן
#הוכתבו
#הוכתבו

#atid
#אוכתב
#תוכתב
#תוכתביֿ
#יוכתב
#תוכתב
#נוכתב
#תוכתבו
ֿ#תוכתבו
#יוכתבו
#יוכתבו

#draw out fst for vowelization changes before coding it


#review purpose of fsa and how it may be applicable/not








#hufal




#look up regex with hebrew letters, also use checker for input for shoresh to make sure its correct and if not then send back an error
#this is the place to put the business logic for all of the conjugations (can be functions or state machines, which would be used in the route handlers)
#do everything in hebrew for the conjugation part- variable names should be english and variables should be hebrew-- string should not be mixed value
#first write conjugations without nekudot and then go back later -- conjugate first

#if doesnt match any then it is shlemim --> else block for the default case
mishkalim_less_specific = {

"pey_aleph": r"^\u05D0[\u05D0-\u05EA]{2}$",
"pey_yod": r"^\u05D9[\u05D0-\u05EA]{2}$",
"pey_nun": r"^\u05E0[\u05D0-\u05EA]{2}$",
"ayin_vav": r"^[\u05D0-\u05EA]\u05D5[\u05D0-\u05EA]$",
"ayin_yod": r"^[\u05D0-\u05EA]\u05D[\u05D0-\u05EA]$",
"lamed_alef": r"^[\u05D0-\u05EA][\u05D0-\u05EA]\u05DO$",
"lamed_hey_yod": r"^[\u05D0-\u05EA][\u05D0-\u05EA][\u05D9\u05E5]$",
"kapolim": r"^[\u05D0-\u05EA][\u05D0-\u05EA]\2$"

}

mishkalim_more_specific = {

"merubayim": r"^[\u05D0-\u05EA][\u05D0-\u05EA][\u05D0-\u05EA][\u05D0-\u05EA]$",
"pey_nun_ayin_vav": r"^\u05E0\u05D5[\u05D0-\u05EA]$",
"pey_nun_ayin_yod": r"^\u05E0\u05D[\u05D0-\u05EA]$"
"lamed_alef_ayin_vav": r"^\u05D5[\u05D0-\u05EA]\u05D0$",
"lamed_alef_ayin_yod": r"^\u05D[\u05D0-\u05EA]\u05D0$",
"ayin_vav_lamed_hey_yod": r"^[\u05D0-\u05EA]\u05D5[\u05D9\u05E5]$",
"ayin_yod_lamed_hey_yod": r"^[\u05D0-\u05EA]\u05D[\u05D9\u05E5]$"

}

mishkalim_hitpael = {

"shin_sin_tav": r"^\u05E9[\u05D0-\u05EA][\u05D0-\u05EA]$",
"samech_tav": r"^\u05E1[\u05D0-\u05EA][\u05D0-\u05EA]$",
"zayin_dalet": r"^\u05D6[\u05D0-\u05EA][\u05D0-\u05EA]$",
"tzadi_tet": r"^\u05E6[\u05D0-\u05EA][\u05D0-\u05EA]$"
#add all possibilities for crossover between multiple --> maybe will have to add another dict


}

special_shoreshim = {
"alef_vav_hey": r"^\u05D0\u05D5\u05D4$"

}




def detect_mishkal(shoresh, binyan):
    for mishkal, regex in special_shoreshim.items():
        if re.match(regex, shoresh):
            return mishkal
    if binyan == "hitpael":
        for mishkal, regex in mishkalim_hitpael.items():
            if re.match(regex, shoresh):
                return mishkal
    for mishkal, regex in mishkalim_more_specific.items():
        if re.match(regex, shoresh):
            return mishkal
    for mishkal, regex in mishkalim_less_specific.items():
        if re.match(regex, shoresh):
            return mishkal



#make a chat bot interface for the root #constructs would be in the value of the dictionary for them to choose from



def render_conjugate (shoresh, binyan, zman, shem_guf):
    mishkal = detect_mishkal(shoresh, binyan)
    # Handle mishkalim from pealim dictionary
    if binyan in pealim and zman in pealim[binyan] and mishkal in pealim[binyan][zman]:
        root1 = shoresh[0]
        root2 = shoresh[1]
        root3 = shoresh[2]
        root4 = shoresh[3]

        conjugation = pealim[binyan][zman][mishkal][shem_guf]
        return conjugation
    else:
        # Handle case where mishkal is not detected
        pass




alef = "u05D0",
nunsofit = "u05DF"
memsofit = "u05DD"
yod = "u05D9"
nun = "u05E0"
hey = "u05D4"
tav_with_mapik = "u05EA u05BC"
vav = "u05D5"
tav = "u05EA"

#consider otiyot sofiyot
shin_sin = "u05E9"
tzadi = "u05E6"
dalet = "u05D3"
tet = "u05D8"
samech = "u05E1"
zayin = "u05D6"


dagesh = "u05BC"
mapik = "u05BC"
xiriq = "u05B4"
qametz = "u05B8"
segol = "u05B6"
shureq = "u05D5, u05BC"
xolammalei = "u05D5, u05B9"
xolam = ""
patax = "u05B7"
shva = "u05B0"
tzerei = "u05B5"



#need to make a regex to interpret input shoresh to which mishkal

    #find the pattern from defns above to use to render the conjugated verb; actually apply shoresh to the pattern
    return ''

    #add some testing calls for here just to check once we define the render_conjugate function

#app route is the api and route functions are typically for api- application program interface
@app.route('/conjugate', methods = ['POST']) #can use state machines in the route handlers
def conjugate():
    shoresh = request.json['shoresh']
    binyan = request.json['binyan']
    zman = request.json['zman']
    shem_guf = request.json['shem_guf']

    outputword = render_conjugate(shoresh, binyan, zman, shem_guf)
    #this is where call functions that you define above

    return jsonify({"shoresh":shoresh, "binyan":binyan, "zman":zman, "outputword":outputword})

@app.route('/parse', methods = ['POST'])
def parse():
    return 'think about what variables i want to create below def'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
