def generate_smupc_name(n, s):
    cnt = 0
    visited = [0] * 26
    answer = ""

    for char in s:
        index = ord(char) - ord('a')
        if visited[index]:
            cnt += 1
        else:
            visited[index] = 1
            answer += char

    answer += str(cnt + 4)
    answer = str(n + 1906) + answer
    answer = answer[::-1]
    answer = "smupc_" + answer

    return answer

# 입력 받기
n, s = input().strip().split()

# 등록 번호와 영어 이름을 적절한 타입으로 변환
n = int(n)

# SMUPC NAME 생성
smupc_name = generate_smupc_name(n, s)

# 결과 출력
print(smupc_name)
