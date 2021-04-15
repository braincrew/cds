import json
import datetime
import requests
import urllib
import pandas as pd
import seaborn as sns
import requests
from requests.auth import HTTPBasicAuth
import os

dataset_files = {
    '국민연금':{
        'info': '2020년 9월 국민연금 데이터셋',
        'data': 'http://sk.jaen.kr:8080/national_pension.csv',
        'filename': 'national_pension.csv',
    },
    '서울시자전거':
    {
        'info': '서울시 따릉이 자전거 대여량 정보',
        'data': 'http://sk.jaen.kr:8080/seoul_bicycle.csv',
        'filename': 'seoul_bicycle.csv',
    }
}

files = {
    '자전거 대여량 예측':
    {
        'train.csv': 'http://sk.jaen.kr:8080/project/bsd/train.csv',
        'test.csv': 'http://sk.jaen.kr:8080/project/bsd/test.csv',
        'submission.csv': 'http://sk.jaen.kr:8080/project/bsd/sampleSubmission.csv',
    },
    '타이타닉 생존자 예측':
    {
        'train.csv': 'http://sk.jaen.kr:8080/2020/titanic_train.csv',
        'test.csv': 'http://sk.jaen.kr:8080/2020/titanic_test.csv',
        'submission.csv': 'http://sk.jaen.kr:8080/2020/titanic_submission.csv',
    },
    '주택 가격 예측':
    {
        'train.csv': 'http://sk.jaen.kr:8080/2020/titanic_train.csv',
        'test.csv': 'http://sk.jaen.kr:8080/2020/titanic_test.csv',
        'submission.csv': 'http://sk.jaen.kr:8080/2020/titanic_submission.csv',
    }
}

####### 데이터셋 관련 모듈 #######

class Dataset:

    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        # data 폴더 생성
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        titles = []
        infos = []
        datas = []
        filenames = []

        for t, data in dataset_files.items():
            titles.append(t)
            infos.append(data['info'])
            datas.append(data['data'])
            filenames.append(data['filename'])

        self.dataset = pd.DataFrame({
            'name': titles,
            'info': infos,
            'data': datas,
            'filename': filenames,
        })


    def info(self):
        display(self.dataset[['name', 'info', 'filename']])
        
        
    def load(self, dataset_name):
        global dataset_files
        fileurl = dataset_files[dataset_name]['data']
        filename = dataset_files[dataset_name]['filename']

        # auth
        username = 'mysuni'
        password = 'mysuni1!'

        r = requests.get(fileurl, auth=HTTPBasicAuth(username, password))
        filepath = os.path.join(self.data_dir, filename)
        open(filepath, 'wb').write(r.content)
        print(f'파일 다운로드: {filepath}')
        
        
dataset = Dataset()


def list_data():
    global dataset
    dataset.info()
    
    
def load_data(dataset_name):
    global dataset
    dataset.load(dataset_name)


####### 프로젝트 관련 모듈 #######

project = None


class Project:
    def __init__(self, project_name, class_info, email):
        self.project_name = project_name
        self.edu_name = "mySUNI"
        self.class_info = class_info
        self.email = email

    def __make_submission(self, submission):
        timestring = datetime.datetime.now().strftime('%H-%M-%S')
        filename = 'submission-{}.csv'.format(timestring)
        submission.to_csv(filename, index=False)
        print('파일을 저장하였습니다. 파일명: {}'.format(filename))
        return filename

    def __project_submission(self, file_name):
        file_path = './'
        url = f'http://manage.jaen.kr/api/studentProject/apiScoring?edu_name={self.edu_name}\
        &edu_rnd={self.class_info}&mail={self.email}&project_name={self.project_name}&file_name={file_name}'
        files = {'file': (file_name, open(file_path + file_name, 'rb'), 'text/csv')}
        r = requests.post(url, files=files)
        r.encoding = 'utf-8'
        message = ''
        if 'msg' in r.text:
            data = json.loads(r.text)
            message = '제출 여부 :{}\n오늘 제출 횟수 : {}\n제출 결과:{}'.format(data['msg'], data['trial'], data['score'])
        else:
            message = r.text
        return message

    def project_final_submission(self, name, csv_file_path, ipynb_file_path):
        url = "http://sk.jaen.kr/submission_final"
        files = [('file', open(csv_file_path, 'rb')), ('file', open(ipynb_file_path, 'rb'))]
        data = {'name': name}
        res = requests.post(url, data=data, files=files)
        print(res.text)

    def submit(self, submission):
        filename = self.__make_submission(submission)
        print(self.__project_submission(filename))


def load_project(project_name, class_info, email):
    global project, files
    project = Project(project_name, class_info=class_info, email=email)

    # data 폴더 경로 지정
    DATA_DIR = 'data'

    # data 폴더 생성
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    project_files = files[project_name]

    # auth
    username = 'mysuni'
    password = 'mysuni1!'
    for filename, fileurl in project_files.items():
        r = requests.get(fileurl, auth=HTTPBasicAuth(username, password))
        filepath = os.path.join(DATA_DIR, filename)
        open(filepath, 'wb').write(r.content)
        print(f'파일 다운로드: {filepath}')


def submit(submission_file):
    global project
    project.submit(submission_file)


def end_project(name, csv_file_path, ipynb_file_path):
    global project
    project.project_final_submission(name, csv_file_path, ipynb_file_path)
