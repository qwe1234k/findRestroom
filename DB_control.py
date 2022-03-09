# mongo db setting
import googlemaps
import hashlib
import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient('', tlsCAFile=ca)
db = client.seoul_restroom

# 회원가입 DB
sign_up_info = {
    'user_id': "test id 1",
    'user_pw': "test pw 1"
}
# db.signup.insert_one(sign_up_info)

# 리뷰 DB
review_info = {
        'name': "test name 1",
        'comment': "test comment 1",
        'star': "test star 1",
        'num': "test num 1"
    }
db.review.insert_one(review_info)


# name_X_Y_ls = list(db.district.find({},{'_id':False}))
# name_X_Y = name_X_Y_ls[4000:] # 4000:
# count = 4000 # 4000
# for ls in name_X_Y:
#     name_target = ls["name"]
#     X = ls["X_WGS84"]
#     Y = ls["Y_WGS84"]
#
#     ## XY convert
#     gmaps = googlemaps.Client(key='')
#     g_list = gmaps.reverse_geocode((Y, X), language='ko')
#
#     dis_ls = []
#     for address in g_list:
#         name = address["formatted_address"]
#         new_Y = address["geometry"]["location"]["lat"]
#         new_X = address["geometry"]["location"]["lng"]
#         dis_ls.append([name, abs(new_Y - Y), abs(new_X - X)])
#
#     dis_ls.sort(reverse=True)
#     converted_address = dis_ls[0][0] ## 한국 주소
#     count += 1
#     print(count)
#
#     restroom_id = count
#     base_info = {
#         'name' : name_target,
#         'restroom_id' : restroom_id,
#         'address' : converted_address
#         }
#     db.base_info.insert_one(base_info)



# # 구이름 DB
# district_info = {
#     'gu_names' : "test gunames 1"
# }
# db.district.insert_one(district_info)
#
# # 리뷰 DB
# review_info = {
#     'comment': "test comment 1",
#     'user_id': "test id 1" # 댓글러 구분용
# }
# db.review.insert_one(review_info)