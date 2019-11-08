<p align="center">
  <a href="#">
    <img src="https://img.shields.io/github/last-commit/Writeup001/QQ_PhoneBrowser_Wallpaper" /></a>
  
  <a href="https://www.python.org/">
     <img src="https://img.shields.io/badge/language-Python3-brightgreen" /></a>
  
  <a href="#">
    <img src="https://img.shields.io/github/repo-size/Writeup001/QQ_PhoneBrowser_Wallpaper?color=brightgreen&label=images%20size" /></a>

  <a href="#">
    <img src="https://img.shields.io/badge/license-GPLv3-blue" /></a>
  <a href="https://github.com/Writeup001/QQ_PhoneBrowser_Wallpaper/">
    <img src="https://img.shields.io/github/stars/Writeup001/QQ_PhoneBrowser_Wallpaper?style=social" /></a>
        
  <a href="https://github.com/Writeup001/QQ_PhoneBrowser_Wallpaper/">
    <img src="https://img.shields.io/github/forks/Writeup001/QQ_PhoneBrowser_Wallpaper?style=social" /></a>

</p>

# QQ_PhoneBrowser_Wallpaper
每天定时抓取手机QQ浏览器的每日特辑高清壁纸，并上传备份到 GitHub

腾讯特辑接口：https://today.html5.qq.com/share?idList=2516073
![Website](https://img.shields.io/website?url=https://today.html5.qq.com/share?idList=2516073)

往日特辑接口：https://api.aynu.top/Phone_Wallpaper/Previous_img/1.png
![Website](https://img.shields.io/website?url=https://api.aynu.top/Phone_Wallpaper/Previous_img/1.png)

每日特辑接口：http://api.aynu.top/QQ_PhoneBrowser_Wallpaper/2019_11_08/1.png
![Website](https://img.shields.io/website?url=http://api.aynu.top/QQ_PhoneBrowser_Wallpaper/2019_11_08/1.png)

2019 年 11 月 06 日之前的图片存放于 **往日特辑** 接口服务器中，共计 6168 张，并且按照自然数字从 1 开始排序，至 6168

2019 年 11 月 06 日及其以后日期的土拍你存放于 **每日特辑** 接口服务器中，以日期作为文件夹，按照自然数字从 1 开始以此类推命名图片。

备份服务器仅为存储备份使用，请大家勿对备份服务器进行爬取造成服务器压力，我会每天定时将从腾讯爬取下来的图片上传至 GitHub 您可以随意下载，如果你所在的地区下载速度较慢，你也可以联系我，我将所有已下载的图片打包发于你。
# 运行环境
```
pip install requests

pip install lxml
```

或者执行
```
pip install -r requirements.txt
```
进行安装运行所需的环境
# 运行
运行之前请确保 **QQ_PhoneBrowser_Wallpaper.py** 文件和 **startID.txt** 文件处于同一目录下，startID.txt 文件内写入的是爬虫文件开始爬取的 ID 你也可以随意修改，腾讯每日特辑第一张图片的 ID 值为：2516073
```
python QQ_PhoneBrowser_Wallpaper.py
```
# 生成文件
默认在当前文件夹下生成以时间形式命名的文件夹，例如：
```
2019_11_06
```
生成的图片文件命名则是以 ID 形式命名的，例如：
```
2522546.png
```
# 接口来源
本接口来源是腾讯旗下手机 QQ 浏览器（项目使用版本 v9.8.0.5433）

具体路径如下：
```
我的 -- 福利中心 -- 下载壁纸 -- 每日特辑
```
接口 URL 如下格式：
```
https://today.html5.qq.com/share?idList=2516073
```
2516073 这个 ID 应该是腾讯正式开始做每日特辑的第一张图片（使用二分法遍历得出来的结果）往后的每一天的每日特辑图片都是在此基础上增加 ID 值的，部分 ID 并不是连续的，但腾讯每天更新图片不会超过 10 张，ID 值不连续增加也不会超过 100

所以，针对上述已知问题此程序对这些问题有进行优化处理，仍可以完整获得每一天的每一张图片。

# 声明
本项目图片来源为腾讯公司，图片版权及其解释权归腾讯公司所有。

# License
GNU General Public License v3.0
