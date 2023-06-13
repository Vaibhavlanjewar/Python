class Flower:
  color = ""

rose = Flower()
rose.color = "RED"

violet=Flower()
violet.color ="BLUE"

this_pun_is_for_you =rose.color+"\n" +violet.color

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 