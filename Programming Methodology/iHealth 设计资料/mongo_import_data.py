#coding=utf8
import datetime
import hashlib
import random
import sys
import pymongo
from bson.objectid import ObjectId

MONGO_HOST = '123.56.8.91'
MONGO_PORT = 27017
MONGO_DBNAME = 'iHealth'
MONGO_AUTHDB = 'iHealth'
MONGO_USER = 'admin'
MONGO_PWD = 'admin123'

def MD5(s):
    '''对字符串s进行md5加密，并返回'''
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

# 连接数据库
client = pymongo.MongoClient('mongodb://%s:%s@%s:%d/%s'%(MONGO_USER,MONGO_PWD,MONGO_HOST,MONGO_PORT,MONGO_AUTHDB))

# 切换数据库
db = client[MONGO_DBNAME]


# 清除集合
# db.articles.drop()
db.users.drop()


# 获取集合
articles = db.articles
users = db.users

# 插入数据
# 创建md5对象
# m = hashlib.md5()

# 插入 article 集合数据
# 资讯标题：title
# 发布时间：pubdate
# 发布人：username*
# 内容：content

# print '插入 articles 集合数据……'
# article_list = []
# article_list.append({
#     'title' : '跑步时出现这3大信号，一定要当心！可能是猝死前兆！',
#     'category' : '养生常识',
#     'read' : 0,
#     'upvote' : 0,
#     'publisher' : '中华养生网',
#     'publisher_src' : 'http://www.cnys.com/',
#     'href' : 'http://www.cnys.com/zixun/74403.html',
#     'pubdate' : datetime.datetime.now(),
#     'img' : 'http://img.cnys.com/upload/picture/2017/10-19/Z08l2d.gif',
#     'intro' : '''近年全民热跑，马拉松赛事开展得如火如荼。
# 这本是好事，却发生了伤心事——“平常没病没痛”的青壮年，跑着跑着就倒下猝死了。
# ''',
#     'content' : '''
# <div class="reads">
#     <p>近年全民热跑，马拉松赛事开展得如火如荼。</p><p>这本是好事，却发生了伤心事——“平常没病没痛”的青壮年，跑着跑着就倒下猝死了。</p><h3><strong>跑步猝死，这是怎么回事?</strong></h3><p>青壮年猝死大多因为心脏的问题——冠心病、心律失常、先天性心脏病等。</p><p>原因：有心脏病，自己却不知道</p><p>运动猝死者多有冠心病，这是运动猝死第一病因，只是他自己不知道。</p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-19/Z08l2d.gif" alt=""></p></center><p>如今冠心病发病年龄大大提前，二三十岁的冠心病患者很多，因为饮食、抽烟、压力方面的原因。</p><p>其中，很多人平时即使有不舒服，也不觉得是心脏问题，更不会去检查，这就留下了运动猝死的隐患。</p><p><strong>信号1： 胸部压迫感+运动后加重</strong></p><p>胸部有压迫感，就是胸闷。它会在运动后(包括快走、上楼梯)以及情绪激动后加重。</p><p>闷，多代表心脏供血不足——给心脏提供血液的冠状动脉出问题了。</p><p>严重胸闷，是冠心病的征兆。若是运动后胸闷缓解了，就不用担心，因为冠心病的胸闷一定不会在运动后减轻。</p><p>另外，跑步时出现胸闷要尽快看医生，别以为休息一下就能好。</p><p>怎么办?</p><p>做活动平板运动试验，各大医院都有。</p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-19/cOCh6Z.jpg" alt=""></p></center><p>在类似跑步机上的仪器上跑步，检测运动时的心率，并记录心电图。</p><p>跑步时间一般不超过10分钟，有专人在旁监护，如果跑的过程中，心脏不舒服了，就会被喊停。</p><p>之后，将跑的时长、跑到多少心率会有不适等指标综合起来，判断心肌是否缺血。</p>
# </div>
#     '''
# })
# article_list.append({
#     'title' : '预防腰椎间盘突出，做好这5点！',
#     'category' : '养生常识',
#     'read' : 0,
#     'upvote' : 0,
#     'publisher' : '中华养生网',
#     'publisher_src' : 'http://www.cnys.com/',
#     'href' : 'http://www.cnys.com/xinde/74390.html',
#     'pubdate' : datetime.datetime.now(),
#     'img' : 'http://img.cnys.com/upload/picture/2017/10-19/6FeA8X.jpg',
#     'intro' : '''腰椎间盘突出症是我们的生活中比较常见的一种疾病，对于这样的一种疾病有什么比较好的治疗方法呢?
# ''',
#     'content' : '''
# <div class="reads">
#     <p>腰椎间盘突出症是我们的生活中比较常见的一种疾病，对于这样的一种疾病有什么比较好的治疗方法呢?</p><p><strong>1、注意保暖。</strong></p><p>腰部受凉后会诱发、加重腰椎间盘突出。</p><p><strong>2、正确用腰。</strong></p><p>搬抬重物，先做好准备姿势，不要突然用力;搬提重物尽可能双侧用力;弯腰捡东西时候先蹲下等。</p><p><strong>3、避免久坐、适当活动。</strong></p><p>不端正坐姿时，腰椎处于后弯的位置，腰部肌肉韧带均处在紧张状态，腰椎间盘承受的压力增大10倍!坐办公室的亲可以多喝水，然后会尿急上厕所，然后需要再接水，强迫自己时不时就动起来。(亲测有效)</p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-19/6FeA8X.jpg" alt=""></p></center><p><strong>4、少穿高跟鞋。</strong></p><p>高跟鞋使身体的重心相对提高，人体为了稳定重心平衡，腰背部肌肉的张力会重新调整，一直处于紧绷状态，如果已经腰椎间盘突出，基本需要告别穿高跟鞋。</p><p><strong>5、有外伤及时治疗。</strong></p><p>外伤如果治疗不及时可能造成慢性损伤，诱发腰椎间盘突出。我们的小绵羊就是因为长期反复的外力(如绑沙袋)造成轻微损害，又没有及时的治疗，最后造成了永久的损伤。</p>
# </div>
#     '''
# })
# article_list.append({
#     'title' : '别说你不信，水果还真能伤牙！',
#     'category' : '养生常识',
#     'read' : 0,
#     'upvote' : 0,
#     'publisher' : '中华养生网',
#     'publisher_src' : 'http://www.cnys.com/',
#     'href' : 'http://www.cnys.com/zixun/74382.html',
#     'pubdate' : datetime.datetime.now(),
#     'img' : 'http://img.cnys.com/upload/picture/2017/10-19/9AKi8Q.jpg',
#     'intro' : '''和蔬菜比起来，广大的人民群众似乎更喜欢水果，主要是因为甜!甜!甜!问题是，水果里的糖会引起蛀牙吗?这绝对是个问题!
# 水果有很多种吃法，主要有新鲜水果、水果罐头、果汁、干果、果脯和果酱等。水果对牙齿好不好，要看怎么吃!
# ''',
#     'content' : '''<div class="reads">
#                     <p>和蔬菜比起来，广大的人民群众似乎更喜欢水果，主要是因为甜!甜!甜!问题是，水果里的糖会引起蛀牙吗?这绝对是个问题!</p><p>水果有很多种吃法，主要有新鲜水果、水果罐头、果汁、干果、果脯和果酱等。水果对牙齿好不好，要看怎么吃!</p><p align="left"></p><h3><strong>新鲜水果对牙齿好吗?</strong></h3><br><center></center><p>看起来这可能是违反直觉，确实含有很多糖的水果确实对牙齿有好处。但是，新鲜水果只有作为平衡膳食的一部分，才对牙齿有好处。</p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-19/9AKi8Q.jpg" alt=""></p></center><p>如果你整天只吃水果，对牙齿就不是那么好了。当经常吃水果时，比如每天吃17次(真有人这么干!)，那么水果就可能引起蛀牙。原因除了水果的糖分外，还有粘在牙齿上未及时清除的水果碎屑。</p><p>然而，如果只是午饭或晚饭后吃一些新鲜水果，没有证据显示水果会引起蛀牙。新鲜水果含有多种维生素，对改善口腔健康有好处。</p><p align="left"></p><h3><strong>水果罐头对牙齿好吗?</strong></h3><br><center></center><p>如今市场上大多数水果罐头，是浸泡在富含糖的浓缩糖浆中的。由于这些添加的糖，水果罐头可能对牙齿非常有害。</p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-19/CNHd0e.jpg" alt=""></p></center><p>在吃水果罐头之前，看看成分表上是否含有糖。大多数水果罐头也会在成分表上说明含有浓缩糖浆或者稀释糖浆。这就说明这些产品含有过量的糖!</p>
#                 </div>
#     '''
# })
# article_list.append({
#     'title' : '头晕眼花失眠健忘都是肾气不足！快用这3个方法给肾打打气！',
#     'category' : '养生常识',
#     'read' : 0,
#     'upvote' : 0,
#     'publisher' : '中华养生网',
#     'publisher_src' : 'http://www.cnys.com/',
#     'href' : 'http://www.cnys.com/zixun/74365.html',
#     'pubdate' : datetime.datetime.now(),
#     'img' : 'http://img.cnys.com/upload/picture/2017/10-18/SH8mQS.jpg',
#     'intro' : '''头昏眼花、视力模糊、还是失眠健忘，你以为是感冒了、发烧了、还是的表示自己老了?其实还有一种可能，那就是肾气不足!
# ''',
#     'content' : '''<div class="reads">
#                     <p>头昏眼花、视力模糊、还是失眠健忘，你以为是感冒了、发烧了、还是的表示自己老了?其实还有一种可能，那就是肾气不足!</p><h3><strong>那么肾气不足会怎么样</strong></h3><p><strong>第一，便秘</strong></p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-18/SH8mQS.jpg" alt=""></p></center><p>为什么越来越容易便秘?因为老人更容易肾气不足，中医说“肾司二便”，所以便秘、腹泻、小便不利都与肾有关。</p><p>除了便秘之外，肾气不足还会表现为腹泻，一般发生在天亮之前，也称之为“五更泻”。</p><p><strong>第二，发育迟缓</strong></p><p>在中医里有一种说法叫做“肾气不足型五迟”，所谓“五迟”指的是发育迟缓，表现为筋骨软弱、出牙迟、语言迟、坐不稳等。</p><p><strong>第三，耳鸣、精力不济</strong></p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-18/pv4TS9.jpg" alt=""></p></center><p>通常会表现为听力下降、耳鸣、工作效率低、注意了不集中。</p><p><strong>第四，腰酸背痛</strong></p><p>这几乎是所有肾气不足人群的共同症状，尤其在过度劳累之后，腰痛、膝盖酸软会表现得很明显。</p><p><strong>第五，脱发、色斑、黑眼圈</strong></p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-18/zVZkhl.jpg" alt=""></p></center><p>女性关注的外貌问题，也会受到肾气不足的影响，表现为白发增多、头发不再有光泽、出现黑眼圈、黄褐斑，甚至还会伴有月经不调。</p><p><strong>第六，畏寒怕冷、抵抗力差</strong></p><p>肾气不足的女性更容易畏寒怕冷，即使穿得多，在冬季仍然会表现为手脚冰凉、整夜双脚不温暖。也容易感冒、咳嗽。点击蓝字了解更多肾虚小常识：肾阳虚吃什么好 这些廉价食物让你“阳”气十足</p><p><strong>第七，出现睡眠问题</strong></p><center><p align="center"><img src="http://img.cnys.com/upload/picture/2017/10-18/8Fo43X.jpg" alt=""></p></center><p>表现为没精神，还会表现为难以入睡、睡眠质量低、易惊醒、容易烦躁等。此外，肾气不足还会表现为早衰、健忘、食欲不振、乏力、不耐疲劳以及牙齿过早松动。</p>
#                 </div>
#     '''
# })
# res = articles.insert_many(article_list)
# print res
# print ''

