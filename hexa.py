class convert:
    print ("Welcome to Our Converter")
    print ("Rules : ")
    print ("Press 1 to convert decimal to hexa")
    print ("Press 2 to convert decimal to binary")
    print ("If the values input not valid programms gonna stop")
    a = str(input("Choose Your Option : "))
    def show(self):
        continiti = 'y'
        while continiti == 'y':
            try:
                if self.a == '1':
                    values = int(input("Enter Your Decimal to Convert Hexa : "))
                    print("The results is ",hex(values))
                else:
                    values = int(input("Enter Your Decimal to Convert Binary : "))
                    print("The results is ",bin(values))
                    print("b is represent a binary")
            except:
                ValueError("Your Value is wrong")
            continiti = input("Continue press 'Y stop press 'X or other alphabet' : ")


if __name__ == "__main__":
    cvok = convert()
    cvok.show()
            
            
        
