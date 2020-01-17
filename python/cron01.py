# < 스케쥴을 맞추기 >

# 리눅스에만 가능함.
# < cron

# pip install apscheduler 아나콘다 프롬프트에 설치

from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval(): # 일정시간 간격으로 수행
    print("hello world") # 이자리에 크롤링하는 주소 넣으면 그 주소로가서 일정 시간에 크롤링 실행함

def exec_cron():
    # 시간을 문자열로 변환해 주는 것에  '%c'라는 빈 값을 정해주고 지역타임에 있는 시간타임을 그 빈 변수에 담아준다! 그것을 문자열로 변환!
    str = time.strftime('%c', time.localtime(time.time())) # strftime => 날짜/시간을 스트링으로 변환하는 함수
    print("cron:", str) # 변환한 것을 프린트!


sched = BlockingScheduler() # APScheduler => 파이썬 스크립트를 주기적으로 실행하게 해주는 것
# BlockingScheduler => 하나의 프로세스가 돌아가야할 때 사용
# 5초 간격으로 exec_interval()함수 호출하기 
# sched.add_job(exec_interval, 'interval', seconds=5 )

# 예약 방식 (매시간 10초 30초 일 경우 구동)
sched.add_job(exec_cron, 'cron', minute="*", second="10, 30")

# 위에 스타트 하는 명령어
sched.start()

# 참고 : https://apscheduler.readthedocs.io/en/v2.1.2/cronschedule.html