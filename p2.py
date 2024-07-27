import pandas as pd
import math


care_areas = pd.read_csv(r"C:\Users\skava\Desktop\Github\Unhack-2024\resources\Student-Dataset-1\Dataset-1\2nd\CareAreas.csv", header=None)
metadata = pd.read_csv(r"C:\Users\skava\Desktop\Github\Unhack-2024\resources\Student-Dataset-1\Dataset-1\2nd\metadata.csv")

main_field_size = metadata.iloc[0,0]
sub_field_size = metadata.iloc[0,1]

def main_field_calculation(main_field_size, care_areas):
    # index = 0
    main_field = []
    for index,row in care_areas.iterrows():
        x1 = row[1]
        x2 = row[2]
        y1 = row[3]
        y2 = row[4]

        x_stage = math.ceil((x2 - x1)/main_field_size)
        y_stage = math.ceil((y2 - y1)/main_field_size)
        
        for i in range(y_stage):
            for j in range(x_stage):
                main_field_x1 = x1 + j * main_field_size
                main_field_y1 = y1 + i * main_field_size
                main_field_x2 = main_field_x1 + main_field_size
                main_field_y2 = main_field_y1 + main_field_size
                                
                if():
                    main_field.append([main_field_x1, main_field_x2, main_field_y1, main_field_y2])
            
                    # sub_field.append([sub_field_x1, sub_field_x2, sub_field_y1, sub_field_y2,index])
        # main_field_x1 = x1
        # main_field_y1 = y1
        # main_field_x2 = main_field_x1 + main_field_size
        # main_field_y2 = main_field_y1 + main_field_size


    df = pd.DataFrame(main_field)
    df.to_csv("mainfield.csv",header=False)


def sub_field_calculation(sub_field_size, care_areas):
    sub_field = []
    # subid = 0
    for index,row in care_areas.iterrows():

        x1 = row[1]
        x2 = row[2]
        y1 = row[3]
        y2 = row[4]

        # print("x1 : ",x1,"x2 : ",x2,"y1 : ",y1,"y2 : ",y2)

        x_stage = math.ceil((x2 - x1)/sub_field_size)
        y_stage = math.ceil((y2 - y1)/sub_field_size)

        # print("No of x field : ",x_stage,"No of y field",y_stage)

        for i in range(y_stage):
            for j in range(x_stage):
                sub_field_x1 = x1 + j * sub_field_size
                sub_field_y1 = y1 + i * sub_field_size
                sub_field_x2 = sub_field_x1 + sub_field_size
                sub_field_y2 = sub_field_y1 + sub_field_size
            
                if (sub_field_x1 <= x2 and sub_field_y1 <= y2):
                    sub_field.append([sub_field_x1, sub_field_x2, sub_field_y1, sub_field_y2,index])
                    # subid = subid+1

    df = pd.DataFrame(sub_field)

    df.to_csv("subfield.csv",header=False)


main_field_calculation(main_field_size, care_areas)

sub_field_calculation(sub_field_size, care_areas)
