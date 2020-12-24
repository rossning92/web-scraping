from collections import Counter
from wordcloud import WordCloud
import itertools
import jieba
import jieba.posseg
import json

stopwords = set(open("stopwords_cn.txt", encoding="utf-8").read().splitlines())

# Enable the deep learning based model for word cutting.
jieba.enable_paddle()

# Load scrawled data
data = json.load(open(r"data.json", encoding="utf-8"))

# Extract all words
words = [word for title in data for word, _ in jieba.posseg.cut(title)]

# Filter out stop words
words = filter(lambda x: x not in stopwords, words)

# Filter out words with length <= 1
words = filter(lambda x: len(x) > 1, words)

# Select top 100 words based on their occurrence
counter = Counter(list(words))
most_common_words = counter.most_common(100)
print(most_common_words)


wordcloud = WordCloud(
    font_path="SourceHanSerifSC-Medium", width=1920, height=1080, colormap="Blues",
).generate_from_frequencies(dict(most_common_words))

im = wordcloud.to_image()
im.save("word-cloud.png")
