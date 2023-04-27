"""Main module."""
from functools import lru_cache
from pathlib import Path

get_resolve_path = lambda path, file=__file__: (Path(file).parent / Path(path)).resolve()


@lru_cache()
def stopwords(source="all"):
    """
    Params:
        langs: string，支持的语言，目前仅支持中文(zh)
        source: string, 停用词来源，目前支持
          - baidu: 百度停用词表
          - hit: 哈工大停用词表
          - ict: 中科院计算所停用词表
          - scu: 四川大学机器智能实验室停用词库
          - cn: 广为流传未知来源的中文停用词表
          - marimo: Marimo multi-lingual stopwords collection 内的中文停用词
          - iso: Stopwords ISO 内的中文停用词
          - all: 上述所有停用词并集
    Return:
        a set, 停用词表集合
    """

    supported_source = ["cn", "baidu", "hit", "scu", "marimo", "ict", "iso", "all"]
    if source not in supported_source:
        raise NotImplementedError("请求了未知来源，请使用`help(stopwords)`查看支持的来源")
    return set(get_resolve_path(f"./data/stopwords.zh.{source}.txt").read_text().strip().split())


def filter_stopwords(words, source='all'):
    sw = stopwords(source)
    return [w for w in words if w not in sw]


if __name__ == '__main__':
    import jieba

    print(filter_stopwords(jieba.cut('欢迎提交更新，共建中文停用词库')))
