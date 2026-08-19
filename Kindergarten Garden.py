class Garden:
    
    list_student = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    plants_dict = {
        "G" : "Grass",
        "C" : "Clover",
        "R" : "Radishes",
        "V" : "Violets"
    }
    def __init__(self, diagram, students = None):
        self.diagram = diagram.splitlines()
        if students is None:
            self.students = self.list_student
        else:
            self.students = sorted(students)
        
        
    def plants(self, student_name):
        student_order = 0
        for index, name in enumerate(self.students):
            if name == student_name:
                student_order = index 
        keywords = []
        keywords.append(self.diagram[0][student_order*2])
        keywords.append(self.diagram[0][student_order*2 + 1])
        keywords.append(self.diagram[1][student_order*2])
        keywords.append(self.diagram[1][student_order*2 + 1])
        
        output =[]
        for item in keywords:
            output.append(self.plants_dict[item])
        return output   