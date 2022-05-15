# MODUlES
from getkey import getkey
import timeit
import os

# STATS
username = os.environ['REPL_OWNER']

upgrades = []
cookies = 0

if username == 'five-nine':
  username = 'None'

# FUNCTIONS
def clear():
  os.system('clear')

#SHOP
class Upgrade:
  def __init__(self, name, cost, cps, cpc):
    self.name = name

    self.cost = cost
    
    self.cps = cps # cookies per second
    self.cpc = cpc # cookies per click

    for upgrade in upgrades:
      if upgrade.name == self.name:
        self.cost += int(self.cost/8)

Cursor = Upgrade('Cursor', 15, 0.1, 0)
Grandma = Upgrade('Grandma', 100, 1, 0)
Farm = Upgrade('Farm', 1100, 8, 1)
Mine = Upgrade('Mine', 12000, 47, 1)
Factory = Upgrade('Factory', 130000, 260, 2)
Bank = Upgrade('Bank', 1400000, 1400, 0)
Temple = Upgrade('Temple', 2000000, 7800, 1)
Wizard_Tower = Upgrade('Wizard Tower', 330000000, 44000, 4)
Shipment = Upgrade('Shipment', 5100000000, 260000, 0)
Alchemy_Lab = Upgrade('Alchemy Lab', 75000000000, 1600000, 3)
Portal = Upgrade('Portal', 1000000000000, 10000000, 6)
Time_Machine = Upgrade('Time Machine', 14000000000000, 65000000, 6)
Cookie_Monster = Upgrade('Cookie Monster', 180000, 350, 70)
Blaster = Upgrade('Blaster', 20000000, 0, 3500)

# GAME
while True: # loop forever
  cps = 0
  cpc = 1

  for upgrade in upgrades:
    cps += upgrade.cps

  for upgrade in upgrades:
    cpc += upgrade.cpc

  print(f"""                Cookie Clicker 🍪                    Stats 📈                  Store🏬
          ────────────────────────────────────────────────────────────────────────────────────────
        
          Cookies: {cookies }                         CPS: {cps}
                                                      CPC: {cpc}""")

  start = timeit.default_timer()
  
  click = getkey()

  end = timeit.default_timer()
  

  if click == "\n" and end-start > 0.04: # prevent spam
    cookies += 1

    for upgrade in upgrades:
      cookies += upgrade.cookie_perc
      
  clear()