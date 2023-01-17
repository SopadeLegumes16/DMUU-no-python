from scikitmcda.dmuu import DMUU

dmuu = DMUU()

payoff = [[300, 300, 300],
          [400, 300, 200],
          [-100, 200, 700]]
alternativas = ["Poupanca", "Dolar", "Fundos"]
scenarios = ["Recessao", "Estabilidade", "Expansao"]

dmuu.dataframe(payoff,alternativas,scenarios)

dmuu.maximax()
#dmuu.maximin()
#dmuu.minimax_regret()
#dmuu.laplace()
#dmuu.hurwicz(0.7)

print(dmuu.pretty_calc())