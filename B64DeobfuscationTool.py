# System:
import os 
import sys

# Encoding:
import base64

def deobfuscate_and_sort_base64(obfuscated_base64):
    # Decode base64
    decoded_bytes = base64.b64decode(obfuscated_base64)
    decoded_str = decoded_bytes.decode('utf-8')
    
    # Check if the string has been reversed
    if decoded_str.endswith("#R"):
        decoded_str = decoded_str[:-2]  # Remove the indicator
        decoded_str = decoded_str[::-1]  # Reverse the string back
    
    # Sort the characters in the string
    sorted_str = ''.join(sorted(decoded_str))
    
    return sorted_str

def un_reverse_base64(base64_str):
    # Check if the string has been reversed
    if base64_str.endswith("#R"):
        base64_str = base64_str[:-2]  # Remove the indicator
        base64_str = base64_str[::-1]  # Reverse the string back
    
    return base64_str

if __name__ == "__main__":
    choice = int(input("Enter 1 to sort base64 or 2 to reverse base64: "))
    
    if choice == 1:
        obfuscated_base64 = input("Enter the obfuscated base64 code: ")
        sorted_base64 = deobfuscate_and_sort_base64(obfuscated_base64)
        print("Sorted base64 code:", sorted_base64)
    
    elif choice == 2:
        base64_str = input("Enter the base64 code: ")
        original_base64 = un_reverse_base64(base64_str)
        print("Un-reversed base64 code:", original_base64)
    
    else:
        print("Invalid choice. Please enter either 1 or 2.")
