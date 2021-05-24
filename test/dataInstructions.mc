.data
.word 0xFFFEFFFFFF 45 67  
.half 22 33 44
  word1: .byte 2 3 4 5
word2 : .half 2 3
.byte 2 3 4 5
# word3: .double 22
byte2: .byte 56 66
string3: .asciiz "abcde"

.text
lw x11, word1