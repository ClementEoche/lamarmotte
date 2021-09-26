from flask import Flask, jsonify,request

# Jsonify for the API request and request for the app routes.

from db import mysql,db_connection,app

# db_connetion for cursor, app for intialization, and mysql for configuration.

# function allows for SQL request and retrieval of API response.

def fetchall_cursor(fetchall_query):
	cursor = db_connection()
	cursor.execute(fetchall_query)
	row = cursor.fetchall()
	resp = jsonify(row)
	resp.status_code=200
	return resp
	
# Retrieves all of the informations in the database

@app.route("/collector/info",methods=["POST"])
def create_info():
    # On recupere le corps (payload) de la requete
    payload = request.form.to_dict()
    result = add_infos(**payload)

    if result:
        return jsonify(status='True', message='Infos inserted')
    return jsonify(status='False')

def add_infos(unityid, tmp_Cuve, tmp_Ext, poids_Lait_Cuve, mesure_PH, mesure_K,concentration_NaCl,niv_Bact_Salmonelle,niv_Bact_Ecoli,niv_Bact_Listeria):
    try:
        data_Set = {
        "unityId" : unityid,
		"tmp_Cuve" : tmp_Cuve,
		"tmp_Ext" : tmp_Ext,
		"poids_Lait_Cuve" : poids_Lait_Cuve,
		"mesure_PH" : mesure_PH,
		"mesure_K" : mesure_K,
		"concentration_NaCl" : concentration_NaCl,
		"niv_Bact_Salmonelle" : niv_Bact_Salmonelle,
		"niv_Bact_Ecoli" : niv_Bact_Ecoli,
		"niv_Bact_Listeria" : niv_Bact_Listeria
	    }
	    
	json_dump = json.dumps(data_Set)
    	# Cast the array to string to send bytes
    	request = bytes(json_dump, 'utf-8')
        session.add(request)
        session.commit()

        return True

    except Exception as e:
        print(e)

        return False
