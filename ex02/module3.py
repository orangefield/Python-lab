# 폴더 안에 있는 module을 불러오자
import sys

# 내장 라이브러리 - import 없이 사용 가능 (디폴트 class-path)
print(sys.modules)
print("="*50)

# 외장 라이브러리 - built-in 모듈 - import 해야 함
# 라이브러리 경로 추가 가능(필요할 때 검색하기)
print(sys.path)
