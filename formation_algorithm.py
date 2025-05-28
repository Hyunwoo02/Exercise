import drones as dr
import numpy as np
import math
import time

# 중심 위치 계산 함수
def calculate_center(drones):
    positions = np.array([drone.position for drone in drones])
    return np.mean(positions, axis=0)

# 목표 위치 계산 함수
# 드론들이 원형으로 배치될 때의 목표 위치를 계산하는 함수
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

# 목표 위치까지 이동 시 필요한 속도 계산 함수 
def calculate_velocity(drones, target_positions, refresh_rate=10):
    velocities = []
    for drone, target in zip(drones, target_positions):
        direction = target - drone.position
        if np.linalg.norm(direction) > 0:
            velocity = direction / np.linalg.norm(direction) * (np.linalg.norm(direction) / refresh_rate)
        else:
            velocity = np.zeros_like(drone.velocity)
        velocities.append(velocity)
    return velocities

# 하나의 드론의 목표 위치 달성 확인 함수
def check_drone_formation(drone, target_position, tolerance=0.1):
    return np.linalg.norm(drone.position - target_position) <= tolerance

# 목표 위치 달성 확인 함수
def check_formation(drones, target_positions, tolerance=0.1):
    for drone, target in zip(drones, target_positions):
        if np.linalg.norm(drone.position - target) > tolerance:
            return False
    return True
# 드론의 위치를 시간에 따라 업데이트하는 함수
def update_drone(drone, dt = 1):
    drone.update_position(dt)
    print(drone)
    
def update_drones(drones, dt=1):
    for drone in drones:
        drone.update_position(dt)
        print(drone)
# 드론의 위치를 설정하는 함수
def set_drone_position(drone, position):
    drone._set_position(position)
    print(f"Drone {drone.id} position set to {position}")


