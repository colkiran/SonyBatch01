

print("find".center(60, "-"))
st = "hello world"
# print(dir(st))

print(f"st :{st}")
idx = st.find("l")
print(f"index :{idx}")

print("-" * 60)
idx = st.find("l", )
print(f"index :{idx}")

idx = st.find("l", st.find("l")+1)
print(f"index :{idx}")

idx = st.find("l", st.find("l", st.find("l")+1)+1)
print(f"index :{idx}")

print("replace".center(60, "-"))
st = "hello world"
print(f"st :{st}")

res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

res = st[:st.find("w")] + st[st.find("w"):].replace("l", "L")
print(f"res :{res}")

# "hello " + "world"
# res= st[:6] + st[6:].replace("l", "L")

print("count".center(60,"-"))
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

print(f"count of 'o' :{st.count('o')}")
print(f"count of 'e' :{st.count('e')}")
print(f"count of 'a' :{st.count('a')}")

print("split".center(60, "-"))
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.split()
print(f"res :{res}")

st = "the,quick,brown,fox,jumps,over,the,lazy,dog"
print(f"st :{st}")

res = st.split(",")
print(f"res :{res}")

print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

a = "helowrd"
b = "HELOWRD"

# The length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
