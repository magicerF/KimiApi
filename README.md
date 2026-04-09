# KimiApi
使用python通过kimi聊天或者生成图片

安装依赖：
```bash
pip install requests
pip install execjs

调用方法：
```python
kimi = KIMI()
print(kimi.kimi_TextQuestion("写一段xxx代码")) #文本聊天
print(kimi.kimi_ImageQuestion("生成xxx图片"))  #生成图片


