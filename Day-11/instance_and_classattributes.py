class Question:
    print("class is loaded")

    valid_types = ['mcq','text']
    total_created = 0

    def __init__(self, text, question_type, marks):
        self.text = text
        self.question_type = question_type
        self.mark = marks


print("Question  created:0", Question.total_created)

q1 = Question("python is ___ language.", "mcq", 2)
q2 = Question("What is Class?", "text", 5)
q3 = Question("What does len() do?", "mcq", 2)

print("Question  created:", Question.total_created)
print("Valid Types:", Question.valid.types)


# Class attr accessible from object too, but it's shared
print(q1.total_created)   # 3 — same number
print(q2.total_created)   # 3 — same number

q4 = Question("what is ur name?", "video", 2)

# This will raise ValueError:
# q4 = Question("Bad type", "video", 2)  ← ValueError