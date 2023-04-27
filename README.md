

![image](https://img.shields.io/pypi/v/stopwords-zh.svg) ![image](https://img.shields.io/travis/yuanjie-ai/stopwords-zh.svg) ![image](https://readthedocs.org/projects/stopwords-zh/badge/?version=latest)



<h1 align = "center">🔥stopwords-zh🔥</h1>

---
### 欢迎提交更新，共建中文停用词库

# Install
```shell
pip install -U stopwords-zh
```

# [Docs](https://yuanjie-ai.github.io/stopwords-zh/)

# Usages
- source: string, 停用词来源，目前支持
  - baidu: 百度停用词表
  - hit: 哈工大停用词表
  - ict: 中科院计算所停用词表
  - scu: 四川大学机器智能实验室停用词库
  - cn: 广为流传未知来源的中文停用词表
  - marimo: Marimo multi-lingual stopwords collection 内的中文停用词
  - iso: Stopwords ISO 内的中文停用词
  - all: 上述所有停用词并集
```python
import jieba
from stopwords import stopwords, filter_stopwords

print(filter_stopwords(jieba.cut('欢迎提交更新，共建中文停用词库')))

```

---
# TODO

- [x] 停用词
- [ ] 情感字典


