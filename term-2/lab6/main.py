from PIL import Image, ImageDraw

IMG_WIDTH = 1280 
IMG_HEIGHT = 720 

ASPECT_RATIO = IMG_WIDTH / IMG_HEIGHT

HORIZON = 0.6
RIVER_UP = HORIZON + 0.025
RIVER_DOWN = HORIZON + 0.1

MOUNTAINS_COLOR     = (171, 171, 209) # горы

GROUND_COLOR        = (147, 199, 105) # ближняя часть земли
FAR_GROUND_COLOR    = (147, 199, 135) # дальняя часть земли

RIVER_COLOR         = (73, 149, 173)
SAND_COLOR          = (217, 208, 165)

PINE_TRUNK_COLOR    = (84, 73, 51)
PINE_CROWN_COLOR    = (99, 191, 101)

HOUSE_WALLS_COLOR   = (209, 200, 192)
HOUSE_ROOF_COLOR    = (200, 205, 220)
HOUSE_WIN_COLOR     = (65, 81, 105)
HOUSE_DOOR_COLOR    = (135, 121, 105)

# Инициализация главного слоя, и создание неба
img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), (215, 235, 250))
draw = ImageDraw.Draw(img)

def __relative_size(val: float, size: int) -> int:
    return int(val * size)

def rel_x(val: float) -> int:
    return __relative_size(val, IMG_WIDTH)

def rel_y(val: float) -> int:
    return __relative_size(val, IMG_HEIGHT)

def rel(x: float, y: float) -> tuple:
    return (rel_x(x), rel_y(y))

def draw_mountains() -> None:
    # горы
    hor = HORIZON
    m1 = [rel(-0.3, hor), rel(0.025, 0.25), rel(0.2, hor)]
    m2 = [rel(0.1, hor), rel(0.25, 0.3), rel(0.5, hor)]
    m3 = [rel(0.36, hor), rel(0.5, 0.27), rel(0.8, hor)]
    m4 = [rel(0.6, hor), rel(0.9, 0.2), rel(2, hor)]

    draw.polygon(m1, fill=MOUNTAINS_COLOR)
    draw.polygon(m2, fill=MOUNTAINS_COLOR)
    draw.polygon(m3, fill=MOUNTAINS_COLOR)
    draw.polygon(m4, fill=MOUNTAINS_COLOR)

def draw_ground() -> None:
    hor = HORIZON
    far_g = [rel(0, hor), rel(1, hor), rel(1,1), rel(0, 1)]
    near_g = [rel(0, hor + 0.05), rel(1, hor + 0.05 ), rel(1,1), rel(0, 1)]

    draw.polygon(far_g, fill=FAR_GROUND_COLOR)
    draw.polygon(near_g, fill=GROUND_COLOR)

def draw_river() -> None:
    sand = [rel(0, RIVER_DOWN), rel(1, RIVER_UP), rel(1,1), rel(0, 1)]
    river = [rel(0, RIVER_DOWN + 0.05), rel(1, RIVER_UP + 0.025), rel(1,1), rel(0, 1)]

    draw.polygon(sand, fill=SAND_COLOR)
    draw.polygon(river, fill=RIVER_COLOR)

