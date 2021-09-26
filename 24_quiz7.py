# Quiz7) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 	보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - X주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
#
# 조건: 파일명은 '01주차.txt', '02주차.txt', ..., '50주차.txt'와 같이 만듭니다.

for week in range(1, 51):
	with open('weekly_reports/{:0>2}주차.txt'.format(week), 'w') as weekly_report:
		weekly_report.write('- {}주차 주간보고 -\n부서 :\n이름 :\n업무 요약:'.format(week))