# 5QPJXzcaZuXgNzfY4CG2t7E20VNB2AWjBaZgb4NJhhk 群組的權杖
import requests

def lineNotifyMessage(token, msg):
    headers = {
      "Authorization": "Bearer " + token, 
      "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
token = '5QPJXzcaZuXgNzfY4CG2t7E20VNB2AWjBaZgb4NJhhk' # 權杖
# 這裡要寫一個if-else判斷式，符合條件就修改訊息並發送
message = '哈囉郭忠霖'
a = input()
if a == 'send':
    lineNotifyMessage(token, message)
