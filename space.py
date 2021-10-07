from PIL import Image

def makeMap():
    # img = Image.new('RGB', [500,500], 255)
    # data = img.load()

    # for x in range(img.size[0]):
    #     for y in range(img.size[1]):
    #         data[x,y] = (
    #             x % 255,
    #             y % 255,
    #             (x**2-y**2) % 255,
    #         )

    # img.save('image.png')

    width = 10
    height = 10
    my_list = [(216,235,52),(52, 235, 122),(52, 89, 235),100,100,100,100]
    img = Image.new('RGB', [4,4], (216, 235, 52))
    img.putdata(my_list)
    img.save('image.png')
