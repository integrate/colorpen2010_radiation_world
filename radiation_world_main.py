import wrap, random

# world
wrap.add_sprite_dir("sprite's")
wrap.world.create_world(1920, 1080)
wrag2 = []
kamen2 = []
money_spisok = []
spisoc_potronov = []
wrap.world.set_back_image("sprite's/world/ground-texture_(32).jpg")
semla = wrap.sprite.add('world', 500, 900, 'lol')
wrap.sprite.add('money', 960, 100, 'shot grn')

# geroy_1
geroy = wrap.sprite.add("human's", 1920 / 2, 1080 / 2, 'geroy1pylimet')


def rock(x, y):
    kamen1 = wrap.sprite.add('steni i camni', x, y, 'rock - jpg')
    kamen2.append(kamen1)


@wrap.always(10000)
def wrag():
    wrag1 = wrap.sprite.add('wrag_enemy', random.randint(0, 1920), random.randint(0, 1080))
    wrag2.append(wrag1)


@wrap.always(100)
def wrag_napal():
    for u in wrag2:
        ygl = wrap.sprite.calc_angle_by_point(u, 960, 540)
        idi(u, ygl, 3)


def otkinyl_wraga():
    for y in wrag2:
        for t in spisoc_potronov:
            ygl_potrona=wrap.sprite.get_angle(t)
            hleb = wrap.sprite.is_collide_sprite(y, t)
            if wrap.sprite.get_costume(y) == 'gif1' and hleb == True:
                idi(y,ygl_potrona,50)
                wrap.sprite.set_costume(y, 'gif2')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'gif2' and hleb == True:
                idi(y,ygl_potrona,100)
                wrap.sprite.set_costume(y, 'gif3')
                wrap.sprite.remove(t)
                spisoc_potronov.remove(t)
            elif wrap.sprite.get_costume(y) == 'gif3' and hleb == True:
                idi(y,ygl_potrona,150)
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


rock(120, 340)
rock(153, 578)
rock(1000, 786)


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


bober = wrap.sprite.add_text('0', 960, 100, )


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


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def zastrelu(pos_x, pos_y):
    avtomat_potron = wrap.sprite.add('pyli', 960, 540)
    wrap.sprite.set_angle(avtomat_potron, wrap.sprite.get_angle(geroy))
    what = wrap.sprite.get_angle(geroy)
    wrap.sprite.move_at_angle(avtomat_potron, what, 45)
    spisoc_potronov.append(avtomat_potron)


@wrap.always
def sleep():
    for i in spisoc_potronov:
        wrap.sprite.move_at_angle_dir(i, 20)
    otkinyl_wraga()


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
    if ygl== None:
        ygl =0
    x, z = wrap.sprite.get_pos(who)
    wrap.sprite.move_at_angle(who, ygl, rastoanie)
    for y in kamen2:
        hleb = wrap.sprite.is_collide_sprite(y, who)
        if hleb == True:
            # wrap.sprite.move_at_angle(who, ygl, -rastoanie)
            wrap.sprite.move_to(who, x, z)


def pavernis(who, pos_x, pos_y):
    bebr = wrap.sprite.get_angle(who)
    wrap.sprite.set_angle_to_point(who, pos_x, pos_y)
    for y in kamen2:
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

@wrap.on_key_always(wrap.K_w,wrap.K_s)
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
