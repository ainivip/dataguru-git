from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open(r'C:\1.txt','r').read()
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=1000, #显示最大词数
    font_path=r'C:\Windows\Fonts\simfang.ttf',  #使用字体
    min_font_size=10,
    max_font_size=80,
    width=400, #图幅宽度
    height=300, #图幅高度
    margin=1
    )
wc.generate(f)
wc.to_file(r"c:\1.png")



plt.imshow(wc)
plt.axis("off")
plt.show()
#wc.to_image("test.png")

