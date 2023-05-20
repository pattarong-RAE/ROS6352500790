obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'dice': [155, 38], 'mouse':
[200, 45], 'keyboard': [298, 65], 'fan': [300, 36]}
data_x = []
answer = []
for k,v in obj_detected.items():
    data_x.append(v[0])
for i in sorted(data_x):
    for k,j in obj_detected.items():
        if i == j[0]:
            answer.append(k)
            break
print(answer)