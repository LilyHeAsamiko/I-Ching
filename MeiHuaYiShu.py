/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
"""
#include <stdio.h>
# -+- coding: utf-8 -+-

Created on Fri Dec 02 06:00:17 2022

@author: LilyHeAsamiko

For some knowledge related to Chinese Antient Culture, GUA and especially referencing 'Iching'. There also includes one fun part about 'Flower May's Prediction' interacting with the visitor.

PS: Quantum Computation is used for computing it's application of the Hamiltonian and Energy, Phase 

Note that need to have the pre-requisit :
pillow, qiskit
pip install pillow
"""
#%matplotlib inline

import qiskit
#qiskit.__version__
#from qiskit import IBMQ
#IBMQ.load_account()
#MY_API_TOKEN = ' '
#provider = IBMQ.enable_account(MY_API_TOKEN)

from qiskit.compiler import transpile, assemble
#from qiskit.tools.jupyter import *
from qiskit.visualization import *

import matplotlib.pyplot as plt
import numpy as np
import math
import os
import sys
import io
import requests
import urllib
from IPython import display
import time 
#import panda as pd

from qiskit import IBMQ, Aer
from qiskit import QuantumCircuit, execute

from qiskit.visualization import plot_histogram
from random import *
from qiskit.visualization.bloch import Bloch
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import qiskit.pulse as pulse
#import qiskit.pulse.pulse_lib as pulse_lib
#import pulse_lib as pulse_lib
#from qiskit.pulse.pulse_lib import Gaussian, GaussianSquare
from qiskit.pulse.library.discrete import gaussian, gaussian_square, drag, constant
from qiskit.pulse.library.pulse import Pulse
from qiskit.pulse.library.waveform import Waveform
#from qiskit.ignis.characterization.calibrations import rabi_schedules, RabiFitter
#from qiskit.qiskit-experiments.library.calibration import rabi_schedules, RabiFitter
from qiskit.tools.monitor import *
#from qiskit.providers.aer.pulse import duffing_system_model
import warnings
warnings.filterwarnings('ignore')
#from qiskit.tools.jupyter import *
#get_ipython().run_line_magic('matplotlib','inline')

#provider = IBMQ.get_provider(hub='ibm-q', group ='open', project = 'main')
#backend = provider.get_backend('ibmq_armonk')
#backend_config = backend.configuration()
#assert backend_config.open_pulse, "Backend doesn't support Pulse"
from qiskit.providers.aer import PulseSimulator
import urllib.request 
from PIL import Image 
import numpy as np

def YAO(digit, language):
    if language == 0: 
        print('爻是最基本的符号，意指交错，有阴阳两种仪态：\n 阳爻[又称奇画,与量子力学中定义相类似，取作qubit记为0];\n  阴爻[又称偶画,与量子力学中定义相类似，取作qubit记为1]; \n')
        print('爻自下而上排列，三个爻的含义为地人天，上有天，下为地，人在其中。现代我们也常说天时地利人和，就连我们的习主席经常谈及的可持续发展也包括环保理念以及和谐社会的人文理念。\n')
    if language == 1:
        print('爻 Yao，is the basic element, standing for cross.\n There are two status referencing darkness and brightness：\n 阳爻,Yang Yao(brightness)[also called 奇画(oddness),Ji Hua, in accordance to the quantum computation, is defined as qubit = 0];\n 阴爻,Yin Yao(darkness)[also called 偶画(oddness),Ou Hua, in accordance to the quantum computation, is defined as qubit = 1];')
        print('爻,Yao, looked from bottom to up, stands for earth, human and sky. Sky above head, ground under foot, people are beneath. Nowadays, we always emphasize the importance of "timing of the nature, advantages of the surroundings and harmony of the people".Our President Xi also sticks to the sustainable development with environment friendly and harmonic sociality. \n')
    if digit == 0:
        print('阴爻, Yin Yao: - -')
    elif digit == 1:
        print('阳爻’, Yang Yao: 一')
    qubit = digit
    return qubit

def main():
# 默认语言为中文
    language = 0
