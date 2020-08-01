mutable_seq = [1, 2, 3, 4]
un_mutable_seq = (1, 2, 3, 4)

before1 = id(mutable_seq)
before2 = id(un_mutable_seq)

mutable_seq += [5]
un_mutable_seq += (5,)

after1 = id(mutable_seq)
after2 = id(un_mutable_seq)

# True
print(before1 == after1)

# False
print(before2 == after2)