# 插入 users 集合数据
# 字段说明：
# # 必填
# 'nickname' : 昵称
# 'email' : 邮箱地址
# 'password' : 密码
# 'sex' : 性别（取值：0-女，1-男）
# 'birthday' : 出生日
# # 选填
# 'name' : 真实姓名
# 'phone' : 手机号
# 'introduction' : 个人介绍
# # 系统自动生成
# 'age' : 年龄
# 'usertype' : 用户类型（取值：0-游客，1-患者，2-医生，3-管理员）
user_list = []
user_list.append({
	# 必填
	'nickname' : '看病的小明',
	'email' : '123456789@qq.com',
	'password' : MD5('123456'),
	'sex' : 1,
	'birthday' : '1994-3-30',
	# 选填
	'name' : '杨英明',
	'phone' : '12345678901',
	'introduction' : '大家好，我是来看病的',
	# 系统自动生成
	'age' : 23,
	'usertype' : 1,	
})
user_list.append({
	# 必填
	'nickname' : '资深医生华仔',
	'email' : '987654321@qq.com',
	'password' : MD5('123456'),
	'sex' : 1,
	'birthday' : '1974-5-30',
	# 选填
	'name' : '李华',
	'phone' : '12345678902',
	'introduction' : '大家好，我会看病',
	# 系统自动生成
	'age' : 43,
	'usertype' : 2,	
})
user_list.append({
	# 必填
	'nickname' : '明天会更好',
	'email' : '987654322@qq.com',
	'password' : MD5('123456'),
	'sex' : 1,
	'birthday' : '1994-1-30',
	# 选填
	'name' : '王大锤',
	'phone' : '12345678903',
	'introduction' : '大家好，我叫王大锤',
	# 系统自动生成
	'age' : 27,
	'usertype' : 1,	
})
res = users.insert_many(user_list)
print res
print ''


