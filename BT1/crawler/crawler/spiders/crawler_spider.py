from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import random

class CrawlerSpider(Spider):
    
    name = "crawler"
    allowed_domains = [""]
    start_urls = [
        "https://baochinhphu.vn/thu-tuong-tiep-xuc-cu-tri-sau-ky-hop-thu-7-quoc-hoi-khoa-xv-102240714091408531.htm",
        "https://baochinhphu.vn/chuyen-tham-lao-campuchia-cua-chu-tich-nuoc-to-lam-thanh-cong-ve-moi-mat-102240714095636811.htm",
        "https://baochinhphu.vn/thu-tuong-quyet-tam-hoan-thanh-khoang-1200-km-cao-toc-cho-dbscl-102240713123625832.htm",
        "https://baochinhphu.vn/thu-tuong-yeu-cau-chu-dong-kiem-soat-ngan-chan-khong-de-lay-lan-bung-phat-benh-bach-hau-102240713190723044.htm",
        "https://baochinhphu.vn/thu-tuong-phan-dau-dua-cac-cao-toc-tai-dbscl-vuot-tien-do-102240713203951085.htm",
        "https://baochinhphu.vn/viet-nam-la-diem-den-dau-tu-quan-trong-trong-trung-va-dai-han-102240714113309146.htm",
        "https://baochinhphu.vn/thu-tuong-yeu-cau-tap-trung-khac-phuc-su-co-sat-lo-dat-tai-ha-giang-102240713112906458.htm",
        "https://baochinhphu.vn/vi-pham-hanh-chinh-trong-quan-ly-gia-bi-phat-toi-300-trieu-dong-102240713172527174.htm",
        "https://baochinhphu.vn/chu-tich-nuoc-to-lam-ket-thuc-tot-dep-chuyen-tham-cap-nha-nuoc-toi-campuchia-102240713200155921.htm",
        "https://baochinhphu.vn/ky-hop-thu-7-cua-quoc-hoi-khang-dinh-tinh-than-doan-ket-dan-chu-ky-cuong-va-trach-nhiem-rat-cao-102240714114613586.htm",

        "https://kpl.gov.la/detail.aspx?id=84232",
        "https://kpl.gov.la/detail.aspx?id=84231",
        "https://kpl.gov.la/detail.aspx?id=84230",
        "https://kpl.gov.la/detail.aspx?id=84229",
        "https://kpl.gov.la/detail.aspx?id=84228",
        "https://kpl.gov.la/detail.aspx?id=84227",
        "https://kpl.gov.la/detail.aspx?id=84226",
        "https://kpl.gov.la/detail.aspx?id=84225",
        "https://kpl.gov.la/detail.aspx?id=84224",
        "https://kpl.gov.la/detail.aspx?id=84223",
        "https://kpl.gov.la/detail.aspx?id=84222",
        "https://kpl.gov.la/detail.aspx?id=84221",
        "https://kpl.gov.la/detail.aspx?id=84220",
        "https://kpl.gov.la/detail.aspx?id=84211",
        "https://kpl.gov.la/detail.aspx?id=84219",
        "https://kpl.gov.la/detail.aspx?id=84218",
        "https://kpl.gov.la/detail.aspx?id=84217",
        "https://kpl.gov.la/detail.aspx?id=84216",
        "https://kpl.gov.la/detail.aspx?id=84215",
        "https://kpl.gov.la/detail.aspx?id=84214",
        "https://kpl.gov.la/detail.aspx?id=84213",
        "https://kpl.gov.la/detail.aspx?id=84212",
        "https://kpl.gov.la/detail.aspx?id=84132",
        "https://kpl.gov.la/detail.aspx?id=84131",
        "https://kpl.gov.la/detail.aspx?id=84130",
        "https://kpl.gov.la/detail.aspx?id=84129",
        "https://kpl.gov.la/detail.aspx?id=84128",
        "https://kpl.gov.la/detail.aspx?id=84127",
        "https://kpl.gov.la/detail.aspx?id=84126",
        "https://kpl.gov.la/detail.aspx?id=84125",
        "https://kpl.gov.la/detail.aspx?id=84124",
        "https://kpl.gov.la/detail.aspx?id=84123",
        "https://kpl.gov.la/detail.aspx?id=84122",
        "https://kpl.gov.la/detail.aspx?id=84121",
        "https://kpl.gov.la/detail.aspx?id=84120",
        "https://kpl.gov.la/detail.aspx?id=84111",
        "https://kpl.gov.la/detail.aspx?id=84119",
        "https://kpl.gov.la/detail.aspx?id=84118",
        "https://kpl.gov.la/detail.aspx?id=84117",
        "https://kpl.gov.la/detail.aspx?id=84116",
        "https://kpl.gov.la/detail.aspx?id=84115",
        "https://kpl.gov.la/detail.aspx?id=84114",
        "https://kpl.gov.la/detail.aspx?id=84113",
        "https://kpl.gov.la/detail.aspx?id=84112",

    ]

    def parse(self, response):

        def split_sentence(text, min_len=10, max_len=25):
            words = text.split()
            sentences = []
            remaining_words = len(words)
            start = 0

            while remaining_words > 0:
                sentence_len = random.randint(min_len, min_len + remaining_words) if remaining_words < max_len else random.randint(min_len, max_len)
                sentence = words[start: start + sentence_len]
                sentences.append(' '.join(sentence))
                start += sentence_len
                remaining_words -= sentence_len

            return sentences
        
        paragraphs_vn = Selector(response).xpath('//div[@class="detail-content afcbc-body clearfix"]/p/text()').extract()
        text_vn = ' '.join(paragraphs_vn)
        sentences_vn = split_sentence(text_vn)

        for sentence in sentences_vn:
            item = CrawlerItem()
            item["Text"] = sentence
            item["Language"] = "Vietnamese"
            yield item

        paragraphs_lao = Selector(response).xpath('//div[@class="post-ct-entry"]/p/span/span/text()').extract()
        text_lao = ' '.join(paragraphs_lao)
        sentences_lao = split_sentence(text_lao, min_len=1, max_len=5)

        for sentence in sentences_lao:
            item = CrawlerItem()
            item["Text"] = sentence
            item["Language"] = "Lao"
            yield item

