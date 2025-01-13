import copy
import opsc
import oobb
import oobb_base
import yaml
import os
from scad_help import *



def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    #setup    
    typ = "all"
    #typ = "fast"
    #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    if typ == "all":
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]        

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]

        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        #fast = True
        fast = False

        sizes = []        
        sizes.append([2, 4])
        if not fast:
            sizes.append([2, 2])
            sizes.append([2, 6])
            sizes.append([4, 4])
            sizes.append([4, 6])
            sizes.append([6, 6])

        if not fast:
            thicknesses = [6,12,18,21,24,30,36,42,60]
        else:
            thicknesses = [18]

        for size in sizes:
            for thickness in thicknesses:
                wid = size[0]
                hei = size[1]
                dep = thickness
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = wid
                p3["height"] = hei
                p3["thickness"] = dep
                part["kwargs"] = p3
                nam = "base"
                part["name"] = "tray_stackable"
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                parts.append(part)


    kwargs["parts"] = parts

    make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_tray_stackable(thing, **kwargs):

    thickness_wall = 1.2 #1.5 #0.8
    thickness_base = 3
    thickness_bottom = 1.5

    thickness_layer = 0.25
    thickness_baseplate_tolerance = 0.5

    thickness_bottom_angle_piece = 1
    thickness_bottom_straight_piece = 2

    thickness_stack_interface = thickness_bottom_angle_piece + thickness_bottom_straight_piece

    thickness_extra_middle = 0.75
    extra_middle = 1.5
    #set in routine now thickness_stack_interface = 1.5
    clearance_inset_stacking = 0.2#0#0.25#0#0.5
    inset_bottom = 0.5 #1.5

    #global thickness_wall, thickness_base, thickness_stack_interface, clearance_inset_stacking, thickness_stack_interface   
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    


    width_mm = width * 15
    height_mm = height * 15
    depth_mm = depth

    

    radius_1 = 5
    radius_2 = radius_1 - thickness_wall
    radius_3 = radius_2 - clearance_inset_stacking
    radius_4 = radius_3 - thickness_wall
    radius_5 = radius_4 - thickness_wall

    wid_top = 0
    hei_top = 0
    wid_bot  =0
    hei_bot = 0

    #base tray
    if True:
    #if False:
        #add plate minus one layer
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = depth_mm - thickness_stack_interface - thickness_layer #depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_layer#thickness_stack_interface+thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #thin half step out slice
        p4 = copy.deepcopy(p3)
        ins = thickness_wall #+ inset_bottom
        p4["size"][0] += -ins
        p4["size"][1] += -ins
        p4["size"][2] = thickness_layer
        p4["radius"] += -ins
        pos1 = copy.deepcopy(pos)
        pos1[2] += thickness_stack_interface
        p4["pos"] = pos1
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)

        p5 = copy.deepcopy(p4)
        p5["type"] = "n"
        p5["size"][0] = width_mm - thickness_wall
        p5["size"][1] = height_mm - thickness_wall
        p5["radius"] = radius_1 - thickness_wall/2
        #p5["m"] = "#"
        p5["pos"][2] = depth - thickness_layer
        oobb_base.append_full(thing,**p5)




        #add cutout
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        p4["size"][0] += -2*thickness_wall
        p4["size"][1] += -2*thickness_wall
        les = -thickness_bottom + thickness_layer    
        p4["size"][2] += les
        p4["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        #p4["m"] = "#"
        p4["pos"][2] += -les        
        oobb_base.append_full(thing,**p4)

    #add joiner
    if True:        
        scalar = 2
        width_bottom_mm = scalar * 15
        height_bottom_mm = scalar * 15
        width_count = int(width / scalar)
        height_count = int(height / scalar)
        for x in range(width_count):
            for y in range(height_count):                
                #add plate
                removal = thickness_wall * 2 + clearance_inset_stacking * 2
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle_extra"    
                wid = width_bottom_mm - removal 
                hei = height_bottom_mm - removal
                dep = thickness_bottom_angle_piece
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_3
                p3["inset"] = inset_bottom *2
                #p3["holes"] = True         uncomment to include default holes
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos) 
                pos1[0] += -(((width-scalar)*15)/2)  + x * 15 * scalar
                pos1[1] += -(((height-scalar)*15)/2) + y * 15 * scalar
                pos1[2] += dep#thickness_stack_interface    
                p3["pos"] = pos1
                pos_main = copy.deepcopy(pos1)
                rot1 = copy.deepcopy(rot)
                rot1[1] = 180
                p3["rot"] = rot1
                oobb_base.append_full(thing,**p3)
                #add angle cutout
                if True:
                    p4 = copy.deepcopy(p3)
                    p4["type"] = "n"
                    size2 = copy.deepcopy(p3.get("size",[]))
                    size2[0] += -2*thickness_wall
                    size2[1] += -2*thickness_wall
                    p4["size"] = size2     
                    p4["radius"] = radius_4            
                    p4["m"] = "#"
                    #more complicated becaue of slicing a cone but part of thickness bottom so not needed
                    #oobb_base.append_full(thing,**p4)

                #straight piece
                p4 = copy.deepcopy(p3)
                p4.pop("inset","")
                size2 = copy.deepcopy(p3.get("size",[]))
                size2[2] = thickness_bottom_straight_piece
                p4["size"] = size2            
                pos2 = copy.deepcopy(pos1)
                pos2[2] += thickness_bottom_straight_piece
                p4["pos"] = pos2
                #p4["m"] = "#"
                oobb_base.append_full(thing,**p4)
                #cutout
                if True:
                    p5 = copy.deepcopy(p4)
                    p5["type"] = "n"
                    size2 = copy.deepcopy(p4.get("size",[]))
                    size2[0] += -2*thickness_wall
                    size2[1] += -2*thickness_wall
                    size2[2] += -thickness_bottom + thickness_bottom_angle_piece + thickness_bottom
                    pos3 = copy.deepcopy(pos2)
                    pos3[2] += +thickness_bottom
                    p5["pos"] = pos3
                    p5["size"] = size2
                    p5["radius"] = radius_4
                    #p5["m"] = "#"
                    oobb_base.append_full(thing,**p5)

            #add sawtooth for overhangs
                if True:
                    #side_sawtooths
                    if True:  
                        end_skip = 2
                        pass  
                        thickness_sawtooth = thickness_layer * 2
                        width_saw_tooth = 0.2
                        width_gap_saw_tooth = 0.6
                        height_saw_tooth = 3.5
                        #repeats_width = int(width_bottom_mm / (width_saw_tooth*2))
                        #repeats_height = int(height_bottom_mm / (width_saw_tooth*2))
                        repeats_width = int(width_bottom_mm / (width_saw_tooth + width_gap_saw_tooth))
                        repeats_height = int(height_bottom_mm / (width_saw_tooth + width_gap_saw_tooth))
                        for xx in range(end_skip,repeats_width-end_skip):                                                   
                            p3 = copy.deepcopy(kwargs)
                            p3["type"] = "n"
                            p3["shape"] = f"oobb_cube"    
                            wid = width_saw_tooth                        
                            hei = height_saw_tooth
                            if xx == 2 or xx == repeats_height - 3:
                                #hei = height_saw_tooth * 1.5
                                #wid = width_saw_tooth * 1                        
                                pass
                            if xx == 1 or xx == repeats_width - 2:
                                #hei = 1
                                #hei = height_saw_tooth * 3
                                pass
                            if xx == 0 or xx == repeats_width - 1:
                                #hei = height_saw_tooth * 5
                                #wid = width_saw_tooth * 1.5                        
                                pass
                            dep = thickness_sawtooth
                            size = [wid, hei, dep]
                            p3["size"] = size                                 
                            #p3["holes"] = True         uncomment to include default holes
                            p3["m"] = "#"
                            pos1 = copy.deepcopy(pos_main)                         
                            #pos1[0] += -((width_bottom_mm)/2)  + (xx+1) * width_saw_tooth * 2 - width_saw_tooth                                                 
                            pos1[0] += -((width_bottom_mm)/2)  + (xx+1) * (width_saw_tooth + width_gap_saw_tooth) - width_saw_tooth                                                 
                            pos1[2] = thickness_stack_interface
                            poss = []
                            pos11 = copy.deepcopy(pos1)
                            pos11[1] += -((height_bottom_mm)/2)
                            pos12 = copy.deepcopy(pos1)
                            pos12[1] += ((height_bottom_mm)/2)
                            poss.append(pos11)
                            poss.append(pos12)
                            p3["pos"] = poss
                            oobb_base.append_full(thing,**p3)
                        for xx in range(end_skip,repeats_height-end_skip):                                                   
                            p3 = copy.deepcopy(kwargs)
                            p3["type"] = "n"
                            p3["shape"] = f"oobb_cube"    
                            hei = width_saw_tooth                        
                            wid = height_saw_tooth
                            if xx == 2 or xx == repeats_height - 3:
                                #hei = width_saw_tooth * 1
                                #wid = height_saw_tooth * 1.5
                                pass
                            if xx == 1 or xx == repeats_width - 2:
                                #hei = width_saw_tooth * 1
                                #wid = height_saw_tooth * 3
                                pass
                            if xx == 0 or xx == repeats_width - 1:
                                #hei = width_saw_tooth * 1.6
                                #wid = height_saw_tooth * 3
                                pass
                            dep = thickness_sawtooth
                            size = [wid, hei, dep]
                            p3["size"] = size                                 
                            #p3["holes"] = True         uncomment to include default holes
                            p3["m"] = "#"
                            pos1 = copy.deepcopy(pos_main)                         
                            #pos1[1] += -((width_bottom_mm)/2)  + (xx+1) * width_saw_tooth * 2 - width_saw_tooth                                                 
                            pos1[1] += -((width_bottom_mm)/2)  + (xx+1) * (width_saw_tooth + width_gap_saw_tooth) - width_saw_tooth                                                 
                            pos1[2] = thickness_stack_interface
                            poss = []
                            pos11 = copy.deepcopy(pos1)
                            pos11[0] += -((height_bottom_mm)/2)
                            pos12 = copy.deepcopy(pos1)
                            pos12[0] += ((height_bottom_mm)/2)
                            poss.append(pos11)
                            poss.append(pos12)
                            p3["pos"] = poss                        
                            oobb_base.append_full(thing,**p3)                            
                    #corner_angles
                    if True:
                        inset_layer = 1
                        p3 = copy.deepcopy(kwargs)
                        p3["type"] = "n"
                        p3["shape"] = f"oobb_cube"
                        wid = 4.5
                        hei = 4.5
                        dep = thickness_layer
                        size = [wid, hei, dep]
                        p3["size"] = size
                        p3["m"] = "#"
                        pos1 = copy.deepcopy(pos_main)
                        pos1[2] = thickness_stack_interface
                        shift_x = width_bottom_mm/2
                        shift_y = height_bottom_mm/2
                        poss = []
                        pos11 = copy.deepcopy(pos1)
                        pos11[0] += -shift_x
                        pos11[1] += -shift_y
                        pos12 = copy.deepcopy(pos1)
                        pos12[0] += shift_x
                        pos12[1] += -shift_y
                        pos13 = copy.deepcopy(pos1)
                        pos13[0] += -shift_x
                        pos13[1] += shift_y
                        pos14 = copy.deepcopy(pos1)
                        pos14[0] += shift_x
                        pos14[1] += shift_y
                        poss.append(pos11)
                        poss.append(pos12)
                        poss.append(pos13)
                        poss.append(pos14)
                        p3["pos"] = poss
                        oobb_base.append_full(thing,**p3)
                        
                        #one layer up
                        p4 = copy.deepcopy(p3)
                        p4["size"][0] += -inset_layer
                        p4["size"][1] += -inset_layer
                        poss = p4["pos"]
                        for pos1 in poss:
                            pos1[2] += thickness_layer
                        p4["m"] = "#"
                        oobb_base.append_full(thing,**p4)
                        #one layer up
                        




    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)