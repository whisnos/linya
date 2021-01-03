from webhandler import basehandler
import tornado.web

from webhandler.authbind import AuthVerifyHandler, AuthVerifyCheckHandler
from webhandler.paycallback import OrderJsapiReceiveHandler
from webhandler.public import PublicAreaCommunityHandler, PublicMarketPoolsHandler, PublicMarketAnswersHandler, \
    PublicRentPoolsHandler, PublicIndexBannerHandler, PublicIndexSearchHandler, PublicCardPoolsHandler, \
    PublicAcessWSHandler, PublicPayHandler, PublicUploadIMGHandler, PublicTaobaoHandler, PublicCityIdHandler
from webhandler.user import RegisterHandler, UserADpoolsHandler, UserCommunityListHandler, UserADpoolsMakeMoneyHandler, \
    UserADpoolDetailHandler, UserBSpoolsHandler, UserMyMoneyRecordHandler, UserMyADListHandler, UserDeitMyADHandler, \
    UserEditMyMarketHandler, UserEditMyRentHandler, UserMsgListHandler, UserMsgDetailHandler, UserCreateMsgHandler, \
    UserCardPoolsListHandler, UserEditMyCardHandler, UserMyMoneyHandler, UserMoneyWithdrawHandler


class MainHandler(basehandler.BaseHandler):
    def get(self):
        # print(self.request.body, self.request.query)
        self.write("Hello, get!")

    def post(self):
        # print(self.request.body, self.request.query)
        self.write("Hello, post!")

class CheckHandler(basehandler.BaseHandler):
    def get(self):
        # print(self.request.body, self.request.query)
        self.write("c3b86c5d62c4e4ed007df9cc122a16a0")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/pAG1aHQVqA.txt$", CheckHandler),
        (r"/public/indexbanner", PublicIndexBannerHandler),         # POST获取首页轮播图
        (r"/public/search", PublicIndexSearchHandler),              # 首页搜索
        (r"/public/cityid", PublicCityIdHandler),              # 首页搜索
        (r"/public/areacommunity", PublicAreaCommunityHandler),     # GET区下的小区 POST绑定小区
        (r"/user/adpools", UserADpoolsHandler),                     # GET广告池 POST发布广告
        (r"/user/adpooldetail", UserADpoolDetailHandler),           # GET广告领取记录 前10
        (r"/user/admakemoney", UserADpoolsMakeMoneyHandler),        # POST领
        (r"/user/myrecord", UserMyMoneyRecordHandler),              # POST个人资金记录
        (r"/user/myadlist", UserMyADListHandler),                   # GET个人AD贴
        (r"/user/mymoney", UserMyMoneyHandler),                     # GET个人余额
        (r"/user/withdraw", UserMoneyWithdrawHandler),              # post提现
        # 私信
        (r"/user/msglist", UserMsgListHandler),                     # GET个人私信列表
        (r"/user/msgdetail", UserMsgDetailHandler),                 # POST个人私信详情
        (r"/user/createmsg", UserCreateMsgHandler),                 # POST创建个人私信
        (r"/ope/editmyad", UserDeitMyADHandler),                    # 编辑个人AD贴 get put delete
        (r"/ope/editmymarket", UserEditMyMarketHandler),            # 编辑个人置换贴 get put delete
        (r"/ope/editmyrent", UserEditMyRentHandler),                # 编辑个人租赁贴 get put delete
        (r"/ope/editmycard", UserEditMyCardHandler),                # 编辑个人名片榜 put delete
        # (r"/user/bspools", UserBSpoolsHandler),                   # GET业务池 POST发布业务
        (r"/user/communitylist", UserCommunityListHandler),         # GET展示用户绑定的小区信息 POST绑定小区
        (r"/user/cardlist", UserCardPoolsListHandler),              # GET展示用户名片信息 POST创建名片
        # 置换
        (r"/public/marketpools", PublicMarketPoolsHandler),         # GET置换池 POST发布置换
        (r"/public/marketanswers", PublicMarketAnswersHandler),     # GET置换池回帖内容 POST回复置换
        # 租赁
        (r"/public/rentpools", PublicRentPoolsHandler),             # GET租赁池 POST发布租赁
        # 名片榜
        (r"/public/cardpools", PublicCardPoolsHandler),             # GET名片池
        (r"/public/uploadimg", PublicUploadIMGHandler),             # 上传图片api

        # (r"/user/login", LoginHandler),                           # 登录
        # (r"/user/register", RegisterHandler),                     # 注册
        # (r"/user/login", LoginHandler),                           # 登录
        (r"/auth/check", AuthVerifyCheckHandler),                   # 是否登录检查
        (r"/auth/verify", AuthVerifyHandler),                       # 授权登录
        (r"/public/access", PublicAcessWSHandler),                  # ws私信
        (r"/public/pay", PublicPayHandler),                         #
        (r"/api/callback", OrderJsapiReceiveHandler),                         #
        (r"/public/taobao", PublicTaobaoHandler),                         #
        ],
    )