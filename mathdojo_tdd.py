import unittest
from mathdojo import MathDojo

class Test_MathDojo(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.md = MathDojo()
        self.num1 = 1
        self.num2 = 1
        self.num3 = 1
        self.num4 = 1

    def test01(self):
        print("Realizando Test 1")
#        md = MathDojo()
        self.assertEqual(self.md.subtract(self.num1,self.num2,self.num3).result, -3)

    def test02(self):
        print("Realizando Test 2")
#        md = MathDojo()
        self.assertEqual(self.md.add(self.num1,self.num2,self.num3,self.num4).result, 4)

    def test03(self):
        print("Realizando Test 3")
#        md= MathDojo()
        self.assertNotEqual(self.md.avg(5,1,4,3,1,1), 3)

    def test04(self):
        print("Realizando Test 4")
#        md= MathDojo()
        self.assertEqual(self.md.subtract(5,1).result, -6)

    def test05(self):
        print("Realizando Test 5")
#        md= MathDojo()
        self.assertEqual(self.md.subtract(-5,1).result, 4)
 

if __name__ == '__main__':
    unittest.main()
