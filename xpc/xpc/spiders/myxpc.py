import scrapy
from ..items import *

class MyxpcSpider(scrapy.Spider):
    name = 'myxpc'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/sort-like?from=navigator']

    def parse(self, response,**wargs):
        
        li_list=response.xpath('//ul[@class="video-list"]/li')
        for li in li_list:
            
            
            duration=li.xpath('./a/span/text()').get()   # 播放时长
            created_at=li.xpath('./a/div[2]/p/text()').get()
            

            pid=li.xpath('./@data-articleid').get() # 作品表主键
            detail_url=f'https://www.xinpianchang.com/a{pid}?from=ArticleList'
            
            posts_dict={'duration':duration,'created_at':created_at}
            
            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail,
                cb_kwargs=posts_dict
                )
        li_list = response.xpath('//ul[@class="video-list"]/li')
        for li in li_list:
            
            duration = li.xpath('.//*[@class="duration fs_12"]/text()').get()   #作品时长
            created_at = li.xpath('.//*[@class="video-hover-con"]/p/text()').get()  # 作品发布时间
            posts_dict={"duration":duration,'created_at':created_at}
            
            detail_url = f'https://www.xinpianchang.com/a{pid}?from=ArticleList'

            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail,
                cb_kwargs=posts_dict
            )
            
    def parse_detail(self,response,**kwargs):
        
        
        
        play_counts=response.xpath('//i[@class="fs_12 fw_300 c_b_6 v-center play-counts"]/@data-curplaycounts').get()
        like_counts=response.xpath('//span[@class="v-center like-counts fs_12 c_w_f fw_300 show"]/@data-counts').get()

        vid=response.xpath('//a[@class="collection-star hollow-star"]/@data-vid').get()
        pid=response.xpath('//a[@class="collection-star hollow-star"]/@data-articleid').get()
        li_list=response.xpath('//div[@class="filmplay-creator right-section"]/ul/li')
        
        video_json_url=f"https://mod-api.xinpianchang.com/mod/api/v2/media/{vid}?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus"             
        comment_json_url=f'https://app2.xinpianchang.com/comments?resource_id={pid}&type=article&page=1&per_page=24&_=1630484185569'
        
        update_dict={'play_counts':play_counts,'like_counts':like_counts}
        kwargs.update(update_dict)
        

        # 视频数据 Posts
        yield scrapy.Request(
                url=video_json_url,
                callback=self.parse_video,
                cb_kwargs=kwargs
                )
        
        # 评论数据 Comment
        yield scrapy.Request(
            url=comment_json_url,
            callback=self.parse_comment
            )
        
        for li in li_list:
            href=li.xpath('./a/@href').get()
            author_url=f'https://www.xinpianchang.com{href}'
            
            yield scrapy.Request(
                url=author_url,
                callback=self.parse_composers
                )
              
    def parse_video(self,response,**kwargs):
        result=response.json()
        pid=result['data']['mid']  # 作品表主键
        title=result['data']['title']  # 作品标题
        thumbnail=result['data']['cover']  # 视频缩略图
        category=result['data']['categories']# 作品分类
        description=result['data']['description']   # 作品描述
        preview=result['data']['resource']['sprite']['images']          # 视频预览图
        video=result['data']['resource']['progressive'][0]['url']        #视频链接
        video_format =result['data']['resource']['progressive'][0]['profile']                    # 视频格式：4K 等
        

        yield PostsItem(duration=kwargs['duration'],created_at=kwargs['created_at'],
                        play_counts=kwargs['play_counts'],like_counts=kwargs['like_counts'],
                        pid=pid,title=title,
                        thumbnail=thumbnail,category=category,
                        description=description,preview=preview,
                        video=video,video_format=video_format
                        )
            
    def parse_comment(self,response,**kwargs):
        result=response.json()
        comment_list=result['data']['list']
        for comment in comment_list:
            commentid=comment['userInfo']['id']
            pid=comment['resource_id']
            cid=comment['userid']
            avatar=comment['userInfo']['avatar']
            uname=comment['userInfo']['username']
            created_at=comment['userInfo']['addtime']
            content=comment['content']
            like_counts=comment['userInfo']['count']['count_liked']
            reply=comment['referid']
            
            yield ComposersItem(commentid=commentid,pid=pid,
                                cid=cid,avatar=avatar,
                                uname=uname,created_at=created_at,
                                content=content,like_counts=like_counts,
                                reply=reply
                                )
            
            
            
    def parse_composers(self,response,**kwargs):
        
        cid=response.xpath('//div[@class="creator-info-wrap"]/div[1]/div[1]/a[3]/@data-userid').get()
        banner=response.xpath('//div[@class="banner-container"]/div[1]/@style').get()
        avatar=response.xpath('/html/body/div[8]/div[2]/div/div/span/img/@src').get()
        if  response.xpath('/html/body/div[8]/div[2]/div/div/span/span/@class'):
            verified='Yes'
        else:
            verified='No'
        name=response.xpath('/html/body/div[8]/div[3]/div/p[1]/text()').get()
        intro=response.xpath('/html/body/div[8]/div[3]/div/p[2]/text()').get()
        like_counts=response.xpath('/html/body/div[8]/div[3]/div/p[3]/span[1]/span[2]/text()').get()
        fans_counts=response.xpath('/html/body/div[8]/div[3]/div/p[3]/span[2]/span[2]/text()').get()
        follow_counts=response.xpath('/html/body/div[8]/div[3]/div/p[3]/span[3]/span[2]/text()').get()
        location=response.xpath('/html/body/div[8]/div[3]/div/p[3]/span[5]/text()').get()
        career=response.xpath('/html/body/div[8]/div[3]/div/p[3]/span[7]/text()').get()
        
        yield ComposersItem(cid=cid, banner=banner, avatar=avatar, verified=verified,
                            name=name,intro=intro,like_counts=like_counts,
                            fans_counts=fans_counts,follow_counts=follow_counts,
                            location=location,career=career
                            )
        
            
            
            
            
            
            
            
            
            
            