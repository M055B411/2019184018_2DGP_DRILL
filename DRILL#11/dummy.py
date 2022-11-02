# # class Star:
# #     x = 100
# #     def change():
# #         x = 200
# #         print('x is', x)
# #
# #
# # print(Star.x)
# # Star.change()
# # print(Star.x)
# #
# # star = Star()
# # print('x IS', star.x)
# # star.change()
#
# class Player:
#     def __init__(self):
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
#
# player = Player()
#
# player.where()
#
# Player.where(player)
#
#

table = {
    "SLEEP": {"HIT": "WAKE"},
    "WAKE": {"TIMER10": "SLEEP"}
}

cur_state = "SLEEP"
print(table[cur_state]["HIT"])

