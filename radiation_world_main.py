import wrap, random

# world
wrap.add_sprite_dir("sprite's")
wrap.world.create_world(1920, 1080)

wrag2 = []
kamen2 = []
money_spisok = []
spisoc_potronov = []
house1_12=[]
giper_ymnie_gribi=[]

semla=wrap.sprite.add('world',960,540,'трава1')


wrap.sprite.add('money', 960, 100, 'shot grn')

hp_bar = wrap.sprite.add('HP', 100, 100, 'O_hp')
wrap.sprite.move_left_to(hp_bar, 10)
wrap.sprite.move_top_to(hp_bar, 10)

hp_bar100 = wrap.sprite.add('HP', 100, 100, '100 HP')
wrap.sprite.move_left_to(hp_bar100, 88)
wrap.sprite.move_top_to(hp_bar100, 25)

# geroy_1
geroy = wrap.sprite.add("human's", 1920 / 2, 1080 / 2, 'geroy1rpg')


def rock(x, y):
    kamen1 = wrap.sprite.add('steni i camni', x, y, 'rock - jpg')
    kamen2.append(kamen1)

def rock_stena(x,y,ygl):
    stena= wrap.sprite.add('steni i camni',x,y,'rock_stena')
    wrap.sprite.set_angle(stena,ygl)
    kamen2.append(stena)

@wrap.always(30000)
def wrag():
    wrag1 = wrap.sprite.add('wrag_enemy', random.randint(0, 1920), random.randint(0, 1080))
    wrag2.append(wrag1)

def spisoc_domow():
    house1_1=wrap.sprite.add("house's",random.randint(-100,1000),0,'house1')
    house1_12.append(house1_1)
spisoc_domow()
spisoc_domow()
@wrap.always(100)
def wrag_napal():
    for u in wrag2:
        ygl = wrap.sprite.calc_angle_by_point(u, 960, 540)
        idi(u, ygl, 3)
    for i in giper_ymnie_gribi:
        ygl = wrap.sprite.calc_angle_by_point(i['id'], 960, 540)
        idi(i['id'], ygl, i['speed'])


# def HP_igroka():

def otkinyl_wraga():
    for y in wrag2:
        for t in spisoc_potronov:
            ygl_potrona = wrap.sprite.get_angle(t)
            hleb = wrap.sprite.is_collide_sprite(y, t)
            if wrap.sprite.get_costume(y) == 'gif1' and hleb == True:
                idi(y, ygl_potrona, 50)
                wrap.sprite.set_costume(y, 'gif2')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'gif2' and hleb == True:
                idi(y, ygl_potrona, 100)
                wrap.sprite.set_costume(y, 'gif3')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'gif3' and hleb == True:
                idi(y, ygl_potrona, 150)
                wrap.sprite.set_costume(y, 'gif4')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'gif4' and hleb == True:
                money(y)
                wrap.sprite.remove(y)
                wrag2.remove(y)
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)

                break

def terarist():
    for y in house1_12:
        for t in spisoc_potronov:
            ygl_potrona = wrap.sprite.get_angle(t)
            hleb = wrap.sprite.is_collide_sprite(y, t)
            if wrap.sprite.get_costume(y) == 'house1' and hleb == True:
                idi(y, ygl_potrona, 50)
                wrap.sprite.set_costume(y, 'house1-2')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'house1-2' and hleb == True:
                idi(y, ygl_potrona, 100)
                wrap.sprite.set_costume(y, 'house1-3')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'house1-3' and hleb == True:
                idi(y, ygl_potrona, 150)
                wrap.sprite.set_costume(y, 'house1-4')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'house1-4' and hleb == True:
                idi(y, ygl_potrona, 150)
                wrap.sprite.set_costume(y, 'house1-5')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'house1-5' and hleb == True:
                wrap.sprite.remove(y)
                house1_12.remove(y)
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)

                break

rock(120, 340)
rock(153, 578)
rock(1550, 856)

rock_stena(700,300,90)
rock_stena(975,300,90)
rock_stena(1250,300,90)
rock_stena(1375,300,90)
rock_stena(700,900,90)
rock_stena(975,900,90)
rock_stena(1250,900,90)
rock_stena(1375,900,90)
rock_stena(1450,758,180)
rock_stena(1450,485,180)
rock_stena(635,485,180)

def money(wrag):
    wragX = wrap.sprite.get_x(wrag)
    wragy = wrap.sprite.get_y(wrag)
    money1 = wrap.sprite.add('money', wragX, wragy, '10 grn')
    money_spisok.append(money1)


shot = 0


def sobiri_monetky():
    global shot
    for y in money_spisok:
        hleb = wrap.sprite.is_collide_sprite(y, geroy)
        if hleb == True:
            wrap.sprite.remove(y)
            money_spisok.remove(y)
            shot += 10
            wrap.sprite_text.set_text(bober, str(shot))


bober = wrap.sprite.add_text('0', 980, 84, font_size=70)

@wrap.always
def pyla_rasbivaitsa():
    for o in spisoc_potronov:
        chipsi=wrap.sprite.is_collide_any_sprite(o,kamen2)
        if chipsi != None:
            wrap.sprite.remove(o)
            spisoc_potronov.remove(o)

@wrap.always(100)
def ybiza():
    for m in spisoc_potronov:
        pylX = wrap.sprite.get_x(m)
        pylY = wrap.sprite.get_y(m)
        if pylY <= 0 or pylY >= 1080:
            wrap.sprite.remove(m)
            spisoc_potronov.remove(m)
        elif pylX <= 0 or pylX >= 1920:
            wrap.sprite.remove(m)
            spisoc_potronov.remove(m)


