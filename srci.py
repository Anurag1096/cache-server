def rev(text,shift=42):
    result=""
    for char in text:
        code = ord(char)
        if 32 <= code <= 126:
            new_code=((code -32 -shift) %95) +32
            result += chr(new_code)

    return result


encoded_text="¢\x91\xa0\x9a\x8d\x8f\x91¢\x91\xa0\x9a\x8d\x8f\x91..."


char_list= ['¢', '\x91', '\xa0', '\x9a', '\x8d', '\x8f', '\x91', '¢', '\x91', '\xa0', '\x9a', '\x8d', '\x8f', '\x91']

encoded_text=''.join(char_list)
decoded = rev(encoded_text)
print("Decoded result:", decoded)
