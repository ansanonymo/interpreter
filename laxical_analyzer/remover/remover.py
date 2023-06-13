"""
Author : Md Tazri
Date : 17 Arpil 2023
Description : 
Remove multi line and single line comment from file. But it is not remove 
multiline comment in string.

Multiline comment Sample : 
/* 
This is multi line comment.
*/

Singleline comment Sample : 
// single line comment.

"""


def single_line_remover(data:str)->str:
    in_string = False;
    in_comment = False;
    final_data:str = "";

    index:int = 0;
    data_len:int = len(data);

    while index < data_len:
        char:str = data[index];
        index += 1;

        # if comment is already start
        if in_comment:
            if(char == "\n"):
                final_data += char;
                in_comment = False;
            continue;
        elif in_string: # if string is already start
            if char == "\\" and index < data_len:
                next_char = data[index];
                index +=1;
                final_data += char+next_char;
            elif char == "\\" and index >= data_len:
                final_data += char;
            elif char == in_string:
                final_data += char;
                in_string = False;
                continue;
            final_data += char;
            continue;
        # if comment start
        elif(char == "/" and in_string == False):
            if index < data_len:
                next_char = data[index];
                index += 1;
                if(next_char == "/"):
                    in_comment = True;
                else:
                    final_data += char + next_char;
            else:
                final_data += char;
        # if string start
        elif (char == '"' or char == "'") and in_comment == False:
            in_string = char;
            final_data += char;
            continue;
        else:
            final_data += char;

    
    return final_data;


def multi_line_remover(data:str)->str:
    in_string = False;
    in_comment = False;
    final_data:str = "";

    index:int = 0;
    data_len:int = len(data);

    while index < data_len:
        char:str = data[index];
        index += 1;

        # if comment is already start
        if in_comment:
            if char == "*" and index < data_len and data[index] == "/":
                index += 1;
                in_comment = False;
            elif char == "\n":
                final_data += char;
            continue;


        elif in_string: # if string is already start
            if char == "\\" and index < data_len:
                next_char = data[index];
                index +=1;
                final_data += char+next_char;
            elif char == "\\" and index >= data_len:
                final_data += char;
            elif char == in_string:
                final_data += char;
                in_string = False;
                continue;
            final_data += char;
            continue;
        # if comment start
        elif(char == "/" and in_string == False):
            if index < data_len:
                next_char = data[index];
                index += 1;
                if(next_char == "*"):
                    in_comment = True;
                else:
                    final_data += char + next_char;
            else:
                final_data += char;
        # if string start
        elif (char == '"' or char == "'") and in_comment == False:
            in_string = char;
            final_data += char;
            continue;
        else:
            final_data += char;

    
    return final_data;



def comment_remover(data:str)->str:
    final_data = single_line_remover(data);
    final_data = multi_line_remover(final_data);
    return final_data;

if __name__ == "__main__":
    file_path = "./test_data/program.c";

    with open(file_path,"r") as file:
        data = file.read();
        filtered = comment_remover(data);
        print("> Data : ");
        print(data);
        print("-------------------------\n> final data : ");
        print(filtered);