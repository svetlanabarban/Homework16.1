#1

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

#2

def build_sentence(benefit):
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    print(build_sentence(list_of_benefits[0]))
    print(build_sentence(list_of_benefits[1]))
    print(build_sentence(list_of_benefits[2]))
    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()