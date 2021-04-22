# mySUNI

Python을 활용한 CDS 과정 수업 활용 모듈



### 의존성 설치

```bash
pip install setuptools twine
```



### pypi 배포 과정

1. 소스코드 수정
   - mySUNI 폴더 내 파일 수정 후 2번 진행
2. whl 파일 생성

```bash
python setup.py bdist_wheel
```

3. whl 파일 업로드 

```bash
twine upload dist/mySUNI-X.X.X-py3-none-any.whl
```

