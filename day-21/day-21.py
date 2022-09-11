piano_keys = ["a","b","c","d","e","f","g"]
piano_tuple = ("do","re","mi","fa","sol","la","ti")

# list slicing
# c,d,e만 slicing
print(piano_keys[2:5]) # c,d,e

# 2부터 리스트 끝까지 slicing
print(piano_keys[2:]) #c,d,e,f,g

# 처음부터 5까지 slicing
print(piano_keys[:5]) #a,b,c,d,e

# 세번째 인자는 증가값, 리스트 처음부터 끝까지 값 중 하나씩 건너뛰면서 가져오기
print(piano_keys[::2]) #a,c,e,g

# 전체 리스트를 끝에서부터 역순으로 가는 리스트
print(piano_keys[::-1]) #g,f,e,d,c,b,a

# tuple slicing
print(piano_tuple[2:5]) #mi, fa, sol
print(piano_tuple[::-1]) #('ti', 'la', 'sol', 'fa', 'mi', 're', 'do')