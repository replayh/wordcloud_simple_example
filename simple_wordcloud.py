import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'sample.txt'), encoding='utf-8').read()

# Generate a word cloud image
wordcloud = WordCloud(font_path='NanumGothic.ttf').generate(text)

# Display the generated image:
# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.show()
