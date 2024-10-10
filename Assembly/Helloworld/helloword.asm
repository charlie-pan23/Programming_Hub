DSEG SEGMENT 
    MESS DB 'Hello World!'
DSEG ENDS

CSEG SEGMENT
    ASSUME  CS:CSEG, DS:DSEG
    BEGIN:  MOV AX,DSEG
            MOV DS,AX

            MOV DX,OFFSET MESS

            MOV AH, 9
            INT 21H

            MOV AH,4CH
            INT 21H
CSEG ENDS
END BEGIN
