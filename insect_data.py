import json
import requests
import xmltodict

# 인증키 저장
key = "4Y1VQ%2BFCILQgfBdtfbv2AGShcA9czXwJPhSXne622ujf7MWF8FHODnOX%2B7QWvUxzm2e81Njv464DtuNT4OKygQ%3D%3D"
# 인증키 정보가 들어간 url 저장
url = f"http://openapi.nature.go.kr/openapi/service/rest/InsectService/isctPrtctList?serviceKey={key}"


content = requests.get(url).content                      # request 모듈을 이용해서 정보 가져오기(byte형태로 가져와지는듯)
dict = xmltodict.parse(content)                         # xmltodict 모듈을 이용해서 딕셔너리화 & 한글화
jsonString = json.dumps(dict, ensure_ascii=False)       # json.dumps를 이용해서 문자열화(데이터를 보낼때 이렇게 바꿔주면 될듯)
jsonObj = json.loads(jsonString)                        # 데이터 불러올 때(딕셔너리 형태로 받아옴)
print(len(jsonObj))
#
for item in jsonObj['response']['body']['items']['item']:
	print(item)
	print(item['imgUrl'], item['insctFamilyNm'], item['insctOfnmScnm'],
	      item['insctPcmtt'], item['insctPilbkNo'], item['insctofnmkrlngnm'])