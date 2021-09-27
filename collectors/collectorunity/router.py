from flask import Flask, jsonify,request, session
import json
from datetime import strftime

# Jsonify for the API request and request for the app routes.

from dbconfig import mysql,db_connection,app

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

def add_infos(unityid,date_prod, tmp_Cuve, tmp_Ext, poids_Lait_Cuve, mesure_PH, mesure_K,concentration_NaCl,niv_Bact_Salmonelle,niv_Bact_Ecoli,niv_Bact_Listeria):
	cursor = db_connection()
	date_prod = strftime(date_prod)
	query =	"""INSERT INTO unities (unityId, date_prod, tmp_Cuve,tmp_Ext,poids_Lait_Cuve,mesure_PH,mesure_K,concentration_NaCl,niv_Bact_Salmonelle,niv_Bact_Ecoli,niv_Bact_Listeria,date_info) VALUES (%f, %s, %f, %f, %f, %f, %f, %f, %f, %f, %f)"""
	record = (unityid,date_prod, tmp_Cuve, tmp_Ext, poids_Lait_Cuve, mesure_PH, mesure_K,concentration_NaCl,niv_Bact_Salmonelle,niv_Bact_Ecoli,niv_Bact_Listeria)
	cursor.execute(query,record)
