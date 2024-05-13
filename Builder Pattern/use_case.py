# Article Refrence:
# https://medium.com/@mehar.chand.cloud/builder-design-pattern-use-case-build-http-response-5b109100c7ef

# The Builder design pattern can be used to simplify the creation of HTTP responses by providing a fluent API that allows you to construct the response step by step. This approach promotes code readability and improves maintainability, especially when dealing with complex response configurations.

class Response:
    
    def __init__(self,status_code,headers,body):
        self.status_code=status_code
        self.headers=headers
        self.body=body

    def get_status_code(self):
        return self.status_code
    
    def get_headers(self):
        return self.headers
    
    def get_body(self):
        return self.body

class ResponseBuilder:
    def __init__(self):
        self._statusCode = None
        self._headers = {}
        self._body = ""

    def set_status_code(self, statusCode):
        self._statusCode = statusCode
        return self

    def add_header(self, key, value):
        self._headers[key] = value
        return self

    def set_body(self, body):
        self._body = body
        return self

    def build(self):
        return Response(self._statusCode, self._headers, self._body)

# Example usage
response_builder = ResponseBuilder()
response_builder.set_status_code(200).add_header("Content-Type", "application/json").set_body('{"message": "Hello, world!"}')
response = response_builder.build()

print("Status Code:", response.get_status_code())
print("Headers:", response.get_headers())
print("Body:", response.get_body())

    
