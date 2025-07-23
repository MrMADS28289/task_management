from terminal ->
Method Not Allowed (POST): /users/profile/
[23/Jul/2025 20:17:08] "POST /users/profile/ HTTP/1.1" 405 0
[23/Jul/2025 20:17:08] "GET /**debug**/history_sidebar/?store_id=5c487e4cf82e47f6b1f12e9d5a167757 HTTP/1.1" 200 9813

from DjDT ->
Request headers
Key Value
Accept text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding gzip, deflate, br, zstd
Accept-Language en-US,en;q=0.9
Connection keep-alive
Cookie => see Request panel
Dnt 1
Host 127.0.0.1:8000
Referer http://127.0.0.1:8000/tasks/manager-dashboard/
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
Content-Length 18742
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
PATH_INFO /users/profile/
QUERY_STRING
REMOTE_ADDR 127.0.0.1
REMOTE_HOST
REQUEST_METHOD GET
SCRIPT_NAME
SERVER_NAME DESKTOP-9RBRKN6
SERVER_PORT 8000
SERVER_PROTOCOL
