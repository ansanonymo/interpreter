"""
Author : Md Tazri
Data : 19 Arpil 2023
Description :
A function checking that's all character are allowed in file or not

checking_all_character(data) -> dict

data:str -> check data.
return -> {
    status : False if find illegal character otherwise True.
    line : line number where find illegal chacater otherwise None.
}
"""

import characters_set;

def checking_all_character(data:str)->dict:
    return_object = {
        "status" : True,
        "line" : None
    }

    line_no = 1;
    index = 0;
    data_len = len(data);

    while index < data_len:
        