# 用户选择，0为中文， 1为英语
    language = input('请选择本程序讲解的语言，0为中文，1为英语。Please choose the language for the upcoming contents with 0 for Chinese and 1 for English.')
    digit = input('Please input another 0 or 1 for qubit initialization: ')
    assert(digit in [0,1], "输入错误，程序自动退出。Wrong Input, program will exit automatically.")
    if language == 0:
        print ('本程序将讲解一些基本的从易经出发，与卦，象，仪相关的概念，并和量子力学相结合，计算相关的能量值以及汉密尔顿值。\n 学习以后，您可做30秒-1分钟左右的冥想，给出两个两位数，我们会运用"梅花易数"，提供您最近运势推断，仅供参考与娱乐。\n未来我们也将继续给出其他功能的推断与介绍，包括风水，财运，面相等，尽请期待。')
    if language == 1:
        print('There will be some introduction derived from "I Ching 易经", including Gua, Xiang, Yi and etc. And combining Quantum Mechanics, we will also exhibit its energy and Hamiltonians. \n After study, you can choose to make one prediction, according to Flower May.(Just meditate for 30 seconds to 1 minute and give us two 2-digit numbers.) Only for reference and fun. \n In the future, there will also be other predictions and explanations, including placing and location with regards to housing,fortune, FaceLook and etc.')
    digit = input('请输入数字0 或 1开始：Please start with inputting 0 or 1: ')
    assert(digit in [0,1], "输入错误，程序自动退出。Wrong Input, program will exit automatically.")
    qubit = YAO(digit, language)
    urllib.request.urlretrieve(  'https://zh.m.wikipedia.org/zh-hant/%E5%85%AB%E5%8D%A6#/media/File%3ABagua-name-earlier.svg', "xtbg.png") 
    img = Image.open("xtbg.png") 
    img.show() 
    if language == 0:
        print('所谓:三求平未，斗非半米。先天八卦相传是伏義所造。\n')        
        print('我们介绍了爻的阴阳两态，以及天地人三部分，爻若两两相重则形成四象（太阴，少阴，太阳，少阳）,四象再增加一爻，就形成八卦。这源于易傳的"易有太极，是生两仪。两仪生四象，四象生八卦"。\n')        
        print('简单来说，三个爻组成一个单卦，又称经卦。八卦意为八个单卦，每一卦代表一种状态或过程。\n')
        print('先天八卦源于中国古代对基本宇宙生成，相应日月地球自转，农业社会和人生哲学相互结合。近代考证认为，所谓太极即宇宙，太极生两仪指地球面对阳光照射角度，关乎公转与自转。两仪生四象为，地球公转右旋太阳与自转中，根据日照光线与影长不同，记在罗盘上天禽二十八宿，总度数365又1/4为合一，定为太阳历日数，区分四季（冬为壬，子，癸三节气，坎卦，水生旺；春为甲，卯，乙三节气，震卦,木生旺；夏为丙，午，丁三节气，离卦，火生旺；秋为庚，酉，辛三节气，兑卦,风（金）生旺；）。四象生八卦则指上述四象会有生旺衰死之消长，气象变化，如冬天水气溶解于土，生于树木，立为垦卦，管丑、艮、寅三节气；春天木氣旺后，转夏天火气旺中，立為巽卦，管辰、巽、巳三节气；夏天火气旺後，會转入秋天金氣旺中，立為坤卦，管未、坤、申三节气；如秋天金(風)氣旺後，會转入冬季水气旺中，立為乾卦，管戌、乾、亥三节气文王作易，將可證明先作太陽曆一年之日數，再分作八季(八卦)廿四節氣，並調查各節氣時，地上所生成重要氣象生態，記註在羅盤上，作廿四節氣字中，作干支曆數，其廿四節氣，以地球右旋公轉太陽，訂立八卦(季)，與節氣名順序並含其意義，作干支組曆表示月、時令之氣象生態。\n')       
        print('四象生八卦则指上述四象会有生旺衰死之消长，气象变化，如冬天水气溶解于土，生于树木，立为垦卦，管丑、艮、寅三节气；春天木氣旺后，转夏天火气旺中，立為巽卦，管辰、巽、巳三节气；夏天火气旺後，會转入秋天金氣旺中，立為坤卦，管未、坤、申三节气；如秋天金(風)氣旺後，會转入冬季水气旺中，立為乾卦，管戌、乾、亥三节气文王作易，將可證明先作太陽曆一年之日數，再分作八季(八卦)廿四節氣，並調查各節氣時，地上所生成重要氣象生態，記註在羅盤上，作廿四節氣字中，作干支曆數，其廿四節氣，以地球右旋公轉太陽，訂立八卦(季)，與節氣名順序並含其意義，作干支組曆表示月、時令之氣象生態。\n')
        print('另外地，两个八卦相叠即成复卦，八八六十四卦，上者外挂，下者内挂。\n')
        print('易經也记载，天地定位，山澤通氣，雷風相薄，水火不相射。\n 具体来说，天地定位：☰（乾）三爻全陽，表示全動，是天體之象。☷（坤）三爻全陰，表示全靜，是大地之象。\n')
        print('先民的宇宙觀是「天動而地靜」:天在上而地在下，即「天地定位」。\n')
        print('山澤通氣:☶（艮）上爻為陽爻，中下爻為陰爻。上面小部份動，下面大部分靜，為「山」之象。☱（兌）上爻為陰爻，中下爻為陽爻。上面小部份靜，下面大部分動，為「降雨」之象。\n 山氣上騰，雨水下降，即「山澤通氣」。澤即是雨，雨降於天，山出於地，因此☱（兌）緊接☰（乾）後面，☶（艮）緊鄰☷（坤）。\n')
        print('雷風相薄:☳（震）下爻為陽爻，中上爻為陰爻。上面大部分靜，下面少部份動，為「雷」之象。古人認為雷從地中起，所以☳（震）也排在☷（坤）的旁邊。☴（巽）下爻為陰爻，中上爻為陽爻。上面大部分動，下面少部份靜，為「風」之象。古人認為風起天上，所以☴（巽）也排在☰（乾）的旁邊。\n 雷發地中而上騰，天之下有空氣在流動（風），就是「雷風相薄」。\n')
        print('水火不相射:☵（坎）中爻為陽爻，上下爻為陰爻。週邊靜而地中動，為「水」之象。☲（離）中爻為陰爻，上下爻為陽爻。週邊動而體中靜，為「火」之象。又為「日」之象。\n 一般認為此八卦排列的對應：天地，山澤，雷風，水火, 合於自然現象。\n')
    if language == 1:
        print('There is the saying about Yao: three Yao makes one gua and if with all halves, they are made into yin. The primordial bagua, also called Earlier Heaven is said to be innovated by Fu Xi.\n')
        print('We have introduced the two status of Yao, darkness and brightness，along with its three partials from bottom to top as earth, people and heaven.Yao, if casted doubly two by two, will turn to four phases(Strong darkness, weak darkness, strong brightness and weak brightness). Four phases adding one more Yao can turn to eight Guas. This is originally from I Ching, "I has TaiChi, making two Yis. Two Yis go to four phases and four phases finally can turn to eight Guas".\n')
        print('The Primordial Ba Gua, Trigrams, origins from ancient Chinese knowledge about universe, combining the self-rotation of sun, moon and earth, agriculture and philosophy. Mordern evidences shows  the concept of Taichi as universe. Taichi makes two Yis by refering to the earth facing sunshine variously with different angles, related both to the rotation around the sun and itself.Then the two Yis go to four phases,mainly because the earth rotate around the sun from right side and according to the different sunshine and shadow length, there recorded 28 Xiu onto the compass with total degrees of 365 and 1/4,noted as solar calender with four seasons(Winter commands three Jie Qi: Ren, Zi, Gui, with Gua,Kan, symbolyzing the water; Spring commands three Jie Qi: Jia, Mao, Yi, with Gua,Zhen,symbolyzing the Wool; Summer commands three Jie Qi: Bin, Wu, Ding, with Li Gua, symbolying fire; Autumn commands three Jie Qi: Gen, You, Xin, with Dui Gua symbolyzing wind(gold).\n ')
        print('Four phases turn into eight Guas and this means the four seasons changes dynamically with lifes and strength. For instances, in winter, water disolves into soil and grows the wool, denoted as the Ken Gua, commanding Chou, Ken, Yin three Jie Qi while in spring, wool grows, denoted as Xun Gua commanding Chen, Xun, Si three Jie Qi while in Autumn, Gold propogates, denoted as Qian Gua, commanding wu, qian, hai three Jie Qi and actually in accordance with the Later Heaven, the whole year can be separatd into eight Guas with 24 Jie Qis and when investigating each of them, the phenomenons are recorded onto the Compass,written as Gan Zhi, which also again combining earth rotation around the sun from right side and denoted as months describing with various climates and phenomenon.\n')
        print('In additionally，two Ba Gua doubly casted into a dual-Gua and eight Guas times eight equals sixty four and the Up Guas towards outside while Down Guas towards insides.\n')
        print('On the other hand, according to the I Ching, the heaven and earth allocate, the mountain and the water vertainlise, the thunder and the wind stricts each other while the water and the fire do not interupt each other.\nSpecifically speaking, heaven and earth allocates with ☰ (111), full three brightness ,referring to full motion, stands for heaven. And ☷ (000), full three darkness ,referring to full silence, stands for earth.\n')
        print('The values of past about universe is [The sky moves while the earth is still]: The heaven is above the earth and it is the allcoation of heaven and earth.\n')
        print('The mountain and the water vertainlize:☶（Ken,001）has brightness as toppest Yao while darkness for middle and bottom yao. The small amount is moving above while the large amount under is still, describing the image of mountain. ☱（Dui,110）has the darkness as toppest Yao while brightness for middle and bottom. The small amount is still above while the large amount under is moving, imaging the rain. \n The Qi of the mauntain rises while the rain drops, leading to the mountain and the water vertenlizer and water stands for saying. Rain drops from sky, mountain stays still from soil. Thatchu ☱（Dui,110）follows☰（Qian,111），☶（Ken,001) is close to ☷（Kun,000）\n')
        print('The thunder and the wind stricts each other:☳（Zhen,100）the bottom yao is brightness，and the middle and upper is darkness. The upper most are still while the down small amount is motive, imaging the thunder. In the past, people think thunder starts from earth and thus ☳（Zhen,100）is next to☷（Kun,000）. ☴（Xun,011）has the down Yao being darkness while brightness as middle and upper yao. Upper most are motive while small amount downside is still imaging wind. In the past, wind is reconed as origin of heaven. That is why ☴（Xun,011）is next to ☰（Qian,111）.\n The thunder starts from the earth and rises while the moving air is under the heaven as wind, imaging the thunder and the wind stricts to each to other。\n')
        print('The water and the fire does not interrupt each other:☵（Kan,010）has the middle yao being brightness while upper and down yaos as darkness. The surrounding is still while the middle is motive, imaging water.☲（Li, 101）has the darkness as middle yao while upper and down yao being brightness.The surrounding is motive while middle is still, imaging fire as well as sun.\n Generally, these eight trigrams called Ba Guas are regarded as the symbol of heaven,earth, mountain, water, thunder, wind, water and fire together as the natural phenomenon.\n')

    urllib.request.urlretrieve(  'https://zh.m.wikipedia.org/zh-hant/%E5%85%AB%E5%8D%A6#/media/File%3AHoutian_Bagua.JPG', "htbg.png") 
    img = Image.open("htbg.png") 
    img.show()
    if language == 0:
        print('至于后天八卦,则为文王所造。\n 卦辭\n乾為天：元亨，利貞。\n 坤為地：元亨，利牝馬之貞。君子有攸往，先迷後得主，利西南得朋，東北喪朋。安貞，吉。\n坎為水：習坎，有孚，維心亨，行有尚。\n 離為火：利貞，亨。畜牝牛，吉。\n 震為雷：亨。震來虩虩，笑言啞啞。震驚百里，不喪匕鬯。\n 艮為山：艮其背，不獲其身，行其庭，不見其人，無咎。\n 巽為風：小亨，利攸往，利見大人。\n 兌為澤：亨，利貞。\n')
    if language == 1:
        print('As for the Manifested Trigram,Ba Gua,called Later Heaven,is created by the King Wen\n Gua Ci\n Qian is the heaven：Full well and good to Virgo.\n Kun is the earth: Full well and is good to the Capricorn. Nobel guy occupies the Aries and confuses but commands later, good to the western south with friendship while lost in east south.Virgo is also satisfied with luck. \n Kan is the water: command the Kan, with response, stick to heart, executive ability outstands.\n Li is the fire: good to the Virgo, prosperus .Taurus got luck.\n Zhen is thunder: prosperus. Thunder brings Pisces, smiles without word. Astonishes hundreds miles, not to fail Leo. \n Ken is mountain: start from the back while not have harvest, walk through the garden but not seeing anyone, get nothing.\n Xun is wind: slight prosperus, good to Aries and is easy to see the big.\n Dui is water: prosperus, good to Virgo.\n') 
    urllib.request.urlretrieve(
  'https://zh.m.wikipedia.org/zh-hant/%E5%85%AB%E5%8D%A6#/media/File%3AFamily_Ba_Gua.gif',"jtbg.png") 
    img = Image.open("jtbg.png") 
    img.show()
    if language == 0:
      print('同时，他認為先有天地，天地相交而生成萬物，天即乾，地即坤，八卦其餘六卦皆為其子女：震為長男，坎為中男，艮（gèn）為少男；巽（xùn）為長女，離為中女，兌為少女，是為文王八卦，又稱後天八卦。八卦符號通常與太極圖搭配出現，代表中國傳統信仰（儒，道）的終極真理。\n') 
      print('除了引入家庭关系，最明显不同的顺序，乾·坎·艮·震·巽·離·坤·兌。对此，清人張潮《幽夢影》中即有,先天八卦，竖看者也；后天八卦，橫看者也一说。多数都认为只是所在方位的相对差别。\n') 
      print('后天八卦方位與東南西北方位存在着一一对应的关系：震離兌坎分別代表正東、正南、正西、正北，剩下四卦則分別為東南，西南，西北，東北四隅。这个顺序良好诠释了我国古代的东方制图，规划发展的坐北朝南，湖海东高西低的传统风水\n')           
    if language == 1:
      print('Meanwhile, King Wen believes that everything starts with heaven and earth and the cross of them derives the all species, and the heaven is Qian while earth is Kun, the rest sox pf the Ba Gua are all the discendents: Zhen is the oldest male, Kan is the middle male, gen is the youngest male; xun is the oldest female, Li is the middle female, Dui is the youngest female. These are also one version of the Manifest Trigrams. The symbols for that is usually with Taichi, referecing to the traditional Chinese believe regards with Ruisms and Daoisms as the eternal truth.\n') 
      print('In addition to the family relations, the biggest difference between the Latter Heaven and the Former Heaven are the orders of the Ba Gua where King Wen sticks to "Qian,Kan, gen, zhen,xun,li,kun,dui". There are quite many different explanations for the difference while most hold the view as the relative difference of the two author location. There is also the <You Meng Yao>by Zhang Chao in Qing Dynasty, claiming the Predormial Trigrams sees world vertically while the Manifestial Trigrams sees world horizontally. \n') 
      print('The Manifestial Ba Gua has correlation between the four geographical directions--Zhen, Li, Dui, Kan stands for the sharp east, south, west and nouth while the rest four, Xun, Kun, Gen,Qian stands for the east south, west south, west north, est south corners. This order interprets the antient architecture of Chinese style, as the habit of locating at north while facing south and the river gos from east to west well \n') 
    urllib.request.urlretrieve(  'https://zh.m.wikipedia.org/zh-hant/%E5%85%AB%E5%8D%A6#/media/File%3AXiantianbagua.png',"zxbg.png") 
    img = Image.open("zxbg.png") 
    img.show()
    if language == 0:
      print('伏羲氏畫八卦，周文王作卦辭，周公作爻辭，孔子作十翼。\n 宋代朱熹在《周易本義》中寫了一首《八卦取象歌》幫助人記住八卦的卦象：\n乾三連（☰），坤六斷（☷）；\n震仰盂（☳），艮覆碗（☶）；\n離中虛（☲），坎中滿（☵）；\n兌上缺（☱），巽下斷（☴）。\n') 
      print('易經的八卦除了代表了古代中國的天文地理哲學等文化思想，其理論還涉及到文學、武術、中國音樂等方面。此外，八卦尚對應着八門，論後天八卦，由正北坎卦始起：休、生、傷、杜、景、死、驚、開\n')
    if language == 1:
      print('As Fu Xi drew the Predormial Trigrams, King Wen composed the Gua Ci while the Zhou Gong created Yao Ci system, Confucious Created Shi Yi.\n Zhu Xi in Song Dynasty wrote a good poem in <Zhou Yi Ben Xi>memorizing the Ba Gua with impressive and easy rythom: \n Qian connects three 乾（☰），Kun brokes into six坤（☷）；\n Zhen looks from one bottom震（☳），Gen covers two bottoms 艮（☶）；\n Li brokes its middle離（☲），Kan connects its middle坎（☵）；\n Dui misses the up part 兌（☱），Xun brokes its down 巽（☴）。\n')  
      print('I Ching Ba Gua not only incolves the antient Chinese culture, Astrology, Geography and Phylosophy but also covers literature, martial arts, Chinese Musics and etc. aspects. In addition, the Ba GUa also corresponds to the Ba Men. Especially, when it comes to the Menifestial Trigrams, from the sharp north, Ba Gua refer to Xiu,Sheng, Shang,Du,Jing,Si,Jing,Kai. \n')
    if language == 0:
      print('现在我们要开始运用梅花易数来推断最近运势咯。梅花易数这主要源于庆历中，邵雍，字尭夫，康节先生，隐居时预言中某女子前来折梅，伤及股而成名。\n 主要在于比较准确的预测能力，可判断最近运势为大吉，小吉，大凶，小凶中何种。')
    if language == 1:
       print("Now we are going to use the small tricks of 'Mei Hua Yi Shu' to predict recent fortune. This is originated from oled literature created by Mr. Kang Jie, named Shao Yong, titled Yao fu. Story is about when his hiding himself in rural place, predicted about a female visiting to pick Flower May and got broken her leg. And nowadays, it is based on the Ba Gua combining meditation, using two 2-digit numbers, giving coarse prediction of the fortune as one result from the four equal-possibilities, 'Big Luck', 'Small luck', 'Big Misery','Small Misery'.\n")
    Gua = ['乾','兌','離','震','巽','坎','艮','坤']
    GuaBinary = [ "111","110", "101", "100", "011", "010", "001","000"]
    GuaWuxing =["金", "金","火","木","木","水","土","土"]
