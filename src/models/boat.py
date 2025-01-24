class Boat:
    def __init__(self, coordinates, heading, speed, item_count):
        self.coordinates = coordinates  # 坐标
        self.heading = heading            # 航向
        self.speed = speed                # 速度
        self.item_count = item_count      # 物品数量

    def sail(self):
        # 行驶逻辑
        pass

    def stop(self):
        # 停止逻辑
        pass

    def return_home(self):
        # 返航逻辑
        pass