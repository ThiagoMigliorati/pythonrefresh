class ClassTest:
    def instance_method(self):
        print(f"Called instance off {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print(f"called static method")

    

ClassTest.static_method();