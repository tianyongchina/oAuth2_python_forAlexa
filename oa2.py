#!/usr/bin/python
# -*- coding: utf-8 -*-


import tornado.web
import reply
import receive
import json
from log import logging
import datetime



import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../')


class Oa2AuthHandle(tornado.web.RequestHandler):
    def get(self):
        try:
            webData = self.request.body
            logging.info("Oa2AuthHandle, webdata is: %s" % (webData))

            state = self.get_argument("state", None)
            client_id = self.get_argument("client_id", None)
            response_type = self.get_argument("response_type", None)
            scope = self.get_argument("scope", None)
            redirect_uri = self.get_argument("redirect_uri", None)
            self.render("login.html", state=state, client_id=client_id, response_type=response_type, scope=scope, redirect_uri=redirect_uri)

        except Exception, Argument:
            self.write(Argument.message)
            logging.error(Argument.message)


class Oa2LoginHandle(tornado.web.RequestHandler):
    '''
    def set_default_headers(self):
        logging.info("setting headers!!!")
        # self.set_header("Access-Control-Allow-Origin", "https://projectx.ling.cn")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        logging.info("options!!!")
        # self.set_default_headers()
        self.set_status(204)
        self.finish()
    '''

    def get(self):
        try:
            webData = self.request.body
            logging.info("Oa2LoginHandle, webdata is: %s" % (webData))

            user = self.get_argument("user", None)
            pwd = self.get_argument("pwd", None)
            state = self.get_argument("state", None)
            client_id = self.get_argument("client_id", None)
            response_type = self.get_argument("response_type", None)
            scope = self.get_argument("scope", None)
            redirect_uri = self.get_argument("redirect_uri", None)

            if user != None:
                resp = 'errors'
                # resp = OtherAuthServer().login(user, pwd) #对用户名和密码进行校验
                if 'errors' in resp:
                    self.write("user name or password is wrong")
                else:
                    # 返回code
                    code = user
                    redirect_uri = redirect_uri + '?code=' + code + '&state=' + state
                    logging.info("Oa2LoginHandle, redirect_uri is: %s" % (redirect_uri))
                    self.write(redirect_uri)
                    # self.redirect(redirect_uri)
            else:
                self.write("user name can't be empty")
        except Exception, Argument:
            self.write(Argument.message)
            logging.error(Argument.message)


class Oa2TokenHandle(tornado.web.RequestHandler):
    def post(self):
        try:
            webData = self.request.body
            logging.info("Oa2TokenHandle, webdata is: %s" % (webData))

            # 增加对code和client_id的校验代码，返回access_token和refresh_token
            code = self.get_argument("code", None)
            client_id = self.get_argument("client_id", None)
            access_token = "aaaaaaaaaaaaaaa"
            refresh_token = "tGzv3JOkF0XG5Qx2TlKWIA"
            resp = {
                "access_token": access_token,
                "token_type": "Bearer",
                "expires_in": 3600*24*7,
                "refresh_token": refresh_token
            }
            self.write(json.dumps(resp))
        except Exception, Argument:
            self.write(Argument.message)
            logging.error(Argument.message)

