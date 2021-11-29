import wrap
#world
wrap.world.create_world(1920, 1080)
wrap.world.set_title('2 player game')
wrap.world.set_back_image("sprite's/world/ground-texture_(32).jpg")
#geroy_1
wrap.add_sprite_dir("sprite's")
geroy=wrap.sprite.add("human's",1920/2,1080/2,'geroy1')

@wrap.on_mouse_move()
def geroy_move(pos_x,pos_y):
    wrap.sprite.set_angle_to_point(geroy,pos_x,pos_y)
@wrap.on_key_always(wrap.K_w)
def geroy_move_w(keys,control_keys):
    if wrap.K_w in keys and not wrap.KMOD_SHIFT in control_keys:
        wrap.sprite.move_at_angle_dir(geroy,5)
    elif wrap.KMOD_SHIFT in control_keys:
        wrap.sprite.move_at_angle_dir(geroy,10)