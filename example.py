# -*- coding: utf-8 -*-
from IISRapi.model import ner,pun,data
ner_re=ner.IISRner(dev=-1)
pun_re=pun.IISRpunctuation(dev=-1)
test_str="行在通政使司辦事吏許信奏各處吏員到部分撥各衙門辦事辰入酉出動經數歲其有去家遠者囊橐空竭無人供應遂致沿街丐食廉恥道喪誠可哀憫請依洪武舊制月給食米俾有所仰事下行在戶部議宣德初年旱澇不常事從撙節辦事吏員不支食米今四方荒歉尤甚轉運艱難更當撙節 上以吏冗宜汰之命貧難不堪任事者悉罷為民堪任事而願歸省者聽"

for element in ner_re(pun_re(test_str)):
    print(element)
    print('\n')
    
print(ner_re(test_str))
print('\n')
print(pun_re(test_str))