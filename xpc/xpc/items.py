# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    table_name = 'posts'
    duration=scrapy.Field() # 播放时长
    created_at=scrapy.Field() # 发表时间
    play_counts=scrapy.Field()  # 播放次数
    like_counts=scrapy.Field() # 被点赞次数
    pid=scrapy.Field() # 作品表主键
    title=scrapy.Field() # 作品标题
    thumbnail = scrapy.Field() # 视频缩略图
    category =scrapy.Field()# 作品分类
    description=scrapy.Field() # 作品描述
    preview=scrapy.Field()      # 视频预览图
    video=scrapy.Field()          # 视频链接
    video_format=scrapy.Field()  # 视频格式：4K 等
    

class ComposersItem(scrapy.Item):
    
    table_name='comments'
    commentid=scrapy.Field()  #评论表主键
    pid=scrapy.Field()        #评论的作品ID
    cid=scrapy.Field()        #评论人ID
    avatar=scrapy.Field()    #评论人头像
    uname=scrapy.Field()      #评论人名称
    created_at=scrapy.Field()  #发表时间
    content=scrapy.Field()    #'评论内容
    like_counts=scrapy.Field()  #被点赞次数
    reply=scrapy.Field()       #回复其他评论的ID，如果不是则为0',
    

class ComposersItem(scrapy.Item):
    
    table_name='composers'
    cid=scrapy.Field()  #创作者表主键
    banner=scrapy.Field()        #用户主页banner图片
    avatar=scrapy.Field()        #用户头像
    verified=scrapy.Field()    #是否加V
    name=scrapy.Field()      #名字
    intro=scrapy.Field()  #自我介绍
    like_counts=scrapy.Field()    #'被点赞次数
    fans_counts=scrapy.Field()  #被关注数量
    follow_counts=scrapy.Field()       #关注数量
    location=scrapy.Field()      #所在位置
    career=scrapy.Field()       #职业
    