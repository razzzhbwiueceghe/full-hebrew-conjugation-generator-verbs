# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import re

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


from flask import Flask, jsonify, request

app = Flask(__name__)





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
                "aniz": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "ata": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "hu": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "anin": "{root1}{olammalei}{root2}{segol}{root3}{segol}{tav}",
                "at": "{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "hi": "{root1}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "anaxnuz": "{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{root1}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
                "aten":"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{tav}",
                "hen":"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{tav}"
            },

            "avar":{
                "ani":"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":"{root1}{qametz}{root2}{patax}{root3}",
                "hi":"{root1}{qametz}{root2}{shva}{root3}{qametz}{hey}",
                "anaxnu":"{root1}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}",
                "atem":"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "hem":"{root1}{qametz}{root2}{shva}{root3}{shureq}",
                "hen":"{root1}{qametz}{root2}{shva}{root3}{shureq}",
            },

            "atid":{
                "ani":"{alef}{segol}{root1}{shva}{root2}{patax}{root3}",
                "ata":"{tav_with_mapik}{xiriq}{root1}{shva}{patax}{root3}",
                "at":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{root1}{shva}{root2}{patax}{root3}",
                "hi":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "anaxnu":"{nun}{xiriq}{root1}{shva}{root2}{patax}{root3}",
                "atem":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hem":"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hen":"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
            },


            "efol":{
                "ani":"{alef}{segol}{root1}{shva}{root2}{xolammalei}{root3}",
                "ata":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "at":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "hi":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "anaxnu":"{nun}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "atem":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hem":"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hen":"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
            },
        },

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": "{root1}{xolammalei}{root2}{segol}{hey}",
                "ata": "{root1}{xolammalei}{root2}{segol}{hey}",
                "hu": "{root1}{xolammalei}{root2}{segol}{hey}",
                "anin": "{root1}{xolammalei}{root2}{qametz}{hey}",
                "at": "{root1}{xolammalei}{root2}{qametz}{hey}",
                "hi": "{root1}{xolammalei}{root2}{qametz}{hey}",
                "anaxnuz": "{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{root1}{xolammalei}{root2}{xolammalei}{tav}",
                "aten":"{root1}{xolammalei}{root2}{xolammalei}{tav}",
                "hen":"{root1}{xolammalei}{root2}{xolammalei}{tav}"
            },

            "avar":{
                "ani":"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":"{root1}{qametz}{root2}{qametz}{hey}",
                "hi":"{root1}{qametz}{root2}{shva}{tav}{qametz}{hey}",
                "anaxnu":"{root1}{qametz}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{qametz}{root2}{shureq}",
                "hen":"{root1}{qametz}{root2}{shureq}"
            },

            "atid":{
                "ani":"{alef}{segol}{root1}{shva}{root2}{segol}{hey}",
                "ata":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "at":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "hi":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "anaxnu":"{nun}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "atem":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",
                "hem":"{yod}{xiriq}{root1}{shva}{root2}{shureq}",
                "hen":"{yod}{xiriq}{root1}{shva}{root2}{shureq}"
            },
        },

        "pey_yod":{

            "hoveh":{
                "aniz": "{yod}{xolammalei}{root2}{tzerei}{root3}",
                "ata": "{yod}{xolammalei}{root2}{tzerei}{root3}",
                "hu": "{yod}{xolammalei}{root2}{tzerei}{root3}",
                "anin": "{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "at": "{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "hi": "{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "anaxnuz": "{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
                "aten":"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
                "hen":"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":"{yod}{qametz}{root2}{patax}{root3}",
                "hi":"{yod}{qametz}{root2}{shva}{root3}{qametz}{hey}",
                "anaxnu":"{yod}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}",
                "atem":"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{yod}{qametz}{root2}{shva}{root3}{shureq}",
                "hen":"{yod}{qametz}{root2}{shva}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tzerei}{root2}{tzerei}{root3}",
                "ata":"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",
                "at":"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":"{yod}{tzerei}{root2}{tzerei}{root3}",
                "hi":"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",
                "anaxnu":"{nun}{tzerei}{root2}{tzerei}{root3}",
                "atem":"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",
                "aten":"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",
                "hem":"{yod}{tzerei}{root2}{shva}{root3}{shureq}",
                "hen":"{yod}{tzerei}{root2}{shva}{root3}{shureq}",
            }
        },

        "lamed_alef":{
            "hoveh":{
                "aniz": "{root1}{xolammalei}{root2}{tzerei}{alef}",
                "ata": "{root1}{xolammalei}{root2}{tzerei}{alef}",
                "hu": "{root1}{xolammalei}{root2}{tzerei}{alef}",
                "anin": "{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "at": "{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "hi": "{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "anaxnuz": "{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "atem": "{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "hem": "{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
                "aten":"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
                "hen":"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{root1}{qametz}{root2}{qametz}{alef}{tav}{xiriq}{yod}",
                "ata":"{root1}{qametz}{root2}{qametz}{alef}{tav}{qametz}",
                "at":"{root1}{qametz}{root2}{qametz}{alef}{tav}{shva}",
                "hu":"{root1}{qametz}{root2}{qametz}{alef}",
                "hi":"{root1}{qametz}{root2}{shva}{alef}{qametz}{hey}",
                "anaxnu":"{root1}{qametz}{root2}{qametz}{alef}{nun}{shureq}",
                "atem":"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{memsofit}",
                "aten":"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{nunsofit}",
                "hem":"{root1}{qametz}{root2}{shva}{alef}{shureq}",
                "hen":"{root1}{qametz}{root2}{shva}{alef}{shureq}"
            },

            "atid":{
                "ani":"{alef}{segol}{root1}{shva}{root2}{qametz}{alef}",
                "ata":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "at":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "hi":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "anaxnu":"{nun}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "atem":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "hem":"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "hen":"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
            }
        },

        "pey_nun":{
            "hoveh":{
                "aniz": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "ata": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "hu": "{root1}{xolammalei}{root2}{tzerei}{root3}",
                "anin": "",
                "at": "",
                "hi": "",
                "anaxnuz": "",
                "atem": "",
                "hem": "",
                "anaxnun":"",
                "aten":"",
                "hen":"",
            },

            "avar":{
                "ani":"",
                "ata":"",
                "at":"",
                "hu":"",
                "hi":"",
                "anaxnu":"",
                "atem":"",
                "aten":"",
                "hem":"",
                "hen":""
            },

            "atid":{
                "ani":"{alef}{root2}{root3}",
                "ata":"{tav_with_mapik}{root2}{root3}",
                "at":"{tav_with_mapik}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{root2}{root3}",
                "hi":"{tav_with_mapik}{root2}{root3}",
                "anaxnu":"{nun}{root2}{root3}",
                "atem":"{tav_with_mapik}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{root2}{root3}{shureq}",
                "hem":"{yod}{root2}{root3}{shureq}",
                "hen":"{yod}{root2}{root3}{shureq}",
            }
        },

        "pey_alef":{
            "hoveh":{
                "aniz": "{alef}{xolammalei}{root2}{root3}",
                "ata": "",
                "hu": "",
                "anin": "{alef}{xolammalei}{root2}{root3}{tav}",
                "at": "{alef}{xolammalei}{root2}{root3}{tav}",
                "hi": "{alef}{xolammalei}{root2}{root3}{tav}",
                "anaxnuz": "{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
                "aten":"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
                "hen":"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{alef}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{alef}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{alef}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{alef}{root2}{root3}",
                "hi":"{alef}{root2}{root3}{hey}",
                "anaxnu":"{alef}{root2}{root3}{nun}{shureq}",
                "atem":"{alef}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{alef}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{alef}{root2}{root3}{shureq}",
                "hen":"{alef}{root2}{root3}{shureq}"
            },


            "atid":{
                "ani":"{alef}{xolammalei}{alef}{root2}{root3}",
                "ata":"{tav}{xolammalei}{alef}{root2}{root3}",
                "at":"{tav}{xolammalei}{alef}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{xolammalei}{alef}{root2}{root3}",
                "hi":"{tav}{xolammalei}{alef}{root2}{root3}",
                "anaxnu":"{nun}{xolammalei}{alef}{root2}{root3}",
                "atem":"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",
                "aten":"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",
                "hem":"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",
                "hen":"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",
            }
        },

        "ayin_vav":{
            "hoveh":{
                "aniz": "{root1}{mapik}{qametz}{root3}",
                "ata": "{root1}{mapik}{qametz}{root3}",
                "hu": "{root1}{mapik}{qametz}{root3}",
                "anin": "{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "at": "{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "hi": "{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "anaxnuz": "{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
                "aten":"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
                "hen":"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":"{root1}{mapik}{qametz}{root3}",
                "hi":"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "anaxnu":"{root1}{mapik}{patax}{root3}{shva}{nun}{shureq}",
                "atem":"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{mapik}{qametz}{root3}{shureq}",
                "hen":"{root1}{mapik}{qametz}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{qametz}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{qametz}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{qametz}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{qametz}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{qametz}{root1}{root2}{root3}",
                "anaxnu":"{nun}{qametz}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "aten":"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "hem":"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "hen":"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",
            }
        },
    },

    "piel":{
        "shlemim":{
            "hoveh":{
                "aniz": "{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}",
                "ata": "{mem}{nikkudchanges}{root1}{root2}{root3}",
                "hu": "{mem}{nikkudchanges}{root1}{root2}{root3}",
                "anin": "{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "at": "{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "hi": "{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
                "aten":"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
                "hen":"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
            },

            #gerate transfucer state here with nekkudot changes

            "avar":{
                "ani":"{root1}{dagesh}{xiriq}{yod}{root2}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{sh}",
                "atem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{segol}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{root1}{root2}{root3}",
                "anaxnu":"{nun}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "hem":"{yod}{root1}{root2}{root3}{shureq}",
                "hen":"{yod}{root1}{root2}{root3}{shureq}",
            }
        },

        "merubayim":{
            "hoveh":{
                "aniz": "{mem}{root1}{root2}{root3}{root4}",
                "ata": "{mem}{root1}{root2}{root3}{root4}",
                "hu": "{mem}{root1}{root2}{root3}{root4}",
                "anin": "{mem}{root1}{root2}{root3}{root4}{tav}",
                "at": "{mem}{root1}{root2}{root3}{root4}{tav}",
                "hi": "{mem}{root1}{root2}{root3}{root4}{tav}",
                "anaxnuz": "{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "atem":  "{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "hem":  "{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "anaxnun": "{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "aten":"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "hen":"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}",
                "atem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{root3}{root4}",
                "ata":"{tav_with_mapik}{root1}{root2}{root3}{root4}",
                "at":"{tav_with_mapik}{root1}{root2}{root3}{root4}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}{root3}{root4}",
                "hi":"{tav_with_mapik}{root1}{root2}{root3}{root4}",
                "anaxnu":"{nun}{root1}{root2}{root3}{root4}",
                "atem":"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",
                "hem":"{yod}{root1}{root2}{root3}{root4}{shureq}",
                "hen":"{yod}{root1}{root2}{root3}{root4}{shureq}"
            }
        },

        "lamed_alef":{
            "hoveh":{
                "aniz": "{mem}{root1}{root2}{root3}",
                "ata": "{mem}{root1}{root2}{root3}",
                "hu": "{mem}{root1}{root2}{root3}",
                "anin": "{mem}{root1}{root2}{root3}{hey}",
                "at": "{mem}{root1}{root2}{root3}{hey}",
                "hi": "{mem}{root1}{root2}{root3}{hey}",
                "anaxnuz": "{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}",
                "atem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{root1}{root2}{root3}{yod}",
                "hu":"{yod}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{root1}{root2}{root3}",
                "anaxnu":"{nun}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "hem":"{yod}{root1}{root2}{root3}{shureq}",
                "hen":"{yod}{root1}{root2}{root3}{shureq}",
            }
        },

        "lamed_hey_yod":{
            "hoveh":{
                "aniz": "{mem}{root1}{root2}{hey}",
                "ata": "{mem}{root1}{root2}{hey}",
                "hu": "{mem}{root1}{root2}{hey}",
                "anin": "{mem}{root1}{root2}{hey}",
                "at": "{mem}{root1}{root2}{hey}",
                "hi": "{mem}{root1}{root2}{hey}",
                "anaxnuz": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{root1}{root2}{xolammalei}{tav}",
                "aten":"{mem}{root1}{root2}{xolammalei}{tav}",
                "hen":"{mem}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{hey}",
                "hi":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{tav}{hey}",
                "anaxnu":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}",
                "atem":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}",
                "hen":"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}",
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{hey}",
                "ata":"{tav_with_mapik}{root1}{root2}{hey}",
                "at":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}{hey}",
                "hi":"{tav_with_mapik}{root1}{root2}{hey}",
                "anaxnu":"{nun}{root1}{root2}{hey}",
                "atem":"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":"{yod}{root1}{root2}{shureq}",
                "hen":"{yod}{root1}{root2}{shureq}",
            }
        }
    },

    "hifil":{
        "shlemim":{
            "hoveh":{
                "aniz": "",
                "ata": "",
                "hu": "",
                "anin": "",
                "at": "",
                "hi": "",
                "anaxnuz": "",
                "atem": "",
                "hem": "",
                "anaxnun":"",
                "aten":"",
                "hen":""
            },

            "avar":{
                "ani":"",
                "ata":"",
                "at":"",
                "hu":"",
                "hi":"",
                "anaxnu":"",
                "atem":"",
                "aten":"",
                "hem":"",
                "hen":""
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{xiriq}{yod}{root3}",
                "ata":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",
                "at":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}{xiriq}{yod}{root3}",
                "hi":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",
                "anaxnu":"{nun}{root1}{root2}{xiriq}{yod}{root3}",
                "atem":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
            }
        },

        "pey_yod":{
            "hoveh":{
                "aniz": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "ata": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hu": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "anin": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "at": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "hi": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xolammalei}{root2}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hi":"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnu":"{hey}{xolammalei}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "ata":"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "at":"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hi":"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "anaxnu":"{nun}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "atem":"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "pey_nun":{
            "hoveh":{
                "aniz": "{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "ata": "{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "hu": "{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "anin": "{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "at": "{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "hi": "{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": "{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}",
                "hi":"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{nun}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{nun}{root2}{xiriq}{yod}{root3}",
                "ata":"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",
                "at":"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":"{yod}{nun}{root2}{xiriq}{yod}{root3}",
                "hi":"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",
                "anaxnu":"{nun}{nun}{root2}{xiriq}{yod}{root3}",
                "atem":"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "ayin_vav_yod":{
            "hoveh":{
                "aniz": "{mem}{root1}{xiriq}{yod}{root3}",
                "ata": "{mem}{root1}{xiriq}{yod}{root3}",
                "hu": "{mem}{root1}{xiriq}{yod}{root3}",
                "anin": "{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "at": "{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "hi": "{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": "{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{root1}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{root1}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{root1}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{root1}{xiriq}{yod}{root3}",
                "hi":"{hey}{root1}{xiriq}{yod}{root3}{hey}",
                "anaxnu":"{hey}{root1}{root3}{shureq}",
                "atem":"{hey}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{root2}{xiriq}{yod}{root3}",
                "ata":"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",
                "at":"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":"{yod}{root2}{xiriq}{yod}{root3}",
                "hi":"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",
                "anaxnu":"{nun}{root2}{xiriq}{yod}{root3}",
                "atem":"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":"{tav}{root2}{xiriq}{root3}{shureq}",
                "hem":"{yod}{root2}{xiriq}{root3}{shureq}",
                "hen":"{yod}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": "{mem}{root1}{root2}{hey}",
                "ata": "{mem}{root1}{root2}{hey}",
                "hu": "{mem}{root1}{root2}{hey}",
                "anin": "{mem}{root1}{root2}{hey}",
                "at": "{mem}{root1}{root2}{hey}",
                "hi": "{mem}{root1}{root2}{hey}",
                "anaxnuz": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{root1}{root2}{xolammalei}{tav}",
                "aten":"{mem}{root1}{root2}{xolammalei}{tav}",
                "hen":"{mem}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{root1}{root2}{yod}{tav_with_mapik}{qametz}",
                "at":"{hey}{root1}{root2}{yod}{tav_with_mapik}{shva}",
                "hu":"{hey}{root1}{root2}{hey}",
                "hi":"{hey}{root1}{root2}{tav}{hey}",
                "anaxnu":"{hey}{root1}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{root1}{root2}{shureq}",
                "hen":"{hey}{root1}{root2}{shureq}"
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{hey}",
                "ata":"{tav_with_mapik}{root1}{root2}{hey}",
                "at":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}{hey}",
                "hi":"{tav_with_mapik}{root1}{root2}{hey}",
                "anaxnu":"{nun}{root1}{root2}{hey}",
                "atem":"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":"{yod}{root1}{root2}{shureq}",
                "hen":"{yod}{root1}{root2}{shureq}"
            }
        },

#hifil_kapolim-- ע״ע where the last letter of shoresh is same as second to last letter
        "kapolim": {
            "hoveh": {
                "aniz": "{mem}{root1}{root2}",
                "ata": "{mem}{root1}{root2}",
                "hu": "{mem}{root1}{root2}",
                "anin": "{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "at": "{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "hi": "{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "anaxnuz": "{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
                "aten":"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
                "hen":"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{root1}{root2}{tav_with_mapik}{xiriq}{yod}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{root1}{root2}{tav_with_mapik}{qametz}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{qametz}",
                "at":"{hey}{root1}{root2}{tav_with_mapik}{shva}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{shva}",
                "hu":"{hey}{root1}{root2}",
                "hi":"{hey}{root1}{root2}{hey}",
                "anaxnu":"{hey}{root1}{root2}{nun}{shureq}/{hey}{root1}{root2}{xolammalei}{nun}{shureq}",
                "atem":"{hey}{root1}{root2}{tav_with_mapik}{segol}{memsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{root1}{root2}{tav_with_mapik}{segol}{nunsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{root1}{root2}{shureq}",
                "hen":"{hey}{root1}{root2}{shureq}"
            },

            "atid":{
                "ani":"{alef}{root1}{root2}",
                "ata":"{tav_with_mapik}{root1}{root2}",
                "at":"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":"{yod}{root1}{root2}",
                "hi":"{tav_with_mapik}{root1}{root2}",
                "anaxnu":"{nun}{root1}{root2}",
                "atem":"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":"{yod}{root1}{root2}{shureq}",
                "hen":"{yod}{root1}{root2}{shureq}"
            }
        }
    },

    "hitpael": {
        "shlemim": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "ata": "{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "hu": "{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "anin":"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "at": "{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "hi": "{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tav}{root1}{root2}{root3}",
                "hi":"{hey}{xiriq}{tav}{root1}{root2}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{tav}{root1}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tav}{root1}{root2}{root3}{shureq}",
                "hen":"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}"
            },

            "atid":{
                "ani":"{alef}{tav}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{tav}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "anaxnu":"{nun}{tav}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "hem":"{yod}{tav}{root1}{root2}{root3}{shureq}",
                "hen":"{yod}{tav}{root1}{root2}{root3}{shureq}",
            }
        },

        "samech_tav": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "ata": "{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "hu": "{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "anin": "{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "at": "{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "hi": "{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{samech}{tav}{root2}{root3}",
                "hi":"{hey}{xiriq}{samech}{tav}{root2}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{samech}{tav}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}",
                "hen":"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
            },


            "atid":{
                "ani":"{alef}{samech}{tav}{root2}{root3}",
                "ata":"{tav_with_mapik}{samech}{tav}{root2}{root3}",
                "at":"{tav_with_mapik}{samech}{tav}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{samech}{tav}{root2}{root3}",
                "hi":"{tav_with_mapik}{samech}{tav}{root2}{root3}",
                "anaxnu":"{nun}{samech}{tav}{root2}{root3}",
                "atem":"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",
                "hem":"{yod}{samech}{tav}{root2}{root3}{shureq}",
                "hen":"{yod}{samech}{tav}{root2}{root3}{shureq}"
            }
        },

        "ayin_yod_vav": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "ata": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "hu": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "anin": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "at": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "hi": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "hi":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hen":"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tav}{root1}{vav}{root3}{root3}",
                "ata":"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",
                "at":"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}",
                "hu":"{yod}{tav}{root1}{vav}{root3}{root3}",
                "hi":"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",
                "anaxnu":"{nun}{tav}{root1}{vav}{root3}{root3}",
                "atem":"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "aten":"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hem":"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hen":"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",
            }
        },

        "lamed_alef": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "ata": "{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "hu": "{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "anin": "{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "at": "{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "hi": "{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "anaxnuz": "{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tav}{root1}{root2}{alef}",
                "hi":"{hey}{xiriq}{tav}{root1}{root2}{alef}{hey}",
                "anaxnu":"{hey}{xiriq}{tav}{root1}{root2}{alef}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}",
                "hen":"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tav}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{tav}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "anaxnu":"{nun}{tav}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "hem":"{yod}{tav}{root1}{root2}{root3}{shureq}",
                "hen":"{yod}{tav}{root1}{root2}{root3}{shureq}",
            }
        },

        "tzadi_tet": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "ata": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hu": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "anin":"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "at": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "hi": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hi":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hen":"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tzadi}{tet}{root2}{root3}",
                "ata":"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",
                "at":"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hi":"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",
                "anaxnu":"{nun}{xiriq}{tzadi}{tet}{root2}{root3}",
                "atem":"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hem":"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hen":"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            }
        },

        "zayin_dalet": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "ata": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hu": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "anin": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "at": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "hi": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hi":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{nun}{shureq}",
                "atem":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hen":"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{zayin}{dalet}{root2}{root3}",
                "ata":"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",
                "at":"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hi":"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",
                "anaxnu":"{nun}{xiriq}{zayin}{dalet}{root2}{root3}",
                "atem":"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hem":"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hen":"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            }
        },

        "shin_sin_tav": {
            "hoveh": {
                "aniz": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "ata": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hu": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "anin": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "at": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "hi": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "anaxnuz": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "atem": "{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "aten":"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "hen":"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hi":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{hey}",
                "anaxnu":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{nun}{shva}",
                "atem":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hen":"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{shin_sin}{tav}{root2}{root3}",
                "ata":"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "at":"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hi":"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "anaxnu":"{nun}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "atem":"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hem":"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hen":"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            }
        },


        #make finite state transducer that considers if first root is shin_sin, tzadi, etc.

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "ata": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "hu": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "anin": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "at": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "hi": "{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "anaxnuz": "{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
                "aten":"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
                "hen":"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tav}{root1}{root2}{hey}",
                "hi":"{hey}{xiriq}{tav}{root1}{root2}{tav}{hey}",
                "anaxnu":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tav}{root1}{root2}{shureq}",
                "hen":"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tav}{root1}{root2}{hey}",
                "ata":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",
                "at":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{tav}{root1}{root2}{hey}",
                "hi":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",
                "anaxnu":"{nun}{xiriq}{tav}{root1}{root2}{hey}",
                "atem":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",
                "hem":"{yod}{xiriq}{tav}{root1}{root2}{shureq}",
                "hen":"{yod}{xiriq}{tav}{root1}{root2}{shureq}"
            }
        },

        "merubayim": {
            "hoveh": {
                "aniz": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "ata": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hu": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "anin": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "at": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "hi": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "anaxnuz": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "atem": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "hem": "{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "anaxnun":"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "aten":"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "hen":"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{qametz}",
                "at":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{shva}",
                "hu":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hi":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{hey}",
                "anaxnu":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{nun}{shureq}",
                "atem":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hen":"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            },

            "atid":{
                "ani":"{alef}{tav}{root1}{root2}{root3}{root4}",
                "ata":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "at":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}",
                "hu":"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hi":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "anaxnu":"{nun}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "atem":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "aten":"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hem":"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hen":"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            }
        }
    },

    ##maybe write a regex for basic vowel patterns for hoveh avar and atid told in regards to root configuration

    "nifal": {
        "shlemim": {
            "hoveh": {
                "aniz": "{nun}{xiriq}{root1}{root2}{root3}",
                "ata": "{nun}{xiriq}{root1}{root2}{root3}",
                "hu": "{nun}{xiriq}{root1}{root2}{root3}",
                "anin": "{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "at": "{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "hi": "{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "anaxnuz": "{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": "{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": "{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{nun}{xiriq}{yod}{root1}{root2}{root3}",
                "hi":"{nun}{xiriq}{yod}{root1}{root2}{root3}{hey}",
                "anaxnu":"{nun}{xiriq}{yod}{root1}{root2}{root3}{nun}{shureq}",
                "atem":"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}",
                "hen":"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":"{alef}{root1}{root2}{root3}",
                "ata":"{tav_with_mapik}{yod}{root1}{root2}{root3}",
                "at":"{tav_with_mapik}{yod}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":"{yod}{yod}{root1}{root2}{root3}",
                "hi":"{tav_with_mapik}{yod}{root1}{root2}{root3}",
                "anaxnu":"{nun}{yod}{root1}{root2}{root3}",
                "atem":"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",
                "aten":"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",
                "hem":"{yod}{yod}{root1}{root2}{root3}{shureq}",
                "hen":"{yod}{yod}{root1}{root2}{root3}{shureq}"
            }
        },

        "pey_yod": {
            "hoveh": {
                "aniz": "{nun}{xolammalei}{root1}{root2}",
                "ata": "{nun}{xolammalei}{root1}{root2}",
                "hu": "{nun}{xolammalei}{root1}{root2}",
                "anin": "{nun}{xolammalei}{root1}{root2}{tav}",
                "at": "{nun}{xolammalei}{root1}{root2}{tav}",
                "hi": "{nun}{xolammalei}{root1}{root2}{tav}",
                "anaxnuz": "{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
                "aten":"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
                "hen":"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":"{nun}{xolammalei}{root2}{root3}",
                "hi":"{nun}{xolammalei}{root2}{root3}{hey}",
                "anaxnu":"{nun}{xolammalei}{root2}{root3}{nun}{shureq}",
                "atem":"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{nun}{xolammalei}{root2}{root3}{shureq}",
                "hen":"{nun}{xolammalei}{root2}{root3}{shureq}"
            },

            "atid": {
                "ani":"{alef}",
                "ata":"",
                "at":"",
                "hu":"",
                "hi":"",
                "anaxnu":"",
                "atem":"",
                "aten":"",
                "hem":"",
                "hen":""
            }
        },

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": "{nun}{xiriq}{root1}{root2}{hey}",
                "ata": "{nun}{xiriq}{root1}{root2}{hey}",
                "hu": "{nun}{xiriq}{root1}{root2}{hey}",
                "anin": "{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "at": "{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "hi":"{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "anaxnuz": "{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": "{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": "{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
                "aten":"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
                "hen":"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{qametz}",
                "at":"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{shva}",
                "hu":"{nun}{xiriq}{root1}{root2}{hey}",
                "hi":"{nun}{xiriq}{root1}{root2}{tav}{hey}",
                "anaxnu":"{nun}{xiriq}{root1}{root2}{yod}{nun}{shureq}",
                "atem":"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{nun}{xiriq}{root1}{root2}{shureq}",
                "hen":"{nun}{xiriq}{root1}{root2}{shureq}"
            },

            "atid": {
                "ani":"",
                "ata":"{tav_with_mapik}{yod}{root1}{root2}{hey}",
                "at":"{tav_with_mapik}{yod}{root1}{root2}{xiriq}{yod}",
                "hu":"{yod}{yod}{root1}{root2}{hey}",
                "hi":"{tav_with_mapik}{yod}{root1}{root2}{hey}",
                "anaxnu":"{nun}{yod}{root1}{root2}{hey}",
                "atem":"{tav_with_mapik}{yod}{root1}{root2}{shureq}",
                "aten":"{tav_with_mapik}{yod}{root1}{root2}{shureq}",
                "hem":"{yod}{yod}{root1}{root2}{shureq}",
                "hen":"{yod}{yod}{root1}{root2}{shureq}"
            }
        },

        "lamed_alef": {
            "hoveh": {
                "aniz": "{nun}{xiriq}{root1}{root2}{alef}",
                "ata": "{nun}{xiriq}{root1}{root2}{alef}",
                "hu": "{nun}{xiriq}{root1}{root2}{alef}",
                "anin": "{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "at": "{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "hi": "{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "anaxnuz": "{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "atem": "{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "hem": "{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
                "aten":"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
                "hen":"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
            },

            "avar":{
                "ani":"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}",
                "ata":"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{qametz}",
                "at":"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{shva}",
                "hu":"{nun}{xiriq}{root1}{root2}{alef}",
                "hi":"{nun}{xiriq}{root1}{root2}{alef}{hey}",
                "anaxnu":"{nun}{xiriq}{root1}{root2}{alef}{nun}{shureq}",
                "atem":"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}",
                "aten":"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}",
                "hem":"{nun}{xiriq}{root1}{root2}{alef}{shureq}",
                "hen":"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
            },

            "atid":{
                "ani":"",
                "ata":"{tav_with_mapik}{yod}{root1}{root2}{alef}",
                "at":"{tav_with_mapik}{yod}{root1}{root2}{alef}{xiriq}{yod}",
                "hu":"{yod}{yod}{root1}{root2}{alef}",
                "hi":"{tav_with_mapik}{yod}{root1}{root2}{alef}",
                "anaxnu":"{nun}{yod}{root1}{root2}{alef}",
                "atem":"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",
                "aten":"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",
                "hem":"{yod}{yod}{root1}{root2}{alef}{shureq}",
                "hen":"{yod}{yod}{root1}{root2}{alef}{shureq}"
            }
        }
    }
}






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
#תוכתבו
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

    "pey_alef": r"^\u05D0[\u05D0-\u05EA]{2}$",
    "pey_yod": r"^\u05D9[\u05D0-\u05EA]{2}$",
    "pey_nun": r"^\u05E0[\u05D0-\u05EA]{2}$",
    "ayin_vav": r"^[\u05D0-\u05EA]\u05D5[\u05D0-\u05EA]$",
    "ayin_yod": r"^[\u05D0-\u05EA]\u05D9[\u05D0-\u05EA]$",
    "lamed_alef": r"^[\u05D0-\u05EA][\u05D0-\u05EA]\u05D0$",
    "lamed_hey_yod": r"^[\u05D0-\u05EA][\u05D0-\u05EA][\u05D9\u05E5]$",
    "kapolim": r"^([\u05D0-\u05EA][\u05D0-\u05EA])\1$"

}

mishkalim_more_specific = {

    "merubayim": r"^[\u05D0-\u05EA][\u05D0-\u05EA][\u05D0-\u05EA][\u05D0-\u05EA]$",
    "pey_nun_ayin_vav": r"^\u05E0\u05D5[\u05D0-\u05EA]$",
    "pey_nun_ayin_yod": r"^\u05E0\u05D9[\u05D0-\u05EA]$",
    "lamed_alef_ayin_vav": r"^\u05D5[\u05D0-\u05EA]\u05D0$",
    "lamed_alef_ayin_yod": r"^\u05D9[\u05D0-\u05EA]\u05D0$",
    "ayin_vav_lamed_hey_yod": r"^[\u05D0-\u05EA]\u05D5[\u05D9\u05E5]$",
    "ayin_yod_lamed_hey_yod": r"^[\u05D0-\u05EA]\u05D9[\u05D9\u05E5]$",
    "efal": r"^[\u05D0-\u05EA][u05D0\u05D4\u05D7\u05E2][u05D0\u05D7\u05E2]$"
}

mishkalim_hitpael = {

    "shin_sin_tav": r"^\u05E9[\u05D0-\u05EA][\u05D0-\u05EA]$",
    "samech_tav": r"^\u05E1[\u05D0-\u05EA][\u05D0-\u05EA]$",
    "zayin_dalet": r"^\u05D6[\u05D0-\u05EA][\u05D0-\u05EA]$",
    "tzadi_tet": r"^\u05E6[\u05D0-\u05EA][\u05D0-\u05EA]$"
#add all possibilities for crossover between multiple --> maybe will have to add another dict


}

special_shoreshim = {
    "alef_vav_hey": r"^\u05D0\u05D5\u05D4$",

    "lamed_bet_shin": r"^\u05DC\u05D1\u05E9$",
    "lamed_mem_dalet": r"^\u05DC\u05DE\u05D3",
    "shin_kaf_bet": r"^\u05E9\u05DB\u05D1"

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
    return "shlemim"



#make a chat bot interface for the root #constructs would be in the value of the dictionary for them to choose from


alef = "\u05D0",
nunsofit = "\u05DF"
memsofit = "\u05DD"
yod = "\u05D9"
nun = "\u05E0"
hey = "\u05D4"
tav_with_mapik = "\u05EA\u05BC"
vav = "\u05D5"
tav = "\u05EA"

#consider otiyot sofiyot
shin_sin = "\u05E9"
tzadi = "\u05E6"
dalet = "\u05D3"
tet = "\u05D8"
samech = "\u05E1"
zayin = "\u05D6"


dagesh = "\u05BC"
mapik = "\u05BC"
xiriq = "\u05B4"
qametz = "\u05B8"
segol = "\u05B6"
shureq = "\u05D5\u05BC"
xolammalei = "\u05D5\u05B9"
xolam = "\u05D5\u05B9"
patax = "\u05B7"
shva = "\u05B0"
tzerei = "\u05B5"
tzeirei = "\u05B5"

def render_conjugate (shoresh, binyan, zman, shem_guf):
    mishkal = detect_mishkal(shoresh, binyan)
    # Handle mishkalim from pealim dictionary
    if binyan in pealim and mishkal in pealim[binyan] and zman in pealim[binyan][mishkal]:
        root1 = shoresh[0]
        root2 = shoresh[1]
        root3 = shoresh[2]
        root4 = shoresh[3 % len(shoresh)]

        conjugation = pealim[binyan][mishkal][zman][shem_guf]
        #want to have it interpret aniz and anin and ani as the same


        final_ans = ""
        commands = re.findall(r"\{\w+\}", conjugation)
        for command in commands:
            if command == "{root1}":
                final_ans += root1
            elif command == "{root2}":
                final_ans += root2
            elif command == "{root3}":
                final_ans += root3
            elif command == "{root4}":
                final_ans == root4
            elif command == "{alef}":
                final_ans += alef
            elif command == "{nunsofit}":
                final_ans += nunsofit
            elif command == "{memsofit}":
                final_ans += memsofit
            elif command == "{yod}":
                final_ans += yod
            elif command == "{nun}":
                final_ans += nun
            elif command == "{hey}":
                final_ans += hey
            elif command == "{tav_with_mapik}":
                final_ans += tav_with_mapik
            elif command == "{vav}":
                final_ans += vav
            elif command == "{tav}":
                final_ans += tav
            elif command == "{shin_sin}":
                final_ans += shin_sin
            elif command == "{tzadi}":
                final_ans += tzadi
            elif command == "{dalet}":
                final_ans += dalet
            elif command == "{tet}":
                final_ans += tet
            elif command == "{samech}":
                final_ans += samech
            elif command == "{zayin}":
                final_ans += zayin
            elif command == "{dagesh}":
                final_ans += dagesh
            elif command == "{mapik}":
                final_ans += mapik
            elif command == "{xiriq}":
                final_ans += xiriq
            elif command == "{qametz}":
                final_ans += qametz
            elif command == "{segol}":
                final_ans += segol
            elif command == "{tzeirei}":
                final_ans += tzeirei
            elif command == "{shureq}":
                final_ans += shureq
            elif command == "{xolammalei}":
                final_ans += xolammalei
            elif command == "{xolam}":
                final_ans += xolam
            elif command == "{patax}":
                final_ans += patax
            elif command == "{shva}":
                final_ans += shva
            elif command == "{shureq}":
                final_ans += shureq



        return final_ans
    else:
        # Handle case where mishkal is not detected
        pass






#need to make a regex to interpret input shoresh to which mishkal

#find the pattern from defns above to use to render the conjugated verb; actually apply shoresh to the pattern

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







@app.route('/conjugations', methods=['GET'])
def get_conjugations():
    verb = request.args.get('verb')
    conjugations = conjugate_verb(verb)
    return jsonify(conjugations)

if __name__ == '__main__':
    app.run(debug=True)
