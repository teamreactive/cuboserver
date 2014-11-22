from string import upper
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpMethodNotAllowed

class CORSResource(object):

	def create_response(self, *args, **kwargs):
		response = super(CORSResource, self).create_response(*args, **kwargs)
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Headers"] = "Content-Type"
		return response

	def method_check(self, request, allowed=None):
		if allowed is None:
			allowed = []

		request_method = request.method.lower()
		allows = ",".join(map(str.upper, str(allowed)))

		if request_method == "options":
			response = HttpResponse(allows)
			response["Access-Control-Allow-Origin"] = "*"
			response["Access-Control-Allow-Headers"] = "Content-Type"
			response["Allow"] = allows
			raise ImmediateHttpResponse(response=response)

		if not request_method in allowed:
			response = http.HttpMethodNotAllowed(allows)
			response["Allow"] = allows
			raise ImmediateHttpResponse(response=response)

		return request_method