#GuaFig = 
    if language == 0: 
      print('请闭眼冥想30秒至1分钟。')
      a= input("请给出2个两位数数字，第1个两位数：\n")
      b= input("第2个两位数：\n")
    if language == 1:
      print('Please meditate 30s to 1 minute.')
      a= input("Please give two 2-digit numbers, first one is: \n")
      b= input("second one is:\n")
#上卦
    if np.mod(a,8) == 0:
      up = 8
    else:
      up = np.mod(a,8)
    UP = Gua[up-1]
    UPW = GuaWuxing[up-1]
#下卦
    if np.mod(b,8) == 0:
      down = 8
    else:
      down = np.mod(b,8)
    DOWN = Gua[down-1]
    DOWNW = GuaWuxing[down-1]
#动爻
    sum = a + b
    if np.mod(sum,6) == 0:
        DY = 6
    else:
        DY = np.mod(sum,6)
#上下卦初始为 体
    A = 0
    B = 0
    if DY > 3:
        A += 1
        if UPW == "木" and DOWNW == "火":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "木" and DOWNW == "土":
            print("用克体, 大凶 Big Misery\n")   
        if UPW == "木" and DOWNW == "金":
            print("体克用, 小吉 Small Luck\n")
        if UPW == "木" and DOWNW == "水":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "火" and DOWNW == "土":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "火" and DOWNW == "金":
            print("用克体, 大凶 Big Misery\n")   
        if UPW == "火" and DOWNW == "水":
            print("体克用, 小吉 Small Luck\n")
        if UPW == "火" and DOWNW == "木":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "土" and DOWNW == "金":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "土" and DOWNW == "水":
            print("用克体, 大凶 Big Misery\n")   
        if UPW == "土" and DOWNW == "木":
            print("体克用, 小吉 Small Luck\n")
        if UPW == "土" and DOWNW == "火":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "金" and DOWNW == "水":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "金" and DOWNW == "木":
            print("用克体, 大凶 Big Misery\n")   
        if UPW == "金" and DOWNW == "火":
            print("体克用, 小吉 Small Luck\n")
        if UPW == "金" and DOWNW == "土":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "水" and DOWNW == "木":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "水" and DOWNW == "火":
            print("用克体, 大凶 Big Misery\n")   
        if UPW == "水" and DOWNW == "土":
            print("体克用, 小吉 Small Luck\n")
        if UPW == "水" and DOWNW == "金":
            print("体生用, 小凶 Small Misery\n")
    else:
        B += 1
        if UPW == "木" and DOWNW == "火":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "木" and DOWNW == "土":
            print("体克用, 小吉 Small Luck\n")   
        if UPW == "木" and DOWNW == "金":
            print("用克体, 大凶 Big Misery\n")
        if UPW == "木" and DOWNW == "水":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "火" and DOWNW == "土":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "火" and DOWNW == "金":
            print("体克用, 小吉 Small Luck\n")   
        if UPW == "火" and DOWNW == "水":
            print("用克体, 大凶 Big Misery\n")
        if UPW == "火" and DOWNW == "木":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "土" and DOWNW == "金":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "土" and DOWNW == "水":
            print("体克用, 小吉 Small Luck\n")   
        if UPW == "土" and DOWNW == "木":
            print("用克体, 大凶 Big Misery\n")
        if UPW == "土" and DOWNW == "火":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "金" and DOWNW == "水":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "金"and DOWNW == "木":
            print("体克用, 小吉 Small Luck\n")   
        if UPW == "金" and DOWNW == "火":
            print("用克体, 大凶 Big Misery\n")
        if UPW == "金" and DOWNW == "土":
            print("用生体, 大吉 Big Luck\n")
        if UPW == "水" and DOWNW == "木":
            print("体生用, 小凶 Small Misery\n")
        if UPW == "水" and DOWNW == "火":
            print("体克用, 小吉 Small Luck\n")   
        if UPW == "水" and DOWNW == "土":
            print("用克体, 大凶 Big Misery\n")
        if UPW == "水" and DOWNW == "金":
            print("用生体, 大吉 Big Luck\n")
    print("感谢使用本程序！\n Thank you for using this program!\n")


