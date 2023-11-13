import foldedcalc
import reader
import writer

# inputing the variables 

craft = reader.read_craft_inp()

'''
for i in range(7):
    print("For iteration: ", i)
    print("craft U, L, W, H, mass is: " + str(craft[i].U) + " " + str(craft[i].L) + " " + str(craft[i].W) + " " + str(craft[i].H) + " " + str(craft[i].mass))
'''

varinps = []

for i in range(7):
    name = "folded outputs/output vals " + str(craft[i].U) + "U.txt"
    # print("The file name is ",name)
    # obj = reader.calcedinps()   # need to declare obj every time to avoid retroactive overwrite
    obj = reader.read_outs(name)
    varinps.append(obj)
    '''
    print("Calculated inputs for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("ptot vtot mtot lenopen widopen " + str(varinps[i].ptot) + " " + str(varinps[i].vtot) + " " + str(varinps[i].mtot)  + " " + str(varinps[i].lenopen)  + " " + str(varinps[i].widopen))
    '''
# calculating intermediate values

intvars = []

for i in range(7):
    # intobj = foldedcalc.intervals()         # need to declare obj every time to avoid retroactive overwrite
    intobj = foldedcalc.get_inter_vals(craft[i],varinps[i])
    intvars.append(intobj)
    
    print("Calculated intermediate values for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("mbody dcom " + str(intvars[i].mbody) + " " + str(intvars[i].dcom))
    print("moipanels ", intvars[i].moipanels)
    print("moibody ", intvars[i].moibody)

writer.write_inter(intvars)

outvars = []

for i in range(7):
    # outobj = foldedcalc.outvals()       # need to declare obj every time to avoid retroactive overwrite
    outobj = foldedcalc.get_outvals(craft[i],varinps[i],intvars[i])
    outvars.append(outobj)
    
    print("Output values for iteration: " + str(i) + " where U is: " + str(craft[i].U))
    print("MOI[0,1,2]: " + str(outvars[i].MOI))
    print("powmass, powvol " + str(outvars[i].powmass) + " " + str(outvars[i].powvol))

writer.write_out(outvars, craft)

writer.make_graphs()

