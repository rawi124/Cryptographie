res = 0xef6b0deebd3cd2f5
l = [0xbf3e4cbfed3d86e5, 0xe043297aeb7383fe, 0xe143283bab66d2ba, 0x9896ad0cb0dd7c3c, 0x89c3ed4ca4d82c79, 0x2702e3f8a51fc06c, 0x3213e6a8e54b8568, 0x3aa85ac87dca8de3, 0x3ebc1acd698bcda7,
     0x9613b7e714a7d7ed, 0x9342e6a704a286f9, 0x0a604f9d1d678bfc, 0x4e240a9d5833cae9, 0xb6dbaf82da4909a1, 0xb69aebc79b1d4cb0, 0x1c13fdda4016fe02, 0x1812e88a0056ba47, 0xdc26ed238d818d56, 0xd862f96788d0cd07]
for el in l:
    res = res ^ el
print(len(hex(res)))
