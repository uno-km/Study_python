# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

print("{0: >10}".format(+500))
print("{0: >10}".format(-500))
# 양수일땐 +표시, 음수일땐 -표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_>+10}".format(+500))
print("{0:_>+10}".format(-500))

# 3자리 마다 콤마찍기
print("{0:,}".format(5000000000000000000))
print("{0:+,}".format(5000000000000000000))
print("{0:+,}".format(-5000000000000000000))
# 3자리 마다 콤마를 찍는데, 부호도 붙이고, 자릿수 확보
# 돈이 많으면 행복하니 빈자리는 ^^로 채우기
print("{0:ㅋ<+30,}".format(10000000000000000000))
# 소수점 출력
print("{0:.10f}".format(5 / 3))
# 소수점 반올림
print("{0:.2f}".format(5 / 3))
