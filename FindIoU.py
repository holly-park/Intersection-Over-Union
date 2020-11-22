def InputBoxValue():
    box1=[]
    print("value of box1")
    left_1 = int(input('left: '))
    right_1 = int(input('right: '))
    top_1 = int(input('top: '))
    bottom_1 = int(input('bottom: '))
    box1.append(left_1)
    box1.append(right_1)
    box1.append(top_1)
    box1.append(bottom_1)

    box2=[]
    print("value of box2")
    left_2 = int(input('left: '))
    right_2 = int(input('right: '))
    top_2 = int(input('top: '))
    bottom_2 = int(input('bottom: '))
    box2.append(left_2)
    box2.append(right_2)
    box2.append(top_2)
    box2.append(bottom_2)
    #print(box1, box2)
    return box1, box2

def CalculateIoU():
    box1, box2 = InputBoxValue()
    box1_res = sum(box1)
    box2_res = sum(box2)
    IoU = 0
    if box1_res < box2_res:
        IoU = box1_res/box2_res
    else:
        IoU = box2_res/box1_res

    print("IoU: ", IoU)

CalculateIoU()
