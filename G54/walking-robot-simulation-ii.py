class Robot:

    def __init__(self, width: int, height: int):
        self.row = height-1
        self.col = width-1
        self.dir = "East"
        self.pos = [0,0]      

    def step(self, num: int) -> None:
       
        num %= 2*self.col+ 2*self.row
        if num == 0 and self.pos == [0,0]:
            self.dir = "South"
            return
        while num > 0:
            if self.dir == "East":
                if num <= self.col-self.pos[0]:
                    new_x = self.pos[0] + num
                    self.pos[0] = new_x
                    break
                else:
                    self.dir = "North"
                    num -= self.col - self.pos[0]
                    self.pos[0] = self.col

            elif self.dir == "North":
                if num <= self.row-self.pos[1]:
                    new_y = self.pos[1] + num
                    self.pos[1] = new_y
                    break
                else:
                    self.dir = "West"
                    num -= self.row - self.pos[1]
                    self.pos[1] = self.row
            elif self.dir == "West":
                if num <= self.pos[0]:
                    new_x = self.pos[0] - num
                    self.pos[0] = new_x
                    break
                else:
                    self.dir = "South"
                    num -= self.pos[0]
                    self.pos[0] = 0
            elif self.dir == "South":
                if num <= self.pos[1]:
                    new_y = self.pos[1] - num
                    self.pos[1] = new_y
                    break
                else:
                    self.dir = "East"
                    num -= self.pos[1]
                    self.pos[1] = 0

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()