"""
# 插入 site 集合数据
print '插入 site 集合数据……'
site = []
site.append({
    'title' : '百度',
    'url'   : 'https://www.baidu.com/',
    'desc': '百度搜索引擎',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '哔哩哔哩',
    'url'   : 'https://www.bilibili.com/',
    'desc': '国内弹幕网站 - B站',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : 'Github',
    'url'   : 'https://github.com/',
    'desc': 'GitHub 是一个面向开源及私有软件项目的托管平台',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : 'Readfree',
    'url'   : 'http://readfree.me/',
    'desc': '一个 kindle 电子书资源站',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '知乎',
    'url'   : 'https://www.zhihu.com/',
    'desc': '知乎- 与世界分享你的知识、经验和见解',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '博客园',
    'url'   : 'https://www.cnblogs.com/',
    'desc': '博客园 - 代码改变世界',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : 'Google',
    'url'   : 'https://www.google.com/',
    'desc': '谷歌搜索 - 全球最大的搜索引擎',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '网易云音乐',
    'url'   : 'http://music.163.com/',
    'desc': '网易云音乐 - 分享你的音乐',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '王垠 - 当然我在扯淡',
    'url'   : 'http://www.yinwang.org/',
    'desc': '王垠的博客',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '书荒部落',
    'url'   : 'https://noveless.com/',
    'desc': '书荒部落',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : 'AcFun',
    'url'   : 'http://www.acfun.cn/',
    'desc': 'AcFun - 认真你就输啦',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '呓语 - 杨英明的个人博客',
    'url'   : 'http://www.yangyingming.com/',
    'desc': '专注于c++、Python，欢迎交流',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '新浪微博',
    'url'   : 'http://weibo.com',
    'desc': '新浪微博 - show 出你的生活',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '优酷',
    'url'   : 'http://www.youku.com/',
    'desc': '视频服务平台,提供视频播放,视频发布',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})
site.append({
    'title' : '爱奇艺',
    'url'   : 'http://www.iqiyi.com/',
    'desc': '全球领先的提供海量、优质、高清的网络视频服务的大型视频网站',
    'create_timestamp' : datetime.datetime.now(),
    'favorite_this_site' : [],
    'tags' : []
})

# 初始化每个站点的用户收藏列表
print '初始化每个站点的用户收藏列表……'
for i in range(len(site)):
	for j in range(10):	# 每个站没多少人收藏
	    user_no = int(random.random()*len(user))
	    print '站点 %s 被用户 %s 收藏'%(site[i]['title'],users.find()[user_no]['nickname'].encode('utf8'))
	    site[i]['favorite_this_site'].append(users.find()[user_no]['_id'])

res = sites.insert_many(site)
print res
print ''


# 插入 tag 集合数据
print '插入 tag 集合数据……'
tag = []
tag.append({
    'title' : '搜索引擎',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '弹幕网站',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : 'ACG',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '视频',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '开源社区',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '社交',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '程序员',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '资源',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '电子书',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '问答社区',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '博客',
    'create_timestamp' : datetime.datetime.now()
    })
tag.append({
    'title' : '音乐',
    'create_timestamp' : datetime.datetime.now()
    })

# 向 mongo 插入数据
res = tags.insert_many(tag)
print res
print ''

print '初始化每个网站的标签列表……'

def siteAppendTag(site_name,*tag_name_list):
	'''为找到的第一个匹配网站标签列表中添加标签'''
	for tag_name in tag_name_list:
		item = sites.find({'title':site_name})[0]
		if tags.find({'title':tag_name})[0]['_id'] in item['tags']:
			# 该网站已经添加过该标签了
			continue
		item['tags'].append(tags.find({'title':tag_name})[0]['_id'])
		sites.save(item)

siteAppendTag('百度','搜索引擎')
siteAppendTag('哔哩哔哩','弹幕网站','ACG','视频')
siteAppendTag('Github','开源社区','社交','程序员')
siteAppendTag('Readfree','资源','电子书')
siteAppendTag('知乎','问答社区','社交')
siteAppendTag('博客园','博客')
siteAppendTag('Google','搜索引擎')
siteAppendTag('网易云音乐','音乐','社交')
siteAppendTag('王垠 - 当然我在扯淡','博客')
siteAppendTag('书荒部落','资源')
siteAppendTag('AcFun','弹幕网站','ACG','视频')
siteAppendTag('呓语 - 杨英明的个人博客','博客')
siteAppendTag('新浪微博','社交')
siteAppendTag('优酷','视频','社交')
siteAppendTag('爱奇艺','视频','社交')

# 列出热门标签
for tag in tags.find():
	print '标签 %s 被标记过 %d 次'%(tag['title'].encode('utf8'),sites.find({'tags':tag['_id']}).count())

# 列出每个站被多少人收藏过
for site in sites.find():
	print '网站 %s 被 %d 人收藏过'%(site['title'].encode('utf8'),len(site['favorite_this_site']))




"""