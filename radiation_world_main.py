import wrap, random

# world
wrap.add_sprite_dir("sprite's")
wrap.world.create_world(1920, 1080)
wrap.world.set_title('2 player game')
wrag2 = []
spisoc_potronov=[]
wrap.world.set_back_image("sprite's/world/ground-texture_(32).jpg")
semla = wrap.sprite.add('world', 500, 900, 'lol')
# geroy_1
geroy = wrap.sprite.add("human's", 1920 / 2, 1080 / 2, 'geroy1pylimet')


@wrap.always(10000)
def wrag():
    wrag1 = wrap.sprite.add('wrag_enemy', random.randint(0, 1920), random.randint(0, 1080))
    wrag2.append(wrag1)

@wrap.always(100)
def wrag_napal():
    for u in wrag2:
        wrap.sprite.move_at_angle_point(u,960,540,3)

def otkinyl_wraga():
    for y in wrag2:
        for t in spisoc_potronov:
            hleb=wrap.sprite.is_collide_sprite(y,t)
            if hleb==True:
               wrap.sprite.move_at_angle(y,wrap.sprite.get_angle(t),5)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def zastrelu(pos_x, pos_y):
    avtomat_potron = wrap.sprite.add('pyli', 960, 540)
    wrap.sprite.set_angle(avtomat_potron, wrap.sprite.get_angle(geroy))
    what = wrap.sprite.get_angle(geroy)
    wrap.sprite.move_at_angle(avtomat_potron, what, 45)
    spisoc_potronov.append(avtomat_potron)
    print(avtomat_potron)

@wrap.always
def sleep():
    for i in spisoc_potronov:
        wrap.sprite.move_at_angle_dir(i,5)
    otkinyl_wraga()


@wrap.on_mouse_move()
def geroy_move(pos_x, pos_y):
    wrap.sprite.set_angle_to_point(geroy, pos_x, pos_y)


def sdvin_mir():
    gerx = wrap.sprite.get_x(geroy)
    gery = wrap.sprite.get_y(geroy)
    yholpox = gerx - 960
    yholpoy = gery - 540

    wrap.sprite.move(semla, -yholpox, -yholpoy)
    wrap.sprite.move(geroy, -yholpox, -yholpoy)
    for o in wrag2:
        wrap.sprite.move(o, -yholpox, -yholpoy)


@wrap.on_key_always(wrap.K_w)
def geroy_move_w(keys, control_keys):
    if wrap.K_w in keys and not wrap.KMOD_SHIFT in control_keys:
        wrap.sprite.move_at_angle_dir(geroy, 5)
    elif wrap.KMOD_SHIFT in control_keys:
        wrap.sprite.move_at_angle_dir(geroy, 10)
    sdvin_mir()
