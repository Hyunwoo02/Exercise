import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import numpy as np

# 드론의 기 정보를 저장하는 클래스
class Drone:
    def __init__ (self, id, position, velocity, leader=False):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.leader = False
    def update_position(self, dt):
        # 드론의 위치를 업데이트하는 메소드
        self.position += self.velocity * dt
    def update_velocity(self, new_velocity):
        # 드론의 속도를 업데이트하는 메소드
        self.velocity = new_velocity
    def get_position(self):
        # 드론의 현재 위치를 반환하는 메소드
        return self.position
    def get_velocity(self):
        # 드론의 현재 속도를 반환하는 메소드
        return self.velocity
    def get_id(self):
        # 드론의 ID를 반환하는 메소드
        return self.id
    def _set_position(self, position):
        # 드론의 위치를 설정하는 메소드
        self.position = position
    def __str__(self):
        return f"Drone {self.id}: Position {self.position}, Velocity {self.velocity}"


# 드론의 위치를 업데이트하는 함수
def update_drones(drones, dt):
    for drone in drones:
        drone.update_position(dt)
        print(drone)

# 중심 위치 계산 함수
def calculate_center(drones):
    positions = np.array([drone.position for drone in drones])
    return np.mean(positions, axis=0)

# 목표 위치 계산 함수
def calculate_formation_positions(center, N, dist):
    r = dist / (2 * np.sin(np.pi / N))
    positions = []
    for i in range(N):
        theta = 2 * np.pi * i / N
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        z = center[2]  # 같은 높이 유지
        positions.append(np.array([x, y, z]))
    return positions


# # 드론의 위치를 시각화하는 함수
# def plot_drones(drones):
#     plt.ion()
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     for _ in range(100):
#         ax.clear()
#         for drone in drones:
#             ax.scatter(drone.position[0], drone.position[1], drone.position[2], label=f"Drone {drone.id}")
#         ax.set_xlim(-30, 30)
#         ax.set_ylim(-30, 30)
#         ax.set_zlim(-30, 30)
#         ax.set_xlabel('X axis')
#         ax.set_ylabel('Y axis')
#         ax.set_zlabel('Z axis')
#         ax.legend()
#         plt.pause(0.1)
#     plt.ioff()
#     plt.show()

# 드론 초기화
drones = [Drone(i, np.random.rand(3) * 20 - 10, np.array([0.0, 0.0, 0.0])) for i in range(10)]
dist = 5  # 드론 간 거리

# 중심과 목표 위치 계산
center = calculate_center(drones)
target_positions = calculate_formation_positions(center, len(drones), dist)
# 실시간 드론 위치 시각화 함수
def plot_drones(drones):
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for _ in range(100):
        ax.clear()
        i = 0
        for drone in drones:
            drone._set_position(target_positions[i])
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
        plt.pause(0.1)
        # update_drones(drones, 0.1)
    plt.ioff()
    plt.show()

# 드론 위치 시각화
plot_drones(drones)
