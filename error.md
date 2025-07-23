Forbidden (403)
CSRF verification failed. Request aborted.

Help
Reason given for failure:

    CSRF token missing.

In general, this can occur when there is a genuine Cross Site Request Forgery, or when Django’s CSRF mechanism has not been used correctly. For POST forms, you need to ensure:

Your browser is accepting cookies.
The view function passes a request to the template’s render method.
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.
You’re seeing the help section of this page because you have DEBUG = True in your Django settings file. Change that to False, and only the initial error message will be displayed.

You can customize this page using the CSRF_FAILURE_VIEW setting.

Request headers
Key Value
Accept text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding gzip, deflate, br, zstd
Accept-Language en-US,en;q=0.9
Connection keep-alive
Cookie => see Request panel
Dnt 1
Host 127.0.0.1:8000
Referer http://127.0.0.1:8000/contact/
Sec-Ch-Ua "Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"
Sec-Ch-Ua-Mobile ?0
Sec-Ch-Ua-Platform "Windows"
Sec-Fetch-Dest document
Sec-Fetch-Mode navigate
Sec-Fetch-Site same-origin
Sec-Fetch-User ?1
Upgrade-Insecure-Requests 1
User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Response headers
Key Value
Content-Length 15699
Content-Type text/html; charset=utf-8
Cross-Origin-Opener-Policy same-origin
Referrer-Policy same-origin
Vary Cookie
X-Content-Type-Options nosniff
X-Frame-Options DENY
WSGI environ
Since the WSGI environ inherits the environment of the server, only a significant subset is shown below.

Key Value
CONTENT_LENGTH
CONTENT_TYPE text/plain
DJANGO_SETTINGS_MODULE task_management.settings
GATEWAY_INTERFACE CGI/1.1
PATH_INFO /
QUERY_STRING
REMOTE_ADDR 127.0.0.1
REMOTE_HOST
REQUEST_METHOD GET
SCRIPT_NAME
SERVER_NAME DESKTOP-9RBRKN6
SERVER_PORT 8000
SERVER_PROTOCOL HTTP/1.1
SERVER_SOFTWARE
