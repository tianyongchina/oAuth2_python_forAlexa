# oAuth2_python_forAlexa
An oAuth2.0 server in python. This demo is used for Alexa Skill's account link.

url = [
    (r'/oa2/auth', Oa2AuthHandle),
    (r'/oa2/token', Oa2TokenHandle),
    (r'/oa2/login', Oa2LoginHandle),
]

其中
/oa2/auth是在skill configuration中的Account Linking中的Authorization URL，
/oa2/token是login.html中登录按钮提交的URL，
/oa2/login是alexa向oauth2 server定期获取token的接口。
