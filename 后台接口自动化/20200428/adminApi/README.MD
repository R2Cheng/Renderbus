# 注意事项
### 请求新平台接口传参都是以json格式传参

1.如果参数用`table2.cell(1,1).value`方法从excel表获取，读取出来的数据是str格式的，则requests方法请求的时候传参就用表单形式，例如
```
payload = self.table2.cell(1,1).value
requests.post(url,data=payload,headers=headers)
```

2.如果参数是直接用字典写死在代码里面，则requests方法请求的时候用json方法，或者先用json.dumps()方法把字典转换成字符串，例如
```
payload = {"amount":10,"currency":1,"agent":"CGLINE","payMethod":2}
r = requests.post(url,data=json.dumps(payload),headers=headers)
或者
r = requests.post(url,json=payload,headers=headers)
```
