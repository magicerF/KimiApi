# KimiApi
使用python通过kimi聊天或者生成图片

安装依赖：
```bash
pip install requests
pip install execjs
```
调用方法：
```python
self.session.headers = {} #登录kimi复制替换自己的headers
```
```python
kimi = KIMI()
print(kimi.kimi_TextQuestion("写一段xxx代码")) #文本聊天
print(kimi.kimi_ImageQuestion("生成xxx图片"))  #生成图片
```
```markdown
文本聊天直接返回文本，图片生成返回下载链接
```


