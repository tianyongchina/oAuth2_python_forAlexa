# oAuth2_python_forAlexa
An oAuth2.0 server in python. This demo is used for Alexa Skill's account link.

url = [
    (r'/oa2/auth', Oa2AuthHandle),
    (r'/oa2/token', Oa2TokenHandle),
    (r'/oa2/login', Oa2LoginHandle),
]

其中
/oa2/auth是在skill configuration中的Account Linking中的Authorization URL，
/oa2/login是login.html中登录按钮提交的URL，
/oa2/token是alexa向oauth2 server定期获取token的接口。

具体流程是：
1、用户在alexa app上enable你开发的skill的时候，会调用/oa2/auth接口，进入到login.html页面（你的系统的登录页面）；
2、用户使用你系统的账号和密码登录，点击connect，调用/oa2/login；
3、在/oa2/login进行用户密码校验，成功之后返回重定向页面（alexa的提示页面），同时返回一个code（你自定义，和user产生关联就好）；
4、alexa调用/oa2/token定期获取token，你需要进行code和client_id等校验，然后返回tocken和refreshtoken。这个token会在skill中每个请求的scope/token。这样就能确定每次你的skill收到的信息是哪个用户发来的了；
5、enable skill完了之后，会有一个discover的动作。你只需要在skill里面处理discover指令，返回对应token（用户）下面的device列表即可。