if __name__ == '__main__':
    main()

# samples need to be multiples of 16
def get_closest_multiple_of_16(num):
    return get_closest_multiple_of(num, granularity)

# Convert seconds to dt
def get_dt_from(sec):
    return get_closest_multiple_of(sec/dt, lcm)

from qiskit import pulse                  # This is where we access all of our Pulse features!
from qiskit.circuit import Parameter      # This is Parameter Class for variable parameters.
from qiskit.circuit import QuantumCircuit, Gate

# Drive pulse parameters (us = microseconds)
drive_sigma_sec = 0.015 * us                           # This determines the actual width of the gaussian
drive_duration_sec = drive_sigma_sec * 8                # This is a truncating parameter, because gaussians don't have 
                                                        # a natural finite length
drive_amp = 0.05

# Create the base schedule
# Start with drive pulse acting on the drive channel
freq = Parameter('freq')
with pulse.build(backend=backend, default_alignment='sequential', name='Frequency sweep') as sweep_sched:
    drive_duration = get_closest_multiple_of_16(pulse.seconds_to_samples(drive_duration_sec))
    drive_sigma = pulse.seconds_to_samples(drive_sigma_sec)
    drive_chan = pulse.drive_channel(qubit)
    pulse.set_frequency(freq, drive_chan)
    # Drive pulse samples
    pulse.play(pulse.Gaussian(duration=drive_duration,
                              sigma=drive_sigma,
                              amp=drive_amp,
                              name='freq_sweep_excitation_pulse'), drive_chan)

