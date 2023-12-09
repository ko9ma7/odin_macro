
import random
import time
import MousePos
import Mouse
import Item
import Dungeon

def changeCharactor(select_charactor): # 캐릭 변경
    Mouse.delayClick(MousePos.menu_mouse_pos)
    Mouse.delayClick(MousePos.change_charactor_mouse_pos)
    Mouse.delayClick(MousePos.ok_btn_mouse_pos)
    time.sleep(random.randrange(40, 60))
    Mouse.delayClick(select_charactor)
    Mouse.delayClick(MousePos.start_game_mouse_pos)
    time.sleep(random.randrange(50, 70))

select_charactor1_mouse_pos = [random.randrange(1644, 1875), random.randrange(94, 166)]
select_charactor2_mouse_pos = [random.randrange(1644, 1875), random.randrange(208, 275)]
select_charactor3_mouse_pos = [random.randrange(1644, 1875), random.randrange(325, 370)]
select_charactor4_mouse_pos = [random.randrange(1644, 1875), random.randrange(430, 482)]
select_charactor5_mouse_pos = [random.randrange(1644, 1875), random.randrange(526, 581)]



dungeon_3rd_mouse_pos = [random.randrange(23, 367), random.randrange(246, 304)]
dungeon_4th_mouse_pos = [random.randrange(23, 367), random.randrange(315, 379)]
dungeon_5th_mouse_pos = [random.randrange(23, 367), random.randrange(390, 450)]
dungeon_6th_mouse_pos = [random.randrange(23, 367), random.randrange(463, 523)]

def cycle(money_dungeon_select_floor, exp_dungeon_select_floor, event_dungeon_select_floor, select_charactor):
    if(select_charactor != select_charactor2_mouse_pos):
        Item.takeOut()
        Item.wearing()

    Dungeon.dungeonAuto(MousePos.fifth_dungeon_mouse_pos, money_dungeon_select_floor)
    Dungeon.dungeonAuto(MousePos.fourth_dungeon_mouse_pos, exp_dungeon_select_floor)
    Dungeon.dungeonAuto(MousePos.first_dungeon_mouse_pos, event_dungeon_select_floor)



    Item.unequip()
    changeCharactor(select_charactor)



def main():
    # cycle(dungeon_6th_mouse_pos, dungeon_6th_mouse_pos, select_charactor2_mouse_pos)

    cycle(dungeon_6th_mouse_pos, dungeon_6th_mouse_pos, dungeon_4th_mouse_pos, select_charactor3_mouse_pos)
    cycle(dungeon_6th_mouse_pos, dungeon_6th_mouse_pos, dungeon_4th_mouse_pos, select_charactor4_mouse_pos)
    cycle(dungeon_6th_mouse_pos, dungeon_6th_mouse_pos, dungeon_4th_mouse_pos, select_charactor5_mouse_pos)
    cycle(dungeon_6th_mouse_pos, dungeon_6th_mouse_pos, dungeon_4th_mouse_pos, select_charactor1_mouse_pos)

main()