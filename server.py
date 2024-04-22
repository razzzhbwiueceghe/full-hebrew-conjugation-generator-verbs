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
                "hen":f"{root1}{xolammalei}{root2}{shva}{root3}{xiriq}{tav}"
            },

            "avar":{
                "ani":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":f"{root1}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":f"{root1}{qametz}{root2}{patax}{root3}",
                "hi":f"{root1}{qametz}{root2}{shva}{root3}{qametz}{hey}",
                "anaxnu":f"{root1}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}",
                "atem":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{shva}{root2}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "hem":f"{root1}{qametz}{root2}{shva}{root3}{shureq}",
                "hen":f"{root1}{qametz}{root2}{shva}{root3}{shureq}",
            },

            "atid":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{patax}{root3}",
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{patax}{root3}",
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{patax}{root3}",
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{patax}{root3}",
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
            },


            "efol":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{xolammalei}{root3}",
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{xolammalei}{root3}",
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{root3}{shureq}",
            },
        },
        
        "lamed_hey_yod": {
            "hoveh": {
                "aniz": f"{root1}{xolammalei}{root2}{segol}{hey}",
                "ata": f"{root1}{xolammalei}{root2}{segol}{hey}",
                "hu": f"{root1}{xolammalei}{root2}{segol}{hey}",
                "anin": f"{root1}{xolammalei}{root2}{qametz}{hey}",
                "at": f"{root1}{xolammalei}{root2}{qametz}{hey}",
                "hi": f"{root1}{xolammalei}{root2}{qametz}{hey}",
                "anaxnuz": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{root1}{xolammalei}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
                "aten":f"{root1}{xolammalei}{root2}{xolammalei}{tav}",
                "hen":f"{root1}{xolammalei}{root2}{xolammalei}{tav}"
            },

            "avar":{
                "ani":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":f"{root1}{qametz}{root2}{qametz}{hey}",
                "hi":f"{root1}{qametz}{root2}{shva}{tav}{qametz}{hey}",
                "anaxnu":f"{root1}{qametz}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{qametz}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{qametz}{root2}{shureq}",
                "hen":f"{root1}{qametz}{root2}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{segol}{hey}",
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{segol}{hey}",
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shureq}",
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shureq}",
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shureq}"
            },
        },   

        "pey_yod":{

            "hoveh":{
                "aniz": f"{yod}{xolammalei}{root2}{tzerei}{root3}",
                "ata": f"{yod}{xolammalei}{root2}{tzerei}{root3}",
                "hu": f"{yod}{xolammalei}{root2}{tzerei}{root3}",
                "anin": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "at": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "hi": f"{yod}{xolammalei}{root2}{segol}{root3}{segol}{tav}",
                "anaxnuz": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{yod}{xolammalei}{root2}{shva}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
                "aten":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
                "hen":f"{yod}{xolammalei}{root2}{shva}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":f"{yod}{qametz}{root2}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":f"{yod}{qametz}{root2}{patax}{root3}",
                "hi":f"{yod}{qametz}{root2}{shva}{root3}{qametz}{hey}",
                "anaxnu":f"{yod}{qametz}{root2}{patax}{root3}{shva}{nun}{shureq}",
                "atem":f"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{yod}{qametz}{root2}{patax}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{yod}{qametz}{root2}{shva}{root3}{shureq}",
                "hen":f"{yod}{qametz}{root2}{shva}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{tzerei}{root2}{tzerei}{root3}",
                "ata":f"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",
                "at":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{xiriq}{yod}",
                "hu":f"{yod}{tzerei}{root2}{tzerei}{root3}",
                "hi":f"{tav_with_mapik}{tzerei}{root1}{tzerei}{root3}",
                "anaxnu":f"{nun}{tzerei}{root2}{tzerei}{root3}",
                "atem":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{tzerei}{root2}{shva}{root3}{shureq}",
                "hem":f"{yod}{tzerei}{root2}{shva}{root3}{shureq}",
                "hen":f"{yod}{tzerei}{root2}{shva}{root3}{shureq}",
            }
        },

        "lamed_alef":{
            "hoveh":{
                "aniz": f"{root1}{xolammalei}{root2}{tzerei}{alef}",
                "ata": f"{root1}{xolammalei}{root2}{tzerei}{alef}",
                "hu": f"{root1}{xolammalei}{root2}{tzerei}{alef}",
                "anin": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "at": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "hi": f"{root1}{xolammalei}{root2}{tzerei}{alef}{tav}",
                "anaxnuz": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "atem": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "hem": f"{root1}{xolammalei}{root2}{shva}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
                "aten":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
                "hen":f"{root1}{xolammalei}{root2}{shva}{alef}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{xiriq}{yod}",
                "ata":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{qametz}",
                "at":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{shva}",
                "hu":f"{root1}{qametz}{root2}{qametz}{alef}",
                "hi":f"{root1}{qametz}{root2}{shva}{alef}{qametz}{hey}",
                "anaxnu":f"{root1}{qametz}{root2}{qametz}{alef}{nun}{shureq}",
                "atem":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{memsofit}",
                "aten":f"{root1}{qametz}{root2}{qametz}{alef}{tav}{segol}{nunsofit}",
                "hem":f"{root1}{qametz}{root2}{shva}{alef}{shureq}",
                "hen":f"{root1}{qametz}{root2}{shva}{alef}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{segol}{root1}{shva}{root2}{qametz}{alef}",
                "ata":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "at":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "hi":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "anaxnu":f"{nun}{xiriq}{root1}{shva}{root2}{qametz}{alef}",
                "atem":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "hem":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
                "hen":f"{yod}{xiriq}{root1}{shva}{root2}{shva}{alef}{shureq}",
            }
        },

        "pey_nun":{
            "hoveh":{
                "aniz": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
                "ata": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
                "hu": f"{root1}{xolammalei}{root2}{tzerei}{root3}",
                "anin": f"",
                "at": f"",
                "hi": f"",
                "anaxnuz": f"",
                "atem": f"",
                "hem": f"",
                "anaxnun":f"",
                "aten":f"",
                "hen":f"",
            },

            "avar":{
                "ani":f"",
                "ata":f"",
                "at":f"",
                "hu":f"",
                "hi":f"",
                "anaxnu":f"",
                "atem":f"",
                "aten":f"",
                "hem":f"",
                "hen":f""
            },

            "atid":{
                "ani":f"{alef}{root2}{root3}",
                "ata":f"{tav_with_mapik}{root2}{root3}",
                "at":f"{tav_with_mapik}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{root2}{root3}",
                "hi":f"{tav_with_mapik}{root2}{root3}",
                "anaxnu":f"{nun}{root2}{root3}",
                "atem":f"{tav_with_mapik}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{root2}{root3}{shureq}",
                "hem":f"{yod}{root2}{root3}{shureq}",
                "hen":f"{yod}{root2}{root3}{shureq}",
            }
        },

        "pey_aleph":{
            "hoveh":{
                "aniz": f"{alef}{xolammalei}{root2}{root3}",
                "ata": f"",
                "hu": f"",
                "anin": f"{alef}{xolammalei}{root2}{root3}{tav}",
                "at": f"{alef}{xolammalei}{root2}{root3}{tav}",
                "hi": f"{alef}{xolammalei}{root2}{root3}{tav}",
                "anaxnuz": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{alef}{xolammalei}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{alef}{xolammalei}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{alef}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{alef}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{alef}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{alef}{root2}{root3}",
                "hi":f"{alef}{root2}{root3}{hey}",
                "anaxnu":f"{alef}{root2}{root3}{nun}{shureq}",
                "atem":f"{alef}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{alef}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{alef}{root2}{root3}{shureq}",
                "hen":f"{alef}{root2}{root3}{shureq}"
            },


            "atid":{
                "ani":f"{alef}{xolammalei}{alef}{root2}{root3}",
                "ata":f"{tav}{xolammalei}{alef}{root2}{root3}",
                "at":f"{tav}{xolammalei}{alef}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xolammalei}{alef}{root2}{root3}",
                "hi":f"{tav}{xolammalei}{alef}{root2}{root3}",
                "anaxnu":f"{nun}{xolammalei}{alef}{root2}{root3}",
                "atem":f"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",
                "aten":f"{tav}{xolammalei}{alef}{root2}{root3}{shureq}",
                "hem":f"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",
                "hen":f"{yod}{xolammalei}{alef}{root2}{root3}{shureq}",
            }
        },

        "ayin_vav":{
            "hoveh":{
                "aniz": f"{root1}{mapik}{qametz}{root3}",
                "ata": f"{root1}{mapik}{qametz}{root3}",
                "hu": f"{root1}{mapik}{qametz}{root3}",
                "anin": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "at": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "hi": f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "anaxnuz": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{root1}{mapik}{qametz}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
                "aten":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
                "hen":f"{root1}{mapik}{qametz}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":f"{root1}{mapik}{qametz}{root3}",
                "hi":f"{root1}{mapik}{qametz}{root3}{qametz}{hey}",
                "anaxnu":f"{root1}{mapik}{patax}{root3}{shva}{nun}{shureq}",
                "atem":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{mapik}{patax}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{mapik}{qametz}{root3}{shureq}",
                "hen":f"{root1}{mapik}{qametz}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{qametz}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{qametz}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{qametz}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "aten":f"{tav_with_mapik}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "hem":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",
                "hen":f"{yod}{qametz}{root1}{root2}{root3}{shva}{shureq}",
            }
        },
    },
    
    "piel":{
        "shlemim":{
            "hoveh":{
                "aniz": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}",
                "ata": f"{mem}{nikkudchanges}{root1}{root2}{root3}",
                "hu": f"{mem}{nikkudchanges}{root1}{root2}{root3}",
                "anin": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "at": f"{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "hi": f"{mem}{nikkudchanges}{root1}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{nikkudchanges}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{dagesh}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
                "aten":f"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
                "hen":f"{mem}{nikkudchanges}{root1}{root2}{root3}{xolam}{tav}",
            },

            #gerate transfucer state here with nekkudot changes

            "avar":{
                "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{qametz}",
                "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{shva}",
                "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{sh}",
                "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shva}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{segol}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "hem":f"{yod}{root1}{root2}{root3}{shureq}",
                "hen":f"{yod}{root1}{root2}{root3}{shureq}",
            }
        },

        "merubayim":{
            "hoveh":{
                "aniz": f"{mem}{root1}{root2}{root3}{root4}",
                "ata": f"{mem}{root1}{root2}{root3}{root4}",
                "hu": f"{mem}{root1}{root2}{root3}{root4}",
                "anin": f"{mem}{root1}{root2}{root3}{root4}{tav}",
                "at": f"{mem}{root1}{root2}{root3}{root4}{tav}",
                "hi": f"{mem}{root1}{root2}{root3}{root4}{tav}",
                "anaxnuz": f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "atem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "hem":  f"{mem}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "anaxnun": f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "aten":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "hen":f"{mem}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}",
                "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{aleph}{root1}{root2}{root3}{root4}",
                "ata":f"{tav_with_mapik}{root1}{root2}{root3}{root4}",
                "at":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}{root3}{root4}",
                "hi":f"{tav_with_mapik}{root1}{root2}{root3}{root4}",
                "anaxnu":f"{nun}{root1}{root2}{root3}{root4}",
                "atem":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{root3}{root4}{shureq}",
                "hem":f"{yod}{root1}{root2}{root3}{root4}{shureq}",
                "hen":f"{yod}{root1}{root2}{root3}{root4}{shureq}"
            }
        },
        
        "lamed_alef":{
            "hoveh":{
                "aniz": f"{mem}{root1}{root2}{root3}",
                "ata": f"{mem}{root1}{root2}{root3}",
                "hu": f"{mem}{root1}{root2}{root3}",
                "anin": f"{mem}{root1}{root2}{root3}{hey}",
                "at": f"{mem}{root1}{root2}{root3}{hey}",
                "hi": f"{mem}{root1}{root2}{root3}{hey}",
                "anaxnuz": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}",
                "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{hey}",
                "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{nun}{shureq}",
                "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
                "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{root3}{shureq}",
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{root1}{root2}{root3}{yod}",
                "hu":f"{yod}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{root3}{shureq}",
                "hem":f"{yod}{root1}{root2}{root3}{shureq}",
                "hen":f"{yod}{root1}{root2}{root3}{shureq}",
            }
        },

        "lamed_hey_yod":{
            "hoveh":{
                "aniz": f"{mem}{root1}{root2}{hey}",
                "ata": f"{mem}{root1}{root2}{hey}",
                "hu": f"{mem}{root1}{root2}{hey}",
                "anin": f"{mem}{root1}{root2}{hey}",
                "at": f"{mem}{root1}{root2}{hey}",
                "hi": f"{mem}{root1}{root2}{hey}",
                "anaxnuz": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{root1}{root2}{xolammalei}{tav}",
                "aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
                "hen":f"{mem}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{hey}",
                "hi":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{tav}{hey}",
                "anaxnu":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}",
                "atem":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{root1}{dagesh}{xiriq}{yod}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}",
                "hen":f"{root1}{dagesh}{xiriq}{yod}{root2}{shureq}",
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}{hey}",
                "ata":f"{tav_with_mapik}{root1}{root2}{hey}",
                "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}{hey}",
                "hi":f"{tav_with_mapik}{root1}{root2}{hey}",
                "anaxnu":f"{nun}{root1}{root2}{hey}",
                "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":f"{yod}{root1}{root2}{shureq}",
                "hen":f"{yod}{root1}{root2}{shureq}",
            }
        }
    },

    "hifil":{
        "shlemim":{
            "hoveh":{
                "aniz": f"",
                "ata": f"",
                "hu": f"",
                "anin": f"",
                "at": f"",
                "hi": f"",
                "anaxnuz": f"",
                "atem": f"",
                "hem": f"",
                "anaxnun":f"",
                "aten":f"",
                "hen":f""
            },

            "avar":{
                "ani":f"",
                "ata":f"",
                "at":f"",
                "hu":f"",
                "hi":f"",
                "anaxnu":f"",
                "atem":f"",
                "aten":f"",
                "hem":f"",
                "hen":f""
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}{xiriq}{yod}{root3}",
                "ata":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",
                "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}{xiriq}{yod}{root3}",
                "hi":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}",
                "anaxnu":f"{nun}{root1}{root2}{xiriq}{yod}{root3}",
                "atem":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":f"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{yod}{root1}{root2}{xiriq}{yod}{root3}{shureq}",
            }
        },

        "pey_yod":{
            "hoveh":{
                "aniz": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "ata": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hu": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "anin": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "at": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "hi": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xolammalei}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{xolammalei}{root2}{root3}{shva}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hi":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnu":f"{hey}{xolammalei}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{hey}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "ata":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "at":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "hi":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "anaxnu":f"{nun}{xolammalei}{root2}{xiriq}{yod}{root3}",
                "atem":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{yod}{xolammalei}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "pey_nun":{
            "hoveh":{
                "aniz": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "ata": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "hu": f"{mem}{nun}{root2}{xiriq}{yod}{root3}",
                "anin": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "at": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "hi": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{nun}{root2}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}",
                "hi":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{nun}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{nun}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{nun}{root2}{xiriq}{yod}{root3}",
                "ata":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",
                "at":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":f"{yod}{nun}{root2}{xiriq}{yod}{root3}",
                "hi":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}",
                "anaxnu":f"{nun}{nun}{root2}{xiriq}{yod}{root3}",
                "atem":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hem":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{yod}{nun}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "ayin_vav_yod":{
            "hoveh":{
                "aniz": f"{mem}{root1}{xiriq}{yod}{root3}",
                "ata": f"{mem}{root1}{xiriq}{yod}{root3}",
                "hu": f"{mem}{root1}{xiriq}{yod}{root3}",
                "anin": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "at": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "hi": f"{mem}{root1}{xiriq}{yod}{root3}{hey}",
                "anaxnuz": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{root1}{xiriq}{yod}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{root1}{xiriq}{yod}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{root1}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{root1}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{root1}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{root1}{xiriq}{yod}{root3}",
                "hi":f"{hey}{root1}{xiriq}{yod}{root3}{hey}",
                "anaxnu":f"{hey}{root1}{root3}{shureq}",
                "atem":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}",
                "hen":f"{hey}{root2}{xiriq}{yod}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{root2}{xiriq}{yod}{root3}",
                "ata":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",
                "at":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{xiriq}{yod}",
                "hu":f"{yod}{root2}{xiriq}{yod}{root3}",
                "hi":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}",
                "anaxnu":f"{nun}{root2}{xiriq}{yod}{root3}",
                "atem":f"{tav_with_mapik}{root2}{xiriq}{yod}{root3}{shureq}",
                "aten":f"{tav}{root2}{xiriq}{root3}{shureq}",
                "hem":f"{yod}{root2}{xiriq}{root3}{shureq}",
                "hen":f"{yod}{root2}{xiriq}{yod}{root3}{shureq}"
            }
        },

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": f"{mem}{root1}{root2}{hey}",
                "ata": f"{mem}{root1}{root2}{hey}",
                "hu": f"{mem}{root1}{root2}{hey}",
                "anin": f"{mem}{root1}{root2}{hey}",
                "at": f"{mem}{root1}{root2}{hey}",
                "hi": f"{mem}{root1}{root2}{hey}",
                "anaxnuz": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{root1}{root2}{xolammalei}{tav}",
                "aten":f"{mem}{root1}{root2}{xolammalei}{tav}",
                "hen":f"{mem}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{qametz}",
                "at":f"{hey}{root1}{root2}{yod}{tav_with_mapik}{shva}",
                "hu":f"{hey}{root1}{root2}{hey}",
                "hi":f"{hey}{root1}{root2}{tav}{hey}",
                "anaxnu":f"{hey}{root1}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{root1}{root2}{shureq}",
                "hen":f"{hey}{root1}{root2}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}{hey}",
                "ata":f"{tav_with_mapik}{root1}{root2}{hey}",
                "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}{hey}",
                "hi":f"{tav_with_mapik}{root1}{root2}{hey}",
                "anaxnu":f"{nun}{root1}{root2}{hey}",
                "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":f"{yod}{root1}{root2}{shureq}",
                "hen":f"{yod}{root1}{root2}{shureq}"
            }
        },

