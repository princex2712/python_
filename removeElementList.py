#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def fun(list_):
    list_.pop(0)
    list_.pop(3)
    list_.pop(3)
    print(list_)
list_ = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
fun(list_)