sweep_gate = Gate("sweep", 1, [freq])

qc_sweep = QuantumCircuit(1, 1)

qc_sweep.append(sweep_gate, [0])
qc_sweep.measure(0, 0)
qc_sweep.add_calibration(sweep_gate, (0,), sweep_sched, [freq])

# Create the frequency settings for the sweep (MUST BE IN HZ)
frequencies_Hz = frequencies_GHz*GHz
exp_sweep_circs = [qc_sweep.assign_parameters({freq: f}, inplace=False) for f in frequencies_Hz]

from qiskit import schedule

sweep_schedule = schedule(exp_sweep_circs[0], backend)
sweep_schedule.draw(backend=backend)

import math

def classify(point: complex):
    """Classify the given state as |0> or |1>."""
    def distance(a, b):
        return math.sqrt((np.real(a) - np.real(b))**2 + (np.imag(a) - np.imag(b))**2)
    return int(distance(point, mean_exc) < distance(point, mean_gnd))




def QC(qubit):
    backend_config = backend.configuration()
    dt = backend_config.dt
print(f"Sampling time: {dt*1e9} ns") 
   # The configuration returns dt in seconds, so multiply by
   # 1e9 to get nanoseconds
#determine granually the length of pulse
    backend.configuration().timing_constraints
    acquire_alignment =     backend.configuration().timing_constraints['acquire_alignment']
    granularity = backend.configuration().timing_constraints['granularity']
    pulse_alignment =       backend.configuration().timing_constraints['pulse_alignment']
    import numpy as np
    lcm = np.lcm(acquire_alignment, pulse_alignment)
    print(f"Least common multiple of acquire_alignment and pulse_alignment: {lcm}"
# unit conversion factors -> all backend properties returned in SI (Hz, sec, etc.)
GHz = 1.0e9 # Gigahertz
MHz = 1.0e6 # Megahertz
us = 1.0e-6 # Microseconds
ns = 1.0e-9 # Nanoseconds

# We will find the qubit frequency for the following qubit.
qubit = 0

# The sweep will be centered around the estimated qubit frequency.
center_frequency_Hz = backend_defaults.qubit_freq_est[qubit]        # The default frequency is given in Hz
                                                                    # warning: this will change in a future release
print(f"Qubit {qubit} has an estimated frequency of {center_frequency_Hz / GHz} GHz.")

# scale factor to remove factors of 10 from the data
scale_factor = 1e-7

# We will sweep 40 MHz around the estimated frequency
frequency_span_Hz = 40 * MHz
# in steps of 1 MHz.
frequency_step_Hz = 1 * MHz

# We will sweep 20 MHz above and 20 MHz below the estimated frequency
frequency_min = center_frequency_Hz - frequency_span_Hz / 2
frequency_max = center_frequency_Hz + frequency_span_Hz / 2
# Construct an np array of the frequencies for our experiment
frequencies_GHz = np.arange(frequency_min / GHz, 
                            frequency_max / GHz, 
                            frequency_step_Hz / GHz)

print(f"The sweep will go from {frequency_min / GHz} GHz to {frequency_max / GHz} GHz \
in steps of {frequency_step_Hz / MHz} MHz.")

if qubit == 0:
    # T1 experiment parameters
    time_max_sec = 450 * us
    time_step_sec = 6.5 * us
    delay_times_sec = np.arange(1 * us, time_max_sec, time_step_sec)

    # We will use the same `pi_pulse` and qubit frequency that we calibrated and used before
    delay = Parameter('delay')
    qc_t1 = QuantumCircuit(1, 1)

    qc_t1.x(0)
    qc_t1.delay(delay, 0)
    qc_t1.measure(0, 0)
    qc_t1.add_calibration("x", (0,), pi_pulse)

    exp_t1_circs = [qc_t1.assign_parameters({delay: get_dt_from(d)}, inplace=False) for d in delay_times_sec]

sched_idx = -1
t1_schedule = schedule(exp_t1_circs[sched_idx], backend)
t1_schedule.draw(backend=backend)

# Execution settings
num_shots = 256

job = backend.run(exp_t1_circs, 
                  meas_level=1, 
                  meas_return='single', 
                  shots=num_shots)

job_monitor(job)
t1_results = job.result(timeout=120)
t1_values = []

for i in range(len(delay_times_sec)):
    iq_data = t1_results.get_memory(i)[:,qubit] * scale_factor
    t1_values.append(sum(map(classify, iq_data)) / num_shots)

plt.scatter(delay_times_sec/us, t1_values, color='black') 
plt.title("$T_1$ Experiment", fontsize=15)
plt.xlabel('Delay before measurement [$\mu$s]', fontsize=15)
plt.ylabel('Signal [a.u.]', fontsize=15)
plt.show()

# Fit the data
fit_params, y_fit = fit_function(delay_times_sec/us, t1_values, 
            lambda x, A, C, T1: (A * np.exp(-x / T1) + C),
            [-3, 3, 100]
            )

_, _, T1 = fit_params

plt.scatter(delay_times_sec/us, t1_values, color='black')
plt.plot(delay_times_sec/us, y_fit, color='red', label=f"T1 = {T1:.2f} us")
plt.xlim(0, np.max(delay_times_sec/us))
plt.title("$T_1$ Experiment", fontsize=15)
plt.xlabel('Delay before measurement [$\mu$s]', fontsize=15)
plt.ylabel('Signal [a.u.]', fontsize=15)
plt.legend()
plt.show()

else: 
# Ramsey experiment parameters
time_max_sec = 1.8 * us
time_step_sec = 0.025 * us
delay_times_sec = np.arange(0.1 * us, time_max_sec, time_step_sec)

# Drive parameters
# The drive amplitude for pi/2 is simply half the amplitude of the pi pulse
drive_amp = pi_amp / 2

# x_90 is a concise way to say pi_over_2; i.e., an X rotation of 90 degrees
with pulse.build(backend) as x90_pulse:
    drive_duration = get_closest_multiple_of_16(pulse.seconds_to_samples(drive_duration_sec))
    drive_sigma = pulse.seconds_to_samples(drive_sigma_sec)
    drive_chan = pulse.drive_channel(qubit)
    pulse.play(pulse.Gaussian(duration=drive_duration,
                              amp=drive_amp,
                              sigma=drive_sigma,
                              name='x90_pulse'), drive_chan)

detuning_MHz = 2 
ramsey_frequency = round(rough_qubit_frequency + detuning_MHz * MHz, 6) # need ramsey freq in Hz

# create schedules for Ramsey experiment 
delay = Parameter('delay')
with pulse.build(backend=backend, default_alignment='sequential', name="Ramsey delay Experiment") as ramsey_schedule:
    drive_chan = pulse.drive_channel(qubit)
    pulse.set_frequency(ramsey_frequency, drive_chan)
    pulse.call(x90_pulse)
    pulse.delay(delay, drive_chan)
    pulse.call(x90_pulse)

ramsey_gate = Gate("ramsey", 1, [delay])

qc_ramsey = QuantumCircuit(1, 1)

qc_ramsey.append(ramsey_gate, [0])
qc_ramsey.measure(0, 0)
qc_ramsey.add_calibration(ramsey_gate, (0,), ramsey_schedule, [delay])

exp_ramsey_circs = [qc_ramsey.assign_parameters({delay: get_dt_from(d)}, inplace=False) for d in delay_times_sec]

ramsey_schedule = schedule(exp_ramsey_circs[2], backend)
ramsey_schedule.draw(backend=backend)

# Execution settings
num_shots = 256

job = backend.run(exp_ramsey_circs, 
                  meas_level=1, 
                  meas_return='single', 
                  shots=num_shots)

job_monitor(job)

ramsey_results = job.result(timeout=120)

ramsey_values = []

for i in range(len(delay_times_sec)):
    iq_data = ramsey_results.get_memory(i)[:,qubit] * scale_factor
    ramsey_values.append(sum(map(classify, iq_data)) / num_shots)
    
plt.scatter(delay_times_sec/us, np.real(ramsey_values), color='black')
plt.xlim(0, np.max(delay_times_sec/us))
plt.title("Ramsey Experiment", fontsize=15)
plt.xlabel('Delay between X90 pulses [$\mu$s]', fontsize=15)
plt.ylabel('Measured Signal [a.u.]', fontsize=15)
plt.show()

fit_params, y_fit = fit_function(delay_times_sec/us, np.real(ramsey_values),
                                 lambda x, A, del_f_MHz, C, B: (
                                          A * np.cos(2*np.pi*del_f_MHz*x - C) + B
                                         ),
                                 [5, 1./0.4, 0, 0.25]
                                )

# Off-resonance component
_, del_f_MHz, _, 




}