def draw_house(pos: tuple[float, float] = (0.5, 0.5), size: float = 1) -> None:
    canvas_x = rel_x(0.75/ASPECT_RATIO)
    canvas_y = rel_y(0.75)

    new_layer = Image.new('RGBA', (canvas_x, canvas_y), (0,0,0,0))
    house = ImageDraw.Draw(new_layer)
    
    def _rel_x(val: float) -> int:
        return __relative_size(val, canvas_x)
    def _rel_y(val: float) -> int:
        return __relative_size(val, canvas_y)
    def _rel(x: float, y: float) -> tuple:
        return (_rel_x(x), _rel_y(y))


    base_walls = [_rel(0.1, 0.4), _rel(0.9, 0.4), _rel(0.9, 0.9), _rel(0.1, 0.9)]
    roofs = [_rel(0.2, 0.25), _rel(0.8, 0.25), _rel(0.95, 0.45), _rel(0.05, 0.45)]
    door = [_rel(0.4, 0.6), _rel(0.6, 0.6), _rel(0.6, 0.9), _rel(0.4, 0.9)]

    win1 = [_rel(0.15, 0.55), _rel(0.35, 0.55), _rel(0.35, 0.7), _rel(0.15, 0.7)]
    win2 = [_rel(1-0.15, 0.55), _rel(1-0.35, 0.55), _rel(1-0.35, 0.7), _rel(1-0.15, 0.7)]

    house.polygon(base_walls, fill=HOUSE_WALLS_COLOR)
    
    house.polygon(roofs, fill=HOUSE_ROOF_COLOR)
    house.polygon(door, fill=HOUSE_DOOR_COLOR)

    house.polygon(win1, fill=HOUSE_WIN_COLOR)
    house.polygon(win2, fill=HOUSE_WIN_COLOR)

    new_layer = new_layer.resize((int(_rel_x(size)), int(_rel_y(size))))
    img.paste(new_layer, (rel_x(pos[0])-(canvas_x//2), rel_y(pos[1])-canvas_y//2), new_layer)
    # img.paste(new_layer, ((IMG_WIDTH-canvas_x)//2, (IMG_HEIGHT-canvas_y)//2), new_layer)

    pass

def draw_pine(pos: tuple[float, float] = (0.5, 0.5), size: float = 1) -> None:
    
    canvas_x = rel_x(0.75/ASPECT_RATIO)
    canvas_y = rel_y(0.75)

    new_layer = Image.new('RGBA', (canvas_x, canvas_y), (0,0,0,0))
    pine = ImageDraw.Draw(new_layer)
    
    def _rel_x(val: float) -> int:
        return __relative_size(val, canvas_x)
    def _rel_y(val: float) -> int:
        return __relative_size(val, canvas_y)
    def _rel(x: float, y: float) -> tuple:
        return (_rel_x(x), _rel_y(y))

    trunk = [_rel(0.47, 0.5), _rel(0.53, 0.5), _rel(0.53, 1), _rel(0.47, 1)]

    crown_up        = [_rel(0.5, 0.05), _rel(0.7, 0.325), _rel(0.3, 0.325)]
    crown_middle    = [_rel(0.5, 0.2), _rel(0.75, 0.525), _rel(0.25, 0.525)]
    crown_down      = [_rel(0.5, 0.35), _rel(0.8, 0.75), _rel(0.2, 0.75)]

    pine.polygon(trunk, fill=PINE_TRUNK_COLOR)
    pine.polygon(crown_down, fill=PINE_CROWN_COLOR)
    pine.polygon(crown_middle, fill=PINE_CROWN_COLOR)
    pine.polygon(crown_up, fill=PINE_CROWN_COLOR)

    y_size_delta = abs(canvas_y - int(_rel_y(size)))
    
    new_layer = new_layer.resize((int(_rel_x(size)), int(_rel_y(size))))
    img.paste(new_layer,
            (rel_x(pos[0])-(canvas_x//2),
            rel_y(pos[1])-(canvas_y-y_size_delta)//2), new_layer)
            
    # img.paste(new_layer, _rel(pos[0], pos[1]), new_layer)
    # img.paste(new_layer, ((IMG_WIDTH-canvas_x)//2, (IMG_HEIGHT-canvas_y)//2), new_layer)
    pass

# int main() // :)
if __name__ == "__main__":

    draw_mountains()
    draw_ground()
    draw_river()

    draw_house(pos=(0.2, HORIZON + 0.025), size=0.6)
    draw_house(pos=(0.5, HORIZON + 0.05), size=0.55)

    draw_pine(pos=(0.9, HORIZON-0.1), size=0.35)
    draw_pine(pos=(0.7, HORIZON-0.1), size=0.4)
    draw_pine(pos=(0.4, HORIZON-0.1), size=0.45)
    draw_pine(pos=(0.1, HORIZON-0.1), size=0.5)

    img.save('./tst-00.png', 'PNG')