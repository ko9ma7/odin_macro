import random
import time
import Mouse
import MousePos

def wearing(): # 장비 입기
    Mouse.delayClick(MousePos.bag_mouse_pos)
    time.sleep(2)
    Mouse.delayClick(MousePos.unequip_mouse_pos)
    Mouse.delayClick(MousePos.esc_mouse_pos)
    


def takeOut(): # 장비 꺼내기
    one_mouse_pos = [random.randrange(26, 96), random.randrange(249, 320)]
    two_mouse_pos = [random.randrange(116, 186), random.randrange(249, 320)]
    three_mouse_pos = [random.randrange(205, 274), random.randrange(249, 320)]
    four_mouse_pos = [random.randrange(291, 360), random.randrange(249, 320)]

    five_mouse_pos = [random.randrange(26, 96), random.randrange(341, 408)]
    six_mouse_pos = [random.randrange(116, 186), random.randrange(341, 408)]
    seven_mouse_pos = [random.randrange(205, 274), random.randrange(341, 408)]
    eight_mouse_pos = [random.randrange(291, 360), random.randrange(341, 408)]

    nine_mouse_pos = [random.randrange(26, 96), random.randrange(430, 495)]
    ten_mouse_pos = [random.randrange(116, 186), random.randrange(430, 495)]
    eleven_mouse_pos = [random.randrange(205, 274), random.randrange(430, 495)]
    twelve_mouse_pos = [random.randrange(291, 360), random.randrange(430, 495)]

    thirteen_mouse_pos = [random.randrange(26, 96), random.randrange(523, 586)]
    fourteen_mouse_pos = [random.randrange(116, 186), random.randrange(523, 586)]
    fifteen_mouse_pos = [random.randrange(205, 274), random.randrange(523, 586)]
    sixteen_mouse_pos = [random.randrange(291, 360), random.randrange(523, 586)]

    seventeen_mouse_pos = [random.randrange(26, 96), random.randrange(605, 676)]
    eighteen_mouse_pos = [random.randrange(116, 186), random.randrange(605, 676)]
    nineteen_mouse_post = [random.randrange(205, 274), random.randrange(605, 676)]

    Mouse.click(MousePos.storage_mouse_pos)
    time.sleep(15)

    Mouse.click(one_mouse_pos)
    Mouse.click(two_mouse_pos)
    Mouse.click(three_mouse_pos)
    Mouse.click(four_mouse_pos)
    Mouse.click(five_mouse_pos)
    Mouse.click(six_mouse_pos)
    Mouse.click(seven_mouse_pos)
    Mouse.click(eight_mouse_pos)
    Mouse.click(nine_mouse_pos)
    Mouse.click(ten_mouse_pos)
    Mouse.click(eleven_mouse_pos)
    Mouse.click(twelve_mouse_pos)
    Mouse.click(thirteen_mouse_pos)
    Mouse.click(fourteen_mouse_pos)
    Mouse.click(fifteen_mouse_pos)
    Mouse.click(sixteen_mouse_pos)
    Mouse.click(seventeen_mouse_pos)
    Mouse.click(eighteen_mouse_pos)
    Mouse.click(nineteen_mouse_post)

    Mouse.delayClick(MousePos.take_out_mouse_pos)
    Mouse.delayClick(MousePos.esc_mouse_pos)


def unequip(): # 장비 창고 넣기
    one_mouse_pos = [random.randrange(1466, 1539), random.randrange(160, 236)]
    two_mouse_pos = [random.randrange(1556, 1620), random.randrange(160, 236)]
    three_mouse_pos = [random.randrange(1646, 1714), random.randrange(160, 236)]
    four_mouse_pos = [random.randrange(1734, 1802), random.randrange(160, 236)]
    five_mouse_pos = [random.randrange(1824, 1893), random.randrange(160, 236)]
    six_mouse_pos = [random.randrange(1466, 1539), random.randrange(250, 321)]
    seven_mouse_pos = [random.randrange(1556, 1620), random.randrange(250, 321)]
    eight_mouse_pos = [random.randrange(1646, 1714), random.randrange(250, 321)]
    nine_mouse_pos = [random.randrange(1734, 1802), random.randrange(250, 321)]
    ten_mouse_pos = [random.randrange(1824, 1893), random.randrange(250, 321)]
    eleven_mouse_pos = [random.randrange(1466, 1539), random.randrange(341, 408)]
    twelve_mouse_pos = [random.randrange(1556, 1620), random.randrange(341, 408)]
    thirteen_mouse_pos = [random.randrange(1646, 1714), random.randrange(341, 408)]
    fourteen_mouse_pos = [random.randrange(1734, 1802), random.randrange(341, 408)]
    fifteen_mouse_pos = [random.randrange(1824, 1893), random.randrange(341, 408)]
    sixteen_mouse_pos = [random.randrange(1466, 1539), random.randrange(428, 496)]
    seventeen_mouse_pos = [random.randrange(1556, 1620), random.randrange(428, 496)]
    eighteen_mouse_pos = [random.randrange(1650, 1700), random.randrange(428, 496)]
    nineteen_mouse_post = [random.randrange(1737, 1800), random.randrange(428, 496)]

    Mouse.delayClick(MousePos.bag_mouse_pos)
    time.sleep(2)
    Mouse.delayClick(MousePos.unequip_mouse_pos)
    time.sleep(2)
    Mouse.delayClick(MousePos.esc_mouse_pos)
    time.sleep(2)
    Mouse.click(MousePos.storage_mouse_pos)
    time.sleep(2)

    Mouse.click(one_mouse_pos)
    Mouse.click(two_mouse_pos)
    Mouse.click(three_mouse_pos)
    Mouse.click(four_mouse_pos)
    Mouse.click(five_mouse_pos)
    Mouse.click(six_mouse_pos)
    Mouse.click(seven_mouse_pos)
    Mouse.click(eight_mouse_pos)
    Mouse.click(nine_mouse_pos)
    Mouse.click(ten_mouse_pos)
    Mouse.click(eleven_mouse_pos)
    Mouse.click(twelve_mouse_pos)
    Mouse.click(thirteen_mouse_pos)
    Mouse.click(fourteen_mouse_pos)
    Mouse.click(fifteen_mouse_pos)
    Mouse.click(sixteen_mouse_pos)
    Mouse.click(seventeen_mouse_pos)
    Mouse.click(eighteen_mouse_pos)
    Mouse.click(nineteen_mouse_post)
    Mouse.delayClick(MousePos.keep_mouse_pos)
    Mouse.delayClick(MousePos.esc_mouse_pos)


