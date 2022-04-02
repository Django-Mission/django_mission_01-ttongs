from django.shortcuts import render
from django.http import HttpResponse
from random import sample

# Create your views here.
def calculator(request):
    #return HttpResponse('계산기 기능 구현 시작입니다.ㅎㅎ') #템플릿을 사용하지 않고 응답할 수 있다.(HttpResponse)
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    #print(f'request __dict__ = {request.__dict__}')
    print(f'num1 = {request.GET.get("num1")}')
    print(f'num2 = {request.GET.get("num2")}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result' : result})

# mission1 - basic
def lotto_basic(request): 
    
    # 1. 처리
    lotto_seed = list(range(1, 46)) # 1부터 45까지 숫자 리스트 생성
    lotto_num = sample(lotto_seed, 6) # 1~45 중 6개 숫자 추출
    
    # 2. 응답
    return render(request,'lotto1.html',{'result': lotto_num})

# mission1 - challenge
def lotto_challenge(request):
    
    # 1. 응답
    return render(request,'lotto2.html')

# mission1 - challenge
def lotto_result(request):

    # 1. 데이터 확인
    num1 = request.GET.get('num1') # 입력한 게임 수 가져오기

    # 2. 처리
    lotto_seed = list(range(1, 46))
    lotto_nums = []
    num = int(num1)

    for i in range(num):
        lotto_num = list(sample(lotto_seed, 6))
        lotto_nums.append(lotto_num)

    # 3. 응답
    return render(request, 'lotto2_result.html', {'result' : lotto_nums, 'num' : num})