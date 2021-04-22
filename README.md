# mySUNI

Python을 활용한 CDS 과정 수업 활용 모듈



### 의존성 설치

```bash
pip install setuptools twine
```



### pypi 배포 과정

1. 소스코드 수정
   - mySUNI 폴더 내 파일 수정 후 2번 진행

2. 버전 업데이트 (setup.py)
   - setup.py 파일내 version +1 업데이트
   - mySUNI 폴더 내 `__init__.py`의 version +1 업데이트

3. whl 파일 생성

```bash
python setup.py bdist_wheel
```

4. whl 파일 업로드 

```bash
twine upload dist/mySUNI-X.X.X-py3-none-any.whl
```

