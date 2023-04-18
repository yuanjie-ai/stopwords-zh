

![image](https://img.shields.io/pypi/v/stopwords-zh.svg) ![image](https://img.shields.io/travis/yuanjie-ai/stopwords-zh.svg) ![image](https://readthedocs.org/projects/stopwords-zh/badge/?version=latest)



<h1 align = "center">🔥stopwords-zh🔥</h1>

---
### 欢迎提交更新，共建中文停用词库

# Install
```python
pip install -U stopwords-zh
```

# [Docs](https://yuanjie-ai.github.io/stopwords-zh/)

# Usages
```
from stopwords import stopwords
import jieba

STOP_WORDS = stopwords()
words = jieba.cut('欢迎提交更新，共建中文停用词库')
print([w for w in words if w not in STOP_WORDS])
```

---
# TODO

- [x] 停用词
- [ ] 情感字典