@wrap.always
def katleta():
    for l in wrag2:
        hleb = wrap.sprite.is_collide_sprite(geroy, l)
        if hleb == True:
            wrap.sprite.set_width_percent(hp_bar100, wrap.sprite.get_width_percent(hp_bar100) - 1)
            wrap.sprite.move_left_to(hp_bar100, 88)
        if wrap.sprite.get_width_percent(hp_bar100) == 0:
            print('GAME:LOSER')
            exit()


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def zastrelu(pos_x, pos_y):
    avtomat_potron = wrap.sprite.add('pyli', 960, 540,'rpg_patron')
    wrap.sprite.set_angle(avtomat_potron, wrap.sprite.get_angle(geroy))
    what = wrap.sprite.get_angle(geroy)
    wrap.sprite.move_at_angle(avtomat_potron, what, 45)
    spisoc_potronov.append(avtomat_potron)


@wrap.always
def sleep():
    for i in spisoc_potronov:
        wrap.sprite.move_at_angle_dir(i, 20)
    otkinyl_wraga()
    terarist()


@wrap.on_mouse_move()
def geroy_move(pos_x, pos_y):
    pavernis(geroy, pos_x, pos_y)


def idi(who, ygl, rastoanie):
    """
    двигает спрайт.

    :param who: ково двигать
    :param ygl: под коким углом сдвигать спрайт
    :param rastoanie: на сколько пикселей
    """
    rastoanie = int(rastoanie)
    if ygl == None:
        ygl = 0
    x, z = wrap.sprite.get_pos(who)
    wrap.sprite.move_at_angle(who, ygl, rastoanie)
    for y in kamen2:
        hleb = wrap.sprite.is_collide_sprite(y, who)
        if hleb == True:
            wrap.sprite.move_to(who, x, z)
    for y in house1_12:
        hleb = wrap.sprite.is_collide_sprite(y, who)
        if hleb == True:
            wrap.sprite.move_to(who, x, z)

def pavernis(who, pos_x, pos_y):
    bebr = wrap.sprite.get_angle(who)
    wrap.sprite.set_angle_to_point(who, pos_x, pos_y)
    for y in kamen2:
        hleb = wrap.sprite.is_collide_sprite(y, who)
        if hleb == True:
            wrap.sprite.set_angle(who, bebr)
    for y in house1_12:
        hleb = wrap.sprite.is_collide_sprite(y, who)
        if hleb == True:
            wrap.sprite.set_angle(who, bebr)


def sdvin_mir():
    gerx = wrap.sprite.get_x(geroy)
    gery = wrap.sprite.get_y(geroy)
    yholpox = gerx - 960
    yholpoy = gery - 540

    wrap.sprite.move(semla, -yholpox, -yholpoy)
    wrap.sprite.move(geroy, -yholpox, -yholpoy)
    for o in wrag2:
        wrap.sprite.move(o, -yholpox, -yholpoy)
    for o in money_spisok:
        wrap.sprite.move(o, -yholpox, -yholpoy)
    for o in kamen2:
        wrap.sprite.move(o, -yholpox, -yholpoy)
    for o in house1_12:
        wrap.sprite.move(o, -yholpox, -yholpoy)
    for o in giper_ymnie_gribi:
        wrap.sprite.move(o['id'], -yholpox, -yholpoy)


@wrap.on_key_always(wrap.K_w, wrap.K_s)
def geroy_move_w(keys, control_keys):
    okeyski = wrap.sprite.get_angle(geroy)
    if wrap.K_w in keys and not wrap.KMOD_SHIFT in control_keys:
        idi(geroy, okeyski, 5)
    elif wrap.KMOD_SHIFT in control_keys:
        idi(geroy, okeyski, 10)
    if wrap.K_s in keys and not wrap.KMOD_SHIFT in control_keys:
        idi(geroy, okeyski, -5)
    sobiri_monetky()
    sdvin_mir()

# i_like_minecraft=[]
# a=1
# v='code3426'
# house1='pelmeni_zawarilis'
# i_like_minecraft=[a,2,3,4,5,6,v,'wow',house1]
#
# kakaoto_peremenaa={'name':'pelmenius','vozrast':15,'igral_v_minecraft':'20let'


# kakoito_mysik={'name':'loxus','age':30,'mtf_group':'mtf11'}
# object_1={'name':'oleg','age':26,'tasks_finished':34,'tasks_failed':2,'mtf_group':'mtf11','role':'commander'}
# secret_object={'name':'???','age':32}
# object_2={'name':'alexey','age':20}
# mtf11=[kakoito_mysik,object_1,secret_object,object_2]
# del kakoito_mysik
# del object_1
# del secret_object
# del object_2
# for object in mtf11:
#     print(object['age'])
#     object['age']+=1
#     print(object['age'])
gripTank=wrap.sprite.add('bosses solders',457,500,'infected wrag tank1_1')
grip_solderTank={'id':gripTank,'speed':3}
giper_ymnie_gribi.append(grip_solderTank)

gripTank=wrap.sprite.add('bosses solders',427,900,'infected wrag tank1_1')
grip_solderTank={'id':gripTank,'speed':3}
giper_ymnie_gribi.append(grip_solderTank)

import wrap_py
wrap_py.app.start()