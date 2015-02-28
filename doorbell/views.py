from django.shortcuts import render
from django.http import HttpResponse
from gcm import GCM

def index(request):
	return HttpResponse("Hello, this is doorbell")

def gcm(request):
	gcm = GCM(API_KEY)
	data = {'param1': 'value1', 'param2': 'value2'}
	reg_ids = ['1234']

	response = gcm.json_request(registration_ids=reg_ids, data=data)
	# Handling errors
	if 'errors' in response:
	    for error, reg_ids in response['errors'].items():
	        # Check for errors and act accordingly
	        if error is 'NotRegistered':
	            # Remove reg_ids from database
	            for reg_id in reg_ids:
	                entity.filter(registration_id=reg_id).delete()
	if 'canonical' in response:
	    for reg_id, canonical_id in response['canonical'].items():
	        # Repace reg_id with canonical_id in your database
	        entry = entity.filter(registration_id=reg_id)
	        entry.registration_id = canonical_id
	        entry.save()
