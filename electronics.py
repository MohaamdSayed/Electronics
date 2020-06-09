gain = 0
import random

counter = 0
target = 10 %the target gain
while (gain < target):
    print("Iteration " + str(counter + 1))
    # Configuration 1
    VCC = 9
    beta = 100
    Vce_Critical = 0.3

    # R in ohms

    R1 = random.randint(1, 100000)
    R2 = random.randint(1, 100000)
    Rc = random.randint(1, 100000)
    Re = random.randint(1, 100000)
    Rload = 180
    Rsig = 280
    Vth = (VCC * R2) / (R2 + R1)
    rth = (R1 * R2) / (R2 + R1)

    Ib = (Vth - 0.7) / (rth + 101 * Re)
    if (Ib == 0):
        counter += 1
        continue
    Ic = beta * Ib
    Ie = Ib + Ic
    Vce = VCC - Ic * Rc - Ie * Re
    Active = False

    if Vce > Vce_Critical:
        Active = True
        # print("ACtIVE MOOD")
        # print("Base Current = " + str(Ib))
        # print("V thevenen = " + str(Vth))
        # print("rth " + str(rth))
        # print("Vce " + str(Vce))
    # else:
    #     print("Not Active")

    if Active:
        Rpi = (25e-3) / Ib
        R3 = rth
        Vo = (Rc * Rload * Ic) / (Rload + Rc)
        Vpi = Rpi * Ib
        Vin = Vpi * (1 + Rsig * ((Rpi + R3) / (Rpi * R3)))
        gain = (Vo / Vin)
        if (gain > target + 5):
            gain=1
            continue
        if (gain > target):
            print("GAAAIN IS =   " + str(gain))
            print("R1 =    " + str(R1))
            print("R2 =    " + str(R2))
            print("Re =    " + str(Re))
            print("Rc =    " + str(Rc))
    counter += 1
