urls = [
    'https://dblp.org/db/conf/cvpr/cvpr2021.html',
    'https://dblp.org/db/conf/cvpr/cvprw2021.html',
    'https://dblp.org/db/conf/cvpr/cvpr2020.html',
    'https://dblp.org/db/conf/cvpr/cvprw2020.html',
    'https://dblp.org/db/conf/cvpr/cvpr2019.html',
    'https://dblp.org/db/conf/cvpr/cvprw2019.html',
    'https://dblp.org/db/conf/cvpr/cvpr2018.html',
    'https://dblp.org/db/conf/cvpr/cvprw2018.html',
    'https://dblp.org/db/conf/cvpr/cvpr2017.html',
    'https://dblp.org/db/conf/cvpr/cvprw2017.html',
    'https://dblp.org/db/conf/iccv/iccv2019.html',
    'https://dblp.org/db/conf/iccv/iccv2017.html',
    'https://dblp.org/db/conf/aaai/aaai2021.html',
    'https://dblp.org/db/conf/aaai/aaai2020.html',
    'https://dblp.org/db/conf/aaai/aaai2019.html',
    'https://dblp.org/db/conf/aaai/aaai2018.html',
    'https://dblp.org/db/conf/aaai/aaai2017.html',
    'https://dblp.org/db/conf/ijcai/ijcai2021.html',
    'https://dblp.org/db/conf/ijcai/ijcai2020.html',
    'https://dblp.org/db/conf/ijcai/ijcai2019.html',
    'https://dblp.org/db/conf/ijcai/ijcai2018.html',
    'https://dblp.org/db/conf/ijcai/ijcai2017.html',
    'https://dblp.org/db/conf/mm/mm2020.html',
    'https://dblp.org/db/conf/mm/mm2019.html',
    'https://dblp.org/db/conf/mm/mm2018.html',
    'https://dblp.org/db/conf/mm/mm2017.html',
    'https://dblp.org/db/conf/bmvc/bmvc2020.html',
    'https://dblp.org/db/conf/bmvc/bmvc2019.html',
    'https://dblp.org/db/conf/bmvc/bmvc2018.html',
    'https://dblp.org/db/conf/bmvc/bmvc2017.html',
    'https://dblp.org/db/conf/nips/neurips2020.html',
    'https://dblp.org/db/conf/nips/nips2019.html',
    'https://dblp.org/db/conf/nips/nips2018.html',
    'https://dblp.org/db/conf/nips/nips2017.html',
]
names = [
    'CVPR2021',
    'CVPRW2021',
    'CVPR2020',
    'CVPRW2020',
    'CVPR2019',
    'CVPRW2019',
    'CVPR2018',
    'CVPRW2018',
    'CVPR2017',
    'CVPRW2017',
    'ICCV2019',
    'ICCV2017',  
    'AAAI2021',
    'AAAI2020',
    'AAAI2019',
    'AAAI2018',
    'AAAI2017',
    'IJCAI2021',
    'IJCAI2020',
    'IJCAI2019',
    'IJCAI2018',
    'IJCAI2017',
    'ACMMM2020',
    'ACMMM2019',
    'ACMMM2018',
    'ACMMM2017',
    'BMVC2020',
    'BMVC2019',
    'BMVC2018',
    'BMVC2017',
    'NeurIPS2020',
    'NeurIPS2019',
    'NeurIPS2018',
    'NeurIPS2017',
]
# For ECCV
for i in range(1,31):
    urls.append(f'https://dblp.org/db/conf/eccv/eccv2020-{i}.html')
    names.append('ECCV2020')
for i in range(1,17):
    urls.append(f'https://dblp.org/db/conf/eccv/eccv2018-{i}.html')
    names.append('ECCV2018')


# NTU, NUS, SUTD, SMU, SIT, SUSS
sg_universities = {
    'NTU':["Nanyang Technological University", "ntu.edu.sg", "NTU"],
    'NUS':["National University of Singapore", "nus.edu.sg", "NUS"],
    'SUTD': ["Singapore University of Technology and Design", "sutd.edu.sg", "SUTD"],
    'SMU':["Singapore Management University", "smu.edu.sg", "SMU"],
    'SIT': ["Singapore Institute of Technology","SingaporeTech.edu.sg", "singaporetech.edu.sg"],
    'SUSS': ["Singapore University of Social Sciences", "suss.edu.sg", "SUSS"]
    }
search_list = []
for uni, keywords in sg_universities.items():
    search_list += keywords


header = ['conference', 'year', 'author', 'title', 'booktitle', 'bibtex', 'electronic_edition']
header_sg = ['university', 'year', 'conference', 'info', 'bibtex', 'electronic_edition']