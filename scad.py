import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
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

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
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
            kwargs["oomp_size"] = "tray_stackable"
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        widths = [2,4,6,8,10]
        heights = [2,4,6,8,10]
        thicknesses = [9,12,15,18,21,24,27,30,45,60,90]
        extras = ["", "bottom"]

        sizes = []
        for width in widths:
            for height in heights:
                    size = [width, height]
                    size_other_way = [height, width]
                    if size in sizes or size_other_way in sizes:
                        pass
                    else:
                        sizes.append(size)

        for size in sizes:
            for thickness in thicknesses:
                for extra in extras:
                    wid = size[0]
                    hei = size[1]
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    p3["width"] = wid
                    p3["height"] = hei
                    p3["thickness"] = thickness
                    if extra != "":
                        p3["extra"] = extra
                    part["kwargs"] = p3
                    nam = "tray_stackable"
                    part["name"] = nam
                    if oomp_mode == "oobb":
                        p3["oomp_size"] = nam
                    parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
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
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_tray_stackable(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    
    thickness_layer = 0.6
    thickness_layer_bottom = 0.4
    thickness_layer_top = 0.9
    
    thickness_bottom = thickness_layer_bottom * 3
    thickness_full_top_piece = depth
    thickness_wall = 1.2
    
    clearance_inset_stacking = 0.2#0#0.25#0#0.5

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
        #main plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = thickness_full_top_piece #depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #main_cutout        
        p5 = copy.deepcopy(p3)
        p5["type"] = "n"
        p5["size"][0] = width_mm - thickness_wall * 2
        p5["size"][1] = height_mm - thickness_wall * 2
        p5["size"][2] = thickness_full_top_piece - thickness_bottom
        p5["radius"] = radius_2
        #p5["m"] = "#"
        p5["pos"][2] = thickness_bottom
        oobb_base.append_full(thing,**p5)


        #add screw holes
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_hole"
            p3["radius_name"] = "m3"
            p3["depth"] = thickness_bottom
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            

            wid_times = width / 2
            hei_times = height / 2
            start_x = -width_mm/2 + 15
            start_y = -height_mm/2 + 15
            poss = []
            for xx in range(int(wid_times)):
                for yy in range(int(hei_times)):            
                    pos1 = copy.deepcopy(pos)         
                    pos1[0] += start_x + xx*30
                    pos1[1] += start_y + yy*30
                    poss.append(pos1)
            p3["pos"] = poss
            oobb_base.append_full(thing,**p3)

   
   #handle extras
    if extra == "bottom":
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[2] = thickness_bottom 
        p3["pos"] = pos1
        #p3["m"] = "#"
        p3["zz"] = "bottom"
        oobb_base.append_full(thing,**p3)
    elif extra == "top":
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[2] = thickness_bottom
        p3["pos"] = pos1
        #p3["m"] = "#"
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    