import modules.perimeter as perimetr
import modyles.factorial as factorial

f1 = factorial.factorial_norm(5)
print(f1)
f2 = factorial.factorial_norm(17)
print(f2)
f3 =  factorial.factorial_norm(5)
print(f3)
f4 =  factorial.factorial_norm(15)
print(f4)

print(f1 == f3, f2 == f4)


p1 = perimeter.perimetr_func([1, 2, 5])
print(p1)

p2 = perimeter.perimetr_func([1, 2, 5, 7, 1])
print(p2)

print('hello world')
