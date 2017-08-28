from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open('data.txt',encoding="utf-8").read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
font = r'C:\Windows\Fonts\simfang.ttf'
wordcloud = WordCloud(font_path=font,width=800, height=600, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.show()
wordcloud.to_file('show.png')