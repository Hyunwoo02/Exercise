import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time



#formation 알고리즘 구현 필요
import drones as dr
import formation_algorithm as fa

# 드론의 초기 위치와 속도를 설정
drone_count = 6
drones = [dr.Drone(i, np.random.rand(3) * 20 - 10, np.array([0.0, 0.0, 0.0])) for i in range(drone_count)]
refresh_rate = 100  # 초당 업데이트 횟수


dist = 10.0  # 드론 간 거리
# 중심과 목표 위치 계산
center = fa.calculate_center(drones)
target_positions = fa.calculate_formation_positions(center, len(drones), dist)
# 드론의 속도를 목표 위치로 향하도록 업데이트
velocities = fa.calculate_velocity(drones, target_positions, refresh_rate)
# 드론의 속도를 업데이트
for drone, velocity in zip(drones, velocities):
    drone.update_velocity(velocity)
# 드론의 위치를 업데이트하는 함수


# 실시간 드론 위치 시각화 함수
def plot_drones(drones):
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for _ in range(100):
        ax.clear()
        # for drone in drones:
        #     ax.scatter(drone.position[0], drone.position[1], drone.position[2], label=f"Drone {drone.id}")
        i = 0
        for drone in drones:
            # if fa.check_drone_formation(drone, target_positions[i]):
            #     drone.update_velocity(np.zeros_like(drone.velocity))
            # fa.update_drone(drone)  # 드론 위치 업데이트
            
            if fa.check_formation(drones, target_positions):
                drone.update_velocity(np.zeros_like(drone.velocity))
                
            i += 1
            ax.scatter(drone.position[0], drone.position[1], drone.position[2], label=f"Drone {drone.id}")
        arg = 20
        ax.set_xlim(-arg, arg)
        ax.set_ylim(-arg, arg)
        ax.set_zlim(-arg, arg)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.legend()
        plt.pause(1/refresh_rate)  # refresh_rate에 따라 업데이트 속도 조절
        fa.update_drones(drones)
    plt.ioff()
    plt.show()

# 드론 위치 시각화
plot_drones(drones)
