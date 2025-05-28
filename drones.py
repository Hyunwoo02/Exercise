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

