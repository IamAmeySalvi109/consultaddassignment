Input_str, Output_str = "ATTCGGTAG", {"T": "A", "A": "T", "C": "G", "G": "C"}


print("".join([Output_str.get(i) for i in Input_str]))