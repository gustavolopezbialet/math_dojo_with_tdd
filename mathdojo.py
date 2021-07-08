class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result = self.result + num
        if len(nums) > 0:
            for i in nums:
                self.result = self.result + i
        return self

#    def add(self, num, *nums):
#        self.result += num
#        for i in range(len(nums)):
#            if type(nums[i]) is list or type(nums[i]) is tuple:
#                for j in nums[i]:
#                    self.result += j
#            else:
#                self.result += nums[i]
#        return self

    def subtract(self, num, *nums):
        self.result = self.result - num
        if len(nums) > 0:
            for i in nums:
                self.result = self.result - i
        return self

#    def subtract(self, num, *nums):
#        self.result -= num
#        for i in range(len(nums)):
#            if type(nums[i]) is list or type(nums[i]) is tuple:
#                for j in nums[i]:
#                    self.result -= j
#           else:
#                self.result -= nums[i]
#        return self

    def avg(self, num, *nums):
        media = (self.add(num,*nums).result) / (len(nums)+1)
        return media


# -------------crear una instruccion:
md = MathDojo()

# -------------- calcula el promedio
md1 = MathDojo()
media = md1.avg(2, 3, 4, 3)
# print(media)

# --------------para probar:

# x = md.add(2).add(2,5,1).subtract(3,2).result
# x = md.add(1,1,1,1).result
# print(x)	# debe imprimir 5

# ---------------corre cada uno de los metodos algunos mas veces y valida el resultado!