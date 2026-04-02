class Question:
    pass

q1 = Question()
print(q1)
print(id(q1))

q2 = Question()
q1.text = "What is Python?"
q2.text = "How is OOPs."

print(q1.text)
print(q2.text)