class Human:

    name = 'Ranjith'

    @classmethod
    def is_male(cls):
        return True


# Create Class Method
# Human.is_male = classmethod(Human.is_male)
print(Human.is_male())