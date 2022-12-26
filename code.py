def cat(re):
    if re<500:
        return "It is a laminar flow"
    
    if re>500 and re<200:
        return "It is going through a transitional flow"
    
    if re>2000:
        return "It is going through a turbulent flow."
def calc_re(density,velocity,diameter,kin_vis):

    return (density*velocity*diameter)/kin_vis

x = True 

while x:
    try:
        a = float(input("density:"))
        b = float(input("velocity"))
        c = float(input("diameter:"))
        d  = float(input("kinetic_viscosity:"))
        re = calc_re(a,b,c,d)
        print(cat(re))
        que = int(input("0 for quiting 1 to continue:"))
        if que==0:
            x = 0
        else:
            continue
    except Exception as e:
        print(e)

