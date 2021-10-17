## Citing FastReID

This repo is for self-use to find top conference papers by keyword and determine whether the authors' institutions are in our designated range.
It will generate the paper lists as csv files, the content format is shown as follows:
### {keyword}_papers_csv:
|**conference**|**year**|**author**|**title**|**booktitle**|**bibtex**|**electronic_edition**|
|-------|-------|-----------|-----------|-----------|-----------|:-------------------------------------------------------------------------------------------------------------|
|CVPR|2021|Yehansen Chen and Lin Wan and Zhihang Li and Qianyan Jing and Zongyuan Sun|Neural Feature Search for RGB-Infrared Person Re-Identification|"{IEEE} Conference on Computer Vision and Pattern Recognition, {CVPR} 2021, virtual, June 19-25, 2021"|https://dblp.org/rec/conf/cvpr/ChenWLJS21.bib|https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Neural_Feature_Search_for_RGB-Infrared_Person_Re-Identification_CVPR_2021_paper.html|

### {university}_{keyword}_papers.csv:
|**university**|**year**|**conference**|**info**|**bibtex**|**electronic_edition**|
|-------|-------|-----------|----------------------|-----------|:-------------------------------------------------------------------------------------------------------------|
|SUTD|2018|CVPR|"Weijian Deng and Liang Zheng and Qixiang Ye and Guoliang Kang and Yi Yang and Jianbin JiaoImage-Image Domain Adaptation With Preserved Self-Similarity and Domain-Dissimilarity for Person Re-Identification2018 {IEEE} Conference on Computer Vision and Pattern Recognition, {CVPR} 2018, Salt Lake City, UT, USA, June 18-22, 2018"|https://dblp.org/rec/conf/cvpr/Deng0YK0J18.bib|https://dblp.org/rec/conf/cvpr/ChenWLJS21.bib|http://openaccess.thecvf.com/content_cvpr_2018/html/Deng_Image-Image_Domain_Adaptation_CVPR_2018_paper.html|

## Requirements
Install all dependences libraries
``` bash
pip3 install -r requirements.txt
```
## Search Range
See [config.py](config.py). You can add your sources to the search range. 

By now the default setting is a set of top conferences on CV (Computer Vision) field in the past 5 years, and those conferences are CVPR, CVPR Workshop, ICCV, AAAI, IJCAI, ACMMM (ACM Multimedia), BMVC, NeurIPS, ECCV.

## Run:

### scrape.py:
``` bash
### Find papers by keyword without figuring out whether authors' institutions are in our range. 
python scrape.py --keyword="person re-id"

### Find papers by keyword and figure out whether authors' institutions are in our range of Singapore universities.
python scrape.py --keyword="person re-id" --find-sg(=True)
```

### outliers.py
* The file is meant to fix the outliers when finding papers of Singapore universities. If you've not tried to find papers of Singapore universities, please do not use this file.

``` bash
### Find papers by keyword without figuring out whether authors' institutions are in our range. 
python outliers.py --keyword="person re-id"
```