#hifil_kapolim-- ע״ע where the last letter of shoresh is same as second to last letter
        "kapolim": {
            "hoveh": {
                "aniz": f"{mem}{root1}{root2}",
                "ata": f"{mem}{root1}{root2}",
                "hu": f"{mem}{root1}{root2}",
                "anin": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "at": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "hi": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{hey}",
                "anaxnuz": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
                "aten":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
                "hen":f"{mem}{shva}{root1}{xiriq}{yod}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{root1}{root2}{tav_with_mapik}{xiriq}{yod}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{root1}{root2}{tav_with_mapik}{qametz}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{qametz}",
                "at":f"{hey}{root1}{root2}{tav_with_mapik}{shva}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{shva}",
                "hu":f"{hey}{root1}{root2}",
                "hi":f"{hey}{root1}{root2}{hey}",
                "anaxnu":f"{hey}{root1}{root2}{nun}{shureq}/{hey}{root1}{root2}{xolammalei}{nun}{shureq}",
                "atem":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{memsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{root1}{root2}{tav_with_mapik}{segol}{nunsofit}/{hey}{root1}{root2}{xolammalei}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{root1}{root2}{shureq}",
                "hen":f"{hey}{root1}{root2}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}",
                "ata":f"{tav_with_mapik}{root1}{root2}",
                "at":f"{tav_with_mapik}{root1}{root2}{xiriq}{yod}",
                "hu":f"{yod}{root1}{root2}",
                "hi":f"{tav_with_mapik}{root1}{root2}",
                "anaxnu":f"{nun}{root1}{root2}",
                "atem":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{root1}{root2}{shureq}",
                "hem":f"{yod}{root1}{root2}{shureq}",
                "hen":f"{yod}{root1}{root2}{shureq}"
            }
        }
    },

    "hitpael": {
        "shlemim": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "ata": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "hu": f"{mem}{xiriq}{tav}{root1}{root2}{root3}",
                "anin":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "at": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "hi": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{tav}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}",
                "hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{tav_with_mapik}{segol}"
            },

            "atid":{
                "ani":f"{alef}{tav}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{tav}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{tav}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",
                "hen":f"{yod}{tav}{root1}{root2}{root3}{shureq}",
            }
        },

        "samech_tav": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "ata": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "hu": f"{mem}{xiriq}{samech}{tav}{root2}{root3}",
                "anin": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "at": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "hi": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{samech}{tav}{root2}{root3}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}",
                "hi":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{samech}{tav}{root2}{root3}{shureq}"
            },
            
            
            "atid":{
                "ani":f"{alef}{samech}{tav}{root2}{root3}",
                "ata":f"{tav_with_mapik}{samech}{tav}{root2}{root3}",
                "at":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{samech}{tav}{root2}{root3}",
                "hi":f"{tav_with_mapik}{samech}{tav}{root2}{root3}",
                "anaxnu":f"{nun}{samech}{tav}{root2}{root3}",
                "atem":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{samech}{tav}{root2}{root3}{shureq}",
                "hem":f"{yod}{samech}{tav}{root2}{root3}{shureq}",
                "hen":f"{yod}{samech}{tav}{root2}{root3}{shureq}"
            }
        },
        
        "ayin_yod_vav": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "ata": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "hu": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "anin": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "at": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "hi": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{tav}{root1}{vav}{root3}{root3}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}",
                "hi":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{tav}{root1}{vav}{root3}{root3}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{tav}{root1}{vav}{root3}{root3}",
                "ata":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",
                "at":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{xiriq}{yod}",
                "hu":f"{yod}{tav}{root1}{vav}{root3}{root3}",
                "hi":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}",
                "anaxnu":f"{nun}{tav}{root1}{vav}{root3}{root3}",
                "atem":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hem":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",
                "hen":f"{yod}{tav}{root1}{vav}{root3}{root3}{shureq}",
            }
        },
        
        "lamed_alef": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "ata": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "hu": f"{mem}{xiriq}{tav}{root1}{root2}{alef}",
                "anin": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "at": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "hi": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{tav}",
                "anaxnuz": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{tav}{root1}{root2}{alef}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}",
                "hi":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{hey}",
                "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}",
                "hen":f"{hey}{xiriq}{tav}{root1}{root2}{alef}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{tav}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{tav}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{tav}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{tav}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{tav}{root1}{root2}{root3}{shureq}",
                "hem":f"{yod}{tav}{root1}{root2}{root3}{shureq}",
                "hen":f"{yod}{tav}{root1}{root2}{root3}{shureq}",
            }
        },
        
        "tzadi_tet": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "ata": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hu": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}",
                "anin":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "at": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "hi": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{tzadi}{tet}{root2}{root3}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hi":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{tzadi}{tet}{root2}{root3}",
                "ata":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",
                "at":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}",
                "hi":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}",
                "anaxnu":f"{nun}{xiriq}{tzadi}{tet}{root2}{root3}",
                "atem":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hem":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}",
                "hen":f"{yod}{xiriq}{tzadi}{tet}{root2}{root3}{shureq}"
            }
        },
        
        "zayin_dalet": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "ata": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hu": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}",
                "anin": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "at": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "hi": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{zayin}{dalet}{root2}{root3}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hi":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{zayin}{dalet}{root2}{root3}",
                "ata":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",
                "at":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}",
                "hi":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}",
                "anaxnu":f"{nun}{xiriq}{zayin}{dalet}{root2}{root3}",
                "atem":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hem":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}",
                "hen":f"{yod}{xiriq}{zayin}{dalet}{root2}{root3}{shureq}"
            }
        },
        
        "shin_sin_tav": {
            "hoveh": {
                "aniz": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "ata": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hu": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "anin": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "at": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "hi": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{tav}",
                "anaxnuz": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "atem": f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{mem}{xiriq}{shin_sin}{tav}{root2}{root3}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hi":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{hey}",
                "anaxnu":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{nun}{shva}",
                "atem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hen":f"{hey}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{shin_sin}{tav}{root2}{root3}",
                "ata":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "at":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "hi":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "anaxnu":f"{nun}{xiriq}{shin_sin}{tav}{root2}{root3}",
                "atem":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hem":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}",
                "hen":f"{yod}{xiriq}{shin_sin}{tav}{root2}{root3}{shureq}"
            }
        },
        
        
        #make finite state transducer that considers if first root is shin_sin, tzadi, etc.
        
        "lamed_hey_yod": {
            "hoveh": {
                "aniz": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "anin": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "at": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{hey}",
                "anaxnuz": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
                "aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
                "hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tav}{root1}{root2}{hey}",
                "hi":f"{hey}{xiriq}{tav}{root1}{root2}{tav}{hey}",
                "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tav}{root1}{root2}{xiriq}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}",
                "hen":f"{hey}{xiriq}{tav}{root1}{root2}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{tav}{root1}{root2}{hey}",
                "ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",
                "at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{tav}{root1}{root2}{hey}",
                "hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{hey}",
                "anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{hey}",
                "atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{shureq}",
                "hem":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}",
                "hen":f"{yod}{xiriq}{tav}{root1}{root2}{shureq}"
            }
        },
        
        "merubayim": {
            "hoveh": {
                "aniz": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "ata": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hu": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "anin": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "at": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "hi": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav}",
                "anaxnuz": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "atem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "hem": f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "aten":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
                "hen":f"{memsofit}{xiriq}{tav}{root1}{root2}{root3}{root4}{xolammalei}{tav}",
            },
            
            "avar":{
                "ani":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{qametz}",
                "at":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{shva}",
                "hu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hi":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{hey}",
                "anaxnu":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{nun}{shureq}",
                "atem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hen":f"{hey}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            },
            
            "atid":{
                "ani":f"{alef}{tav}{root1}{root2}{root3}{root4}",
                "ata":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "at":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{xiriq}{yod}",
                "hu":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "hi":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "anaxnu":f"{nun}{xiriq}{tav}{root1}{root2}{root3}{root4}",
                "atem":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "aten":f"{tav_with_mapik}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hem":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}",
                "hen":f"{yod}{xiriq}{tav}{root1}{root2}{root3}{root4}{shureq}"
            }
        }
    },

    ##maybe write a regex for basic vowel patterns for hoveh avar and atid told in regards to root configuration

    "nifal": {
        "shlemim": {
            "hoveh": {
                "aniz": f"{nun}{xiriq}{root1}{root2}{root3}",
                "ata": f"{nun}{xiriq}{root1}{root2}{root3}",
                "hu": f"{nun}{xiriq}{root1}{root2}{root3}",
                "anin": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "at": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "hi": f"{nun}{xiriq}{root1}{root2}{root3}{tav}",
                "anaxnuz": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "atem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "hem": f"{nun}{xiriq}{root1}{root2}{root3}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
                "aten":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
                "hen":f"{nun}{xiriq}{root1}{root2}{root3}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}",
                "hi":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{hey}",
                "anaxnu":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{nun}{shureq}",
                "atem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}",
                "hen":f"{nun}{xiriq}{yod}{root1}{root2}{root3}{shureq}"
            },

            "atid":{
                "ani":f"{alef}{root1}{root2}{root3}",
                "ata":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",
                "at":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{xiriq}{yod}",
                "hu":f"{yod}{yod}{root1}{root2}{root3}",
                "hi":f"{tav_with_mapik}{yod}{root1}{root2}{root3}",
                "anaxnu":f"{nun}{yod}{root1}{root2}{root3}",
                "atem":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",
                "aten":f"{tav_with_mapik}{yod}{root1}{root2}{root3}{shureq}",
                "hem":f"{yod}{yod}{root1}{root2}{root3}{shureq}",
                "hen":f"{yod}{yod}{root1}{root2}{root3}{shureq}"
            }
        },

        "pey_yod": {
            "hoveh": {
                "aniz": f"{nun}{xolammalei}{root1}{root2}",
                "ata": f"{nun}{xolammalei}{root1}{root2}",
                "hu": f"{nun}{xolammalei}{root1}{root2}",
                "anin": f"{nun}{xolammalei}{root1}{root2}{tav}",
                "at": f"{nun}{xolammalei}{root1}{root2}{tav}",
                "hi": f"{nun}{xolammalei}{root1}{root2}{tav}",
                "anaxnuz": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{nun}{xolammalei}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
                "aten":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
                "hen":f"{nun}{xolammalei}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{qametz}",
                "at":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{shva}",
                "hu":f"{nun}{xolammalei}{root2}{root3}",
                "hi":f"{nun}{xolammalei}{root2}{root3}{hey}",
                "anaxnu":f"{nun}{xolammalei}{root2}{root3}{nun}{shureq}",
                "atem":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{nun}{xolammalei}{root2}{root3}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{nun}{xolammalei}{root2}{root3}{shureq}",
                "hen":f"{nun}{xolammalei}{root2}{root3}{shureq}"
            },

            "atid": {
                "ani":f"{alef}",
                "ata":f"",
                "at":f"",
                "hu":f"",
                "hi":f"",
                "anaxnu":f"",
                "atem":f"",
                "aten":f"",
                "hem":f"",
                "hen":f""
            }
        },

        "lamed_hey_yod": {
            "hoveh": {
                "aniz": f"{nun}{xiriq}{root1}{root2}{hey}",
                "ata": f"{nun}{xiriq}{root1}{root2}{hey}",
                "hu": f"{nun}{xiriq}{root1}{root2}{hey}",
                "anin": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "at": f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "hi":f"{nun}{xiriq}{root1}{root2}{yod}{tav}",
                "anaxnuz": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "atem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "hem": f"{nun}{xiriq}{root1}{root2}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
                "aten":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
                "hen":f"{nun}{xiriq}{root1}{root2}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{qametz}",
                "at":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{shva}",
                "hu":f"{nun}{xiriq}{root1}{root2}{hey}",
                "hi":f"{nun}{xiriq}{root1}{root2}{tav}{hey}",
                "anaxnu":f"{nun}{xiriq}{root1}{root2}{yod}{nun}{shureq}",
                "atem":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{nun}{xiriq}{root1}{root2}{yod}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{nun}{xiriq}{root1}{root2}{shureq}",
                "hen":f"{nun}{xiriq}{root1}{root2}{shureq}"
            },

            "atid": {
                "ani":f"",
                "ata":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",
                "at":f"{tav_with_mapik}{yod}{root1}{root2}{xiriq}{yod}",
                "hu":f"{yod}{yod}{root1}{root2}{hey}",
                "hi":f"{tav_with_mapik}{yod}{root1}{root2}{hey}",
                "anaxnu":f"{nun}{yod}{root1}{root2}{hey}",
                "atem":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",
                "aten":f"{tav_with_mapik}{yod}{root1}{root2}{shureq}",
                "hem":f"{yod}{yod}{root1}{root2}{shureq}",
                "hen":f"{yod}{yod}{root1}{root2}{shureq}"
            }
        },

        "lamed_alef": {
            "hoveh": {
                "aniz": f"{nun}{xiriq}{root1}{root2}{alef}",
                "ata": f"{nun}{xiriq}{root1}{root2}{alef}",
                "hu": f"{nun}{xiriq}{root1}{root2}{alef}",
                "anin": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "at": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "hi": f"{nun}{xiriq}{root1}{root2}{alef}{tav}",
                "anaxnuz": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "atem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "hem": f"{nun}{xiriq}{root1}{root2}{alef}{xiriq}{yod}{memsofit}",
                "anaxnun":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
                "aten":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
                "hen":f"{nun}{xiriq}{root1}{root2}{alef}{xolammalei}{tav}",
            },

            "avar":{
                "ani":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{xiriq}{yod}",
                "ata":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{qametz}",
                "at":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{shva}",
                "hu":f"{nun}{xiriq}{root1}{root2}{alef}",
                "hi":f"{nun}{xiriq}{root1}{root2}{alef}{hey}",
                "anaxnu":f"{nun}{xiriq}{root1}{root2}{alef}{nun}{shureq}",
                "atem":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{memsofit}",
                "aten":f"{nun}{xiriq}{root1}{root2}{alef}{tav_with_mapik}{segol}{nunsofit}",
                "hem":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}",
                "hen":f"{nun}{xiriq}{root1}{root2}{alef}{shureq}"
            },

            "atid":{
                "ani":f"",
                "ata":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",
                "at":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{xiriq}{yod}",
                "hu":f"{yod}{yod}{root1}{root2}{alef}",
                "hi":f"{tav_with_mapik}{yod}{root1}{root2}{alef}",
                "anaxnu":f"{nun}{yod}{root1}{root2}{alef}",
                "atem":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",
                "aten":f"{tav_with_mapik}{yod}{root1}{root2}{alef}{shureq}",
                "hem":f"{yod}{yod}{root1}{root2}{alef}{shureq}",
                "hen":f"{yod}{yod}{root1}{root2}{alef}{shureq}"
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
    "pey_nun_ayin_yod": r"^\u05E0\u05D[\u05D0-\u05EA]$",
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
