def maxBatteryEnergy(N, K, energy):
    max_change = 0  # 배터리 에너지 변화의 최댓값을 저장하는 변수

    # 자석의 크기를 2부터 N까지 변경하면서 최댓값을 구함
    for size in range(2, N + 1):
        total_energy = 0  # 배터리의 총 에너지 변화량을 저장하는 변수

        # 자석의 N극과 S극이 놓인 칸의 인덱스 범위를 계산
        start = 0
        end = N - size

        # 자석을 이동하며 배터리의 에너지 변화량을 계산
        for i in range(start, end + 1):
            n_pole_energy = energy[i]  # N극이 놓인 칸의 에너지 상수
            s_pole_energy = energy[i + size - 1]  # S극이 놓인 칸의 에너지 상수
            diff_energy = (i + size - 1) - i  # N극과 S극의 번호 차이

            # 배터리의 에너지 변화량 계산
            energy_change = n_pole_energy + s_pole_energy - K * diff_energy
            total_energy += energy_change

        # 최댓값 갱신
        max_change = max(max_change, total_energy)

    return max_change

# 입력 받기
N, K = map(int, input().split())
energy = list(map(int, input().split()))

# 함수 호출하여 결과 출력
result = maxBatteryEnergy(N, K, energy)
print(result)
