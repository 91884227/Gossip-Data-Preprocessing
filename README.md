# Gossip-Data-Preprocessing

## 將開頭為 **[新聞]** **Re:** 的title 刪除
e.g. [新聞] 國王的女兒說我性侵她該怎麼辦？

## 刪除標籤
e.g. [問卦] 國王的女兒說我性侵她該怎麼辦？ -> 國王的女兒說我性侵她該怎麼辦？

## 保留去除標籤後 字數>10的title



# How to use
python Gossip_preprocessing.py Gossip_title_39000_to_39010.csv

即可產生 Gossip_title_39000_to_39010_preprocessing.npy 的檔案
