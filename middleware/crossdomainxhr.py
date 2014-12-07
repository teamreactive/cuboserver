from django import http 
 
class XsSharing(object):
	"""
	This middleware allows cross-domain XHR using the html5 postMessage API.
	 
	Access-Control-Allow-Origin: http://foo.example
	Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE

	Based off https://gist.github.com/426829
	"""
	def process_request(self, request):
		if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
			response = http.HttpResponse()
			response['Access-Control-Allow-Origin']  = "*"
			response['Access-Control-Allow-Methods'] = "POST, GET, HEAD, OPTIONS, PUT, UPDATE, DELETE" 
			response['Access-Control-Allow-Headers'] = "Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
			response['Access-Control-Allow-Credentials'] = "true"
			return response
 
		return None
 
	def process_response(self, request, response):
		response['Access-Control-Allow-Origin']  = "*"
		response['Access-Control-Allow-Methods'] = "POST, GET, HEAD, OPTIONS, PUT, UPDATE, DELETE"
		response['Access-Control-Allow-Headers'] = "Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
		response['Access-Control-Allow-Credentials'] = "true"
 
		return response


class DisableCSRF(object):
	def process_request(self, request):
		setattr(request, '_dont_enforce_csrf_checks', True)