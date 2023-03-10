#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance, Force
SendMode, Input ; Recommended for new scripts due to its superior speed and reliability.
SetBatchLines, -1
SetWorkingDir, %A_ScriptDir% ; Ensures a consistent starting directory.
#Hotstring, EndChars  


^`;:: 
if not GetKeyState("Shift", "P") {
    send :
    Send ‎
    send )
}
Return

+^`;:: 
send :
Send ‎
send D
Return
